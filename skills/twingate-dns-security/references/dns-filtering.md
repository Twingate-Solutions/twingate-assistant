---
source: https://www.twingate.com/docs/dns-filtering
type: docs
fetched: 2026-09-20
source_version: 2794e856b31a7a4b5074bfce10eecc8aadd3ef99970ef06970d474d3be05fe0a
---

# DNS Filtering

## Summary
Twingate DNS filtering intercepts and filters all DNS traffic using DNS-over-HTTPS (DoH) for macOS, Windows, and Linux clients. It blocks security threats and content categories via configurable profiles assigned to user Groups. Available as a Business/Enterprise add-on.

## Key Information
- Operates at DNS layer — blocks all traffic types (HTTPS, SSH, etc.) to blocked domains
- Mobile platforms **not supported**; macOS, Windows, Linux only
- No client-side configuration required beyond running Twingate Client
- Block pages show by default for HTTP; requires **Twingate Browser Extension** for HTTPS block pages
- Limit of **10 DNS filtering profiles**
- Logs exportable to AWS S3 as JSON (one event per line)

## Prerequisites
- Business or Enterprise plan with DNS Filtering add-on
- Secure DNS enabled in Admin Console (Internet Security tab)
- Twingate Client running on endpoints

## Step-by-Step: Enable DNS Filtering
1. Navigate to **Admin Console → Internet Security tab**
2. If Secure DNS disabled: enable it, select **"Twingate DNS Filtering"**
3. If Secure DNS already enabled: change DoH resolver to **"Twingate DNS Filtering"**
4. Configure profiles via profile name → **Manage → Edit Filtering Rules**

## Configuration Values

### Profile Rules
| Rule Type | Options |
|-----------|---------|
| Allowlist | Specific domains (overrides all other rules) |
| Denylist | Specific domains or TLDs (e.g., `.zip`) |
| Security Categories | Threat feeds, Google Safe Browsing, DNS rebinding, IDN homograph, typosquatting, DGA, newly registered domains, parked domains |
| Content Categories | Gambling, Dating, Adult, Piracy, Social media, Games, Streaming, Force Safe Search, YouTube safe mode |
| Privacy Protection | Block disguised trackers, affiliate/tracking links, ads & trackers |

### S3 Log Event Schema
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
- **Profile priority**: Higher-ranked profiles take precedence; users in multiple Groups use highest-ranked profile
- **Exception Groups override enrolled Groups**: User in both = DNS filtering disabled for that user
- **Signed-out devices**: Use lowest-ranked DNS filtering profile (when "always run Internet Security" is configured)
- **Newly registered domains** category is **disabled by default**
- Groups can only be assigned to **one profile at a time**
- Blocking tracking links may break email unsubscribe links
- Blocking ads/trackers may break some site functionality
- Allowlist takes precedence over **all** other rules including security categories

## Related Docs
- DNS-over-HTTPS (DoH) documentation
- Internet Security Client Configuration (always-on)
- Exception Groups
- Twingate Browser Extension deployment
- Syncing data to S3
- Filtering Analytics / AI Usage Overview