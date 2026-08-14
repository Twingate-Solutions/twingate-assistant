---
source: https://www.twingate.com/docs/oss-macos-and-ios-client-applications
type: docs
fetched: 2026-08-14
source_version: b5a1f8a3e35c2b530ac7db79ed514e33a4bdcb205f6947c4f96a6e462d557b72
---

# Twingate macOS and iOS Client Applications – OSS Notices

## Page Title
macOS and iOS Client Applications – Open Source Component Licenses

## Summary
This page lists all third-party open source components bundled in Twingate's macOS and iOS client applications, along with their full license texts. It serves as the legally required third-party notice disclosure for these clients.

## Key Information

**Components included:**
| Component | License |
|-----------|---------|
| libssl | Apache 2.0 |
| libevent, lwip | BSD 3-Clause |
| siphash | CC0 1.0 Universal |
| libjansson, jwt-cpp, args, Sentry-cocoa, pubnub, quicly | MIT |
| catch2 | Boost Software License 1.0 |
| zlib, nanopb | zlib License |
| fmt | MIT-variant (with embedded object code exception) |

## Prerequisites
- None — reference/compliance document only

## Step-by-Step
N/A — informational/legal disclosure page

## Configuration Values
N/A

## Gotchas
- **fmt** has a non-standard license with an additional exception: embedded portions in machine-executable object code may be redistributed without including copyright/permission notices
- **siphash** uses CC0 (public domain dedication), not a traditional license — no attribution required, but trademark/patent rights are not waived
- BSD 3-Clause components (libevent, lwip) prohibit using contributor names for endorsement without permission

## Related Docs
- [Twingate OSS notices for other platforms] (Linux/Windows client equivalents, if available)
- Twingate main client documentation for macOS/iOS deployment