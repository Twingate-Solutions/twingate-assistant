# Internet Security Overview

## Page Title
Internet Security Overview

## Summary
Twingate offers DNS-over-HTTPS (DoH) as an internet security feature for desktop clients (Windows, macOS, Linux). It operates at the network level to encrypt all DNS traffic system-wide without requiring per-application configuration. Additional capabilities are planned but not yet documented.

## Key Information
- Current feature: DNS encryption via DNS-over-HTTPS (DoH)
- Supported platforms: Windows, macOS, Linux (desktop only)
- DoH encrypts **all** DNS traffic regardless of originating application
- No user-side configuration changes required beyond running the Twingate Client
- Twingate's network-level operation enables system-wide DNS security

## Prerequisites
- Twingate Client installed and running on a supported desktop OS
- Feature must be enabled by network administrator

## Exclusions / Gotchas
- **Headless clients in service account mode never use DoH** — regardless of platform
- Mobile platforms not mentioned as supported
- Feature is desktop-only; no mobile or server-mode support

## Configuration Values
- No direct CLI flags or env vars documented on this page
- Configuration handled via:
  - DNS filtering guide (separate doc)
  - DoH configuration guide (separate doc)

## Related Docs
- [DNS Filtering Guide](https://www.twingate.com/docs/dns-filtering)
- [DoH Configuration Guide](https://www.twingate.com/docs/doh-configuration)
- Twingate DNS behavior overview (linked inline)
- Headless clients / service account mode documentation