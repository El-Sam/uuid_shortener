from typing import Optional, Callable
from uuid import UUID, uuid4
from pybaseconv import Converter, BASE


class UuidShortener:

    @property
    def prefix(self):
        return self._prefix

    def __init__(self, prefix: Optional[str] = None):
        self._prefix = prefix

    def shorten(self, uuid: UUID) -> str:
        """
        shortens the the given uuid and appends it to
        the prefix if any was provided
        :param uuid: The uuid number to shorten
        :return: the shortened version
        """
        # stringify the uuid and lower all letters
        stringified_uuid = str(uuid).lower()

        # remove all dashes
        stringified_uuid = stringified_uuid.replace('-', '')

        # uuid is a hex number, we convert it to FLICKER BASE 58 base
        # which give encoding that is suitable for usage in urls
        converter = Converter(BASE.HEX, BASE.FLICKER_BASE_58)
        converted_uuid = converter.convert(stringified_uuid)

        return f'{self.prefix}-{converted_uuid}' if \
            self.prefix is not None else converted_uuid

    def unshorten(self, short_uuid: str) -> UUID:
        """
        Strips the prefix from the given number, if any,
        and unshortens the rest.
        The given short number must have been shortened by
        the shorten method to avoid any errors.
        :param short_uuid: the shortened number to convert back to UUID
        :return: the UUID rep of the shortened number
        """

        prefix_substr = f'{self.prefix}-'

        if short_uuid.startswith(prefix_substr):
            short_uuid = short_uuid.replace(prefix_substr, '')

        converter = Converter(BASE.FLICKER_BASE_58, BASE.HEX)
        uuid_number = converter.convert(short_uuid)

        if len(uuid_number) < 32:
            left_pad = '0' * (32 - len(uuid_number))
            uuid_number = left_pad + uuid_number

        return UUID(uuid_number)


class ShortUuidGenerator:
    def __init__(self, prefix=None, uuid_fn: Callable = uuid4):
        self.shortener = UuidShortener(prefix)
        self.uuid_fn = uuid_fn

    def __call__(self):
        return self.shortener.shorten(self.uuid_fn())
