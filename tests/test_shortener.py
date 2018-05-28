from unittest import TestCase
from uuid_shortener import UuidShortener
from uuid import uuid4


class TestUuidShortener(TestCase):

    def test_shorten_and_unshorten_with_prefix(self):
        uuid = uuid4()

        shortener = UuidShortener('dev')

        short_uuid = shortener.shorten(uuid)

        self.assertEqual(0, short_uuid.index('dev-'))
        self.assertEqual(uuid, shortener.unshorten(short_uuid))

    def test_shorten_and_unshorten_without_prefix(self):
        uuid = uuid4()

        shortener = UuidShortener()

        short_uuid = shortener.shorten(uuid)

        self.assertEqual(uuid, shortener.unshorten(short_uuid))
