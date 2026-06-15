# macOS and iOS Client Applications — OSS Third-Party Notices

## Page Title
Twingate macOS and iOS Client Applications — Open Source Component Licenses

## Summary
This page lists all third-party open source components bundled in Twingate's macOS and iOS client applications, along with their full license texts. It serves as the required legal attribution notice for redistributed open source software.

## Key Information

### Component Inventory by License

| License | Components |
|---------|------------|
| Apache 2.0 | libssl |
| BSD 3-Clause | libevent, lwip |
| CC0 1.0 Universal | siphash |
| MIT | libjansson, jwt-cpp, args, Sentry-cocoa, pubnub, quicly |
| Boost Software License 1.0 | catch2 |
| zlib | zlib, nanopb |
| Custom (MIT-like) | fmt |

### Component Purposes
- **args** — CLI argument parsing
- **catch2** — C++ testing framework
- **fmt** — String formatting
- **jwt-cpp** — JWT token handling
- **libevent** — Event notification library
- **libjansson** — JSON library
- **libssl** — TLS/SSL (OpenSSL)
- **lwip** — Lightweight TCP/IP stack
- **nanopb** — Protocol Buffers for embedded systems
- **pubnub** — Real-time messaging
- **quicly** — QUIC protocol implementation
- **Sentry-cocoa** — Crash reporting (iOS/macOS)
- **siphash** — Hash function
- **zlib** — Data compression

## Prerequisites
- N/A — Reference/legal documentation only

## Step-by-Step
- N/A — No implementation steps; informational page only

## Configuration Values
- N/A

## Gotchas
- **fmt** uses a custom license (MIT-like) with an added exception: embedded portions in compiled object code may be redistributed without the copyright notice
- **siphash** uses CC0 1.0 (public domain dedication), not a traditional OSS license — no attribution required but trademark/patent rights are explicitly not waived
- **libssl** is Apache 2.0 (OpenSSL project), not the historical OpenSSL license — redistribution requires NOTICE file inclusion

## Related Docs
- [Twingate OSS notices for other platforms] (see sibling pages in the OSS section)
- Apache License 2.0: http://www.apache.org/licenses/