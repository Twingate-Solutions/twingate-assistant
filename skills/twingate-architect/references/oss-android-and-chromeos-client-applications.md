# Android and ChromeOS Client Applications - OSS Notices

## Page Title
Twingate Android and ChromeOS Client Applications — Open Source Software (OSS) Third-Party Notices

## Summary
This page lists all third-party open source components used in Twingate's Android and ChromeOS client applications, along with their respective licenses. It serves as the legal attribution document required by the included OSS licenses. No implementation guidance is provided.

## Key Information

### Components by License

**Apache License 2.0:**
- AndroidX, Dagger 2, Kotlin, Logback Android, Moshi, OkHttp, Retrofit, Retrofit Rx adapter, RxAndroid, RxJava, Timber, libssl

**BSD 3-Clause:**
- libevent, lwip, Sentry

**MIT License:**
- libjansson, jwt-cpp, args, Sentry SDK for Java and Android, SLF4J, pubnub, quicly

**zlib License:**
- zlib, nanopb

**Boost Software License 1.0:**
- catch2

**CC0 1.0 Universal (Public Domain):**
- siphash

**Other (MIT-like):**
- fmt (with optional embedded object code exception)

## Prerequisites
- N/A — reference/legal document only

## Step-by-Step
- N/A — no implementation steps

## Configuration Values
- N/A

## Gotchas
- **Redistribution requires license inclusion**: Apache 2.0, MIT, BSD 3-Clause, and Boost components all require copyright/license notices in redistributed copies
- **BSD 3-Clause** components (libevent, lwip, Sentry) prohibit using contributor names for endorsement without permission
- **fmt** includes an optional exception allowing embedded object code redistribution without copyright notices
- **siphash** is CC0 (effectively public domain), but CC0 does not waive patent or trademark rights

## Related Docs
- [Twingate OSS Notices (other platforms)](https://www.twingate.com/docs/oss-notices) — likely contains similar notices for iOS, Windows, macOS clients