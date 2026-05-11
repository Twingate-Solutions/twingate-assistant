# Internet Security Overview

## Page Title
Internet Security Overview

## Summary
Twingate offers DNS-over-HTTPS (DoH) as an internet security feature for desktop users, encrypting all DNS traffic system-wide without requiring per-application configuration. The feature operates at the network level on user devices, covering all applications automatically.

## Key Information
- Current capability: DNS encryption via DNS-over-HTTPS (DoH)
- Supported platforms: Windows, macOS, Linux (desktop only)
- Operates system-wide — encrypts all DNS traffic regardless of originating application
- No configuration changes required on end-user side beyond running the Twingate Client
- More internet security capabilities planned for future releases

## Prerequisites
- Twingate Client installed on supported desktop OS (Windows, macOS, or Linux)
- User must be part of a Twingate network

## Exclusions / Gotchas
- **Headless clients in service account mode will never use DoH** — regardless of platform
- Mobile platforms not supported for DoH
- Feature is desktop-only; no mention of support for mobile or browser-based clients

## Configuration Values
- No end-user configuration required
- Admin configuration available via the DoH configuration guide (linked separately)

## Related Docs
- [DNS Filtering Guide](https://www.twingate.com/docs/dns-filtering)
- [DoH Configuration Guide](https://www.twingate.com/docs/doh-configuration)
- DNS and Twingate (how Twingate handles DNS internally)
- Headless Clients / Service Accounts documentation