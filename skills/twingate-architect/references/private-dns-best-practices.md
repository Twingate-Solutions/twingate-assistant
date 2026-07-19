# Best Practices for Configuring Private DNS with Twingate

## Summary
Twingate recommends using private DNS exclusively for Resources rather than IP addresses or public DNS entries. DNS zones can be mapped to Twingate Resources and Groups to enable automatic access control. The Connector handles FQDN resolution using its host's configured DNS servers.

## Key Information
- Private DNS preferred over public DNS or IP addresses for security and usability
- Public DNS entries for private Resources leak network information unnecessarily
- IP addresses cause ambiguity when IP overlap exists across multiple Networks
- DNS zone-based Resources automatically include new hosts added to that zone—no manual Resource updates needed
- Connector resolves FQDNs using the DNS servers configured on its host machine
- Custom DNS server on Connector is possible but adds configuration complexity

## Prerequisites
- A private DNS zone (AWS Route 53, Azure DNS, or on-premises DNS server)
- Connector deployed on the same subnet/network as target Resources
- DNS resolvable from the Connector host

## Step-by-Step: DNS Zone → Twingate Resource → Group Mapping

1. **Define DNS zone** aligned to a role/team (e.g., `.engineering.yourcompany.com`)
2. **Add hosts** under the zone (e.g., `host1.engineering.yourcompany.com`)
3. **Create one Twingate Resource** pointing to the DNS zone wildcard (e.g., `*.engineering.yourcompany.com`)
4. **Map the Resource** to the corresponding Twingate Group (e.g., Engineering group)
5. **Verify Connector resolution** by running on the Connector host:
   ```bash
   nslookup hostX.Y.mycompany.com
   ```

## Configuration Values
| Parameter | Recommended Value |
|-----------|------------------|
| DNS server for Connector | Use host's existing configured DNS (default) |
| Custom DNS server | Avoid unless necessary |
| Resource definition | DNS zone wildcard, not individual IPs |

## Gotchas
- **Connector DNS dependency**: If the Connector host can't resolve a name, Twingate users can't reach it—always validate with `nslookup` from the Connector host
- **Custom DNS server** on Connector increases configuration complexity; use host defaults instead
- **Public DNS for private Resources** is a security risk—avoid exposing internal hostnames publicly
- IP-based Resources fail when IP overlap occurs across Networks; DNS names resolve this

## Related Docs
- IP Overlap handling (referenced in-page)
- AWS Route 53 (external)
- Azure DNS (external)
- Twingate Groups and Resource access control