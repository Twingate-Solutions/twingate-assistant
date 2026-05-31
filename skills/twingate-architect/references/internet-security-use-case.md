# Internet Security Use Case

## Summary
Twingate can secure public internet traffic through DNS filtering and DNS-over-HTTPS (DoH), providing threat protection, content filtering, and traffic visibility. A single Twingate client handles both private resource access and public internet security without requiring a separate agent.

## Key Information
- **DNS Filtering**: Blocks malicious domains (malware, phishing, C2 servers) and unwanted content categories (adult, gambling, etc.)
- **DNS-over-HTTPS**: Encrypts DNS requests for privacy on untrusted networks (hotels, coffee shops)
- **Shadow IT Visibility**: Provides insights into employee traffic destinations
- **BYOD Support**: Centrally manage DNS-level filtering on personal devices
- **Single Agent**: No separate client needed—same Twingate client handles both private access and internet security

## Use Cases
- Proactive threat blocking via DNS-level filtering
- Privacy protection for remote/traveling employees
- Content policy enforcement
- Shadow IT monitoring and control
- BYOD security management

## Implementation Guides
1. [How to enable DNS filtering in Twingate](#)
2. [How to enable DNS-over-HTTPS in Twingate](#)
3. [How to configure AnyConnect (with Umbrella) to work with Twingate](#)
4. [How to configure Cloudflare for DNS-over-HTTPS and DNS Filtering in Twingate](#)

## Gotchas
- This is a feature overview page—actual configuration steps are in linked sub-guides
- Filtering applies at DNS level; encrypted traffic (HTTPS) destinations are visible but content is not inspected
- BYOD deployments require Twingate client installation on personal devices

## Related Docs
- DNS Filtering configuration guide
- DNS-over-HTTPS configuration guide
- Cloudflare integration guide
- Cisco AnyConnect/Umbrella coexistence guide