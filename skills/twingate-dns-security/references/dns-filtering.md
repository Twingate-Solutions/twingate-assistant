# DNS Filtering

## Page Title
DNS Filtering Overview

## Summary
Twingate's native DNS filtering intercepts and filters all DNS traffic via DNS-over-HTTPS on macOS, Windows, and Linux clients. Rules are configured through profiles assigned to Groups, with allowlists, denylists, security categories, content categories, and privacy protection options. Available as a Business/Enterprise add-on.

## Key Information
- **Platform support**: macOS, Windows, Linux only (no mobile)
- **Protocol**: DNS-over-HTTPS (DoH) — no client configuration changes required
- **Activation**: Admin Console → "Internet Security" tab → Enable Secure DNS → Select "Twingate DNS Filtering"
- **Profile limit**: Max 10 DNS filtering profiles
- **Default**: Single profile created with "Everyone" group assigned; all security categories enabled except "newly registered domains"
- **Allowlist takes precedence** over all other rules including security/content categories
- **Exception Groups** take precedence over Enrolled Groups (user in both = no filtering)
- **Block pages**: HTTP by default; HTTPS requires Twingate Browser Extension deployed
- **Log retention**: 90-day analytics; logs exportable to AWS S3 in JSON (one event per line)
- **Signed-out devices**: Can still filter if configured with "always run Internet Security"

## Prerequisites
- Business or Enterprise plan with DNS Filtering add-on
- Twingate Client running on macOS, Windows, or Linux
- Secure DNS enabled in Admin Console
- Browser Extension for HTTPS block pages

## Step-by-Step: Enable DNS Filtering
1. Navigate to Admin Console → **Internet Security** tab
2. If Secure DNS disabled: enable it → select **Twingate DNS Filtering**
3. If Secure DNS already enabled: change DoH resolver to **Twingate DNS Filtering**
4. Configure profiles: click profile name → **Manage** → **Edit Filtering Rules**

## Configuration Values

### Profile Priority
- Higher-ranked profiles take precedence for users in multiple groups
- Lowest-ranked profile with "Everyone" group serves as catch-all default
- Signed-out devices (always-on mode) use lowest-ranked profile

### Security Categories (all enabled by default except marked)
- Threat Intelligence Feeds, Google Safe Browsing, DNS rebinding, IDN homograph attacks, Typosquatting, Domain generation algorithms, Parked domains
- `newly_registered_domains` — **disabled by default**

### S3 Log Event Schema
```json
{
  "event_type": "dns_filtering",
  "event": {
    "version": 1,
    "time": "<UTC datetime>",
    "domain": "<queried domain>",
    "root": "<root domain>",
    "device": { "id": "<twingate_id or hardware_id>", "name": "<device name>" },
    "connection": { "client_ip": "<ip>", "protocol": "DNS-over-HTTPS" },
    "status": "default|blocked|allowed",
    "reasons": [{ "id": "category:social-networks", "name": "Social Networks" }]
  }
}
```

## Gotchas
- Groups can only be assigned to **one** DNS filtering profile at a time
- A group cannot be both enrolled and excluded simultaneously
- Blocking tracking links may break email unsubscribe functionality
- Blocking ads/trackers may break site functionality
- Client versions before macOS `2024.311` / Windows `2024.351` show generic device info for signed-out devices
- TLDs can be added to denylist (e.g., `.zip` blocks all `.zip` domains)
- Users not in any assigned Group have **no filtering applied**

## Related Docs
- DNS-over-HTTPS (DoH) documentation
- Internet Security Client Configuration (always-on)
- Exception Groups configuration
- Twingate Browser Extension deployment
- Syncing data to AWS S3