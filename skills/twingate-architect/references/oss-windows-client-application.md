# Windows Client Application - OSS Third Party Notices

## Page Title
Twingate Windows Client Application — Open Source Component Licenses

## Summary
This page lists all third-party open source components bundled in the Twingate Windows client application, along with their respective licenses. It serves as the legal attribution/notice document required by the included OSS licenses. No implementation guidance is provided.

## Key Information

**Components included in the Windows client:**
- **Networking/Protocol:** libevent, lwip, libssl (OpenSSL), quicly, nanopb
- **Data/Serialization:** libjansson, Newtonsoft JSON.NET, fmt, nanopb, zlib, protobuf (nanopb)
- **Auth:** jwt-cpp
- **UI/WPF:** ModernWpf, MVVMLight, wpf-notifyicon
- **Logging/Monitoring:** nlog, Sentry
- **Messaging:** pubnub
- **Testing:** catch2, args
- **Hashing:** siphash
- **IoC:** CommonServiceLocator

**License breakdown:**
| License | Components |
|---------|-----------|
| Apache 2.0 | libssl |
| BSD 3-Clause | libevent, lwip, nlog |
| MIT | libjansson, jwt-cpp, args, ModernWpf, MVVMLight, Newtonsoft JSON.NET, Sentry, pubnub, quicly |
| zlib | zlib, nanopb |
| Boost 1.0 | catch2 |
| CC0 1.0 | siphash |
| Code Project Open License | wpf-notifyicon |
| Microsoft Public License | CommonServiceLocator |
| fmt license (MIT variant) | fmt |

## Prerequisites
N/A — reference/legal document only.

## Step-by-Step
N/A — no implementation steps.

## Configuration Values
N/A

## Gotchas
- **wpf-notifyicon** uses the Code Project Open License, which prohibits selling the component standalone and requires retaining attribution notices — more restrictive than MIT/BSD.
- **CC0 (siphash)** is a public domain dedication, not a traditional license — no attribution required.
- **fmt** includes an optional exception allowing embedded portions in machine-executable object code to be redistributed without copyright notices.
- **CommonServiceLocator** uses Microsoft Public License (Ms-PL), which is incompatible with GPL.

## Related Docs
- [Twingate Windows Client setup documentation]
- Other platform OSS notices (macOS, Linux, iOS, Android client equivalents)