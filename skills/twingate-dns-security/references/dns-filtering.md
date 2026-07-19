# DNS Filtering

## Summary
Twingate provides native DNS-over-HTTPS (DoH) based filtering for macOS, Windows, and Linux clients. It controls website access through configurable profiles with allowlists, denylists, security threat blocking, and content category filtering. Available as an add-on for Business and Enterprise plans.

## Key Information
- **Platforms**: macOS, Windows, Linux only (no mobile support)
- **Protocol**: DNS-over-HTTPS (DoH) — intercepts all DNS traffic automatically
- **Limit**: Maximum 10 DNS filtering profiles
- **Log retention**: 90-day analytics window; real-time logs viewable in Admin Console
- **Block pages**: HTTP sites blocked by default; HTTPS block pages require Twingate Browser Extension deployed
- **Profile priority**: Higher-ranked profiles take precedence; Exception Groups override Enrolled Groups

## Prerequisites
- Business or Enterprise plan with DNS Filtering add-on
- Twingate Client running on supported OS
- Secure DNS enabled in Admin Console

## Step-by-Step: Enable DNS Filtering
1. Navigate to **Internet Security** tab in Admin Console
2. If Secure DNS disabled → enable it → select **Twingate DNS Filtering**
3. If Secure DNS already enabled → change DoH resolver to **Twingate DNS Filtering**
4. Configure profiles: click profile name → **Manage** → **Edit Filtering Rules**

## Configuration Values

### Filtering Rule Categories
| Category | Options |
|----------|---------|
| Security | Threat Intelligence Feeds, Google Safe Browsing, DNS rebinding, IDN homograph, Typosquatting, DGA, Newly registered domains, Parked domains |
| Content | Gambling, Dating, Adult, Piracy, Social Media, Games, Streaming, Force Safe Search, YouTube Safe Mode |
| Privacy | Block disguised trackers, Block affiliate/tracking links, Block ads and trackers |

### S3 Export JSON Fields
```
event_type, event.version, event.time, event.domain, event.root,
event.device.id, event.device.name, event.connection.client_ip,
event.connection.protocol, event.status, event.reasons[].id, event.reasons[].name
```
**Status values**: `default` (allowed lookup), `blocked`, `allowed` (allowlist match)

## Gotchas
- **Allowlist takes precedence** over all other rules including security/content categories
- **Exception Groups override Enrolled Groups** — user in both will NOT have filtering
- **Groups can only belong to one profile** at a time
- **Signed-out devices**: use lowest-ranked profile if configured for always-on Internet Security
- **Client version requirements**: macOS ≥ 2024.311, Windows ≥ 2024.351 for proper signed-out hostname logging; older versions show "No hostname"/"No device"
- Blocking tracking links may break email unsubscribe functionality
- Newly registered domains category is **disabled by default**
- Users not in any Group assigned to a profile receive **no DNS filtering**

## Related Docs
- DNS-over-HTTPS (DoH) documentation
- Internet Security Client Configuration (always-on setup)
- Exception Groups configuration
- Twingate Browser Extension deployment
- Syncing data to S3