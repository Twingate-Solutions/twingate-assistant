# Windows Client Application - Open Source Components

## Page Title
Twingate Windows Client Application — Third Party OSS Notices

## Summary
This page lists all open-source software components bundled in the Twingate Windows client application, along with their full license texts. It serves as the legal third-party notice disclosure required by the respective open-source licenses.

## Key Information

### Components by License

| License | Components |
|---------|------------|
| Apache 2.0 | libssl |
| BSD 3-Clause | libevent, lwip, nlog |
| CC0 1.0 Universal | siphash |
| MIT | libjansson, jwt-cpp, args, ModernWpf, MVVMLight, Newtonsoft JSON.NET, Sentry, pubnub, quicly |
| Boost Software License 1.0 | catch2 |
| zlib License | zlib, nanopb |
| Code Project Open License | wpf-notifyicon |
| Microsoft Public License | CommonServiceLocator |
| MIT-variant | fmt |

### Full Component List
- **Networking/Protocol**: libevent, lwip, quicly, libssl
- **Serialization**: libjansson, nanopb, Newtonsoft JSON.NET, protobuf-adjacent (nanopb)
- **UI/WPF**: ModernWpf, MVVMLight, wpf-notifyicon
- **Auth**: jwt-cpp
- **Logging**: nlog, Sentry
- **Messaging**: pubnub
- **Utilities**: fmt, zlib, args, siphash, catch2 (testing), CommonServiceLocator

## Prerequisites
- N/A — this is a legal disclosure page, not a configuration guide.

## Step-by-Step
- N/A

## Configuration Values
- N/A

## Gotchas
- **wpf-notifyicon (CPOL)**: Cannot sell the component standalone; cannot remove copyright notices; accompanying articles cannot be redistributed without author consent.
- **CC0 (siphash)**: Trademark and patent rights are explicitly **not** waived under CC0.
- **fmt**: Includes an optional exception allowing embedded object-form redistribution without copyright notices.
- **nlog/libevent/lwip (BSD 3-Clause)**: Cannot use contributor names for endorsement without permission.

## Related Docs
- [Twingate Windows Client Setup](https://www.twingate.com/docs/windows-client)
- OSS notices for other platforms (macOS, Linux, iOS, Android clients likely have separate pages)