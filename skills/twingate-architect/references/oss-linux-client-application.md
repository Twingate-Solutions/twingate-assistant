# Linux Client Application – OSS Third-Party Notices

## Page Title
Linux Client Application (Open Source Components & Licenses)

## Summary
This page documents the open-source software components bundled in the Twingate Linux client application. It lists each third-party library along with its applicable license text. No installation or configuration guidance is provided—this is a legal/compliance reference page.

## Key Information

### Components and Licenses

| Component | License |
|-----------|---------|
| libssl | Apache 2.0 |
| libevent, lwip | BSD 3-Clause |
| siphash | CC0 1.0 Universal |
| libjansson, jwt-cpp, args, pubnub, quicly | MIT |
| catch2 | Boost Software License 1.0 |
| zlib, nanopb | zlib License |
| fmt | MIT-style (with embedded object code exception) |

## Prerequisites
- None. This is a reference/compliance document only.

## Step-by-Step
- N/A (informational page only)

## Configuration Values
- None

## Gotchas
- **fmt exception**: Unlike standard MIT, `fmt` includes an optional exception allowing redistribution of embedded object code without copyright notice requirements.
- **siphash** uses CC0 (public domain dedication), not a traditional license—no attribution required.
- **catch2** (Boost license) requires copyright notices in all copies unless distributed solely as machine-executable object code.
- **Apache 2.0 (libssl)** requires NOTICE file preservation and prominent modification notices—stricter than MIT for redistribution scenarios.

## Related Docs
- Twingate Linux Client installation documentation
- Twingate general OSS/third-party notices