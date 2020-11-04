from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRES = ['pybaseconv==0.*']

setup(
    name="uuid-shortener-py",
    version="0.0.3",
    author="Samira El Aabidi",
    url='https://github.com/El-Sam/uuid_shortener',
    author_email="sam.elaabidi@gmail.com",
    keywords=["Python", "UUID", "UUID Shortener", "Hex base", "Short URL"],
    description="Shorten a uuid into a URL friendly format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=REQUIRES,
    packages=['uuid_shortener'],
    classifiers=(
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
