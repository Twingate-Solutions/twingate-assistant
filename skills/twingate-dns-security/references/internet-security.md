# Internet Security Overview

## Page Title
Internet Security Overview

## Summary
Twingate offers DNS-over-HTTPS (DoH) as an internet security feature for desktop users, encrypting all DNS traffic system-wide without requiring application-level configuration. Coverage is limited to desktop OS clients (Windows, macOS, Linux); headless/service account clients are explicitly excluded.

## Key Information
- **Current capability**: DNS encryption via DNS-over-HTTPS (DoH)
- **Supported platforms**: Windows, macOS, Linux (desktop clients only)
- **Unsupported**: Headless clients running in service account mode — never use DoH
- **Scope**: Encrypts *all* DNS traffic system-wide, regardless of originating application
- **Configuration requirement**: No app-level changes needed; enabling DoH only requires running the Twingate Client
- Twingate operates at the network level, enabling system-wide DNS security without per-app configuration

## Prerequisites
- Twingate Client installed on a supported desktop OS (Windows, macOS, or Linux)
- DoH must be enabled via network/policy configuration (see DoH configuration guide)

## Configuration Values
- No specific env vars or CLI flags documented on this page
- Refer to the **DoH configuration guide** for configuration parameters
- Refer to the **DNS filtering guide** for filtering options

## Gotchas
- **Headless clients in service account mode will never use DoH** — do not rely on DoH for encrypted DNS in automated/service deployments
- Mobile platforms not mentioned — DoH appears limited to desktop OS only
- Feature is described as evolving ("as we add more capabilities") — check for updates

## Related Docs
- [DNS Filtering Guide](https://www.twingate.com/docs/dns-filtering) — filtering configuration
- [DoH Configuration Guide](https://www.twingate.com/docs/doh-configuration) — setup and enablement
- Twingate DNS behavior overview (linked inline as "Learn more")
- Headless clients / service accounts documentation