# Best Practices for Configuring Private DNS with Twingate

## Summary
Twingate recommends using private DNS exclusively for Resources rather than IP addresses or public DNS entries. DNS zones can map directly to Twingate Groups, enabling automatic access for new hosts without manual Resource configuration. The Connector handles FQDN resolution using its host's configured DNS servers.

## Key Information
- Private DNS is recommended but not required
- Connectors resolve FQDNs the same way any host on the same subnet would
- DNS zone wildcards in Twingate Resources automatically include new hosts added to that zone
- Cloud services (AWS Route 53, Azure DNS) eliminate need for dedicated DNS servers
- On-premises networks typically need a DNS server deployed on the internal network

## Why Private DNS Over IP or Public DNS
- Public DNS entries for private Resources leak network information to potential attackers
- IP addresses are error-prone and unfriendly for end users
- IP overlap (same IP on two different Networks) is resolved by using DNS names — Twingate can distinguish Resources by FQDN even when IPs collide

## Configuration Pattern: DNS Zone → Twingate Resource → Group
1. Define a DNS zone scoped to a role/team (e.g., `.engineering.yourcompany.com`)
2. Create a single Twingate Resource pointing to the DNS zone wildcard
3. Map that Resource to the corresponding Twingate Group (e.g., Engineering)
4. New hosts added under that zone are automatically accessible — no additional Resource configuration needed

## DNS Resolution Behavior
- **Who resolves:** The Connector resolves FQDNs using the DNS servers configured on the Connector host
- **Verify resolution:** SSH into Connector host and run:
  ```
  nslookup hostX.Y.mycompany.com
  ```
- **Custom DNS server:** Supported but adds configuration complexity — not recommended; prefer the Connector host's existing DNS configuration

## Gotchas
- Custom DNS server on Connector is possible but complicates setup — avoid unless necessary
- DNS zone structure should be planned before deployment; retrofitting is harder
- Connector must be on a subnet where it can resolve the private DNS zone — placement matters

## Related Docs
- [IP Overlap](https://www.twingate.com/docs) (referenced inline)
- AWS Route 53 documentation
- Azure DNS documentation