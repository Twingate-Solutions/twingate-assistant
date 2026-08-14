---
source: https://www.twingate.com/docs/private-dns-best-practices
type: docs
fetched: 2026-08-14
source_version: 6524dae2fddb94c7f25dd0d0a3353288e8cd805123776560796b79a462b22cb8
---

# Best Practices for Configuring Private DNS with Twingate

## Summary
Twingate recommends using private DNS exclusively for Resources rather than IP addresses or public DNS entries. The Connector handles FQDN resolution using its host's configured DNS servers. Structuring DNS zones around permission boundaries enables scalable, automatic Resource access management.

## Key Information
- Private DNS preferred over public DNS (security) and IP addresses (ambiguity, UX)
- Public DNS entries for private Resources expose unnecessary information to attackers
- IP overlap (same IP on multiple networks) is resolved by using DNS names
- Connector resolves FQDNs the same way any host on its subnet would
- DNS zone-based Resources auto-include new hosts — no manual Resource additions needed
- Managed DNS options: AWS Route 53, Azure DNS (no dedicated server required)
- On-premises: deploy DNS server on internal network host

## Prerequisites
- A private DNS zone configured (managed service or self-hosted)
- Connector deployed on a host with access to the internal DNS servers
- Twingate Groups created for access control mapping

## Step-by-Step: DNS Zone–Based Resource Setup
1. Define a DNS zone aligned to a permission boundary (e.g., `.engineering.yourcompany.com`)
2. Place all relevant hosts under that zone (`host1.engineering.yourcompany.com`, etc.)
3. Create a single Twingate Resource pointing to the DNS zone wildcard
4. Map the Resource to the corresponding Twingate Group (e.g., Engineering)
5. New hosts added to the zone automatically become accessible — no further configuration needed

## Configuration Values
- **Resource definition**: DNS zone (e.g., `*.engineering.yourcompany.com`) rather than individual FQDNs or IPs
- **Custom DNS server**: Supported on Connector but not recommended — use host's default DNS config instead

## Verification Command
```bash
# Run on the Connector host to confirm DNS resolution
nslookup hostX.Y.mycompany.com
```

## Gotchas
- Connector uses DNS servers configured on its **host OS** by default — ensure these can resolve private zones
- Custom DNS server on Connector is possible but increases configuration complexity
- Public DNS entries for private Resources are a security risk, not just a preference issue
- IP-based Resources will break in IP overlap scenarios; DNS names are the only reliable solution

## Related Docs
- [IP Overlap](https://www.twingate.com/docs/ip-overlap)
- [AWS Route 53](https://aws.amazon.com/route53/)
- [Azure DNS](https://azure.microsoft.com/en-us/services/dns/)
- Twingate Resources configuration
- Twingate Groups and access control