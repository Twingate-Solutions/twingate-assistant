# Windows Client Application - Open Source Components

## Page Title
Twingate Windows Client Application — Third Party OSS Notices

## Summary
This page lists all open-source software components bundled in the Twingate Windows client application, along with their full license texts. It serves as the required legal attribution notice for third-party dependencies. No installation or configuration guidance is provided.

## Key Information

### Components Included
| Component | License |
|-----------|---------|
| libssl (OpenSSL) | Apache 2.0 |
| libevent, lwip, nlog | BSD 3-Clause |
| siphash | CC0 1.0 Universal |
| libjansson, jwt-cpp, args, ModernWpf, MVVMLight, Newtonsoft JSON.NET, Sentry, pubnub, quicly | MIT |
| catch2 | Boost Software License 1.0 |
| zlib, nanopb | zlib License |
| wpf-notifyicon | Code Project Open License (CPOL) |
| CommonServiceLocator | Microsoft Public License (Ms-PL) |
| fmt | MIT (with optional embedding exception) |

### Component Purposes (inferred)
- **Networking**: libevent, lwip, quicly, libssl
- **Serialization**: libjansson, nanopb, Newtonsoft JSON.NET, protobuf (nanopb)
- **UI**: ModernWpf, MVVMLight, wpf-notifyicon
- **Auth**: jwt-cpp
- **Logging**: nlog, Sentry
- **Messaging**: pubnub
- **Utilities**: fmt, args, zlib, siphash, catch2

## Prerequisites
- N/A — this is a legal/attribution reference page only

## Step-by-Step
- N/A — no configuration or installation steps

## Configuration Values
- N/A

## Gotchas
- **CPOL (wpf-notifyicon)**: More restrictive than typical OSS licenses — prohibits selling the component standalone; accompanying articles cannot be redistributed without author consent
- **fmt**: Includes an optional exception allowing embedded object-form redistribution without copyright notices — relevant if statically linking
- **CC0 (siphash)**: Does **not** waive trademark or patent rights held by the affirmer
- **Ms-PL (CommonServiceLocator)**: Patent license terminates automatically if you bring patent claims against any contributor

## Related Docs
- Twingate OSS notices for other platforms (Linux, macOS clients likely have separate pages)
- Twingate Windows client installation/deployment documentation