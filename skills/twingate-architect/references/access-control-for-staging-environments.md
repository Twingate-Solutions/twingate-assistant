# Best Practices for Non-production Environment Access

## Summary
Twingate routes private traffic based on destination FQDN **before** DNS resolution, enabling transparent routing to separate environments (dev/staging/prod) without user reconfiguration. Resources are coupled to Remote Networks, so the address field determines which network handles the request and performs local DNS resolution.

## Key Information
- Traffic routing decisions happen pre-DNS resolution, using FQDN as the routing key
- Each environment gets its own Remote Network + Connector pair(s)
- Local DNS on each subnet resolves hostnames to internal IPs
- Users never need to switch VPN profiles or manually select environments
- Non-prod environments remain invisible to the public internet (no public DNS exposure)
- Granular access control: grant access to specific resources (e.g., `staging.example.com`) without exposing entire subnet

## Prerequisites
- Twingate Connectors deployed in each target subnet (deploy in pairs for load balancing)
- Local/private DNS configured per subnet for internal hostname resolution
- Distinct FQDNs per environment (e.g., `dev.example.com`, `staging.example.com`)
- See [Private DNS Best Practices](https://www.twingate.com/docs/private-dns-best-practices) if local DNS is not yet configured

## Configuration Pattern

| Component | Dev Environment | Staging Environment |
|-----------|----------------|---------------------|
| Remote Network | Dev subnet | Staging subnet |
| Resource address | `dev.example.com` | `staging.example.com` |
| Connector location | Dev subnet (×2) | Staging subnet (×2) |
| DNS resolution | Local dev DNS → `10.0.x.x` | Local staging DNS → `10.0.x.x` |

## Step-by-Step
1. Deploy Connector pair in each environment's subnet
2. Create a Remote Network in Twingate mapped to each subnet
3. Create a Resource for each environment using its FQDN as the address
4. Assign Resources to appropriate groups (developers, contractors, execs, etc.)
5. Users connect once to Twingate — routing is automatic based on requested hostname

## Gotchas
- Requires private/local DNS per subnet; without it, hostname resolution fails inside the environment
- If an environment is publicly hosted (not private), this pattern doesn't apply — see [Whitelisting Traffic to Public Services](https://www.twingate.com/docs/whitelisting-traffic-to-public-services) instead
- FQDNs must be distinct per environment; shared hostnames across environments will not route correctly
- Users must not have conflicting split-tunnel or DNS configurations that intercept requests before Twingate

## Related Docs
- [Private DNS Best Practices](https://www.twingate.com/docs/private-dns-best-practices)
- [Whitelisting Traffic to Public Services](https://www.twingate.com/docs/whitelisting-traffic-to-public-services)
- [Getting Started on AWS](https://www.twingate.com/docs/aws)
- [Getting Started on GCP](https://www.twingate.com/docs/gcp)