# Internet Security Overview

## Page Title
Internet Security Overview

## Summary
Twingate offers DNS-over-HTTPS (DoH) as an internet security feature for desktop users on Windows, macOS, and Linux. Because Twingate operates at the network level, DoH encrypts all DNS traffic system-wide without per-application configuration. This is an expanding feature area with additional capabilities planned.

## Key Information
- **Current feature**: DNS encryption via DNS-over-HTTPS (DoH)
- **Supported platforms**: Windows, macOS, Linux (desktop clients only)
- **Scope**: Encrypts all DNS traffic regardless of originating application
- **No user-side configuration required** beyond running the Twingate Client
- Twingate's network-level operation enables system-wide DNS security

## Prerequisites
- Twingate Client running on a supported desktop OS (Windows, macOS, or Linux)
- Feature must be enabled/configured by network administrator

## Exclusions / Gotchas
- **Headless clients in service account mode will never use DoH** — regardless of platform
- Mobile platforms are not mentioned as supported
- Feature set is still expanding; not all capabilities are currently available

## Configuration Values
- No client-side configuration required
- Admin configuration covered in linked guides (DNS filtering guide, DoH configuration guide)

## Related Docs
- [DNS filtering guide](https://www.twingate.com/docs/dns-filtering)
- [DoH configuration guide](https://www.twingate.com/docs/doh-configuration)
- Twingate DNS behavior overview (linked inline as "Learn more")
- Headless clients / service account documentation