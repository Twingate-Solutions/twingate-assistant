---
source: https://www.twingate.com/docs/dns-security
type: docs
fetched: 2026-10-25
source_version: 90eafdc2370ed13e6dde6ab1113daa8396fdcc30ace80c634d043a5a2f409e67
trust: official
---

# DNS-over-HTTPS (DoH) — Twingate

## Summary
Twingate provides native DNS-over-HTTPS encryption for all DNS traffic on macOS, Windows, and Linux clients. DoH encrypts all non-Resource DNS queries automatically once enabled in the Admin Console, with no per-application configuration needed.

## Key Information
- **Platform support**: macOS, Windows, Linux only (not mobile)
- DoH is **disabled by default**
- Encrypts all DNS A queries not destined for a Twingate Resource
- AAAA (IPv6) queries not supported; falls back to IPv4 before DoH encapsulation
- If client is set to start at login, DoH activates on machine boot

## Prerequisites
- Twingate Client running on macOS, Windows, or Linux
- Admin Console access → **Internet Security** tab → **Secure DNS** page

## Configuration Options

| Setting | Details |
|---|---|
| Enable/Disable DoH | Account-wide toggle; disabled by default |
| DoH Resolver | Pre-configured public resolvers or custom HTTPS endpoint |
| Fallback Behavior | `Strict` (never fall back) or `Automatic` (fall back on failure) — default: Automatic |
| Exception Groups | Groups excluded from DoH; use device's local DNS instead |

## Custom Resolver Template Fields
Append device context to custom resolver URLs:

| Field | Example Value |
|---|---|
| `${deviceName}` | Alex's MacBook Pro |
| `${deviceId}` | Twingate device ID |
| `${deviceModel}` | MacBook Pro (16-inch, M1 Pro, Late 2021) |
| `${deviceHostname}` | alexs-macbook-pro.local |
| `${userEmail}` | user@example.com |

**Example**: `https://doh.example/query?deviceHostname=${deviceHostname}`

## DoH as a Resource
- If the DoH resolver's domain matches a Twingate Resource, DoH traffic routes through that Resource
- Wildcard Resources (e.g., `*.autoco.internal`) are supported
- **DoH Resources MUST use a Device-only Resource Policy** — otherwise users cannot authenticate and DNS breaks entirely

## Fallback Methods
- **Strict**: DNS fails completely if DoH resolver is unreachable; private DNS may also fail
- **Automatic**: Falls back to standard DNS if resolver unavailable or lookup fails

## Gotchas
- Custom resolver URL is only validated as an HTTPS endpoint — misconfiguration + Strict mode = DNS failure for all users
- AAAA queries unsupported; IPv6 falls back to IPv4
- Exception group membership: if a user belongs to **any** exception group, DoH is disabled for them
- Private DNS addresses cannot resolve via public DoH resolvers — use Automatic mode or route through a Resource
- DoH Resources without Device-only policy will break end-user DNS authentication

## Related Docs
- Twingate Client configuration
- Resource Policies (Device-only policy)
- Internet Security / Secure DNS Admin Console page