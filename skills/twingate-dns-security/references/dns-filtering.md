# DNS Filtering

## Page Title
DNS Filtering Overview

## Summary
Twingate provides native DNS filtering via DNS-over-HTTPS (DoH) for macOS, Windows, and Linux clients, requiring no client-side configuration changes. Filtering is profile-based, assigned to Groups, and supports security threat blocking, content categories, privacy protection, allowlists/denylists, and S3 log export.

## Key Information
- **Availability**: Add-on for Business and Enterprise plans; desktop only (macOS, Windows, Linux) — no mobile support
- **Mechanism**: Intercepts all DNS traffic via DoH; blocks at DNS layer (affects HTTPS, SSH, all protocols)
- **Block pages**: HTTP blocked sites redirect to block page by default; HTTPS requires Twingate Browser Extension deployment
- **Profile limit**: Maximum 10 DNS filtering profiles
- **Profile priority**: Higher-ranked profiles take precedence; Exception Groups override Enrolled Groups
- **Signed-out devices**: DNS filtering continues if "always run Internet Security" is configured; uses lowest-ranked profile
- **Log retention**: 90-day analytics window; recent activity logs with device hostname, IP, profile used, block reason

## Prerequisites
- Business or Enterprise plan with DNS filtering add-on
- Twingate Client running on macOS, Windows, or Linux
- Secure DNS enabled in Admin Console

## Step-by-Step: Enable DNS Filtering
1. Navigate to **Internet Security** tab in Admin Console
2. If Secure DNS is disabled → enable it → select **Twingate DNS Filtering**
3. If Secure DNS already enabled → change DoH resolver to **Twingate DNS Filtering**
4. Configure profiles: click profile name or **Manage → Edit Filtering Rules**

## Configuration Values

### Filtering Rule Categories
| Type | Options |
|------|---------|
| Security | Threat Intelligence Feeds, Google Safe Browsing, DNS rebinding, IDN homograph, Typosquatting, DGA, Newly registered domains (off by default), Parked domains |
| Content | Gambling, Dating, Adult content, Piracy, Social media, Games, Streaming, Force Safe Search, YouTube safe mode |
| Privacy | Block disguised 3rd-party trackers, Block affiliate/tracking links, Block ads and trackers |

### S3 Log Export JSON Fields
- `event_type`: `"dns_filtering"`
- `status`: `"default"` (allowed lookup) | `"blocked"` | `"allowed"` (allowlist match)
- `device.id`: Twingate device ID or hardware ID if never logged in
- `reasons[].id`: e.g., `"category:social-networks"`

## Gotchas
- **Allowlist overrides everything** — domains on allowlist are never blocked regardless of other rules
- **Group assignment**: A Group can only be in one DNS filtering profile at a time; cannot be both enrolled and excluded simultaneously
- **No filtering if unassigned**: Users not in any Group assigned to a profile receive no DNS filtering
- **Blocking tracking links** may break email unsubscribe flows
- **Blocking ads/trackers** may break some sites
- **Client version requirement**: macOS < 2024.311 or Windows < 2024.351 shows generic device info (`"No hostname"` / `"No device"`) for signed-out devices
- **TLD blocking**: Add `.zip` to denylist to block all `.zip` TLD domains

## Related Docs
- DNS-over-HTTPS (DoH) documentation
- Internet Security Client Configuration (always-on)
- Twingate Browser Extension (HTTPS block pages)
- Exception Groups setup
- Syncing data to S3