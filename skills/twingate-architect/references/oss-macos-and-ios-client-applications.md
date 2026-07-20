# Twingate macOS and iOS Client Applications - OSS Third Party Notices

## Page Title
macOS and iOS Client Applications (Open Source Third Party Notices)

## Summary
This page lists all third-party open source components bundled in Twingate's macOS and iOS client applications, along with their full license texts. It serves as the required legal attribution notice for OSS components used in the clients.

## Key Information

- **Total components**: 14 third-party libraries
- **License breakdown**:
  - **Apache 2.0**: `libssl` (OpenSSL Project)
  - **BSD 3-Clause**: `libevent`, `lwip`
  - **CC0 1.0 Universal**: `siphash`
  - **MIT**: `libjansson`, `jwt-cpp`, `args`, `Sentry-cocoa`, `pubnub`, `quicly`
  - **Boost Software License 1.0**: `catch2`
  - **zlib**: `zlib`, `nanopb`
  - **Custom (MIT-like)**: `fmt` (with embedded object code exception)

## Component Inventory

| Component | License | Purpose |
|-----------|---------|---------|
| args | MIT | CLI argument parsing |
| catch2 | Boost 1.0 | Testing framework |
| fmt | Custom/MIT-like | String formatting |
| jwt-cpp | MIT | JWT handling |
| libevent | BSD 3-Clause | Event notification |
| libjansson | MIT | JSON processing |
| libssl | Apache 2.0 | TLS/SSL (OpenSSL) |
| lwip | BSD 3-Clause | Lightweight TCP/IP stack |
| nanopb | zlib | Protocol Buffers (small footprint) |
| pubnub | MIT | Real-time messaging |
| quicly | MIT | QUIC protocol |
| Sentry-cocoa | MIT | Error reporting |
| siphash | CC0 1.0 | Hash function |
| zlib | zlib | Compression |

## Prerequisites
- None (informational/legal page only)

## Configuration Values
- None applicable

## Gotchas
- **`fmt` has an embedded object code exception**: redistribution of compiled object code does not require including the copyright notice — unlike standard MIT
- **`siphash` uses CC0** (public domain dedication), not a standard permissive license; no attribution legally required but included here
- **`libssl` is Apache 2.0**, not OpenSSL License — relevant if combining with GPL code (Apache 2.0 + GPLv3 is compatible; Apache 2.0 + GPLv2 is not)
- `catch2` (Boost 1.0) only requires copyright notice inclusion in source/non-object-code distributions

## Related Docs
- Twingate OSS notices for other platforms (Linux, Windows clients likely have separate pages)
- [Twingate Client documentation](https://www.twingate.com/docs/)