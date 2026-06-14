# Twingate Windows Client Application - OSS Third Party Notices

## Page Title
Windows Client Application - Open Source Component Licenses

## Summary
This page lists all third-party open source components bundled in the Twingate Windows client application. It provides full license texts for each dependency as required by their respective licenses. No implementation guidance is provided—this is a legal compliance/attribution page.

## Key Information

### Components Included
| Component | License | Copyright |
|-----------|---------|-----------|
| libssl | Apache 2.0 | OpenSSL Project |
| libevent, lwip, nlog | BSD 3-Clause | Various |
| siphash | CC0 1.0 Universal | — |
| libjansson, jwt-cpp, args, ModernWpf, MVVMLight, Newtonsoft JSON.NET, Sentry, pubnub, quicly | MIT | Various |
| catch2 | Boost Software License 1.0 | Catch2 Authors |
| zlib, nanopb | zlib License | Various |
| wpf-notifyicon | Code Project Open License | Philipp Sumi |
| CommonServiceLocator | Microsoft Public License | Microsoft 2008 |
| fmt | MIT-variant | Victor Zverovich |

### License Summary by Type
- **Apache 2.0**: libssl
- **BSD 3-Clause**: libevent, lwip, nlog
- **CC0 1.0**: siphash
- **MIT**: libjansson, jwt-cpp, args, ModernWpf, MVVMLight, Newtonsoft JSON.NET, Sentry, pubnub, quicly
- **Boost 1.0**: catch2
- **zlib**: zlib, nanopb
- **CPOL**: wpf-notifyicon
- **Ms-PL**: CommonServiceLocator

## Prerequisites
N/A — informational/legal page only.

## Step-by-Step
N/A

## Configuration Values
N/A

## Gotchas
- **wpf-notifyicon (CPOL)**: Prohibits selling the component standalone; cannot remove copyright notices; accompanying articles cannot be redistributed without author consent.
- **fmt**: Includes an optional exception allowing embedded portions in compiled object code to be redistributed without copyright notices.
- **siphash (CC0)**: Does not waive trademark or patent rights held by the affirmer.
- **CommonServiceLocator (Ms-PL)**: Patent license terminates automatically if patent claims are brought against contributors.

## Related Docs
- [Twingate OSS notices for other platforms] (macOS, Linux client equivalents)
- Twingate Windows client installation documentation