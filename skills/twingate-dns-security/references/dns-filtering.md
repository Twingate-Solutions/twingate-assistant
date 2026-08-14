---
source: https://www.twingate.com/docs/dns-filtering
type: docs
fetched: 2026-08-14
source_version: e1d70c8a5e45e89185c1712a67c49fe403263969cae631ee2e227edadde456ce
---

# DNS Filtering

## Summary
Twingate provides native DNS filtering via DNS-over-HTTPS (DoH) for macOS, Windows, and Linux clients. It blocks domains at the DNS layer, intercepting all traffic types (HTTPS, SSH, etc.) to blocked domains. Requires Business or Enterprise plan as an add-on.

## Key Information
- **Platforms**: macOS, Windows, Linux only (no mobile)
- **Protocol**: DNS-over-HTTPS (DoH)
- **Profiles**: Max 10 DNS filtering profiles; profile ranking determines priority for users in multiple groups
- **Allowlist takes precedence** over all other rules including security categories
- **Everyone group** is assigned to default profile by default
- **Log retention**: 90-day analytics; recent activity logs available
- **Block pages**: HTTP by default; HTTPS block pages require Twingate Browser Extension deployment

## Prerequisites
- Business or Enterprise plan with DNS Filtering add-on
- Twingate Client running on macOS, Windows, or Linux
- Secure DNS must be enabled in Admin Console

## Step-by-Step: Enable DNS Filtering
1. Navigate to **Internet Security** tab in Admin Console
2. If Secure DNS disabled: enable it → select **Twingate DNS Filtering**
3. If Secure DNS already enabled: change DoH resolver to **Twingate DNS Filtering**
4. Click a profile name → **Manage** → **Edit Filtering Rules** to configure rules

## Configuration Values

### Security Categories (all enabled by default except noted)
- `Threat Intelligence Feeds`
- `Google Safe Browsing`
- `DNS rebinding`
- `IDN homograph attacks`
- `Typosquatting`
- `Domain generation algorithms`
- `Newly registered domains` *(disabled by default)*
- `Parked domains`

### Content Restrictions
- Gambling, Dating, Adult content, Piracy, Social media, Games, Streaming sites
- `Force Safe Search`, `YouTube safe mode`

### Privacy Protection
- Block disguised third-party trackers
- Block affiliate & tracking links *(may break email unsubscribe links)*
- Block ads and trackers

## S3 Log Export Format (JSON)
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
- Users in both an enrolled Group and an Exception Group **will not** have DNS filtering (exception takes precedence)
- Groups can only be assigned to **one** profile at a time
- Signed-out devices use the **lowest-ranked** profile (when always-on Internet Security is configured)
- Client versions before macOS `2024.311` / Windows `2024.351` show generic device info for signed-out devices
- Blocking ads/tracking links may break site functionality and email interactions
- TLDs can be denylisted (e.g., `.zip` blocks all `.zip` domains)

## Related Docs
- DNS-over-HTTPS (DoH) documentation
- Internet Security Client Configuration (always-on)
- Exception Groups setup
- Syncing data to S3
- Twingate Browser Extension deployment