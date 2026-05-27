# Android and ChromeOS Client Applications - OSS Notices

## Page Title
Open Source Software (OSS) Notices: Android and ChromeOS Client Applications

## Summary
This page lists all third-party open source components used in Twingate's Android and ChromeOS client applications, along with their respective licenses. It serves as the legal attribution document required by the included open source licenses. No implementation guidance is provided.

## Key Information

### Components by License

| License | Components |
|---------|-----------|
| Apache 2.0 | AndroidX, Dagger 2, Kotlin, libssl, Logback Android, Moshi, OkHttp, Retrofit, Retrofit Rx adapter, RxAndroid, RxJava, Timber |
| BSD 3-Clause | libevent, lwip, Sentry |
| MIT | args, jwt-cpp, libjansson, pubnub, quicly, Sentry SDK for Java and Android, SLF4J |
| zlib | nanopb, zlib |
| Boost Software License 1.0 | catch2 |
| CC0 1.0 Universal | siphash |
| Custom (MIT-like) | fmt |

## Prerequisites
N/A — Reference/legal document only.

## Step-by-Step
N/A — No implementation steps.

## Configuration Values
N/A

## Gotchas
- **fmt** uses a non-standard license with an optional exception: embedded portions in compiled object code may be redistributed without the copyright/permission notice.
- **Sentry** appears under both BSD 3-Clause (native SDK) and MIT (Java/Android SDK) — two separate components with different licenses.
- Apache 2.0 components require NOTICE file preservation when redistributing derivative works.
- BSD 3-Clause components prohibit using contributor names for endorsement without permission.

## Related Docs
- Twingate OSS notices for other platforms (iOS, macOS, Windows, Linux clients)
- [Apache License 2.0](http://www.apache.org/licenses/)