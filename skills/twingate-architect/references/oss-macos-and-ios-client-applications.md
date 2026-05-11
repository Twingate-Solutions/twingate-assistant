# macOS and iOS Client Applications – OSS Third-Party Notices

## Page Title
Twingate macOS and iOS Client Applications – Open Source Components & Licenses

## Summary
This page lists all third-party open source components bundled in Twingate's macOS and iOS client applications, along with their full license texts. It serves as the required legal attribution/notice document for OSS compliance. No implementation guidance is provided.

## Key Information

### Components and Their Licenses

| Component | License | Copyright Holder |
|-----------|---------|-----------------|
| libssl | Apache 2.0 | OpenSSL Project (1998–2020) |
| libevent | BSD 3-Clause | Niels Provos, Nick Mathewson |
| lwip | BSD 3-Clause | Swedish Institute of Computer Science |
| siphash | CC0 1.0 Universal | (public domain dedication) |
| libjansson | MIT | Petri Lehtinen (2009–2020) |
| jwt-cpp | MIT | Dominik Thalhammer (2018) |
| args | MIT | Taylor C. Richberger, Pavel Belikov |
| Sentry-cocoa | MIT | Sentry (2015) |
| pubnub | MIT | PubNub (2015) |
| quicly | MIT | Fastly, Kazuho Oku (2017) |
| catch2 | Boost 1.0 | Catch2 Authors |
| zlib | zlib License | Jean-loup Gailly, Mark Adler |
| nanopb | zlib License | Petteri Aimonen (2011) |
| fmt | MIT-style + optional exception | Victor Zverovich (2012–present) |

## Prerequisites
- N/A (legal/compliance reference document only)

## Step-by-Step
- N/A

## Configuration Values
- N/A

## Gotchas
- **fmt** has an additional license exception: embedded portions in machine-executable object code may be redistributed without including the copyright/permission notices
- **siphash** uses CC0 (public domain dedication), not a traditional license — no attribution strictly required, but CC0 fallback license applies if waiver is legally invalid in a jurisdiction
- **BSD 3-Clause** components (libevent, lwip) prohibit using contributor names for endorsement of derived products without permission

## Related Docs
- [Twingate OSS notices for other platforms] (see sibling pages in the OSS section)
- Apache License 2.0: http://www.apache.org/licenses/