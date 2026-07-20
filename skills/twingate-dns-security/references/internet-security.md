# Internet Security Overview

## Page Title
Internet Security Overview

## Summary
Twingate offers DNS-over-HTTPS (DoH) as an internet security feature for desktop users on Windows, macOS, and Linux. It operates at the network level to encrypt all DNS traffic system-wide without requiring per-application configuration. Headless clients in service account mode are excluded from DoH functionality.

## Key Information
- Current internet security offering: DNS encryption via DNS-over-HTTPS (DoH)
- System-wide DNS encryption — covers all applications on the device, not just Twingate traffic
- No configuration changes required on the user side beyond running the Twingate Client
- Feature is platform-limited: desktop only (Windows, macOS, Linux)
- Headless clients running in service account mode **never** use DoH, regardless of platform

## Prerequisites
- Twingate Client installed on a supported desktop OS (Windows, macOS, or Linux)
- Users must be part of a Twingate network
- DoH must be enabled by the network administrator (see DoH configuration guide)

## Configuration Values
- No client-side configuration flags or env vars documented on this page
- Admin configuration covered in linked DoH configuration guide

## Gotchas
- **Headless clients / service accounts**: DoH is explicitly excluded — service account mode will never use DoH
- **Mobile platforms not supported**: DoH is desktop-only; iOS and Android clients are not mentioned as supported
- Feature set is actively expanding; capabilities listed here are not exhaustive

## Related Docs
- [DNS Filtering Guide](https://www.twingate.com/docs/dns-filtering) — configuring DNS filtering rules
- [DoH Configuration Guide](https://www.twingate.com/docs/doh-configuration) — enabling and configuring DNS-over-HTTPS
- Twingate DNS behavior overview (linked inline as "Learn more")
- Headless Clients documentation
- Service Accounts documentation