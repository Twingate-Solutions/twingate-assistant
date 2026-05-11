# Twingate Windows Client Application - OSS Third Party Notices

## Page Title
Windows Client Application - Open Source Components & Licenses

## Summary
This page lists all third-party open source components bundled in the Twingate Windows client application, along with their full license texts. It serves as the required legal attribution/notice document for OSS compliance. No implementation guidance is provided.

## Key Information

**Components included in the Windows client:**
- **Networking/Crypto:** libssl (OpenSSL), libevent, lwip, quicly
- **Data/Serialization:** libjansson, nanopb, protobuf-adjacent, zlib
- **Auth:** jwt-cpp
- **UI (WPF):** ModernWpf, MVVMLight, wpf-notifyicon, Newtonsoft JSON.NET
- **Logging/Monitoring:** nlog, Sentry
- **Messaging:** pubnub
- **Utilities:** fmt, args, siphash, catch2, CommonServiceLocator

**License breakdown:**
| License | Components |
|---------|-----------|
| Apache 2.0 | libssl |
| BSD 3-Clause | libevent, lwip, nlog |
| MIT | libjansson, jwt-cpp, args, ModernWpf, MVVMLight, Newtonsoft JSON.NET, Sentry, pubnub, quicly |
| zlib | zlib, nanopb |
| CC0 1.0 Universal | siphash |
| Boost 1.0 | catch2 |
| Code Project Open License | wpf-notifyicon |
| Microsoft Public License | CommonServiceLocator |
| MIT-variant | fmt |

## Prerequisites
- N/A — this is a legal notices/attribution page only

## Step-by-Step
- N/A — no implementation steps

## Configuration Values
- N/A

## Gotchas
- **wpf-notifyicon (CPOL)** has redistribution restrictions: the accompanying Articles cannot be redistributed without author consent; the Work itself cannot be sold standalone
- **fmt** includes an optional license exception allowing embedded portions in compiled object form to be redistributed without copyright notices
- **siphash** uses CC0 (public domain dedication), not a standard permissive license — no attribution required
- **CommonServiceLocator** uses Microsoft Public License, which terminates patent grants if patent litigation is filed against contributors

## Related Docs
- [Twingate Windows Client installation docs] (implied)
- OSS notices for other platforms (macOS, Linux, iOS, Android clients likely have separate pages)