# Android and ChromeOS Client Applications - OSS Third Party Notices

## Page Title
Twingate Android and ChromeOS Client Applications — Open Source Component Licenses

## Summary
This page lists all third-party open source components used in the Twingate Android and ChromeOS client applications, along with their respective licenses. It serves as the required legal attribution notice for OSS dependencies. No configuration or implementation guidance is provided.

## Key Information

### Components by License

| License | Components |
|---------|-----------|
| Apache 2.0 | AndroidX, Dagger 2, Kotlin, Logback Android, Moshi, OkHttp, Retrofit, Retrofit Rx adapter, RxAndroid, RxJava, Timber, libssl |
| BSD 3-Clause | libevent, lwip, Sentry |
| MIT | libjansson, jwt-cpp, args, Sentry SDK for Java/Android, SLF4J, pubnub, quicly |
| zlib | zlib, nanopb |
| Boost Software License 1.0 | catch2 |
| CC0 1.0 Universal | siphash |
| fmt (MIT-variant) | fmt |

### Full Component List
`AndroidX`, `args`, `catch2`, `Dagger 2`, `fmt`, `jwt-cpp`, `Kotlin`, `libevent`, `libjansson`, `libssl`, `Logback Android`, `lwip`, `Moshi`, `nanopb`, `OkHttp`, `pubnub`, `quicly`, `Retrofit`, `Retrofit Rx adapter`, `RxAndroid`, `RxJava`, `Sentry`, `Sentry SDK for Java and Android`, `siphash`, `SLF4J`, `Timber`, `zlib`

## Prerequisites
- N/A (legal/attribution page only)

## Step-by-Step
- N/A

## Configuration Values
- N/A

## Gotchas
- `fmt` uses a near-MIT license with an additional optional exception: embedded object-form redistributions do not require inclusion of copyright/permission notices
- `siphash` is CC0 (public domain dedication), not a traditional open source license — no attribution legally required but listed for completeness
- Sentry appears twice under different licenses: the native component (BSD 3-Clause) and the Java/Android SDK (MIT)

## Related Docs
- [Twingate OSS Notices (other platforms)](https://www.twingate.com/docs/) — check for iOS, Windows, Linux client OSS pages
- Apache License 2.0: https://www.apache.org/licenses/