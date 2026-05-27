# Twingate macOS and iOS Client Applications – OSS Notices

## Page Title
macOS and iOS Client Applications (Open Source Software Notices)

## Summary
This page lists all third-party open source components bundled in the Twingate macOS and iOS client applications, along with their respective licenses. It serves as the required legal attribution document for OSS components. No implementation or configuration guidance is provided.

## Key Information

### Components and Licenses

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
| fmt | MIT-like (with object-form exception) | Victor Zverovich (2012–present) |

## Prerequisites
- N/A (legal/attribution reference only)

## Step-by-Step
- N/A

## Configuration Values
- N/A

## Gotchas
- **fmt** has a non-standard license exception: embedded portions in machine-executable object form may be redistributed without including copyright/permission notices.
- **siphash** uses CC0 (public domain dedication), not a traditional OSS license — no attribution legally required, but noted here.
- BSD 3-Clause components (libevent, lwip) prohibit using contributor names for endorsement without permission.

## Related Docs
- [Twingate OSS Notices – other platforms] (see sibling pages in the OSS section)
- Twingate Client Installation documentation