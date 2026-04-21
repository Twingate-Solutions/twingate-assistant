## Page Title
Best Practices for Non-production Environment Access

## Summary
Explains how to use Twingate to provide transparent, FQDN-based routing to separate dev/staging/production environments without requiring users to switch VPNs or reconfigure clients. Routing decisions are made before DNS resolution, so the same FQDN can route to different backend subnets depending on which Connector is assigned to the corresponding Resource.

## Key Information
- **Core mechanism**: Twingate makes routing decisions based on destination FQDN *before* DNS resolution -- the FQDN is the routing key, not the IP
- **Per-environment Resources**: Define separate Resources for each environment (e.g., `dev.example.com`, `staging.example.com`) each mapped to the appropriate Connector/subnet
- **Local DNS handles resolution**: Once traffic reaches the Connector, the Connector resolves the FQDN against that subnet's private DNS -- no public DNS exposure
- **User experience**: Users access resources at the same FQDNs they always used; Twingate transparently routes to the correct environment; no VPN switching required
- **Access control**: Different Groups can be given access to different environment Resources -- e.g., contractors get staging but not production
- **Environments invisible to public internet**: Private DNS means dev/staging FQDNs are not publicly resolvable

## Prerequisites
- Connectors deployed in each environment subnet (deploy in pairs for load balancing/redundancy)
- Private DNS configured in each subnet (see `/docs/private-dns-best-practices`)

## Step-by-Step
1. Deploy Connector pairs in each environment subnet (dev, staging, prod)
2. Create a Remote Network per environment
3. Create Resources using environment-specific FQDNs (e.g., `dev.example.com`, `staging.example.com`)
4. Assign each Resource to the appropriate Remote Network/Connector
5. Grant Groups access to the appropriate Resources only

## Configuration Values
None specific -- standard Resource and Group configuration in Admin Console.

## Gotchas
- Requires private DNS per subnet; if no private DNS exists, Resources must be defined by IP instead
- If two environments share an identical FQDN, routing is determined by which Resource definition matches -- ensure no FQDN overlap across environments

## Related Docs
- `/docs/private-dns-best-practices` -- private DNS setup guide
- `/docs/whitelisting-traffic-to-public-services` -- handling publicly-hosted environments
- `/docs/resources` -- Resource configuration
- `/docs/remote-networks` -- Remote Network setup
