# Best Practices for Configuring Private DNS with Twingate

## Summary
Twingate recommends using private DNS exclusively for Resources instead of IP addresses or public DNS entries. DNS zones can be mapped to Twingate Resources and Groups to simplify access management and avoid IP overlap issues.

## Key Information
- Private DNS is recommended but not required
- Connectors handle FQDN resolution (using the DNS servers configured on the Connector host)
- DNS zones can serve as wildcard Resources—new hosts added to a zone are automatically accessible without manual Resource configuration
- Cloud options: AWS Route 53, Azure DNS (no dedicated server needed)
- On-premises: deploy a DNS server on a host within the internal network

## Why Private DNS Over IP/Public DNS
- Public DNS entries for private Resources leak information to potential attackers
- IP addresses are error-prone and not user-friendly
- DNS names resolve IP overlap issues (same private IP on two separate networks)

## Setup Pattern: DNS Zone → Resource → Group
1. Define a DNS zone scoped to a role/team (e.g., `.engineering.yourcompany.com`)
2. Create a single Twingate Resource pointing to the DNS zone wildcard
3. Map that Resource to the corresponding Twingate Group (e.g., Engineering)
4. New hosts added under the zone are automatically accessible—no additional Resource config needed

## DNS Resolution Behavior
- **Connector resolves FQDNs**, not the client machine
- Resolution works the same as any host on the same subnet as the Connector
- To verify Connector can resolve a hostname:
  ```bash
  nslookup hostX.Y.mycompany.com
  ```
  (run from the Connector host)

## Configuration Notes
| Option | Recommendation |
|--------|---------------|
| DNS server for Connector | Use DNS servers already configured on the Connector host |
| Custom DNS server for Connector | Supported but increases configuration complexity—not recommended |

## Gotchas
- Custom DNS server on the Connector is possible but complicates setup; default (host-configured DNS) is preferred
- DNS structure should be planned before deployment—retrofitting zones to match permission boundaries is harder
- Public DNS entries for private Resources are a security risk even if functional

## Related Docs
- IP Overlap handling
- AWS Route 53 (external)
- Azure DNS (external)
- Twingate Resources configuration
- Twingate Groups configuration