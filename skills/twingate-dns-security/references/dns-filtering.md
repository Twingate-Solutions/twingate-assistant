# DNS Filtering Overview

## Summary
Twingate DNS filtering intercepts and filters all DNS traffic via DNS-over-HTTPS for macOS, Windows, and Linux clients. It blocks security threats and content categories using profile-based rules assigned to user Groups. Available as an add-on for Business and Enterprise plans.

## Key Information
- Uses DNS-over-HTTPS (DoH); no client-side config changes required beyond running Twingate Client
- **Not available** on mobile devices (iOS/Android)
- Blocks at DNS layer — affects HTTPS, SSH, and all other traffic types
- Block pages require **Twingate Browser Extension** for HTTPS sites
- Logs retained for 90 days; can be synced to AWS S3
- Maximum **10 DNS filtering profiles**

## Prerequisites
- Business or Enterprise plan with DNS filtering add-on
- Twingate Client running on macOS, Windows, or Linux
- Secure DNS enabled in Admin Console → Internet Security tab

## Step-by-Step: Enable DNS Filtering
1. Navigate to Admin Console → **Internet Security** tab
2. If Secure DNS disabled: enable it, select **Twingate DNS Filtering**
3. If Secure DNS enabled: change DoH resolver to **Twingate DNS Filtering**
4. Configure profiles: click profile name → **Manage** → **Edit Filtering Rules**

## Configuration Values

### Profile Rules
| Rule Type | Options |
|-----------|---------|
| Allowlist/Denylist | Specific domains or TLDs (e.g., `.zip`) |
| Security Categories | Threat feeds, Google Safe Browsing, DNS rebinding, IDN homograph, typosquatting, DGA, newly registered domains, parked domains |
| Content Restrictions | Gambling, Dating, Adult, Piracy, Social media, Games, Streaming, Force Safe Search, YouTube safe mode |
| Privacy Protection | Block disguised trackers, affiliate/tracking links, ads & trackers |

### S3 Log Event Fields
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
- **Allowlist takes precedence** over all other rules including security categories
- **Exception Groups override enrolled Groups** — if user is in both, filtering is disabled for that user
- A Group can only be assigned to **one profile** at a time; cannot be both enrolled and excluded simultaneously
- Signed-out devices use the **lowest-ranked profile** (when always-on Internet Security is configured)
- Client versions before macOS `2024.311` / Windows `2024.351` show generic device info for signed-out users
- Blocking tracking links may break email unsubscribe functionality
- Default: all security categories enabled **except** newly registered domains
- Users not in any assigned Group have **no filtering applied**

## Related Docs
- DNS-over-HTTPS (DoH) configuration
- Internet Security Client Configuration (always-on)
- Exception Groups setup
- Syncing data to AWS S3
- Twingate Browser Extension deployment