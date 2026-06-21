# DNS-over-HTTPS (DoH) - Twingate

## Summary
Twingate provides native DoH capabilities that encrypt all DNS traffic at the network level on macOS, Windows, and Linux clients. No per-application configuration is required. DoH is configured account-wide via the Admin Console with group-level exceptions.

## Key Information
- **Platform support**: macOS, Windows, Linux only (not mobile)
- **Default state**: DoH is **disabled** by default
- **Scope**: Encrypts all DNS A queries not destined for a Twingate Resource
- **IPv6**: AAAA queries not supported; falls back to IPv4 before DoH encapsulation
- **Activation**: If client starts at login, DoH activates immediately on boot

## Prerequisites
- Twingate Client running on macOS, Windows, or Linux
- Admin Console access (Internet Security → Secure DNS)
- For DoH as a Resource: macOS 2024.311+, Windows 2024.351+, Linux 2024.331+

## Configuration Options (Admin Console)
| Setting | Options | Default |
|---|---|---|
| DoH enabled | On/Off | Off |
| Resolver | Pre-configured public resolvers or custom HTTPS URL | — |
| Fallback method | Strict / Automatic | Automatic |
| Exception groups | Any number of groups | None |

## Fallback Modes
- **Automatic**: Falls back to regular DNS if resolver unavailable or lookup fails
- **Strict**: Never falls back; all DNS fails if resolver is unavailable (including private DNS)

## Custom Resolver Template Variables
Append device-specific info to custom resolver URLs:
```
${deviceName}       # Friendly Twingate name
${deviceId}         # Twingate device ID
${deviceModel}      # Hardware model string
${deviceHostname}   # Device hostname
${userEmail}        # Device owner email
```
Example: `https://doh.example/query?host=${deviceHostname}`

## DoH as a Resource
- If DoH resolver domain matches a Twingate Resource, DoH traffic routes through that Resource
- Wildcard Resources (e.g., `*.autoco.internal`) are supported
- **Required**: DoH Resource must use a **Device-only Resource Policy** — otherwise users lose DNS entirely

## Gotchas
- Custom resolver URL is only validated as an HTTPS endpoint — misconfiguration + Strict mode = DNS failure for all users
- Strict mode breaks private DNS resolution (public DoH resolvers can't resolve internal names)
- Exception group membership is OR logic: one exception group membership disables DoH for that user
- DoH Resources without Device-only policy cause authentication failures, breaking DNS for end users
- Private DoH resolvers are common with DNS filtering services; use custom resolver field for these

## Related Docs
- Twingate Client setup
- Resource Policies (Device-only policy)
- Internet Security configuration
- DNS filtering service integration