# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-01-16

### Added
- Initial release of `bgg-pi`.
- Fully asynchronous `BggClient` using `aiohttp`.
- Support for fetching user plays (`fetch_plays`).
- Support for recording plays securely (`record_play`).
- Support for fetching user collections with extensive filtering (`fetch_collection`).
- Support for fetching rich game metadata (`fetch_thing_details`).
- Full test suite with 100% core coverage.
- GitHub Actions for CI (testing/linting) and CD (PyPI publishing).
