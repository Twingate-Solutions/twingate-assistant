# Internet Security Use Case

## Page Title
Twingate Internet Security Use Case

## Summary
Twingate extends its client to secure public internet traffic via DNS filtering and DNS-over-HTTPS (DoH), protecting against malware, phishing, and inappropriate content. A single Twingate client handles both private resource access and public internet security without requiring a separate agent.

## Key Information
- DNS filtering blocks known malicious domains: malware, phishing, command-and-control servers
- DoH encrypts DNS requests, protecting privacy on untrusted networks (hotels, coffee shops)
- Supports BYOD devices with centrally managed DNS-level filtering
- Provides shadow IT visibility and content category blocking (adult, gambling, etc.)
- Single client deployment covers both Zero Trust Network Access (ZTNA) and internet security

## Prerequisites
- Twingate client deployed on employee devices
- Admin access to Twingate console to configure DNS policies

## Configuration Options
Four implementation paths available:

| Method | Guide |
|--------|-------|
| Native DNS filtering | "How to enable DNS filtering in Twingate" |
| DNS-over-HTTPS | "How to enable DNS-over-HTTPS in Twingate" |
| Cisco Umbrella (AnyConnect) integration | "How to configure AnyConnect (with Umbrella) to work with Twingate" |
| Cloudflare integration | "How to configure Cloudflare for DNS-over-HTTPS and DNS Filtering in Twingate" |

## Gotchas
- No standalone agent needed — avoid deploying a separate DNS filtering agent if Twingate client is already present
- BYOD coverage requires the Twingate client to be installed and active on personal devices
- Filtering only applies when the Twingate client is running; no client = no protection

## Related Docs
- How to enable DNS filtering in Twingate
- How to enable DNS-over-HTTPS in Twingate
- How to configure AnyConnect (with Umbrella) to work with Twingate
- How to configure Cloudflare for DNS-over-HTTPS and DNS Filtering in Twingate