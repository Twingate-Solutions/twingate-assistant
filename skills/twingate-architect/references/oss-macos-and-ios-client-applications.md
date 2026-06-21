# macOS and iOS Client Applications – OSS Third-Party Notices

## Page Title
Twingate macOS and iOS Client Applications – Open Source Component Licenses

## Summary
This page lists all third-party open source components bundled in Twingate's macOS and iOS client applications, along with their full license texts. It serves as the required third-party notice disclosure for legal compliance purposes. No implementation guidance is provided.

## Key Information

### Components and Their Licenses

| Component | License | Copyright Holder |
|-----------|---------|-----------------|
| libssl | Apache 2.0 | OpenSSL Project |
| libevent | BSD 3-Clause | Niels Provos, Nick Mathewson |
| lwip | BSD 3-Clause | Swedish Institute of Computer Science |
| siphash | CC0 1.0 Universal | — |
| libjansson | MIT | Petri Lehtinen |
| jwt-cpp | MIT | Dominik Thalhammer |
| args | MIT | Taylor C. Richberger, Pavel Belikov |
| Sentry-cocoa | MIT | Sentry |
| pubnub | MIT | PubNub |
| quicly | MIT | Fastly, Kazuho Oku |
| catch2 | Boost Software License 1.0 | Catch2 Authors |
| zlib | zlib License | Jean-loup Gailly, Mark Adler |
| nanopb | zlib License | Petteri Aimonen |
| fmt | MIT-like (with optional exception) | Victor Zverovich |

## Prerequisites
- N/A – This is a legal disclosure page only.

## Step-by-Step
- N/A – No implementation steps; reference only.

## Configuration Values
- N/A

## Gotchas
- `fmt` uses a non-standard license variant: includes an optional exception allowing embedded portions in compiled object form to be redistributed **without** copyright notices.
- `siphash` uses CC0 (public domain dedication), not a traditional license.
- BSD 3-Clause components (`libevent`, `lwip`) prohibit use of contributor names for endorsement without permission.

## Related Docs
- [Twingate OSS Notices – other platforms](#) (check Twingate docs for Windows/Linux equivalents)
- [Twingate Client Documentation](https://www.twingate.com/docs/)