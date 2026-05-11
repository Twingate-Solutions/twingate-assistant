# Internet Security Use Case

## Summary
Twingate can secure public internet traffic on employee devices through DNS filtering and DNS-over-HTTPS (DoH). It provides threat blocking, traffic visibility, and encrypted DNS within a single client deployment alongside private resource access.

## Key Information
- DNS filtering blocks malicious domains: malware, phishing, command-and-control servers
- DNS-over-HTTPS encrypts DNS requests (protects privacy on untrusted networks like hotels/cafes)
- Supports BYOD devices with centrally managed DNS-level filtering
- Shadow IT visibility: see where employee traffic goes, block unwanted content categories (adult, gambling, etc.)
- Single Twingate client handles both private resource access AND internet security — no separate agent needed

## Prerequisites
- Twingate client deployed on employee devices
- Admin access to Twingate management console
- Optional: Third-party DNS provider (Cloudflare, Umbrella/AnyConnect) if using external filtering

## Configuration Options
No direct config values listed on this page. Implementation is via linked guides:

| Feature | Guide |
|---|---|
| DNS Filtering | "How to enable DNS filtering in Twingate" |
| DNS-over-HTTPS | "How to enable DNS-over-HTTPS in Twingate" |
| AnyConnect + Umbrella integration | "How to configure AnyConnect (with Umbrella) to work with Twingate" |
| Cloudflare DoH + DNS Filtering | "How to configure Cloudflare for DNS-over-HTTPS and DNS Filtering in Twingate" |

## Gotchas
- This page is overview only — actual configuration steps are in linked sub-guides
- BYOD coverage requires Twingate client installed on personal devices (not agentless)
- DNS filtering provides domain-level blocking, not deep packet inspection

## Related Docs
- How to enable DNS filtering in Twingate
- How to enable DNS-over-HTTPS in Twingate
- How to configure AnyConnect (with Umbrella) to work with Twingate
- How to configure Cloudflare for DNS-over-HTTPS and DNS Filtering in Twingate