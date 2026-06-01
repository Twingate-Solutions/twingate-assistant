# Best Practices for Non-production Environment Access

## Summary
Twingate enables transparent routing between development, staging, and production environments using FQDN-based routing decided before DNS resolution. Users connect to different environments simply by using different hostnames, with no manual VPN switching required. Resources are coupled to Remote Networks, and routing destination determines which subnet handles DNS resolution.

## Key Information
- Routing decisions happen **before DNS resolution**, using the FQDN in the user's request
- Each environment gets its own Twingate Resource (e.g., `dev.example.com`, `staging.example.com`) mapped to its corresponding Remote Network
- Local DNS on each subnet resolves the FQDN to the appropriate internal IP
- Environments remain invisible to the public internet (no public DNS exposure)
- Fine-grained access: grant access to specific Resources (e.g., only `staging.example.com`) rather than entire network

## Prerequisites
- Twingate Connectors deployed in each target subnet (deploy in pairs for load balancing)
- Local/private DNS configured on each subnet
- Resources defined and coupled to correct Remote Networks in Twingate admin
- See [Private DNS Best Practices](https://www.twingate.com/docs/private-dns-best-practices) if no local DNS exists

## Configuration Pattern

| Component | Dev Example | Staging Example |
|-----------|-------------|-----------------|
| Resource address | `dev.beamreachinc.com` | `staging.beamreachinc.com` |
| Remote Network | Development subnet | Staging subnet |
| DNS resolution | Local DNS → `10.0.2.77` | Local DNS → staging IP |
| Connector placement | Dev subnet (×2) | Staging subnet (×2) |

## Step-by-Step
1. Deploy Connector pairs into each environment subnet (dev, staging, prod)
2. Configure local/private DNS on each subnet for internal hostname resolution
3. Create a Remote Network in Twingate for each environment
4. Create Resources with environment-specific FQDNs, coupled to corresponding Remote Networks
5. Assign user/group access policies per Resource (not per network)
6. Users access environments via FQDN — routing is automatic and transparent

## Gotchas
- **No local DNS?** Routing still works but DNS resolution must be handled — see Private DNS guide
- If an environment is publicly hosted, FQDN routing alone doesn't hide it; use [Whitelisting Traffic to Public Services](https://www.twingate.com/docs/whitelisting-traffic) instead
- Users must NOT need to switch VPN profiles — if they do, the Resource/Network coupling is misconfigured
- Connector pairs required per subnet for load balancing and redundancy

## Related Docs
- [Private DNS Best Practices](https://www.twingate.com/docs/private-dns-best-practices)
- [Whitelisting Traffic to Public Services](https://www.twingate.com/docs/whitelisting-traffic)
- [Getting Started on AWS](https://www.twingate.com/docs/aws)
- [Getting Started on GCP](https://www.twingate.com/docs/gcp)