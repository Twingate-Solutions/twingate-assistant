# Internet Security Overview

## Page Title
Internet Security Overview

## Summary
Twingate offers DNS-over-HTTPS (DoH) as an internet security feature for desktop users on Windows, macOS, and Linux. It encrypts all DNS traffic system-wide at the network level without requiring per-application configuration. This is the foundational overview page linking to more detailed implementation guides.

## Key Information
- DNS security feature: DNS-over-HTTPS (DoH) encryption
- Supported platforms: Windows, macOS, Linux (desktop clients only)
- Encrypts **all** DNS traffic regardless of originating application
- No user-side configuration required beyond running the Twingate Client
- Twingate operates at network level on device to achieve system-wide coverage
- More internet security capabilities planned for future releases

## Prerequisites
- Twingate Client installed on a supported desktop OS (Windows, macOS, or Linux)
- User must be part of a Twingate network

## Exclusions / Gotchas
- **Headless clients in service account mode never use DoH** — regardless of platform
- DoH is desktop-only; mobile platforms not mentioned as supported
- This page is an overview only; actual configuration is in linked guides

## Configuration Values
- No configuration values on this page; settings handled in DoH configuration guide

## Related Docs
- [DNS Filtering Guide](https://www.twingate.com/docs/dns-filtering) — for filtering configuration
- [DoH Configuration Guide](https://www.twingate.com/docs/doh-configuration) — for enabling/configuring DoH
- Twingate DNS behavior overview (linked inline on page)
- Headless clients / service account documentation