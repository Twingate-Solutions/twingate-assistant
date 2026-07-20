# Internet Security Use Case

## Page Title
Twingate Internet Security Use Case

## Summary
Twingate secures public internet traffic on employee devices using DNS filtering and DNS-over-HTTPS (DoH). It provides threat blocking, traffic visibility, and privacy protection through the same client used for private resource access—no separate agent required.

## Key Information
- **DNS filtering**: Blocks domains hosting malware, phishing, command-and-control servers
- **DNS-over-HTTPS**: Encrypts DNS requests for privacy on untrusted networks (hotels, coffee shops)
- **Single client**: Handles both private resource access (Zero Trust) and internet security simultaneously
- **BYOD support**: Centrally managed DNS filtering applies to personal devices
- **Shadow IT visibility**: Provides insights into where employee traffic is going
- **Content blocking**: Can restrict access to adult content, gambling, and other non-work categories

## Prerequisites
- Twingate client deployed on employee devices
- Admin access to Twingate management console

## Configuration Options

### Available Integrations
| Integration | Use Case |
|---|---|
| Twingate native DNS filtering | Built-in threat filtering |
| DNS-over-HTTPS | Encrypted DNS requests |
| Cisco AnyConnect + Umbrella | Coexistence with existing stack |
| Cloudflare | DoH + DNS filtering via Cloudflare |

## Related Guides (Step-by-Step Links)
1. [Enable DNS filtering in Twingate](https://www.twingate.com/docs/dns-filtering)
2. [Enable DNS-over-HTTPS in Twingate](https://www.twingate.com/docs/dns-over-https)
3. [Configure AnyConnect (with Umbrella) to work with Twingate](https://www.twingate.com/docs/anyconnect-umbrella)
4. [Configure Cloudflare for DoH and DNS Filtering in Twingate](https://www.twingate.com/docs/cloudflare-dns)

## Gotchas
- This page is an overview only—no configuration values are provided here; follow the specific guides above for implementation details
- DNS filtering and DoH are separate features that may require separate configuration steps
- BYOD deployments require the Twingate client to be installed on personal devices for filtering to apply

## Related Docs
- Twingate DNS Filtering guide
- Twingate DNS-over-HTTPS guide
- AnyConnect/Umbrella coexistence guide
- Cloudflare DNS integration guide