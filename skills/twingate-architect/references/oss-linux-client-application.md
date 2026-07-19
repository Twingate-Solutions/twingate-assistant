# Linux Client Application - OSS Third Party Notices

## Page Title
Twingate Linux Client Application — Open Source Components & Licenses

## Summary
This page documents the open-source third-party components bundled in the Twingate Linux client application. It serves as the legal third-party notice disclosure required by the licenses of each included component. No implementation guidance or configuration details are provided.

## Key Information

### Components Included
| Component | License |
|-----------|---------|
| libssl | Apache 2.0 |
| libevent, lwip | BSD 3-Clause |
| siphash | CC0 1.0 Universal |
| libjansson, jwt-cpp, args, pubnub, quicly | MIT |
| catch2 | Boost Software License 1.0 |
| zlib, nanopb | zlib License |
| fmt | MIT-like (with optional exception) |

### License Summary by Type
- **Apache 2.0**: Requires license copy, notice file, and change documentation on redistribution
- **BSD 3-Clause**: Prohibits use of contributor names for endorsement without permission
- **CC0 1.0**: Public domain dedication; no restrictions on use
- **MIT**: Requires copyright notice inclusion in copies/substantial portions
- **Boost 1.0**: Similar to MIT; copyright notice required except in binary-only distributions
- **zlib**: Prohibits misrepresentation of origin; notice must be preserved in source distributions

## Prerequisites
- N/A — this is a legal disclosure page, not a setup guide

## Step-by-Step
- N/A

## Configuration Values
- N/A

## Gotchas
- **fmt** includes an optional exception: embedded portions in machine-executable object code may be redistributed without including copyright/permission notices
- **catch2** (Boost license) does not require copyright notices in binary-only (machine-executable object code) distributions — differs from MIT
- **CC0 (siphash)** does **not** waive trademark or patent rights

## Related Docs
- Twingate Linux Client installation documentation
- Other platform OSS notices (macOS, Windows, iOS, Android clients)