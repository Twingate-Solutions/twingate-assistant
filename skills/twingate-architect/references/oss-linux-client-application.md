# Linux Client Application - OSS Third Party Notices

## Page Title
Twingate Linux Client Application — Open Source Component Licenses

## Summary
This page documents the open-source software components bundled in the Twingate Linux client application. It lists all third-party libraries with their applicable licenses and copyright holders. No installation or configuration guidance is provided.

## Key Information

**Components and Licenses:**

| Component | License | Copyright |
|-----------|---------|-----------|
| libssl | Apache 2.0 | OpenSSL Project (1998-2020) |
| libevent | BSD 3-Clause | Niels Provos, Nick Mathewson |
| lwip | BSD 3-Clause | Swedish Institute of Computer Science |
| siphash | CC0 1.0 Universal | — |
| libjansson | MIT | Petri Lehtinen (2009-2020) |
| jwt-cpp | MIT | Dominik Thalhammer (2018) |
| args | MIT | Taylor C. Richberger, Pavel Belikov |
| pubnub | MIT | PubNub (2015) |
| quicly | MIT | Fastly, Kazuho Oku (2017) |
| catch2 | Boost 1.0 | Catch2 Authors |
| zlib | zlib License | Jean-loup Gailly, Mark Adler |
| nanopb | zlib License | Petteri Aimonen (2011) |
| fmt | MIT-variant | Victor Zverovich (2012-present) |

## Prerequisites
- None (reference/compliance document only)

## Step-by-Step
N/A — This is a legal/compliance reference page only.

## Configuration Values
None.

## Gotchas
- **fmt** uses a non-standard MIT variant with an additional exception: embedded portions in compiled object code may be redistributed without copyright notices
- **siphash** uses CC0 (public domain dedication), not a traditional license — no attribution required
- BSD 3-Clause components (libevent, lwip) prohibit using contributor names for endorsement without permission

## Related Docs
- Twingate Linux Client installation documentation
- Other platform OSS notices (macOS, Windows, iOS, Android clients)