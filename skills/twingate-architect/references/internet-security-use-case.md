# Internet Security Use Case

## Page Title
Twingate Internet Security Use Case

## Summary
Twingate secures public internet traffic on employee devices using DNS filtering and DNS-over-HTTPS (DoH). It operates through the existing Twingate client, eliminating the need for a separate agent. Coverage applies to both corporate and BYOD devices.

## Key Information
- **DNS filtering**: Blocks domains associated with malware, phishing, command-and-control servers
- **DNS-over-HTTPS**: Encrypts DNS requests, protecting browsing privacy on untrusted networks (hotel/coffee shop Wi-Fi)
- **Shadow IT visibility**: Provides traffic insights and ability to block undesirable content categories (adult content, gambling, etc.)
- **Single client**: Same Twingate client handles both private resource access and internet security — no separate agent required
- **BYOD support**: Centrally managed DNS filtering applies to personal devices enrolled in Twingate

## Prerequisites
- Twingate client deployed on employee devices
- Appropriate Twingate plan with DNS filtering/DoH features enabled

## Configuration Guides (Linked)
1. Enable DNS filtering in Twingate
2. Enable DNS-over-HTTPS in Twingate
3. Configure AnyConnect (with Umbrella) to work alongside Twingate
4. Configure Cloudflare for DNS-over-HTTPS and DNS filtering in Twingate

## Gotchas
- This page is an overview only — actual configuration steps are in the linked guides above
- BYOD device coverage requires devices to have the Twingate client installed and configured
- Third-party integrations (Umbrella, Cloudflare) require separate configuration steps

## Related Docs
- How to enable DNS filtering in Twingate
- How to enable DNS-over-HTTPS in Twingate
- AnyConnect + Umbrella coexistence guide
- Cloudflare DoH + DNS filtering configuration guide