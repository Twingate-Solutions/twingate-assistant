# Best Practices for Non-Production Environment Access

## Summary
Twingate routes private traffic based on destination FQDN **before** DNS resolution, enabling transparent routing to separate environments (dev/staging/prod) without user reconfiguration. Resources are coupled to Remote Networks, so the address field determines which target network handles the request and performs local DNS resolution.

## Key Information
- Routing decisions happen **before** DNS resolution using the FQDN in the user's request
- Each environment needs Twingate Connectors deployed in its subnet (deploy in pairs for load balancing)
- Users connect to different environments simply by using different FQDNs—no manual connect/disconnect required
- Private DNS on each subnet resolves hostnames locally (e.g., `dev.beamreachinc.com` → `10.0.2.77` on dev subnet)
- Environments remain invisible to the public internet when using private DNS

## Prerequisites
- Twingate Connectors deployed in each environment's subnet
- Local/private DNS configured per subnet (see [Private DNS Best Practices](https://www.twingate.com/docs/private-dns-best-practices))
- Remote Networks defined in Twingate admin for each environment

## Configuration Pattern

| Environment | Twingate Resource | Remote Network | DNS Resolution |
|-------------|-------------------|----------------|----------------|
| Development | `dev.example.com` | Dev subnet | Local dev DNS |
| Staging | `staging.example.com` | Staging subnet | Local staging DNS |
| Production | `prod.example.com` | Prod subnet | Local prod DNS |

## Step-by-Step
1. Deploy Connector pairs in each environment subnet
2. Create a Remote Network in Twingate admin for each subnet
3. Create Resources with environment-specific FQDNs, coupled to the corresponding Remote Network
4. Grant user/group access to specific Resources (not entire networks)
5. Users access environments via FQDN—routing is automatic and transparent

## Access Control Capabilities
- Grant narrow resource-level access (e.g., only `staging.example.com`) to external contractors, vendors, or internal non-engineering teams
- No need to update IP whitelists when access changes
- Granular access without exposing entire environments

## Gotchas
- Requires private/local DNS per subnet; without it, routing won't resolve correctly
- If an environment is **publicly hosted** (not private DNS), use [Whitelisting Traffic to Public Services](https://www.twingate.com/docs/whitelisting-traffic-to-public-services) instead
- Legacy VPN muscle memory—users no longer need to (and should not) manually switch network connections

## Related Docs
- [Private DNS Best Practices](https://www.twingate.com/docs/private-dns-best-practices)
- [Whitelisting Traffic to Public Services](https://www.twingate.com/docs/whitelisting-traffic-to-public-services)
- Getting Started on AWS / GCP tutorials
- Twingate Starter (free tier supports this pattern)