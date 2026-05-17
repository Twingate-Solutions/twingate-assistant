# DNS-over-HTTPS (DoH) - Twingate

## Summary
Twingate provides native DoH capabilities for macOS, Windows, and Linux clients, encrypting all DNS traffic at the network level without per-application configuration. DoH is managed via the Admin Console and supports public resolvers, custom resolvers, fallback modes, and group exceptions.

## Key Information
- DoH is **disabled by default**; must be explicitly enabled in Admin Console
- Only supports **DNS A queries** (IPv4); AAAA/IPv6 queries fall back to IPv4 before DoH encapsulation
- DoH encrypts all non-Twingate-Resource DNS traffic on the device
- If Client is set to start at login, DoH activates immediately on boot

## Prerequisites
- macOS, Windows, or Linux Twingate Client (mobile not supported)
- "DoH as a Resource" requires minimum versions: macOS 2024.311, Windows 2024.351, Linux 2024.331
- Admin Console access (Internet Security → Secure DNS)

## Configuration Options

| Setting | Options | Default |
|---|---|---|
| DoH enabled | On/Off | Off |
| Resolver | Pre-configured public resolvers or custom HTTPS URL | — |
| Fallback method | Strict / Automatic | Automatic |
| Exception groups | Any number of groups | None |

## Fallback Methods
- **Strict**: Never falls back to regular DNS. If DoH resolver unavailable, all DNS fails (including private DNS)
- **Automatic**: Falls back to regular DNS if resolver unavailable or lookup fails

## Custom DoH Resolver Template Fields
Append device-specific data to custom resolver URLs:

```
${deviceName}       # Friendly Twingate name
${deviceId}         # Twingate device ID
${deviceModel}      # Hardware model string
${deviceHostname}   # Device hostname
${userEmail}        # Device owner email
```

Example: `https://doh.example/query?host=${deviceHostname}`

## DoH as a Resource
- When DoH resolver domain matches a Twingate Resource, traffic routes through that Resource
- Wildcard Resources (e.g., `*.autoco.internal`) are supported
- **Required**: DoH Resource must use a **Device-only Resource Policy** — user-authenticated policies will break DNS for end users

## Gotchas
- Custom resolver URLs are **not validated** as actual DoH endpoints—only checked as HTTPS URLs. Misconfiguration + Strict mode = DNS failure for all users
- Strict mode can break **private DNS resolution** (public resolvers can't resolve internal names)
- Users in **any** exception group bypass DoH entirely
- IPv6 (AAAA) queries are unsupported; local resolution falls back to IPv4

## Related Docs
- Twingate Client setup (macOS, Windows, Linux)
- Resource Policies (Device-only policy configuration)
- Internet Security settings in Admin Console