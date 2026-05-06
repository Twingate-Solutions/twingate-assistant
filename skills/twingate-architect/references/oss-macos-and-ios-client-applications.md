# Twingate macOS and iOS Client Applications – OSS Notices

## Page Title
macOS and iOS Client Applications (Open Source Software Notices)

## Summary
This page lists all third-party open source components used in Twingate's macOS and iOS client applications, along with their respective licenses. It serves as the legal attribution/notice document required by the included OSS licenses. No implementation guidance is provided.

## Key Information

### Components and Licenses

| Component | License | Copyright Holder |
|-----------|---------|-----------------|
| libssl | Apache 2.0 | OpenSSL Project (1998–2020) |
| libevent | BSD 3-Clause | Niels Provos, Nick Mathewson |
| lwip | BSD 3-Clause | Swedish Institute of Computer Science |
| siphash | CC0 1.0 Universal | (public domain dedication) |
| libjansson | MIT | Petri Lehtinen |
| jwt-cpp | MIT | Dominik Thalhammer |
| args | MIT | Taylor C. Richberger, Pavel Belikov |
| Sentry-cocoa | MIT | Sentry (2015) |
| pubnub | MIT | PubNub (2015) |
| quicly | MIT | Fastly, Kazuho Oku |
| catch2 | Boost 1.0 | Catch2 Authors |
| zlib | zlib License | Jean-loup Gailly, Mark Adler |
| nanopb | zlib License | Petteri Aimonen |
| fmt | MIT-like + optional exception | Victor Zverovich |

## Prerequisites
- N/A – Reference/legal document only

## Step-by-Step
- N/A – No procedural content

## Configuration Values
- N/A

## Gotchas
- **fmt** has an optional license exception: embedded portions in compiled machine-executable object form may be redistributed without including copyright/permission notices
- **siphash** uses CC0 (public domain dedication), not a traditional OSS license; no attribution legally required, but fallback license grant exists if waiver is invalid
- BSD 3-Clause components (libevent, lwip) prohibit use of contributor names for endorsement without permission

## Related Docs
- Twingate OSS notices for other platforms (Linux, Windows clients)
- [Apache License 2.0](http://www.apache.org/licenses/)