# Windows Client Application - OSS Third Party Notices

## Page Title
Twingate Windows Client Application — Open Source Component Licenses

## Summary
This page lists all third-party open source components used in the Twingate Windows client application, along with their full license texts. It serves as the required legal attribution/notice document for OSS components bundled in the Windows client.

## Key Information

**Components included in the Windows client:**
- **Networking/Security:** libssl (OpenSSL), libevent, lwip, quicly
- **Data/Serialization:** libjansson, nanopb, Newtonsoft JSON.NET, fmt
- **Auth:** jwt-cpp
- **UI (WPF):** ModernWpf, MVVMLight, wpf-notifyicon
- **Logging/Monitoring:** nlog, Sentry
- **Messaging:** pubnub
- **Utilities:** args, siphash, zlib, catch2, CommonServiceLocator

**License breakdown:**
| License | Components |
|---------|-----------|
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
- N/A (reference/legal document only)

## Step-by-Step
- N/A (informational page, no implementation steps)

## Configuration Values
- N/A

## Gotchas
- **wpf-notifyicon (CPOL):** Cannot sell the component standalone; accompanying Articles cannot be redistributed without author consent — more restrictive than MIT/Apache
- **CommonServiceLocator (Ms-PL):** Source redistribution requires including full Ms-PL license; incompatible with GPL in some interpretations
- **fmt:** Includes an optional exception allowing embedded object-form redistribution without copyright notices — useful for statically linked builds
- **siphash (CC0):** Trademark/patent rights are NOT waived by CC0, only copyright

## Related Docs
- [Twingate Windows Client setup documentation](https://www.twingate.com/docs/windows)
- Equivalent OSS notice pages exist for other Twingate client platforms (macOS, Linux, iOS, Android)