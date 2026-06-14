# Linux Client Application - OSS Third Party Notices

## Page Title
Twingate Linux Client Application — Open Source Component Licenses

## Summary
This page lists all third-party open source components bundled in the Twingate Linux client application, along with their full license texts. It serves as the legal third-party notice disclosure required by the respective open source licenses.

## Key Information

- **Purpose**: Legal compliance disclosure for OSS components used in the Linux client
- **Total components**: 13 third-party libraries
- **License types used**: Apache 2.0, BSD 3-Clause, CC0 1.0 Universal, MIT, Boost Software License 1.0, zlib, and a custom MIT-variant (fmt)

## Component License Matrix

| Component | License | Copyright Holder |
|-----------|---------|-----------------|
| libssl | Apache 2.0 | OpenSSL Project |
| libevent | BSD 3-Clause | Niels Provos, Nick Mathewson |
| lwip | BSD 3-Clause | Swedish Institute of Computer Science |
| siphash | CC0 1.0 Universal | — |
| libjansson | MIT | Petri Lehtinen |
| jwt-cpp | MIT | Dominik Thalhammer |
| args | MIT | Taylor C. Richberger, Pavel Belikov |
| pubnub | MIT | PubNub |
| quicly | MIT | Fastly, Kazuho Oku |
| catch2 | Boost Software License 1.0 | Catch2 Authors |
| zlib | zlib License | Jean-loup Gailly, Mark Adler |
| nanopb | zlib License | Petteri Aimonen |
| fmt | MIT-variant (custom) | Victor Zverovich |

## Prerequisites
- N/A — informational/legal page only

## Step-by-Step
- N/A — no actionable steps

## Configuration Values
- N/A

## Gotchas
- **fmt exception**: The `fmt` library includes an optional exception allowing embedded portions in machine-executable object code to be redistributed without the copyright notice — differs slightly from standard MIT
- **BSD 3-Clause restriction**: Components `libevent` and `lwip` prohibit use of copyright holder names for endorsement without written permission
- **catch2 (Boost)**: Requires copyright notices in all copies unless distributed solely as machine-executable object code

## Related Docs
- Twingate Linux Client installation documentation
- Other platform OSS notices (macOS, Windows, iOS, Android clients)