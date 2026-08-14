---
source: https://www.twingate.com/docs/internet-security-use-case
type: docs
fetched: 2026-08-14
source_version: 27dc6eb8984b89880ca9b0429ef9671fd7a4959c83501c91f6b79b6f1d440208
---

# Internet Security Use Case

## Page Title
Twingate Internet Security Use Case

## Summary
Twingate secures public internet traffic on employee devices using DNS filtering and DNS-over-HTTPS (DoH). It consolidates private resource access and internet security enforcement into a single client agent, eliminating the need for separate security tools.

## Key Information
- **DNS filtering**: Blocks domains hosting malware, phishing sites, and C2 servers
- **DNS-over-HTTPS**: Encrypts DNS requests, protecting browsing privacy on untrusted networks (hotels, coffee shops)
- **Shadow IT visibility**: Provides traffic insights and ability to block non-work-appropriate content categories (adult content, gambling, etc.)
- **Single agent**: Same Twingate client handles both private resource access and internet security enforcement — no separate agent required
- **BYOD support**: Centrally managed DNS filtering applies to personal devices

## Prerequisites
- Twingate client deployed on employee devices
- Appropriate Twingate plan with DNS filtering/DoH features enabled
- Admin access to Twingate admin console

## Configuration Guides (Step-by-Step links)
1. **DNS Filtering**: Follow [How to enable DNS filtering in Twingate]
2. **DNS-over-HTTPS**: Follow [How to enable DNS-over-HTTPS in Twingate]
3. **AnyConnect + Umbrella compatibility**: Follow [How to configure AnyConnect (with Umbrella) to work with Twingate]
4. **Cloudflare integration**: Follow [How to configure Cloudflare for DNS-over-HTTPS and DNS Filtering in Twingate]

## Configuration Values
- No specific env vars or API params documented on this page
- Configuration handled via Twingate admin console (DNS filtering policies, DoH settings)
- Third-party integrations: Cisco Umbrella, Cloudflare

## Gotchas
- DNS filtering and DoH are separate features — enabling one does not automatically enable the other
- BYOD deployments require device enrollment with the Twingate client; filtering only applies to enrolled devices
- Third-party DNS security tools (e.g., Umbrella) require specific compatibility configuration to avoid conflicts with Twingate

## Related Docs
- How to enable DNS filtering in Twingate
- How to enable DNS-over-HTTPS in Twingate
- How to configure AnyConnect (with Umbrella) to work with Twingate
- How to configure Cloudflare for DNS-over-HTTPS and DNS Filtering in Twingate