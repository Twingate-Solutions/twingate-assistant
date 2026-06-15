# Internet Security Use Case

## Summary
Twingate extends beyond private resource access to secure public internet traffic on employee devices via DNS filtering and DNS-over-HTTPS (DoH). A single Twingate client handles both private resource access and internet security enforcement with no separate agent required.

## Key Information
- **DNS filtering**: Blocks domains associated with malware, phishing, and command-and-control servers
- **DNS-over-HTTPS**: Encrypts DNS requests to protect browsing privacy on untrusted networks (hotels, coffee shops)
- **Content control**: Block categories like adult content, gambling, shadow IT applications
- **Traffic visibility**: Provides insights into where employee traffic is directed
- **BYOD support**: Centrally managed DNS filtering applies to personal devices
- **Single agent**: Existing Twingate client handles both private access and internet security

## Prerequisites
- Twingate client deployed on employee devices
- Appropriate Twingate plan supporting DNS filtering/DoH features

## Implementation Guides
Four specific configuration paths available:
1. **DNS filtering in Twingate** — native Twingate DNS filtering setup
2. **DNS-over-HTTPS in Twingate** — native DoH configuration
3. **AnyConnect (with Umbrella) + Twingate** — integration for existing Cisco Umbrella deployments
4. **Cloudflare + Twingate** — DNS-over-HTTPS and filtering via Cloudflare

## Gotchas
- No configuration values or CLI flags documented on this page; refer to linked guides for specifics
- BYOD enforcement depends on Twingate client being installed and active on personal devices — no agentless enforcement implied

## Related Docs
- How to enable DNS filtering in Twingate
- How to enable DNS-over-HTTPS in Twingate
- How to configure AnyConnect (with Umbrella) to work with Twingate
- How to configure Cloudflare for DNS-over-HTTPS and DNS Filtering in Twingate