# Linux Client Application - OSS Third Party Notices

## Page Title
Twingate Linux Client Application — Open Source Component Licenses

## Summary
This page lists all open-source third-party components bundled in the Twingate Linux client application, along with their respective licenses. It serves as the required legal attribution document for OSS components. No implementation guidance or configuration details are provided.

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
| pubnub | MIT | PubNub (2015) |
| quicly | MIT | Fastly, Kazuho Oku |
| catch2 | Boost 1.0 | Catch2 Authors |
| zlib | zlib License | Jean-loup Gailly, Mark Adler |
| nanopb | zlib License | Petteri Aimonen |
| fmt | MIT-variant | Victor Zverovich |

## Prerequisites
- N/A — This is a legal/compliance reference page only.

## Step-by-Step
- N/A

## Configuration Values
- N/A

## Gotchas
- **fmt** carries an optional exception: embedded object-form compilations may omit copyright/permission notices.
- **siphash** uses CC0 (public domain dedication), not a traditional license — no attribution legally required, but waiver is irrevocable.
- BSD 3-Clause components (**libevent**, **lwip**) prohibit use of contributor names for endorsement without permission.

## Related Docs
- [Twingate Linux Client Setup](https://www.twingate.com/docs/linux)
- OSS notices for other Twingate client platforms (macOS, Windows, iOS, Android)