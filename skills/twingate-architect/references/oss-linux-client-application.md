# Linux Client Application - OSS Third Party Notices

## Page Title
Linux Client Application – Open Source Component Licenses

## Summary
This page lists all open-source third-party components bundled in the Twingate Linux client application, along with their respective licenses. It serves as the required legal attribution document for OSS components. No installation or configuration guidance is provided.

## Key Information

### Components and Licenses

| Component | License | Copyright Holder |
|-----------|---------|-----------------|
| libssl | Apache 2.0 | OpenSSL Project / Eric A. Young |
| libevent | BSD 3-Clause | Niels Provos, Nick Mathewson |
| lwip | BSD 3-Clause | Swedish Institute of Computer Science |
| siphash | CC0 1.0 Universal | (public domain dedication) |
| libjansson | MIT | Petri Lehtinen |
| jwt-cpp | MIT | Dominik Thalhammer |
| args | MIT | Taylor C. Richberger, Pavel Belikov |
| pubnub | MIT | PubNub |
| quicly | MIT | Fastly, Kazuho Oku |
| catch2 | Boost Software License 1.0 | Catch2 Authors |
| zlib | zlib License | Jean-loup Gailly, Mark Adler |
| nanopb | zlib License | Petteri Aimonen |
| fmt | MIT-like (with object-code exception) | Victor Zverovich |

## Prerequisites
- N/A — reference/legal document only

## Step-by-Step
- N/A — no actionable steps

## Configuration Values
- N/A

## Gotchas
- **fmt** has an additional exception: embedded object-code distributions do not require inclusion of copyright notices, unlike standard MIT
- **siphash** uses CC0 (public domain dedication), not a traditional OSS license — no attribution legally required, but noted for completeness
- **catch2** (Boost License) requires copyright notices only in source/binary distributions, not in machine-executable object code

## Related Docs
- Twingate Linux Client installation docs
- Other platform OSS notices (macOS, Windows, iOS, Android clients)