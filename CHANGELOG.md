# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2020-11-05
### Added
- A one-way generator of the shortened uuids with unit tests and example.
- CHANGELOG file


## [1.0.0] - 2020-11-04
### Added
- Support for Python 3.7 & Python 3.8
- Min test coverage of 100%

### Changed
- Start using f-strings in the examples

### Removed
- pep8 pytest plugin as it causes deprecation errors
- Support for Python 3.5


## [0.0.2] - 2018-06-22
### Fixed
- add left zero padding when the resulted uuid is shorter than 32 characters


## [0.0.1] - 2018-05-28
### Added
- Uuid Shortener with optional prefix 
