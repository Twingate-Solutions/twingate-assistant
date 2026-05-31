# DNS-over-HTTPS (DoH) - Twingate

## Summary
Twingate provides native DoH capabilities that encrypt all DNS traffic at the network level on macOS, Windows, and Linux clients. Configuration is managed via the Admin Console with options for resolver selection, fallback behavior, and group exceptions. DoH is disabled by default.

## Key Information
- Encrypts all DNS A record queries not destined for Twingate Resources
- AAAA (IPv6) queries not supported; falls back to IPv4 before DoH encapsulation
- Only applies when user is logged into the Twingate Client
- If Client is set to start at login, DoH activates immediately on boot

## Prerequisites
- macOS, Windows, or Linux Twingate Client (mobile not supported)
- For DoH as a Resource: macOS ≥2024.311, Windows ≥2024.351, Linux ≥2024.331
- Admin Console access (Internet Security → Secure DNS)

## Configuration Values

| Setting | Options | Default |
|---|---|---|
| DoH enabled | Toggle on/off | Disabled |
| Fallback method | `Strict` / `Automatic` | Automatic |
| Resolver | Pre-configured public resolvers or custom HTTPS URL | — |
| Exception groups | Any number of groups | None |

### Custom Resolver URL Template Fields
```
${deviceName}      # Friendly Twingate name
${deviceId}        # Twingate device ID
${deviceModel}     # Hardware model string
${deviceHostname}  # Device hostname
${userEmail}       # Device owner email
```
Example: `https://doh.example/query?host=${deviceHostname}`

## Fallback Behavior
- **Strict**: Never falls back to regular DNS. If DoH resolver unavailable, all DNS fails (including private DNS)
- **Automatic**: Falls back to regular DNS if resolver unavailable or lookup fails

## DoH as a Resource
- When DoH resolver domain matches a Twingate Resource, DoH traffic routes through that Resource
- Wildcard Resources (e.g., `*.autoco.internal`) supported
- **DoH Resource must use Device-only Resource Policy** — otherwise users cannot authenticate and DNS breaks entirely

## Gotchas
- Custom resolver URLs are only validated as HTTPS endpoints, not as valid DoH resolvers — misconfiguration with Strict mode will break DNS for all users
- Private DNS addresses cannot be resolved by public DoH resolvers; use Automatic fallback or route via a Resource
- If a user belongs to at least one exception group, their client uses device-configured DNS (not DoH)
- Exception group members receive no DoH configuration at all

## Related Docs
- Twingate Client setup (macOS, Windows, Linux)
- Resource Policy configuration (Device-only policies)
- Internet Security / Secure DNS Admin Console section