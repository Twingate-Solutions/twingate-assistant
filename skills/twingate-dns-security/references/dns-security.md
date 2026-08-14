---
source: https://www.twingate.com/docs/dns-security
type: docs
fetched: 2026-08-14
source_version: f10073668f4f6227f4b5911bbdc34d232606689a6d2a5cdceb2286cc5fe53943
---

# DNS-over-HTTPS (DoH) - Twingate

## Summary
Twingate provides native DNS-over-HTTPS (DoH) for macOS, Windows, and Linux clients, encrypting all DNS traffic at the network level without per-application configuration. DoH is disabled by default and configured via the Admin Console under Internet Security > Secure DNS.

## Key Information
- **Platform support**: macOS, Windows, Linux only (not mobile)
- **Scope**: Encrypts all DNS A record queries not destined for Twingate Resources
- **AAAA (IPv6)**: Not supported; falls back to IPv4 before DoH encapsulation
- **Default state**: DoH disabled; fallback method defaults to Automatic
- **Startup behavior**: If Client is set to start at login, DoH activates immediately after boot

## Prerequisites
- Twingate Client running on macOS, Windows, or Linux
- For DoH as a Resource: macOS ≥2024.311, Windows ≥2024.351, Linux ≥2024.331
- Admin Console access to Internet Security > Secure DNS

## Configuration Options

| Setting | Options | Default |
|---|---|---|
| DoH enabled | On/Off | Off |
| Resolver | Pre-configured public resolvers or custom HTTPS URL | — |
| Fallback method | Strict / Automatic | Automatic |
| Exception groups | Any number of groups | None |

## Custom Resolver URL Template Fields
Append device-specific info to custom resolver URLs:

```
${deviceName}       # Friendly Twingate name
${deviceId}         # Twingate device ID
${deviceModel}      # Hardware model string
${deviceHostname}   # Device hostname
${userEmail}        # Device owner email
```

Example: `https://doh.example/query?host=${deviceHostname}`

## Fallback Behavior
- **Automatic**: Falls back to regular DNS if DoH resolver unreachable or lookup fails
- **Strict**: Never falls back; DNS fails entirely if resolver unavailable (including private DNS)

## DoH as a Resource
- If DoH resolver domain matches a Twingate Resource (including wildcards like `*.autoco.internal`), DoH traffic routes through that Resource
- **Required**: DoH Resource must use a **Device-only Resource Policy** — otherwise end users lose DNS functionality entirely

## Exception Groups
- Groups added to exception list bypass DoH entirely
- User needs membership in only **one** exception group to be excluded
- Excluded users use DNS as configured on their local device

## Gotchas
- Custom resolver URL is not validated beyond being an HTTPS endpoint — misconfiguration + Strict mode = DNS failure for all affected users
- Private DNS addresses cannot resolve through public DoH resolvers; use Automatic fallback or route resolver through a Resource
- DoH Resource without Device-only policy breaks DNS for users (authentication prompt blocks resolution)
- IPv6 (AAAA) queries are not supported

## Related Docs
- Twingate Client setup (macOS/Windows/Linux)
- Resource Policies (Device-only policy configuration)
- Internet Security / Secure DNS admin settings