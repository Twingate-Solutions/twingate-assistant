# Best Practices for Non-production Environment Access

## Summary
Twingate enables transparent routing between development, staging, and production environments using FQDN-based routing decided before DNS resolution. Users connect to different environments without switching VPN profiles or reconfiguring anything. Resources are coupled to Remote Networks, and the destination address determines routing.

## Key Information
- Routing decisions are made **before DNS resolution** based on destination FQDN
- Resources are coupled to Remote Networks (private subnets)
- DNS resolution happens on the local subnet after routing — requires local/private DNS
- Environments remain completely invisible to the public internet
- Users never need to know which backend network they're connecting to

## Prerequisites
- Twingate Connectors deployed in each target subnet (deploy in pairs for load balancing)
- Private/local DNS configured on each subnet (see: Private DNS Best Practices)
- Twingate Resources defined per environment (e.g., `dev.example.com`, `staging.example.com`)
- Resources mapped to their corresponding Remote Networks

## Configuration Pattern

| Environment | Resource FQDN | Remote Network | Resolved IP (local DNS) |
|-------------|--------------|----------------|------------------------|
| Development | `dev.beamreachinc.com` | Dev subnet | `10.0.2.77` |
| Staging | `staging.beamreachinc.com` | Staging subnet | internal IP |
| Production | `prod.beamreachinc.com` | Prod subnet | internal IP |

## Step-by-Step
1. Deploy Connector pairs into each environment's subnet
2. Create a Remote Network in Twingate for each subnet
3. Define a Resource per environment with its FQDN and associate to the correct Remote Network
4. Grant user/group access to specific Resources (not entire networks)
5. Users connect via Twingate — routing is automatic based on FQDN

## Access Control
- Grant narrow Resource access to specific groups (contractors, vendors, marketing) without exposing full environments
- Use Groups to separate access: e.g., contractors get `staging.example.com` only
- No whitelist management required for internal private resources

## Gotchas
- **Requires private/local DNS per subnet** — without it, resolution after routing will fail
- Routing is FQDN-based pre-DNS, so wildcard or IP-based resources behave differently
- If an environment is publicly hosted, this pattern doesn't apply — see "Whitelisting Traffic to Public Services" instead
- Connectors must be deployed inside each target subnet for correct DNS resolution context

## Related Docs
- Private DNS Best Practices
- Whitelisting Traffic to Public Services
- Getting Started with Twingate on AWS
- Getting Started with Twingate on GCP