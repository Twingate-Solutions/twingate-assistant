# Windows Client Application - OSS Third Party Notices

## Page Title
Twingate Windows Client Application — Open Source Component Licenses

## Summary
This page lists all third-party open source components bundled in the Twingate Windows client application, along with their full license texts. It serves as the legal attribution/notice document required by the respective licenses. No installation or configuration guidance is provided.

## Key Information
- **Purpose**: Legal compliance disclosure for OSS components used in the Windows client
- **Total components**: 19 third-party libraries

### Component → License Mapping

| License | Components |
|---------|-----------|
| Apache 2.0 | libssl |
| BSD 3-Clause | libevent, lwip, nlog |
| CC0 1.0 Universal | siphash |
| MIT | libjansson, jwt-cpp, args, ModernWpf, MVVMLight, Newtonsoft JSON.NET, Sentry, pubnub, quicly |
| Boost Software License 1.0 | catch2 |
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
- **wpf-notifyicon (CPOL)**: More restrictive than typical OSS — prohibits selling the component standalone; articles accompanying the work cannot be redistributed without author consent
- **fmt**: Includes an optional exception allowing embedded portions in compiled object form to be redistributed without copyright notices
- **siphash**: Licensed under CC0, effectively public domain — no attribution required
- **CommonServiceLocator**: Under Microsoft Public License, not MIT/Apache — check compatibility if redistributing

## Related Docs
- Twingate OSS notices for other platforms (macOS, Linux, iOS, Android clients likely have separate pages)
- Twingate Windows client installation documentation