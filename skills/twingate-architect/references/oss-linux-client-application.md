# Linux Client Application – OSS Third-Party Notices

## Page Title
Linux Client Application (Open Source Components & Licenses)

## Summary
This page lists all open-source components bundled in the Twingate Linux client application along with their full license texts. It serves as the required third-party notice disclosure for the Linux client. No installation or configuration guidance is provided.

## Key Information

### Components and Licenses

| Component | License | Notable Copyright |
|-----------|---------|-------------------|
| libssl | Apache 2.0 | OpenSSL Project, 1998–2020 |
| libevent | BSD 3-Clause | Niels Provos, 2000–2012 |
| lwip | BSD 3-Clause | Swedish Institute of Computer Science |
| siphash | CC0 1.0 Universal | Public domain dedication |
| libjansson | MIT | Petri Lehtinen, 2009–2020 |
| jwt-cpp | MIT | Dominik Thalhammer, 2018 |
| args | MIT | Taylor C. Richberger, 2016–2017 |
| pubnub | MIT | PubNub, 2015 |
| quicly | MIT | Fastly/Kazuho Oku, 2017 |
| catch2 | Boost 1.0 | Catch2 Authors |
| zlib | zlib License | Jean-loup Gailly & Mark Adler |
| nanopb | zlib License | Petteri Aimonen, 2011 |
| fmt | MIT-variant | Victor Zverovich, 2012–present |

## Prerequisites
- None (reference/legal document only)

## Step-by-Step
N/A – This is a legal notices page, not a setup guide.

## Configuration Values
N/A

## Gotchas
- **fmt** uses a non-standard MIT variant with an embedding exception: embedded object-form portions may be redistributed without including copyright/permission notices.
- **siphash** is CC0 (public domain dedication), not a traditional license — no attribution required.
- BSD 3-Clause components (**libevent**, **lwip**) prohibit using contributor names for endorsement without permission.

## Related Docs
- [Twingate Linux Client Setup](https://www.twingate.com/docs/linux)
- Other platform OSS notices (macOS, Windows clients)