# DNS-over-HTTPS (DoH) - Twingate

## Summary
Twingate provides native DoH capabilities on macOS, Windows, and Linux clients, encrypting all DNS traffic at the network level with no per-application configuration. Configuration is managed via the Admin Console under **Internet Security > Secure DNS**.

## Key Information
- DoH is **disabled by default**
- Only supports **DNS A queries** (IPv4); AAAA/IPv6 queries fall back to IPv4 first
- DoH encrypts all non-Twingate-Resource DNS traffic automatically when client is logged in
- If client is set to start at login, DoH protection begins at machine boot

## Prerequisites
- Twingate Client running on macOS, Windows, or Linux (not available on mobile)
- Admin Console access
- For DoH as a Resource: macOS 2024.311+, Windows 2024.351+, Linux 2024.331+

## Configuration Steps
1. Navigate to Admin Console → **Internet Security** → **Secure DNS**
2. Toggle DoH enabled for the account
3. Select a pre-configured public resolver or enter a custom DoH resolver URL
4. Set fallback behavior (Strict or Automatic)
5. Optionally add exception groups to exclude from DoH

## Configuration Values

**Fallback Modes:**
- `Strict` — Never falls back to regular DNS; all queries fail if DoH resolver unavailable (including private DNS)
- `Automatic` *(default)* — Falls back to regular DNS if resolver unavailable or lookup fails

**Custom Resolver URL Template Fields:**
| Field | Description |
|---|---|
| `${deviceName}` | Device's friendly Twingate name |
| `${deviceId}` | Device's Twingate ID |
| `${deviceModel}` | Device model string |
| `${deviceHostname}` | Device hostname |
| `${userEmail}` | Device owner's email |

Example: `https://doh.example/query?deviceHostname=${deviceHostname}`

## DoH as a Resource
- When DoH resolver domain matches a Twingate Resource, DoH traffic routes through that Resource
- Wildcard Resources (e.g., `*.autoco.internal`) are supported
- **Required:** DoH Resource must use a **Device-only Resource Policy** — users cannot authenticate otherwise, causing DNS failure

## Gotchas
- Custom resolver URLs are only validated as HTTPS endpoints — misconfigured URLs + Strict mode = DNS failure for all users
- Strict mode blocks **private DNS resolution** (private names can't resolve via public DoH resolvers)
- Exception group membership: if a user is in *any* exception group, DoH is fully disabled for that user
- AAAA (IPv6) queries are not supported

## Related Docs
- Twingate Client setup (macOS, Windows, Linux)
- Resource Policies (Device-only policy)
- Internet Security configuration