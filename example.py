from uuid_shortener import UuidShortener, ShortUuidGenerator
from uuid import uuid4

if __name__ == "__main__":
    print('******** Without prefix')

    shortener = UuidShortener()

    uuid_4 = uuid4()

    short_uuid = shortener.shorten(uuid_4)
    unshortened_uuid = shortener.unshorten(short_uuid)

    print(f'Uuid to shorten: {uuid_4}')
    print(f'shortened uuid: {short_uuid}')
    print(f'unshortened uuid(original uuid): {unshortened_uuid}')

    print("\n\n")
    print('******** With prefix: meow')

    shortener = UuidShortener('meow')
    uuid_4 = uuid4()

    short_uuid = shortener.shorten(uuid_4)
    unshortened_uuid = shortener.unshorten(short_uuid)

    print(f'Uuid to shorten: {uuid_4}')
    print(f'shortened uuid: {short_uuid}')
    print(f'unshortened uuid (original uuid): {unshortened_uuid}')

    print("\n\n")
    print('******** With a one-way generator')

    easy_generator = ShortUuidGenerator()
    short_uuid = easy_generator()
    # Reusing the previously created shortener to unshorten.
    unshortened_uuid = shortener.unshorten(short_uuid)

    print(f'One-way shortened uuid: {short_uuid}')
    print(f'unshortened uuid (original uuid): {unshortened_uuid}')
