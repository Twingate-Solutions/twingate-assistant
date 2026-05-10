# Best Practices for Configuring Private DNS with Twingate

## Summary
Twingate recommends using private DNS exclusively for Resources rather than IP addresses or public DNS entries. DNS zones can be mapped to Twingate Resources and Groups to simplify access management. The Connector handles FQDN resolution using its host's configured DNS servers.

## Key Information
- Private DNS prevents information leakage from public DNS entries pointing to private Resources
- DNS names eliminate IP overlap ambiguity (same IP on different networks)
- DNS zones can be structured to match permission boundaries (e.g., `.engineering.yourcompany.com`)
- A single Twingate Resource can point to an entire DNS zone — new hosts added to the zone are automatically accessible without additional Resource configuration
- The **Connector** resolves FQDNs, not the client — resolution behavior matches any host on the Connector's subnet

## Prerequisites
- A private DNS zone (AWS Route 53, Azure DNS, or on-prem DNS server)
- Connector deployed on a host with access to the private DNS server

## Setup Pattern
1. Define DNS zones aligned with access roles (e.g., `*.engineering.yourcompany.com`)
2. Create a Twingate Resource pointing to the DNS zone wildcard
3. Map the Resource to the corresponding Twingate Group (e.g., Engineering group)
4. New hosts added under the zone inherit access automatically

## Configuration Values
- Resource value: DNS zone pattern (e.g., `*.engineering.yourcompany.com`)
- Custom DNS server: Optional per-Connector setting (not recommended — use host DNS instead)

## Verification Command
```bash
# Run on the Connector host to confirm DNS resolution
nslookup hostX.Y.mycompany.com
```

## Gotchas
- Connector uses DNS servers configured on its **host OS** by default — ensure the host resolves private zones correctly before assuming Connector will work
- Custom DNS server on Connector is possible but increases configuration complexity — avoid unless necessary
- Public DNS entries for private Resources are a security risk even if Twingate is in use

## Related Docs
- IP Overlap documentation
- AWS Route 53
- Azure DNS
- Connector configuration