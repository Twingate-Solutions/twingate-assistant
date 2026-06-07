# Linux Client Application - OSS Third Party Notices

## Page Title
Twingate Linux Client Application – Open Source Component Licenses

## Summary
This page documents the open-source software components bundled in the Twingate Linux client application. It lists each third-party library along with its applicable license text. This is a legal compliance/attribution page, not an implementation guide.

## Key Information

### Components and Their Licenses

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
| fmt | MIT-like (with embedding exception) | Victor Zverovich |

## Prerequisites
- N/A – informational/legal page only

## Step-by-Step
- N/A – no implementation steps

## Configuration Values
- N/A

## Gotchas
- **fmt** has an additional exception: embedded portions in compiled object form may be redistributed without including copyright/permission notices
- **siphash** uses CC0 (public domain dedication), not a traditional license; no attribution required but patent/trademark rights are not waived
- **Apache 2.0** (libssl) has explicit patent license termination clauses if litigation is initiated
- **BSD 3-Clause** prohibits using contributor names for endorsement without permission

## Related Docs
- Twingate Linux Client installation documentation
- Other platform OSS notices (macOS, Windows, iOS, Android clients)