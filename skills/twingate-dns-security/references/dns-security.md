# DNS-over-HTTPS (DoH) - Twingate

## Summary
Twingate provides native DoH capabilities for macOS, Windows, and Linux clients, encrypting all DNS traffic at the network level without per-application configuration. DoH is configured account-wide via the Admin Console with options for resolvers, fallback behavior, and group exceptions.

## Key Information
- DoH is **disabled by default**
- Only supports **DNS A queries** (IPv4); AAAA/IPv6 not supported — falls back to IPv4 before DoH encapsulation
- Encrypts all DNS traffic regardless of originating application
- Config delivered server-side when user logs into client
- If client starts at login, DoH activates immediately on boot

## Prerequisites
- macOS, Windows, or Linux Twingate Client (mobile not supported)
- For DoH as a Resource: macOS ≥2024.311, Windows ≥2024.351, Linux ≥2024.331
- Admin Console access (Internet Security → Secure DNS)

## Configuration Options

| Setting | Options | Default |
|---|---|---|
| DoH enabled | On/Off | Off |
| Resolver | Pre-configured public resolvers or custom HTTPS URL | — |
| Fallback method | Strict / Automatic | Automatic |
| Exception groups | Any number of groups | None |

## Fallback Behavior
- **Strict**: Never falls back to regular DNS. If resolver unavailable, all DNS fails (including private DNS)
- **Automatic**: Falls back to regular DNS if resolver unavailable or lookup fails

## Custom DoH Resolver Template Fields
Append device-specific data to resolver URLs:

```
https://doh.example/query?host=${deviceHostname}&user=${userEmail}
```

| Field | Description |
|---|---|
| `${deviceName}` | Friendly Twingate name |
| `${deviceId}` | Twingate device ID |
| `${deviceModel}` | Hardware model string |
| `${deviceHostname}` | Device hostname |
| `${userEmail}` | Device owner email |

## DoH as a Resource
- When resolver domain matches a Twingate Resource, DoH traffic routes through that Resource
- Wildcard Resources (e.g., `*.autoco.internal`) supported
- **Required**: DoH Resource must have **Device-only Resource Policy** — otherwise users cannot authenticate and DNS fails

## Gotchas
- Custom resolver URL is only validated as an HTTPS endpoint — misconfigured URL + Strict mode = DNS failure for all users
- Private DNS addresses cannot be resolved by public DoH resolvers; use Automatic fallback or route through a Resource
- Users in any exception group revert to device-configured public DNS entirely
- DoH does not activate until user logs into the client (unless auto-start is enabled)

## Related Docs
- Twingate Client setup (macOS/Windows/Linux)
- Resource Policy configuration (Device-only policy)
- Internet Security / Admin Console settings