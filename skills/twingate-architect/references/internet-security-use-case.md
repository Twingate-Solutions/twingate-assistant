# Internet Security Use Case

## Page Title
Internet Security Use Case

## Summary
Twingate secures public internet traffic on employee devices through DNS filtering and DNS-over-HTTPS (DoH). A single Twingate client handles both private resource access and public internet security without requiring a separate agent.

## Key Information
- **DNS filtering**: Blocks domains hosting malware, phishing sites, and command-and-control servers
- **DNS-over-HTTPS**: Encrypts DNS requests for privacy on untrusted networks (hotels, coffee shops)
- **BYOD support**: Centrally manage DNS-level filtering across personal and corporate devices
- **Shadow IT visibility**: Monitor and block unauthorized SaaS/web usage
- **Content filtering**: Block categories like adult content, gambling
- **Single agent**: Same Twingate client used for private access also enforces internet security policies

## Prerequisites
- Twingate client deployed on employee devices
- Admin access to Twingate console to configure DNS filtering policies

## Configuration Guides
1. [Enable DNS filtering in Twingate](https://www.twingate.com/docs/dns-filtering)
2. [Enable DNS-over-HTTPS in Twingate](https://www.twingate.com/docs/dns-over-https)
3. [Configure AnyConnect (with Umbrella) to work with Twingate](https://www.twingate.com/docs/anyconnect-umbrella)
4. [Configure Cloudflare for DNS-over-HTTPS and DNS Filtering](https://www.twingate.com/docs/cloudflare-doh)

## Gotchas
- Separate agent deployment is **not** required — existing Twingate client supports both use cases
- BYOD devices require Twingate client installation to receive DNS filtering protections

## Related Docs
- DNS Filtering configuration guide
- DNS-over-HTTPS configuration guide
- AnyConnect/Umbrella integration
- Cloudflare DoH/DNS Filtering integration