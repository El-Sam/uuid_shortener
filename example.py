from uuid_shortener import UuidShortener
from uuid import uuid4

if __name__ == "__main__":
    print('******** Without prefix')

    shortener = UuidShortener()

    uuid_4 = uuid4()

    short_uuid = shortener.shorten(uuid_4)
    unshortened_uuid = shortener.unshorten(short_uuid)

    print('Uuid to shorten: {}'.format(str(uuid_4)))
    print('shortened uuid: {}'.format(short_uuid))
    print('unshortened uuid(original uuid): {}'.
          format(str(shortener.unshorten(short_uuid))))

    print("\n\n")
    print('******** With prefix')

    shortener = UuidShortener('meow')  # ;)
    uuid_4 = uuid4()

    short_uuid = shortener.shorten(uuid_4)
    unshortened_uuid = shortener.unshorten(short_uuid)

    print('Uuid to shorten: {}'.format(str(uuid_4)))
    print('shortened uuid: {}'.format(short_uuid))
    print('unshortened uuid (original uuid): {}'.
          format(str(shortener.unshorten(short_uuid))))
