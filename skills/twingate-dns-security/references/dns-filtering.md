# DNS Filtering

## Page Title
DNS Filtering Overview

## Summary
Twingate's native DNS filtering intercepts all DNS traffic via DNS-over-HTTPS (DoH) on macOS, Windows, and Linux clients. It provides security threat blocking, content category filtering, and privacy protection through configurable profiles assigned to user Groups. Available as a paid add-on for Business and Enterprise plans.

## Key Information
- **Platform support**: macOS, Windows, Linux only (no mobile)
- **Protocol**: DNS-over-HTTPS (DoH) — no client-side config changes required beyond running the Twingate Client
- **Block pages**: HTTP sites show block pages by default; HTTPS requires deploying the Twingate Browser Extension
- **Profile limit**: Max 10 DNS filtering profiles
- **Log retention**: 90-day analytics window; logs exportable to AWS S3 in JSON format
- **Default profile**: `Everyone` group assigned to single profile on creation
- **Priority**: Allowlist overrides all other rules; Exception Groups override Enrolled Groups; higher-ranked profiles take priority

## Prerequisites
- Business or Enterprise plan with DNS Filtering add-on
- Secure DNS enabled in Admin Console → Internet Security tab
- Twingate Client running on user devices

## Step-by-Step: Enable DNS Filtering
1. Navigate to **Admin Console → Internet Security tab**
2. If Secure DNS is disabled: enable it, select **Twingate DNS Filtering**
3. If Secure DNS already enabled: change DoH resolver to **Twingate DNS Filtering**
4. Click a profile name or **Manage → Edit Filtering Rules** to configure rules

## Configuration Values

### Filtering Rule Types
| Type | Notes |
|------|-------|
| Allowlist/Denylist | TLDs supported (e.g., `.zip` blocks all `.zip` domains) |
| Security Categories | Threat feeds, Google Safe Browsing, DNS rebinding, IDN homograph, typosquatting, DGA, newly registered domains, parked domains |
| Content Restrictions | Gambling, Dating, Adult, Piracy, Social Media, Games, Streaming, Force Safe Search, YouTube Safe Mode |
| Privacy Protection | Block disguised trackers, affiliate/tracking links, ads and trackers |

### S3 Log Export Event Schema
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
- **Multi-group users**: Profile ranking determines which rule applies — highest-ranked profile wins
- **Signed-out devices**: Uses lowest-ranked profile; client versions before macOS 2024.311 / Windows 2024.351 show generic device info (`No hostname` / `No device`)
- **Groups**: Cannot be assigned to multiple profiles simultaneously; cannot be both enrolled and excluded
- **Tracking link blocking**: May break email unsubscribe links
- **Always-on filtering**: Requires Internet Security Client Configuration setup separately
- **Default security categories**: All enabled except "newly registered domains"

## Related Docs
- DNS-over-HTTPS (DoH) documentation
- Internet Security Client Configuration (always-on setup)
- Exception Groups
- Twingate Browser Extension deployment
- Syncing data to S3