# Linux Client Application - OSS Third Party Notices

## Page Title
Linux Client Application (Open Source Components / Third Party Notices)

## Summary
This page lists all open source components bundled in the Twingate Linux client application along with their respective licenses. It serves as the legal attribution document required for OSS license compliance. No implementation guidance is provided.

## Key Information

### Components and Licenses

| Component | License | Copyright |
|-----------|---------|-----------|
| libssl | Apache 2.0 | OpenSSL Project 1998-2020 |
| libevent | BSD 3-Clause | Niels Provos 2000-2012 |
| lwip | BSD 3-Clause | Swedish Institute of Computer Science 2001-2002 |
| siphash | CC0 1.0 Universal | (public domain dedication) |
| libjansson | MIT | Petri Lehtinen 2009-2020 |
| jwt-cpp | MIT | Dominik Thalhammer 2018 |
| args | MIT | Taylor C. Richberger 2016-2017 |
| pubnub | MIT | PubNub 2015 |
| quicly | MIT | Fastly, Kazuho Oku 2017 |
| catch2 | Boost Software License 1.0 | Catch2 Authors |
| zlib | zlib License | Jean-loup Gailly & Mark Adler 1995-2017 |
| nanopb | zlib License | Petteri Aimonen 2011 |
| fmt | MIT-style (with embedding exception) | Victor Zverovich 2012-present |

## Prerequisites
- N/A (informational/legal page only)

## Step-by-Step
- N/A

## Configuration Values
- N/A

## Gotchas
- **fmt** has a non-standard license exception: embedded portions in compiled object code may be redistributed without including copyright notices
- **siphash** uses CC0 (public domain dedication), not a traditional OSS license — no attribution required but trademark/patent rights are not waived
- BSD 3-Clause components (libevent, lwip) prohibit using contributor names for endorsement without permission

## Related Docs
- Twingate Linux Client installation documentation
- Other platform OSS notices (macOS, Windows, iOS, Android clients)