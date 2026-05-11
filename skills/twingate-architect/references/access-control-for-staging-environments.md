# Best Practices for Non-production Environment Access

## Summary
Twingate enables transparent routing between development, staging, and production environments using FQDN-based routing decided before DNS resolution. Users access different environments without switching clients or configurations. Resources are coupled to Remote Networks, with the destination address determining routing.

## Key Information
- Routing decisions happen **before DNS resolution**, based on destination FQDN
- Resources are coupled to Remote Networks (target private networks)
- DNS resolution occurs locally on the target subnet after routing
- Environments remain completely hidden from public internet when using private DNS
- Users never need to know which backend network they're connecting to

## Prerequisites
- Twingate Connectors deployed in each subnet (deploy in pairs for load balancing)
- Local/private DNS configured per subnet (see Private DNS Best Practices guide)
- Resources defined in Twingate for each environment (e.g., `dev.example.com`, `staging.example.com`)

## Configuration Pattern

| Environment | Twingate Resource | Remote Network | Resolves To |
|-------------|-------------------|----------------|-------------|
| Development | `dev.example.com` | Dev subnet | `10.0.2.77` (via local DNS) |
| Staging | `staging.example.com` | Staging subnet | local IP (via local DNS) |
| Production | `prod.example.com` | Prod subnet | local IP (via local DNS) |

## Step-by-Step
1. Deploy Connector pairs in each environment subnet
2. Configure private/local DNS on each subnet
3. Create a Remote Network in Twingate per environment
4. Create Resources (by FQDN) coupled to their respective Remote Networks
5. Assign user/group access policies per Resource
6. Users connect once — routing is automatic based on FQDN

## Access Control Benefits
- Grant narrow Resource access to specific groups (contractors, vendors, marketing) without exposing full environments
- No whitelist rule updates needed when users change
- No port forwarding, static IPs, or DDNS required

## Gotchas
- Requires private/local DNS per subnet — without it, routing still works but name resolution won't function correctly
- If an environment is publicly hosted (not private DNS), use the Whitelisting Traffic to Public Services approach instead
- Users should never need to disconnect/reconnect between environments — if they do, Resources or Remote Networks may be misconfigured

## Related Docs
- Private DNS Best Practices
- Whitelisting Traffic to Public Services
- Getting Started with Twingate on AWS
- Getting Started with Twingate on GCP