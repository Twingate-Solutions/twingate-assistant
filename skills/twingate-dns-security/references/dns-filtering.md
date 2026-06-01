# DNS Filtering

## Page Title
DNS Filtering Overview

## Summary
Twingate provides native DNS filtering via DNS-over-HTTPS (DoH) for macOS, Windows, and Linux clients, requiring no client-side configuration changes. Filtering is profile-based and assigned to Groups, blocking threats, content categories, and specific domains. Available as an add-on for Business and Enterprise plans.

## Key Information
- **Platform support**: macOS, Windows, Linux only (no mobile)
- **Protocol**: DNS-over-HTTPS (DoH) — intercepts all DNS traffic automatically
- **Block pages**: HTTP sites blocked by default; HTTPS requires Twingate Browser Extension deployment
- **Profile limit**: Maximum 10 DNS filtering profiles
- **Priority**: Allowlist > profile ranking order > default rules
- **Exception Groups** override Enrolled Groups (excluded user won't be filtered even if in enrolled group)
- **Signed-out devices**: Use lowest-ranked profile if configured for always-on Internet Security
- **Log retention**: 90-day analytics; recent activity logs filterable by allowed/blocked status
- **S3 export**: JSON format, one event per line

## Prerequisites
- Business or Enterprise plan with DNS Filtering add-on
- Secure DNS enabled in Admin Console
- Twingate Client running on user devices
- Browser Extension for HTTPS block pages

## Step-by-Step: Enable DNS Filtering
1. Navigate to **Internet Security** tab in Admin Console
2. If Secure DNS disabled → enable it → select **Twingate DNS Filtering**
3. If Secure DNS already enabled → change DoH resolver to **Twingate DNS Filtering**
4. Configure profiles: click profile name or **Manage → Edit Filtering Rules**

## Configuration Values

### DNS Filtering Profile Rules
| Category | Options |
|----------|---------|
| Allowlist/Denylist | Specific domains or TLDs (e.g., `.zip`) |
| Security Categories | Threat feeds, Google Safe Browsing, DNS rebinding, IDN homograph, typosquatting, DGA, newly registered domains, parked domains |
| Content Restrictions | Gambling, Dating, Adult, Piracy, Social Media, Games, Streaming, Force Safe Search, YouTube Safe Mode |
| Privacy Protection | Block disguised trackers, affiliate/tracking links, ads and trackers |

### S3 Event JSON Fields
```json
{
  "event_type": "dns_filtering",
  "event": {
    "version": 1,
    "time": "<UTC datetime>",
    "domain": "<queried domain>",
    "root": "<root domain>",
    "device": { "id": "<device_id>", "name": "<device_name>" },
    "connection": { "client_ip": "<ip>", "protocol": "DNS-over-HTTPS" },
    "status": "default|blocked|allowed",
    "reasons": [{ "id": "category:social-networks", "name": "Social Networks" }]
  }
}
```

## Gotchas
- Newly registered domains category is **disabled by default**; all other security categories are enabled by default
- A Group can only be assigned to **one** DNS filtering profile at a time
- Blocking ads/trackers/tracking links may break some site functionality and email unsubscribe links
- Client versions before macOS **2024.311** or Windows **2024.351** show generic device info for signed-out devices (`No hostname`/`No device`)
- Users not in any assigned Group are **not filtered** at all — create a catch-all profile with Everyone group as lowest priority

## Related Docs
- DNS-over-HTTPS (DoH) documentation
- Internet Security Client Configuration (always-on filtering)
- Exception Groups setup
- Syncing data to S3
- Twingate Browser Extension deployment