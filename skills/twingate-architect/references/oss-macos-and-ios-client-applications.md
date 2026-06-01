# macOS and iOS Client Applications – OSS Third-Party Notices

## Page Title
Twingate macOS and iOS Client Applications – Open Source Component Licenses

## Summary
This page lists all third-party open source components bundled in Twingate's macOS and iOS client applications, along with their full license texts. It serves as the legally required third-party notice disclosure for the client software.

## Key Information

### Components and Their Licenses

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
| fmt | MIT-style + optional exception | Victor Zverovich |

## Prerequisites
- N/A – informational/legal disclosure page only

## Step-by-Step
- N/A – no actionable procedures

## Configuration Values
- N/A

## Gotchas
- **fmt exception**: The `fmt` library includes an optional license exception allowing embedded portions in compiled object form to be redistributed without including copyright notices
- **siphash** uses CC0 (public domain dedication), not a traditional open-source license; no attribution technically required
- **Apache 2.0 (libssl)**: If redistributing modified versions, you must retain NOTICE files and mark changed files explicitly
- **BSD 3-Clause**: Cannot use copyright holders' names to endorse derived products without permission

## Related Docs
- [Twingate OSS notices for other platforms] (check sibling pages for Windows/Linux/Android equivalents)
- [Twingate Client documentation](https://www.twingate.com/docs/)