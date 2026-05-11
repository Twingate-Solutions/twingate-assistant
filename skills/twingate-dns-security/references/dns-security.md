# DNS-over-HTTPS (DoH) - Twingate

## Summary
Twingate provides native DoH capabilities on macOS, Windows, and Linux clients, encrypting all DNS traffic at the network level without per-application configuration. DoH is managed via the Admin Console and supports public resolvers, custom resolvers, fallback modes, and group-based exceptions.

## Key Information
- **Platform support**: macOS, Windows, Linux only (not mobile)
- DoH is **disabled by default**
- Encrypts all DNS A record queries not destined for a Twingate Resource
- AAAA (IPv6) queries not supported; falls back to IPv4 before DoH encapsulation
- If Client is set to start at login, DoH activates immediately on boot

## Prerequisites
- Twingate Client running on macOS, Windows, or Linux
- Admin Console access (Internet Security → Secure DNS)
- For DoH as a Resource: Client versions macOS 2024.311+, Windows 2024.351+, Linux 2024.331+

## Configuration Options

| Setting | Details |
|---|---|
| Enable/Disable | Account-wide toggle; disabled by default |
| Resolver | Pre-configured public resolvers or custom HTTPS endpoint |
| Fallback Method | `Strict` or `Automatic` (default: Automatic) |
| Exception Groups | Groups excluded from DoH; use device's local DNS instead |

## Custom Resolver URL Template Fields
```
${deviceName}       # Friendly Twingate device name
${deviceId}         # Twingate device ID
${deviceModel}      # Hardware model string
${deviceHostname}   # Device hostname
${userEmail}        # Device owner email
```
Example: `https://doh.example/query?host=${deviceHostname}`

## Fallback Behavior
- **Strict**: Never falls back to regular DNS; all queries fail if DoH resolver unavailable (including private DNS)
- **Automatic**: Falls back to regular DNS if resolver is unavailable or lookup fails

## DoH as a Resource
- When DoH resolver domain matches a Twingate Resource, DoH traffic routes through that Resource
- Wildcard Resources (e.g., `*.autoco.internal`) are supported
- **Required**: DoH Resource must use a **Device-only Resource Policy** — otherwise users cannot authenticate and DNS breaks entirely

## Gotchas
- Custom resolver URL is **not validated** as a DoH endpoint beyond being HTTPS — misconfiguration + Strict mode = DNS failure for all users
- Private DNS names will fail in Strict mode if using a public DoH resolver (public resolvers can't resolve private addresses)
- Exception group membership is OR logic: one matching exception group disables DoH for that user
- DoH configuration is received from server only when user is **logged in** to the Client

## Related Docs
- Twingate Client setup
- Internet Security / Secure DNS (Admin Console)
- Resource Policies (Device-only policy configuration)