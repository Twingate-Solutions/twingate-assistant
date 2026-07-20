# DNS-over-HTTPS (DoH) - Twingate

## Summary
Twingate provides native DoH capabilities for macOS, Windows, and Linux clients, encrypting all DNS traffic at the network level without per-application configuration. DoH is disabled by default and configured via the Admin Console under Internet Security > Secure DNS.

## Key Information
- **Supported platforms**: macOS, Windows, Linux only (not mobile)
- DoH encrypts all DNS A queries not destined for a Twingate Resource
- AAAA (IPv6) queries not supported; falls back to IPv4 before DoH encapsulation
- If Client is set to start at login, DoH activates immediately after boot
- Default fallback method: **Automatic**
- DoH disabled by default

## Prerequisites
- Client versions for "DoH as a Resource":
  - macOS ≥ 2024.311
  - Windows ≥ 2024.351
  - Linux ≥ 2024.331

## Configuration (Admin Console: Internet Security > Secure DNS)

| Setting | Options | Default |
|---|---|---|
| DoH enabled | On/Off | Off |
| Resolver | Pre-configured public resolvers or custom HTTPS URL | — |
| Fallback method | Strict / Automatic | Automatic |
| Exception groups | Any Twingate groups | None |

## Fallback Modes
- **Strict**: Never falls back to regular DNS. If DoH resolver unavailable, all DNS fails (including private DNS)
- **Automatic**: Falls back to regular DNS if resolver unavailable or lookup fails

## Custom DoH Resolver Template Fields
Append device-specific data to custom resolver URLs:

```
https://doh.example/query?host=${deviceHostname}&user=${userEmail}
```

| Field | Description |
|---|---|
| `${deviceName}` | Friendly Twingate device name |
| `${deviceId}` | Twingate device ID |
| `${deviceModel}` | Device model string |
| `${deviceHostname}` | Device hostname |
| `${userEmail}` | Device owner email |

## DoH as a Resource
- When DoH resolver domain matches a Twingate Resource, traffic routes through that Resource
- Wildcards (e.g., `*.autoco.internal`) supported
- **Required**: DoH Resource must use a **Device-only Resource Policy** — otherwise users cannot authenticate and DNS breaks entirely

## Gotchas
- Custom resolver URLs are only validated as HTTPS endpoints — invalid DoH URLs in Strict mode will break DNS for **all users**
- Private DNS addresses cannot be resolved via public DoH resolvers; use Automatic mode or route through a Resource
- Exception group membership is additive: if a user is in *any* exception group, DoH is disabled for them
- DoH is applied per-account; group exceptions are the only per-user granularity

## Related Docs
- Twingate Client setup (macOS, Windows, Linux)
- Resource Policies (Device-only policy)
- Internet Security overview