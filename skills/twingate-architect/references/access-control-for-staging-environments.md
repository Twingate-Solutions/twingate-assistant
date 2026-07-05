# Best Practices for Non-production Environment Access

## Summary
Twingate routes private traffic based on destination FQDN **before** DNS resolution, enabling transparent routing to separate dev/staging/production environments without user reconfiguration. Resources are coupled to Remote Networks, so the address field determines which private network handles the request and DNS resolution.

## Key Information
- Routing decisions happen pre-DNS resolution, using FQDN as the routing key
- Each environment requires: a Remote Network + deployed Connector pair + a Resource with environment-specific FQDN
- Local DNS on each subnet resolves the FQDN to the correct private IP
- Users need zero configuration changes to switch between environments
- Environments remain invisible to the public internet (no public DNS exposure)

## Prerequisites
- Twingate Connectors deployed (in pairs recommended for load balancing) in each subnet
- Local DNS configured per subnet for private hostname resolution
- Separate Remote Networks defined in Twingate admin for each environment

## Configuration Pattern

| Environment | Resource Address | Remote Network | Resolves To |
|------------|-----------------|----------------|-------------|
| Dev | `dev.example.com` | Dev subnet | `10.0.2.77` (via local DNS) |
| Staging | `staging.example.com` | Staging subnet | staging IP (via local DNS) |
| Production | `prod.example.com` | Prod subnet | prod IP (via local DNS) |

## Step-by-Step
1. Deploy Connector pairs into each private subnet (dev, staging, prod)
2. Create a Remote Network in Twingate admin for each environment
3. Associate each Connector with its corresponding Remote Network
4. Create a Resource per environment using the environment-specific FQDN as the address
5. Assign user/group access policies to each Resource as needed
6. Configure local DNS on each subnet to resolve the FQDN to the correct private IP

## Access Control Notes
- Grant narrow Resource access to external users (contractors, vendors) without exposing entire environments
- Grant staging-only access to internal non-engineering teams (marketing, executives)
- No whitelist management required since environments are private by default

## Gotchas
- Requires local/private DNS per subnet — without it, resolution will fail (see *Private DNS Best Practices*)
- If an environment is **publicly hosted**, this pattern doesn't apply — use the *Whitelisting Traffic to Public Services* approach instead
- Connector pairs are recommended; single Connectors create a single point of failure

## Related Docs
- [Private DNS Best Practices](https://www.twingate.com/docs/private-dns-best-practices)
- [Whitelisting Traffic to Public Services](https://www.twingate.com/docs/whitelisting-traffic-to-public-services)
- Getting Started with Twingate on AWS
- Getting Started with Twingate on GCP