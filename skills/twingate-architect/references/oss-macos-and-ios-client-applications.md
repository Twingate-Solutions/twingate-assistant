# macOS and iOS Client Applications - OSS Third Party Notices

## Summary
This page lists all open-source third-party components bundled in Twingate's macOS and iOS client applications, along with their full license texts. It serves as the legal attribution/notice document required by the respective open-source licenses.

## Key Information

- **Purpose**: Legal compliance document listing OSS components and their licenses
- **Platform**: Twingate macOS and iOS client applications

### Components by License

| License | Components |
|---------|-----------|
| Apache 2.0 | `libssl` (OpenSSL Project) |
| BSD 3-Clause | `libevent`, `lwip` |
| CC0 1.0 Universal | `siphash` |
| MIT | `libjansson`, `jwt-cpp`, `args`, `Sentry-cocoa`, `pubnub`, `quicly` |
| Boost Software License 1.0 | `catch2` |
| zlib | `zlib`, `nanopb` |
| Other (MIT-like) | `fmt` |

## Component Details

- **args** – CLI argument parsing (Taylor C. Richberger, 2016–2017)
- **catch2** – C++ testing framework (Catch2 Authors)
- **fmt** – String formatting library (Victor Zverovich, 2012–present)
- **jwt-cpp** – JWT handling (Dominik Thalhammer, 2018)
- **libevent** – Event notification library (Niels Provos / Nick Mathewson, 2000–2012)
- **libjansson** – JSON library (Petri Lehtinen, 2009–2020)
- **libssl** – TLS/SSL (OpenSSL Project, 1998–2020)
- **lwip** – Lightweight TCP/IP stack (Swedish Institute of Computer Science, 2001–2002)
- **nanopb** – Protocol Buffers for embedded systems (Petteri Aimonen, 2011)
- **pubnub** – Real-time messaging (PubNub, 2015)
- **quicly** – QUIC protocol library (Fastly/Kazuho Oku, 2017)
- **Sentry-cocoa** – Error tracking SDK (Sentry, 2015)
- **siphash** – Hash function (CC0 public domain)
- **zlib** – Compression library (Jean-loup Gailly / Mark Adler, 1995–2017)

## Gotchas

- `fmt` includes an **optional exception**: embedded portions in machine-executable object code may be redistributed without the copyright/permission notices
- `siphash` is CC0 (public domain dedication), not a traditional license—no attribution legally required but included for completeness
- BSD 3-Clause components (`libevent`, `lwip`) prohibit using contributor names for endorsement without permission

## Prerequisites
N/A – Reference/legal document only

## Related Docs
- [Twingate OSS Notices (other platforms)](https://www.twingate.com/docs/) – check for Windows/Linux equivalents
- Apache License 2.0: https://www.apache.org/licenses/