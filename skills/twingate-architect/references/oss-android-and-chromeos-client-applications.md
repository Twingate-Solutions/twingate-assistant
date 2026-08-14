---
source: https://www.twingate.com/docs/oss-android-and-chromeos-client-applications
type: docs
fetched: 2026-08-14
source_version: 1c9f5ecf995e85526e3e966c55ac7969b2fdf50d4d58f60f9c9f0c463ea18f07
---

# Android and ChromeOS Client Applications - OSS Notices

## Page Title
Twingate Android and ChromeOS Client Applications - Open Source Software Notices

## Summary
This page lists all third-party open source components used in the Twingate Android and ChromeOS client applications, along with their respective licenses. It serves as the required third-party notices disclosure for the client software.

## Key Information

### Components by License

| License | Components |
|---------|------------|
| Apache 2.0 | libssl, AndroidX, Dagger 2, Kotlin, Logback Android, Moshi, OkHttp, Retrofit, Retrofit Rx adapter, RxAndroid, RxJava, Timber |
| BSD 3-Clause | libevent, lwip, Sentry |
| MIT | libjansson, jwt-cpp, args, Sentry SDK for Java/Android, SLF4J, pubnub, quicly |
| zlib | zlib, nanopb |
| Boost 1.0 | catch2 |
| CC0 1.0 Universal | siphash |
| Custom (MIT-like) | fmt |

### Full Component List
- **Networking/Transport**: OkHttp, libevent, lwip, quicly
- **Serialization**: Moshi, nanopb, libjansson
- **Auth**: jwt-cpp, libssl
- **Reactive**: RxJava, RxAndroid, Retrofit Rx adapter
- **DI**: Dagger 2
- **Logging**: Timber, Logback Android, SLF4J
- **Error Reporting**: Sentry, Sentry SDK for Java and Android
- **Messaging**: pubnub
- **Utilities**: fmt, zlib, siphash, args, catch2, Kotlin, AndroidX

## Prerequisites
- N/A — this is a legal/compliance reference page, not an implementation guide

## Step-by-Step
- N/A

## Configuration Values
- N/A

## Gotchas
- **siphash** uses CC0 1.0 (public domain dedication), not a standard permissive license — no attribution required but trademark/patent rights are not waived
- **fmt** includes an optional exception allowing embedded portions in compiled object code without attribution notices
- **Sentry** (native) uses BSD 3-Clause; **Sentry SDK for Java and Android** uses MIT — two separate Sentry components with different licenses
- Redistribution of Apache 2.0 components requires including the full license text and a NOTICE file if present

## Related Docs
- Twingate OSS notices for other platforms (iOS, macOS, Windows, Linux clients)
- [Apache License 2.0](http://www.apache.org/licenses/)