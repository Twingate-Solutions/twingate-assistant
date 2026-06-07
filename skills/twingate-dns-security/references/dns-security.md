# DNS-over-HTTPS (DoH) - Twingate

## Summary
Twingate provides native DoH capabilities for macOS, Windows, and Linux clients, encrypting all DNS traffic at the network level without per-application configuration. Settings are managed centrally via the Admin Console and pushed to clients automatically.

## Key Information
- DoH is **disabled by default**
- Only supports DNS **A queries** (IPv4); AAAA/IPv6 not supported — falls back to IPv4 before encapsulation
- Applies to all DNS traffic **not** destined for a Twingate Resource
- If client is set to start at login, DoH activates immediately on boot

## Prerequisites
- macOS, Windows, or Linux Twingate Client (mobile not supported)
- For DoH as a Resource: macOS ≥2024.311, Windows ≥2024.351, Linux ≥2024.331
- Admin Console access to **Internet Security → Secure DNS**

## Configuration Steps
1. Navigate to Admin Console → **Internet Security** → **Secure DNS**
2. Toggle DoH enabled for the account
3. Select a pre-configured public resolver or enter a custom HTTPS endpoint
4. Set fallback method: **Strict** or **Automatic** (default: Automatic)
5. Optionally add exception groups to exclude from DoH

## Configuration Values

**Fallback Modes:**
| Mode | Behavior |
|------|----------|
| `Automatic` | Falls back to regular DNS if resolver unavailable or lookup fails (default) |
| `Strict` | Never falls back; all DNS fails if resolver unreachable |

**Custom Resolver URL Template Fields:**
| Field | Description |
|-------|-------------|
| `${deviceName}` | Friendly Twingate device name |
| `${deviceId}` | Twingate device ID |
| `${deviceModel}` | Hardware model string |
| `${deviceHostname}` | Device hostname |
| `${userEmail}` | Device owner email |

Example: `https://doh.example/query?host=${deviceHostname}`

## DoH as a Resource
- When the DoH resolver domain matches a Twingate Resource, traffic routes through that Resource
- Wildcard Resources (e.g., `*.autoco.internal`) are supported
- **Required**: DoH Resource must use a **Device-only Resource Policy** — user-authenticated policies will break DNS

## Gotchas
- Custom resolver URL is only validated as an HTTPS endpoint — **no DoH functionality check**; misconfiguration + Strict mode = DNS failure for all users
- Strict mode can break **private DNS** resolution (private names can't resolve via public DoH resolver)
- Exception group membership is OR logic: one matching exception group disables DoH for that user
- AAAA queries unsupported; IPv6 falls back to IPv4 before DoH encapsulation

## Related Docs
- Twingate Client configuration
- Resource Policies (Device-only policy)
- Internet Security settings