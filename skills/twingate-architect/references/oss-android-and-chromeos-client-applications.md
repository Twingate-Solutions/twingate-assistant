# Android and ChromeOS Client Applications - OSS Components

## Page Title
Twingate Android and ChromeOS Client Applications – Open Source Components & Third-Party Notices

## Summary
This page lists all open-source third-party components used in Twingate's Android and ChromeOS client applications, along with their respective licenses. It serves as the legal third-party notice document for the client. No implementation guidance is provided.

## Key Information

### Components by License

| License | Components |
|---------|-----------|
| Apache 2.0 | libssl, AndroidX, Dagger 2, Kotlin, Logback Android, Moshi, OkHttp, Retrofit, Retrofit Rx adapter, RxAndroid, RxJava, Timber |
| BSD 3-Clause | libevent, lwip, Sentry |
| MIT | libjansson, jwt-cpp, args, Sentry SDK for Java and Android, SLF4J, pubnub, quicly |
| zlib | zlib, nanopb |
| Boost Software License 1.0 | catch2 |
| CC0 1.0 Universal | siphash |
| Other (MIT-like) | fmt |

## Prerequisites
- N/A (informational/legal page only)

## Step-by-Step
- N/A

## Configuration Values
- N/A

## Gotchas
- `siphash` uses CC0 1.0 (public domain dedication), not a standard OSI license — no attribution legally required, but trademark/patent rights are **not** waived under CC0.
- `fmt` includes an optional embedded-binary exception to its MIT-style license, permitting redistribution of embedded portions without copyright notices.
- BSD 3-Clause components (`libevent`, `lwip`, `Sentry`) prohibit use of contributor names for endorsement without permission.
- Apache 2.0 redistribution requires including a copy of the license and marking modified files.

## Related Docs
- Twingate OSS notices for other platforms (iOS, Windows, Linux, macOS clients)
- [Apache License 2.0](http://www.apache.org/licenses/)