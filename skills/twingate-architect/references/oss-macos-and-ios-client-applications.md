# Twingate macOS and iOS Client Applications – OSS Third-Party Notices

## Page Title
macOS and iOS Client Applications (Open Source Component Licenses)

## Summary
This page lists all third-party open source components bundled in Twingate's macOS and iOS client applications, along with their full license texts. It serves as the legal third-party notices disclosure required by each component's license. No implementation guidance is provided.

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
| fmt | MIT-like (with object code exception) | Victor Zverovich |

## Prerequisites
- N/A (reference/legal document only)

## Step-by-Step
- N/A (no procedural content)

## Configuration Values
- N/A

## Gotchas
- **fmt** has a non-standard license with an optional exception: embedded object code portions may be redistributed without including copyright/permission notices
- **siphash** uses CC0 (public domain dedication), not a traditional license — no attribution required
- BSD 3-Clause components (**libevent**, **lwip**) prohibit use of contributor names for endorsement without permission

## Related Docs
- [Twingate OSS notices for other platforms] (see sidebar for Windows/Linux equivalents)
- Twingate Client installation documentation