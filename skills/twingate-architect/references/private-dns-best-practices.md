# Best Practices for Configuring Private DNS with Twingate

## Summary
Twingate recommends using private DNS exclusively for Resources rather than IP addresses or public DNS entries. The Connector handles FQDN resolution using its host's DNS configuration. Structuring DNS zones around permission boundaries simplifies Resource management.

## Key Information
- Private DNS prevents information leakage from public DNS entries for internal resources
- DNS names resolve IP overlap issues (same IP on multiple networks)
- Connector resolves FQDNs the same way any host on its subnet would
- DNS zones can map directly to Twingate Groups, enabling wildcard-style Resource coverage
- Adding hosts to a DNS zone automatically makes them accessible without new Resource configuration

## Prerequisites
- A private DNS solution (AWS Route 53, Azure DNS, or on-prem DNS server)
- Connector deployed on the target network
- Twingate Groups configured for access control

## Setup Pattern

**DNS Zone → Twingate Resource → Group mapping:**
1. Define a DNS zone aligned to a role/permission boundary (e.g., `.engineering.yourcompany.com`)
2. Create a single Twingate Resource pointing to the DNS zone wildcard
3. Map that Resource to the corresponding Twingate Group (e.g., Engineering)
4. New hosts added under the zone are automatically accessible to the group

## Configuration Values
- **Resource value**: DNS zone wildcard (e.g., `*.engineering.yourcompany.com`)
- **Custom DNS**: Configurable per-Connector but not recommended due to added complexity

## Verification Command
```bash
# Run on the Connector host to confirm DNS resolution
nslookup hostX.Y.mycompany.com
```

## Gotchas
- Connector uses DNS servers configured on its **host OS** by default — ensure host DNS is correctly pointed at private DNS
- Custom DNS server on Connector is possible but increases configuration complexity
- Public DNS entries for private resources create an attack surface — remove them
- IP-based Resources break when IP overlap exists across networks; DNS names avoid this

## Related Docs
- [IP Overlap](https://www.twingate.com/docs/ip-overlap)
- [AWS Route 53](https://aws.amazon.com/route53/)
- [Azure DNS](https://azure.microsoft.com/en-us/services/dns/)