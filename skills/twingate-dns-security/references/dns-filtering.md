# DNS Filtering

## Summary
Twingate's native DNS filtering intercepts and filters all DNS traffic via DNS-over-HTTPS (DoH) for macOS, Windows, and Linux clients. Rules are organized into profiles assigned to Groups, with allowlists/denylists, security threat categories, content categories, and privacy protection options. Available as a Business/Enterprise add-on.

## Key Information
- **Platform support**: macOS, Windows, Linux only (no mobile)
- **Protocol**: DNS-over-HTTPS (DoH) — no client config changes needed beyond running the Twingate Client
- **Limit**: 10 DNS filtering profiles maximum
- **Log retention**: 90 days of filtering analytics
- **Block pages**: HTTP sites blocked by default; HTTPS block pages require deploying the Twingate Browser Extension
- **Profile priority**: Higher-ranked profiles take precedence; users with no assigned Group profile are unfiltered
- **Exception Groups override enrolled Groups** — user in both = DNS filtering disabled for that user
- **Signed-out devices**: Can still use DNS filtering if configured via Internet Security Client Configuration; uses lowest-ranked profile

## Prerequisites
- Business or Enterprise plan with DNS Filtering add-on
- Secure DNS enabled in Admin Console → Internet Security tab
- Twingate Client running on macOS/Windows/Linux

## Step-by-Step: Enable DNS Filtering
1. Navigate to Admin Console → **Internet Security** tab
2. If Secure DNS is disabled: enable it and select **Twingate DNS Filtering**
3. If Secure DNS already enabled: change DoH resolver to **Twingate DNS Filtering**
4. Configure profiles: click profile name or **Manage → Edit Filtering Rules**

## Configuration Options

### Security Categories (all enabled by default except newly registered domains)
- Threat Intelligence Feeds, Google Safe Browsing, DNS rebinding, IDN homograph attacks, Typosquatting, Domain generation algorithms, Newly registered domains, Parked domains

### Content Restrictions
- Gambling, Dating, Adult content, Piracy, Social media, Games, Streaming sites, Force Safe Search, YouTube safe mode

### Privacy Protection
- Block disguised third-party trackers, Block affiliate & tracking links, Block ads and trackers

## S3 Export Event Format
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
- **Allowlist takes absolute precedence** over all other rules including security categories
- **TLDs can be denylisted** (e.g., `.zip` blocks all `.zip` domains)
- Blocking tracking links may break email unsubscribe links
- Blocking ads/trackers may break certain websites
- Client versions before macOS `2024.311` / Windows `2024.351` show generic device info for signed-out devices
- Groups can only be assigned to **one** DNS filtering profile at a time

## Related Docs
- DNS-over-HTTPS (DoH) documentation
- Internet Security Client Configuration (always-on filtering)
- Exception Groups setup
- Syncing data to S3
- Twingate Browser Extension deployment