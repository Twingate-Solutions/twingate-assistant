# Twingate Android and ChromeOS Client Applications — OSS Components

## Page Title
Android and ChromeOS Client Applications (Open Source Components / Third Party Notices)

## Summary
This page lists all third-party open source components used in the Twingate Android and ChromeOS client applications. It provides full license texts for each dependency grouped by license type. This is a legal/compliance reference page, not an implementation guide.

## Key Information

**Components by License:**

| License | Components |
|---------|-----------|
| Apache 2.0 | AndroidX, Dagger 2, Kotlin, libssl (OpenSSL), Logback Android, Moshi, OkHttp, Retrofit, Retrofit Rx adapter, RxAndroid, RxJava, Timber |
| BSD 3-Clause | libevent, lwip, Sentry (native) |
| MIT | libjansson, jwt-cpp, args, Sentry SDK for Java/Android, SLF4J, pubnub, quicly |
| Boost 1.0 | catch2 |
| zlib | zlib, nanopb |
| CC0 1.0 Universal | siphash |
| Custom (MIT-like) | fmt |

## Prerequisites
- N/A — this is a reference/compliance page only

## Step-by-Step
- N/A — no actionable implementation steps

## Configuration Values
- N/A

## Gotchas
- **fmt** uses a non-standard license (MIT-like with an object code embedding exception) — verify compliance separately if redistributing
- **siphash** uses CC0 1.0 (public domain dedication), not a traditional OSS license
- **Sentry** appears twice under different licenses: the native SDK is BSD 3-Clause; the Java/Android SDK is MIT

## Related Docs
- [Twingate OSS iOS Client Applications](https://www.twingate.com/docs/oss-ios-client-applications) *(likely counterpart page)*
- [Twingate OSS Desktop Client Applications](https://www.twingate.com/docs/oss-desktop-client-applications) *(likely counterpart page)*