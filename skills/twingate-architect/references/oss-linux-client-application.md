---
source: https://www.twingate.com/docs/oss-linux-client-application
type: docs
fetched: 2026-08-14
source_version: 4411ae11bdbba4acba5a1bc1375372855b66f9c6e3685b3fc04d814f079bbf46
---

# Linux Client Application - OSS Third-Party Notices

## Page Title
Twingate Linux Client Application – Open Source Component Licenses

## Summary
This page documents the open-source software components used in the Twingate Linux client application. It provides full license texts for all third-party dependencies. This is a legal/compliance reference page with no configuration or setup guidance.

## Key Information

### Components by License

| License | Components |
|---------|-----------|
| Apache 2.0 | `libssl` (OpenSSL Project) |
| BSD 3-Clause | `libevent`, `lwip` |
| CC0 1.0 Universal | `siphash` |
| MIT | `libjansson`, `jwt-cpp`, `args`, `pubnub`, `quicly` |
| Boost 1.0 | `catch2` |
| zlib | `zlib`, `nanopb` |
| Custom (MIT-like) | `fmt` |

### Component Purposes
- **libssl** – TLS/SSL cryptography
- **libevent** – Async event notification
- **lwip** – Lightweight TCP/IP stack
- **jwt-cpp** – JWT token handling
- **quicly** – QUIC protocol implementation
- **pubnub** – Real-time messaging
- **nanopb** – Protocol Buffers (small footprint)
- **catch2** – C++ testing framework
- **fmt** – String formatting
- **args** – CLI argument parsing
- **libjansson** – JSON handling
- **siphash** – Hash function

## Prerequisites
N/A – Reference/compliance page only.

## Step-by-Step
N/A – No configuration steps.

## Configuration Values
None.

## Gotchas
- `fmt` includes an **optional exception**: embedded portions in machine-executable object code may be redistributed without including copyright/permission notices.
- `siphash` is CC0 (public domain dedication), not a traditional license — no attribution required.
- Redistribution of Apache 2.0 components requires preserving NOTICE files if present.

## Related Docs
- [Twingate Linux Client Setup](https://www.twingate.com/docs/linux)
- [Twingate OSS notices for other platforms] (check Twingate docs for macOS/Windows equivalents)