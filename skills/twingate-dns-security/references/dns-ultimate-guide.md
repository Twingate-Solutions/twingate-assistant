---
source: https://www.twingate.com/docs/dns-ultimate-guide
type: docs
fetched: 2026-08-14
source_version: 44723d791b5a5730490a06e7252a90b33c710a52de3eae69e091f246b9c3f183
---

# The Ultimate Guide to DNS & Twingate

## Page Title
The Ultimate Guide to DNS & Twingate

## Summary
This is a navigation/index page that organizes Twingate's DNS documentation into topic-based sections. It directs users to specific guides depending on their DNS knowledge level and use case. No implementation details are on this page itself.

## Key Information
- **Five distinct DNS topic areas** covered across separate linked guides:
  1. DNS fundamentals (intro for new users)
  2. Benefits of running a private DNS server (best practices)
  3. How Twingate resolves private FQDNs (core DNS behavior)
  4. Running DNS queries (`dig`/`nslookup`) from the Twingate Client (troubleshooting)
  5. DNS traffic encryption (security)

## Prerequisites
None — page is an index/navigation hub.

## Core Concepts Referenced

| Topic | Key Detail |
|---|---|
| CGNAT IP addresses | Twingate Client returns CGNAT IPs for private FQDNs, not actual private IPs |
| Private FQDN resolution | Twingate Client intercepts traffic; separate guide covers full resolution flow |
| DNS query troubleshooting | Use `dig` or `nslookup` via DNS forwarding to retrieve actual private IPs |
| DNS encryption | Twingate can encrypt all DNS traffic, including non-private resource queries |

## Gotchas
- When using `dig` or `nslookup` on the Twingate Client, results return CGNAT IPs by default — not the real private IP of the resource. A specific DNS forwarding configuration is needed to retrieve actual IPs.
- DNS encryption covers **all** DNS traffic, not just traffic to private resources.

## Related Docs
- Complete introduction to DNS (linked, external to this page)
- DNS best practices guide (private DNS server benefits)
- In-depth practical guide: DNS with Twingate (FQDN resolution mechanics)
- Guide: Twingate DNS query forwarding (troubleshooting with `dig`/`nslookup`)
- Guide: DNS security / encryption in Twingate