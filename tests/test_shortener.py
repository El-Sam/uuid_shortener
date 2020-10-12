from unittest import TestCase
from uuid_shortener import UuidShortener, ShortUuidGenerator
from uuid import uuid4, UUID


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

    def test_regression_1_left_padding_with_zeros(self):
        expected_uuid = UUID("0c1dda28-48fa-46e1-97e2-18e1c6d0fb60")

        shortened_uuid = '2uMfE2CfWdX3vJcN3yTWgJ'

        shortener = UuidShortener()

        self.assertEqual(expected_uuid,  shortener.unshorten(shortened_uuid))


class TestShortenedUuidGenerator(TestCase):

    def test_one_way_shortener_with_prefix(self):
        shortener = UuidShortener("dev")
        short_id = ShortUuidGenerator(prefix="dev", uuid=uuid4)

        short_uuid = short_id()

        self.assertGreater(len(short_uuid), 4)
        self.assertEqual(0, short_uuid.index("dev-"))
        self.assertNotEqual(
            shortener.unshorten(short_uuid),
            UUID("00000000-0000-0000-0000-000000000000")
        )

    def test_one_way_shortener_without_prefix(self):
        shortener = UuidShortener()
        short_id = ShortUuidGenerator(uuid=uuid4)

        short_uuid = short_id()

        self.assertGreater(len(short_uuid), 0)
        self.assertNotEqual(
            shortener.unshorten(short_uuid),
            UUID("00000000-0000-0000-0000-000000000000")
        )
