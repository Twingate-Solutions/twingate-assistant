## Page Title
Internet Security

## Summary
Use case overview for using Twingate to secure outbound public internet traffic on employee devices via DNS filtering and DNS-over-HTTPS. Runs in the same client as private resource access — no separate agent required.

## Key Information
- **DNS filtering**: proactively blocks domains hosting malware, phishing, C2 servers, inappropriate content, shadow IT
- **DNS-over-HTTPS (DoH)**: encrypts DNS queries to a configurable resolver — protects against eavesdropping on public Wi-Fi (hotels, coffee shops)
- Supported DoH resolvers: Google, Cloudflare, OpenDNS, NextDNS, and custom
- BYOD privacy: encrypted DNS applies to personal devices enrolled in the policy
- Shadow IT visibility: logs show which non-approved SaaS services employees are accessing
- Single Twingate client handles both private resource access and internet security — no second agent
- Compatible with Cisco AnyConnect/Umbrella (requires configuration) and Cloudflare Zero Trust

## Prerequisites
- Business or Enterprise plan required for DNS filtering
- Twingate client deployed on employee devices

## Step-by-Step
Not applicable on this page — see linked feature guides.

## Configuration Values
None on this page.

## Gotchas
- DNS filtering and DoH are separate features; DoH alone does not filter content — it only encrypts DNS queries
- AnyConnect/Umbrella coexistence requires specific configuration to avoid kernel module conflicts
- DNS filtering policies apply at the Twingate network level — configure per-network in Admin Console

## Related Docs
- `/docs/dns-filtering` — DNS filtering setup and block categories
- `/docs/dns-security` — DNS-over-HTTPS configuration
- `/docs/internet-security-client-configuration` — MDM/machine key deployment
- `/docs/configuring-anyconnect-with-umbrella` — AnyConnect coexistence
- `/docs/doh-cloudflare` — Cloudflare DoH integration
- `/docs/nextdns-configuration` — NextDNS integration
