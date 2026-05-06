# Twingate Android and ChromeOS Client Applications - OSS Notices

## Page Title
Android and ChromeOS Client Applications (Open Source Software Notices)

## Summary
This page lists all third-party open source components used in the Twingate Android and ChromeOS client applications, along with their respective licenses. It serves as the legal attribution document required by the licenses of included dependencies.

## Key Information

### Components by License

| License | Components |
|---------|------------|
| Apache 2.0 | AndroidX, Dagger 2, Kotlin, libssl, Logback Android, Moshi, OkHttp, Retrofit, Retrofit Rx adapter, RxAndroid, RxJava, Timber |
| BSD 3-Clause | libevent, lwip, Sentry |
| MIT | args, jwt-cpp, libjansson, pubnub, quicly, Sentry SDK for Java and Android, SLF4J |
| zlib | nanopb, zlib |
| Boost 1.0 | catch2 |
| CC0 1.0 Universal | siphash |
| Custom (MIT-like) | fmt |

## Prerequisites
- N/A — this is a legal/compliance reference page, not a configuration guide.

## Step-by-Step
- N/A

## Configuration Values
- N/A

## Gotchas
- **siphash** uses CC0 1.0 (public domain dedication), not a traditional open source license — no attribution required but trademark/patent rights are not waived.
- **fmt** includes an optional exception allowing embedded object code redistribution without license notices.
- **Sentry** appears under two separate licenses: the native SDK under BSD 3-Clause and the Java/Android SDK under MIT.
- Apache 2.0 components require NOTICE file preservation when redistributing derivative works.

## Related Docs
- [Twingate OSS notices for other platforms] (iOS, Windows, macOS, Linux clients likely have separate OSS pages)
- Apache License 2.0: https://www.apache.org/licenses/