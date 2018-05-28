from typing import Optional
from uuid import UUID
from pybaseconv import Converter, BASE


class UuidShortener(object):

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

        return '{}-{}'.format(self.prefix, converted_uuid) if \
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

        prefix_substr = '{}-'.format(self.prefix)

        if short_uuid.startswith(prefix_substr):
            short_uuid = short_uuid.replace(prefix_substr, '')

        converter = Converter(BASE.FLICKER_BASE_58, BASE.HEX)
        uuid_number = converter.convert(short_uuid)

        return UUID(uuid_number)
