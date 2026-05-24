# DNS-over-HTTPS (DoH) - Twingate

## Summary
Twingate provides native DoH capabilities that encrypt all DNS traffic at the network level on macOS, Windows, and Linux clients. No per-application configuration is required. DoH is managed centrally via the Admin Console and disabled by default.

## Key Information
- **Platform support**: macOS, Windows, Linux only (not mobile)
- DoH encrypts all DNS A record queries not destined for a Twingate Resource
- AAAA (IPv6) queries not supported; falls back to IPv4 before DoH encapsulation
- If Client is set to start at login, DoH activates immediately on boot
- DoH disabled by default; must be explicitly enabled per account

## Prerequisites
- Twingate Client versions for "DoH as a Resource" feature:
  - macOS ≥ 2024.311
  - Windows ≥ 2024.351
  - Linux ≥ 2024.331

## Configuration (Admin Console → Internet Security → Secure DNS)

| Setting | Options | Default |
|---|---|---|
| DoH enabled | On/Off | Off |
| Resolver | Pre-configured public resolvers or custom HTTPS URL | — |
| Fallback method | Strict / Automatic | Automatic |
| Exception groups | Any number of groups | None |

## Custom Resolver URL Template Fields
Append device-specific info to custom resolver URLs:

```
https://doh.example/query?host=${deviceHostname}&user=${userEmail}
```

| Field | Example Value |
|---|---|
| `${deviceName}` | Alex's MacBook Pro |
| `${deviceId}` | (Twingate internal ID) |
| `${deviceModel}` | MacBook Pro (16-inch, M1 Pro, Late 2021) |
| `${deviceHostname}` | alexs-macbook-pro.local |
| `${userEmail}` | alex@company.com |

## DoH as a Resource
- When DoH resolver domain matches a Twingate Resource, DoH traffic routes through that Resource
- Wildcard Resources (e.g., `*.autoco.internal`) are supported
- **Required**: DoH Resource must use a **Device-only Resource Policy** — users cannot authenticate otherwise, breaking DNS entirely

## Fallback Behavior
- **Strict**: Never falls back to regular DNS; all queries fail if resolver unavailable (including private DNS)
- **Automatic**: Falls back to regular DNS if resolver unavailable or lookup fails

## Gotchas
- Custom resolver URL is not validated beyond being an HTTPS endpoint — misconfiguration + Strict mode = DNS failure for all users
- Private DNS names cannot be resolved by public DoH resolvers; use Automatic mode or route via a Resource
- Exception group membership: if user is in **any** exception group, DoH is disabled for that user
- DoH Resources without Device-only policy will break DNS for end users

## Related Docs
- Twingate Client setup
- Internet Security / Resource Policies
- Device-only Resource Policy configuration