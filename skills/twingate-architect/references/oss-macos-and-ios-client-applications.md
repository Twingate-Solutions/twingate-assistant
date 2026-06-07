# Twingate macOS and iOS Client Applications – OSS Third-Party Notices

## Page Title
macOS and iOS Client Applications (Open Source Components & Licenses)

## Summary
This page lists all third-party open source components bundled in Twingate's macOS and iOS client applications, along with their respective licenses. It serves as the required legal attribution/notice document for OSS compliance. No implementation guidance is provided.

## Key Information

### Components and Licenses

| Component | License | Copyright Holder |
|-----------|---------|-----------------|
| libssl | Apache 2.0 | OpenSSL Project |
| libevent | BSD 3-Clause | Niels Provos, Nick Mathewson |
| lwip | BSD 3-Clause | Swedish Institute of Computer Science |
| siphash | CC0 1.0 Universal | (public domain dedication) |
| libjansson | MIT | Petri Lehtinen |
| jwt-cpp | MIT | Dominik Thalhammer |
| args | MIT | Taylor C. Richberger, Pavel Belikov |
| Sentry-cocoa | MIT | Sentry |
| pubnub | MIT | PubNub |
| quicly | MIT | Fastly, Kazuho Oku |
| catch2 | Boost Software License 1.0 | Catch2 Authors |
| zlib | zlib License | Jean-loup Gailly, Mark Adler |
| nanopb | zlib License | Petteri Aimonen |
| fmt | MIT-variant (with object code exception) | Victor Zverovich |

## Prerequisites
- N/A (legal reference document only)

## Step-by-Step
- N/A

## Configuration Values
- N/A

## Gotchas
- **fmt** uses a non-standard MIT variant: includes an exception allowing redistribution of embedded object code without copyright notices — differs from standard MIT
- **siphash** is CC0 (public domain dedication), not a traditional license; trademark/patent rights are explicitly **not** waived under CC0
- BSD 3-Clause components (libevent, lwip) prohibit use of contributor names for endorsement without permission

## Related Docs
- Twingate OSS notices for other platforms (Linux, Windows clients)
- [Apache License 2.0](http://www.apache.org/licenses/)