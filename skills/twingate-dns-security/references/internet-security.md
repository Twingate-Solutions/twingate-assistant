---
source: https://www.twingate.com/docs/internet-security
type: docs
fetched: 2026-08-14
source_version: 4b35ee7143342a0826d0bde951d459a5e7480685ccf48e492fe550f87dab626a
---

# Internet Security Overview

## Page Title
Internet Security Overview (Twingate)

## Summary
Twingate offers DNS-over-HTTPS (DoH) as an internet security feature for desktop users on Windows, macOS, and Linux. It encrypts all DNS traffic system-wide at the network level with no per-application configuration required. Additional internet security capabilities are planned for future release.

## Key Information
- **Feature**: DNS encryption via DNS-over-HTTPS (DoH)
- **Scope**: All DNS traffic on the device, regardless of originating application
- **Platform support**: Windows, macOS, Linux (desktop only)
- **Exclusions**: Headless clients running in service account mode **never** use DoH
- **Configuration**: No user-side configuration required beyond running the Twingate Client
- Twingate operates at the network level, enabling system-wide DNS security without per-app changes

## Prerequisites
- Twingate Client installed on a supported desktop OS (Windows, macOS, or Linux)
- User must **not** be running in headless/service account mode

## Configuration Values
- No explicit env vars or CLI flags documented on this page
- DoH is enabled/disabled via network configuration (see DoH configuration guide)

## Gotchas
- **Headless clients in service account mode are explicitly excluded** from DoH — this applies regardless of platform
- Feature is limited to desktop clients; mobile platform support not mentioned
- Page is a high-level overview; actual configuration details are in linked guides

## Related Docs
- [DNS Filtering Guide](https://www.twingate.com/docs/dns-filtering) — filtering configuration
- [DoH Configuration Guide](https://www.twingate.com/docs/doh-configuration) — setup and enabling DoH
- Twingate DNS behavior overview (linked inline as "Learn more")
- Headless clients / service account documentation