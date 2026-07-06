# Best Practices for Configuring Private DNS with Twingate

## Summary
Twingate recommends using private DNS exclusively for Resources rather than IP addresses or public DNS entries. The Connector handles FQDN resolution using its host's configured DNS servers. Structuring DNS zones around permission boundaries enables scalable, automatic access control.

## Key Information
- Private DNS preferred over public DNS (security) and IP addresses (usability, overlap issues)
- IP overlap (same IP on 2 networks) is resolved by using DNS names instead
- DNS zone = Resource boundary: one Twingate Resource can cover an entire DNS zone (e.g., `*.engineering.yourcompany.com`)
- New hosts added under a DNS zone are automatically accessible without manual Resource configuration
- **Connector resolves FQDNs** — it acts like any host on the same subnet

## Prerequisites
- A private DNS zone (AWS Route 53, Azure DNS, or on-prem DNS server)
- Connector deployed on a host with access to the private DNS server
- Twingate Groups defined to map to DNS zones

## Setup: DNS Zone → Resource → Group Pattern

1. Define DNS zones aligned to roles/permissions (e.g., `.engineering.yourcompany.com`)
2. Place all relevant hosts under that zone (`host1.engineering.yourcompany.com`, etc.)
3. Create a **single Twingate Resource** pointing to the DNS zone wildcard
4. Map the Resource to the corresponding Twingate Group (e.g., Engineering)
5. New hosts added to the zone become accessible automatically

## Configuration Values
| Item | Example |
|------|---------|
| DNS Zone / Resource value | `*.engineering.yourcompany.com` |
| Verify Connector DNS resolution | `nslookup hostX.Y.mycompany.com` (run on Connector host) |
| Custom DNS server | Supported but not recommended |

## Gotchas
- **Custom DNS on Connector** complicates configuration — use the Connector host's system DNS instead
- DNS resolution is performed by the **Connector**, not the client — test from the Connector host, not a user machine
- Public DNS entries for private Resources expose internal network info unnecessarily — avoid
- IP-based Resources can fail with overlapping IPs across networks; DNS names eliminate ambiguity

## Related Docs
- [IP Overlap](https://www.twingate.com/docs) (referenced in page)
- [AWS Route 53](https://aws.amazon.com/route53/)
- [Azure DNS](https://azure.microsoft.com/en-us/products/dns)
- Twingate Resources configuration
- Twingate Groups configuration