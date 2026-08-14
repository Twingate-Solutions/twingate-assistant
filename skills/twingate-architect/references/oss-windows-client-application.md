---
source: https://www.twingate.com/docs/oss-windows-client-application
type: docs
fetched: 2026-08-14
source_version: 6a148075b4be5c773f177c0013cf0c15637922223ea486dcbf936fa7e3460e2e
---

# Windows Client Application - Open Source Components

## Page Title
Twingate Windows Client Application — Third Party OSS Notices

## Summary
This page lists all open-source software components bundled in the Twingate Windows client application, along with their full license texts. It serves as the required legal attribution document for third-party dependencies. No installation or configuration guidance is provided.

## Key Information

**Components included in the Windows client:**

| Component | License |
|-----------|---------|
| libssl (OpenSSL) | Apache 2.0 |
| libevent, lwip, nlog | BSD 3-Clause |
| siphash | CC0 1.0 Universal |
| libjansson, jwt-cpp, args, ModernWpf, MVVMLight, Newtonsoft JSON.NET, Sentry, pubnub, quicly | MIT |
| catch2 | Boost Software License 1.0 |
| zlib, nanopb | zlib License |
| wpf-notifyicon | Code Project Open License (CPOL) |
| CommonServiceLocator | Microsoft Public License (MS-PL) |
| fmt | MIT (with optional object-code exception) |

## Prerequisites
- N/A — This is a legal/compliance reference page only.

## Step-by-Step
- N/A — No procedural content.

## Configuration Values
- N/A — No environment variables, CLI flags, or API parameters.

## Gotchas
- **wpf-notifyicon (CPOL)**: Cannot sell the component standalone; cannot remove copyright notices; accompanying articles cannot be redistributed without author consent.
- **fmt**: Has an optional exception allowing redistribution of machine-compiled object code without including copyright notices.
- **CC0 (siphash)**: Does not waive trademark or patent rights held by the affirmer.
- **CPOL**: Requires indemnification of the author for any damages arising from your use — stricter than typical permissive licenses.

## Related Docs
- [Twingate OSS notices for other platforms] (not linked on this page)
- Twingate client installation documentation (separate pages per OS)