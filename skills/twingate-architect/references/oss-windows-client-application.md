# Twingate Windows Client Application - OSS Third Party Notices

## Page Title
Windows Client Application - Open Source Component Licenses

## Summary
This page lists all third-party open source components bundled in the Twingate Windows client application. It serves as the legal attribution/notice document required by the respective licenses of each included library.

## Key Information

**Components included in Windows client:**
- **Networking/Protocol:** libevent, lwip, libssl (OpenSSL), quicly, nanopb
- **UI/WPF:** ModernWpf, MVVMLight, wpf-notifyicon
- **Data/Serialization:** libjansson, Newtonsoft JSON.NET, fmt, nanopb, protobuf (nanopb)
- **Auth:** jwt-cpp
- **Logging/Monitoring:** nlog, Sentry
- **Messaging:** pubnub
- **Utilities:** args, siphash, zlib, catch2 (testing), CommonServiceLocator

## License Breakdown

| License | Components |
|---------|-----------|
| Apache 2.0 | libssl (OpenSSL) |
| BSD 3-Clause | libevent, lwip, nlog |
| MIT | libjansson, jwt-cpp, args, ModernWpf, MVVMLight, Newtonsoft JSON.NET, Sentry, pubnub, quicly |
| Boost 1.0 | catch2 |
| zlib | zlib, nanopb |
| CC0 1.0 Universal | siphash |
| Code Project Open License | wpf-notifyicon |
| Microsoft Public License | CommonServiceLocator |
| MIT-variant | fmt |

## Prerequisites
- N/A — this is a legal notices/attribution page, not an implementation guide

## Step-by-Step
- N/A

## Configuration Values
- N/A

## Gotchas
- **wpf-notifyicon (CPOL):** Cannot sell the component standalone; articles accompanying the work cannot be redistributed without author consent
- **fmt:** Includes an optional exception allowing embedded compiled portions to be redistributed without copyright notices
- **OpenSSL (Apache 2.0):** Dual copyright — OpenSSL Project (1998–2020) and Eric A. Young/Tim J. Hudson (1995–1998)
- **siphash (CC0):** Trademark and patent rights are NOT waived under CC0, only copyright

## Related Docs
- Twingate OSS notices for other platforms (macOS, Linux, iOS, Android clients)
- Twingate Connector OSS notices