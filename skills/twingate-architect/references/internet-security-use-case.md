# Internet Security Use Case

## Page Title
Internet Security Use Case

## Summary
Twingate extends beyond private resource access to secure public internet traffic on employee devices via DNS filtering and DNS-over-HTTPS (DoH). A single Twingate client handles both private access and internet security enforcement without requiring a separate agent.

## Key Information
- **DNS filtering**: Blocks domains associated with malware, phishing, and command-and-control servers
- **DNS-over-HTTPS**: Encrypts DNS requests, protecting browsing privacy on untrusted networks (hotels, cafes)
- **BYOD support**: Centrally apply DNS filtering to personal devices
- **Shadow IT visibility**: Provides traffic insights and ability to block undesirable content categories (adult, gambling, etc.)
- **Single client**: No separate agent needed — same Twingate client enforces both Zero Trust access and DNS filtering

## Prerequisites
- Twingate client deployed on employee devices
- Appropriate Twingate plan that includes DNS filtering/DoH features

## Configuration Guides (Linked)
1. Enable DNS filtering in Twingate
2. Enable DNS-over-HTTPS in Twingate
3. Configure AnyConnect (with Umbrella) to work with Twingate
4. Configure Cloudflare for DNS-over-HTTPS and DNS filtering in Twingate

## Use Cases
| Scenario | Feature |
|----------|---------|
| Block malware/phishing domains | DNS filtering |
| Protect browsing on public Wi-Fi | DNS-over-HTTPS |
| Enforce content policies | DNS filtering categories |
| Audit internet traffic patterns | DNS visibility/reporting |
| BYOD threat protection | Centralized DNS policy |

## Gotchas
- This page is overview-only; actual configuration values and steps are in the linked guides
- AnyConnect/Umbrella and Cloudflare require separate integration steps if already in use

## Related Docs
- How to enable DNS filtering in Twingate
- How to enable DNS-over-HTTPS in Twingate
- How to configure AnyConnect (with Umbrella) to work with Twingate
- How to configure Cloudflare for DNS-over-HTTPS and DNS Filtering in Twingate