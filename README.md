# uuid_shortener

[![Build Status](https://travis-ci.com/El-Sam/uuid_shortener.svg?branch=master)](https://travis-ci.com/El-Sam/uuid_shortener)
[![PyPI supported versions](https://img.shields.io/pypi/pyversions/uuid-shortener-py.svg)](https://pypi.python.org/pypi/uuid-shortener-py)
[![PyPI version](https://badge.fury.io/py/uuid-shortener-py.svg)](https://badge.fury.io/py/uuid-shortener-py)

**uuid_shortener** is a library for shortening UUIDs into an alphanumerical format suitable for usage in URLs.

The alphanumerical format is Flicker base 58 encoding.

## Installation

from [Pypi](https://pypi.org/project/uuid-shortener-py/):

` pip install uuid-shortener-py `

## Module usage

The `UuidShortener` object can be created with/without a prefix.

##### Example 1: without prefix

```python
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
    print('unshortened uuid(original uuid): {}'.format(str(shortener.unshorten(short_uuid)), str(uuid_4)))

```

##### Output 1:

```
******** Without prefix
Uuid to shorten: 177d1b53-77d5-42b2-8b8f-8d86579deb52
shortened uuid: 3Ueemi554rN46ioLFw3dZG
unshortened uuid(original uuid): 177d1b53-77d5-42b2-8b8f-8d86579deb52
```
-----
##### Example 2: with prefix

```python
from uuid_shortener import UuidShortener
from uuid import uuid4

if __name__ == "__main__":
    print('******** With prefix')

    shortener = UuidShortener('meow')  # ;)
    uuid_4 = uuid4()

    short_uuid = shortener.shorten(uuid_4)
    unshortened_uuid = shortener.unshorten(short_uuid)

    print('Uuid to shorten: {}'.format(str(uuid_4)))
    print('shortened uuid: {}'.format(short_uuid))
    print('unshortened uuid (original uuid): {}'.format(str(shortener.unshorten(short_uuid)), str(uuid_4)))

```

##### Output 2:

```
******** With prefix
Uuid to shorten: 2bea23d4-2b96-485d-8788-0c606ab93319
shortened uuid: meow-6qwbaCZnHtxJsj4uJTKJSV
unshortened uuid (original uuid): 2bea23d4-2b96-485d-8788-0c606ab93319
```


## License

[MIT](./LICENSE)
