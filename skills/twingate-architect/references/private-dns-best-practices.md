# Best Practices for Configuring Private DNS with Twingate

## Summary
Twingate recommends using private DNS exclusively for Resources rather than IP addresses or public DNS entries. Connectors handle FQDN resolution using their host's configured DNS servers. Structuring DNS zones around team/role boundaries enables automatic Resource access as new hosts are added.

## Key Information
- Private DNS preferred over public DNS (information leak risk) and IP addresses (error-prone, IP overlap issues)
- Connectors resolve FQDNs the same way any host on the same subnet would
- DNS zone-based Resources auto-include new hosts added to that zone—no manual Resource updates needed
- Managed DNS services (AWS Route 53, Azure DNS) eliminate need for self-hosted DNS servers
- On-prem networks typically require a DNS server deployed on the internal network

## Prerequisites
- Connector deployed on host with access to private DNS servers
- Private DNS zone configured (self-hosted or managed service)
- Twingate Groups defined for access control

## Step-by-Step: Zone-Based Resource Setup
1. Define a DNS zone aligned to a role/team (e.g., `.engineering.yourcompany.com`)
2. Add all relevant hosts under that zone (`host1.engineering.yourcompany.com`, etc.)
3. Create a single Twingate Resource pointing to the DNS zone wildcard
4. Map that Resource to the corresponding Twingate Group (e.g., Engineering)
5. New hosts added to the zone become automatically accessible—no additional Resource config needed

## Configuration Values
- **Resource definition**: DNS zone (e.g., `*.engineering.yourcompany.com`) rather than individual hostnames or IPs
- **Connector DNS**: Uses host's system-configured DNS servers by default
- **Custom DNS override**: Available on Connector but not recommended (increases configuration complexity)

## Validation Command
```bash
# Run on the Connector host to verify DNS resolution
nslookup hostX.Y.mycompany.com
```

## Gotchas
- Connector resolves DNS—if the Connector host can't resolve a name, neither can Twingate clients
- Custom DNS server on Connector is possible but complicates setup; use host's default DNS instead
- Public DNS entries for private Resources expose internal network topology unnecessarily
- IP overlap (same IP on two networks) is only resolvable via DNS names, not IP-based Resources

## Related Docs
- IP Overlap handling
- AWS Route 53 private DNS setup
- Azure DNS private zones
- Twingate Connector deployment
- Twingate Groups and Resource access control