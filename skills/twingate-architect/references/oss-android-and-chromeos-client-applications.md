# Android and ChromeOS Client Applications - OSS Notices

## Page Title
Twingate Android and ChromeOS Client Applications — Open Source Software Notices

## Summary
This page lists all third-party open source components used in the Twingate Android and ChromeOS client applications, along with their respective licenses. It serves as the legal attribution document required by the included open source licenses. No implementation guidance is provided.

## Key Information

### Components by License

| License | Components |
|---------|------------|
| **Apache 2.0** | AndroidX, Dagger 2, Kotlin, libssl (OpenSSL), Logback Android, Moshi, OkHttp, Retrofit, Retrofit Rx adapter, RxAndroid, RxJava, Timber |
| **BSD 3-Clause** | libevent, lwip, Sentry |
| **MIT** | args, jwt-cpp, libjansson, pubnub, quicly, Sentry SDK for Java/Android, SLF4J |
| **CC0 1.0 Universal** | siphash |
| **Boost Software License 1.0** | catch2 |
| **zlib** | nanopb, zlib |
| **Custom (MIT-like)** | fmt |

## Prerequisites
- N/A — reference/legal document only

## Step-by-Step
- N/A — no implementation steps

## Configuration Values
- N/A

## Gotchas
- `libssl` is listed under Apache 2.0 but is part of the OpenSSL project; actual OpenSSL license terms may differ from what is listed here
- `siphash` uses CC0 (public domain dedication), not a traditional license
- `fmt` uses a custom license with an **optional exception** allowing redistribution of embedded portions in compiled object form without copyright notices

## Related Docs
- [Twingate OSS Notices (other platforms)](https://www.twingate.com/docs/) — check for iOS, macOS, Windows, Linux equivalents
- Apache License 2.0: https://www.apache.org/licenses/