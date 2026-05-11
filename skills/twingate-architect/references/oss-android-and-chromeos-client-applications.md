# Android and ChromeOS Client Applications - OSS Components

## Page Title
Twingate Android and ChromeOS Client Applications — Open Source Components & Third-Party Notices

## Summary
This page lists all open-source third-party components used in Twingate's Android and ChromeOS client applications, along with their licenses and copyright notices. It serves as the required legal attribution document for OSS dependencies. No implementation guidance is provided.

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
| Other (MIT-variant) | fmt |

## Prerequisites
- N/A — reference/legal document only

## Step-by-Step
- N/A — no implementation steps

## Configuration Values
- N/A

## Gotchas
- **siphash** uses CC0 1.0 (public domain dedication), not a standard OSS license — no attribution required but trademark/patent rights are not waived
- **fmt** includes an optional exception allowing redistribution of embedded object code without copyright notices
- **Sentry** appears under two different licenses: the native SDK under BSD 3-Clause, the Java/Android SDK under MIT
- Redistribution of Apache 2.0 components requires preserving NOTICE files if present

## Related Docs
- [Twingate OSS notices for other platforms] (not linked on this page)
- Apache License 2.0: http://www.apache.org/licenses/