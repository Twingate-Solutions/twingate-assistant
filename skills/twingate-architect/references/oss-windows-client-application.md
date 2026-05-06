# Windows Client Application - OSS Third Party Notices

## Page Title
Twingate Windows Client Application – Open Source Component Licenses

## Summary
This page lists all third-party open source components bundled in the Twingate Windows client application, along with their respective licenses. It serves as the legal attribution/compliance notice required by each component's license terms. No installation or configuration guidance is provided.

## Key Information

**Components included in the Windows client:**
- **Networking/Security:** libssl (OpenSSL), libevent, lwip, quicly
- **Data/Serialization:** libjansson, nanopb, protobuf-adjacent, zlib, Newtonsoft JSON.NET
- **Auth:** jwt-cpp
- **UI/WPF:** ModernWpf, MVVMLight, wpf-notifyicon
- **Logging/Monitoring:** nlog, Sentry
- **Messaging:** pubnub
- **CLI/Utility:** args, fmt, siphash, catch2, CommonServiceLocator

**License breakdown:**
| License | Components |
|---------|------------|
| Apache 2.0 | libssl |
| BSD 3-Clause | libevent, lwip, nlog |
| CC0 1.0 Universal | siphash |
| MIT | libjansson, jwt-cpp, args, ModernWpf, MVVMLight, Newtonsoft JSON.NET, Sentry, pubnub, quicly |
| Boost 1.0 | catch2 |
| zlib | zlib, nanopb |
| Code Project Open License | wpf-notifyicon |
| Microsoft Public License | CommonServiceLocator |
| MIT-variant | fmt |

## Prerequisites
- N/A (informational/legal page only)

## Step-by-Step
- N/A

## Configuration Values
- N/A

## Gotchas
- **wpf-notifyicon (CPOL):** Has additional restrictions vs. permissive licenses — cannot sell the component standalone; accompanying Articles cannot be redistributed without author consent
- **fmt:** Includes an optional exception allowing embedded object-form redistribution without copyright notices
- **siphash (CC0):** Trademark and patent rights are explicitly *not* waived under CC0
- **CommonServiceLocator (Ms-PL):** Source redistribution requires including the full Ms-PL license text

## Related Docs
- Twingate Windows Client installation docs
- Other platform OSS notices (macOS, Linux, iOS, Android clients)