# Best Practices for Non-production Environment Access

## Summary
Twingate enables logical separation of dev/staging/production environments using FQDN-based routing without requiring users to switch VPN connections or reconfigure their network. Routing decisions happen before DNS resolution, allowing transparent environment separation based on destination hostname. Private DNS on each subnet handles final resolution to internal IPs.

## Key Information
- Routing is determined by destination FQDN **before** DNS resolution occurs
- Resources are coupled to Remote Networks; the resource address determines which network receives the request
- DNS resolution happens on the target subnet's local DNS, not the client's
- Users never need to know which backend network they're connecting to
- Environments remain invisible to the public internet when using private DNS

## Prerequisites
- Twingate Connectors deployed in each environment subnet (deploy in pairs for load balancing)
- Local/private DNS configured on each subnet to resolve internal hostnames
- Resources defined in Twingate admin for each environment (e.g., `dev.example.com`, `staging.example.com`)
- See [Private DNS Best Practices](https://www.twingate.com/docs/private-dns-best-practices) if no local DNS exists

## Configuration Pattern

| Environment | Twingate Resource | Remote Network | Resolves To |
|-------------|------------------|----------------|-------------|
| Development | `dev.example.com` | Dev subnet | `10.0.2.77` (via local DNS) |
| Staging | `staging.example.com` | Staging subnet | Internal IP (via local DNS) |
| Production | `prod.example.com` | Prod subnet | Internal IP (via local DNS) |

## Step-by-Step
1. Deploy Connector pairs in each environment subnet
2. Create a Remote Network in Twingate for each environment
3. Create a Resource per environment using environment-specific FQDNs
4. Assign Resources to appropriate user groups (limit scope per group)
5. Users connect once to Twingate — routing is automatic based on FQDN

## Access Control Notes
- Grant narrow resource access to external users (contractors, vendors) — e.g., staging server only, not entire subnet
- Grant selective access to internal non-engineering groups (marketing, executives) scoped to staging review URLs
- No whitelist rule updates needed when users change; Twingate handles authorization

## Gotchas
- Local DNS must exist on each subnet; without it, resolution fails even if routing is correct
- If an environment is publicly hosted (not private DNS), use [Whitelisting Traffic to Public Services](https://www.twingate.com/docs/whitelisting-traffic) instead
- Connector pairs required per subnet for load balancing/redundancy

## Related Docs
- [Private DNS Best Practices](https://www.twingate.com/docs/private-dns-best-practices)
- [Whitelisting Traffic to Public Services](https://www.twingate.com/docs/whitelisting-traffic)
- [Getting Started on AWS](https://www.twingate.com/docs/aws)
- [Getting Started on GCP](https://www.twingate.com/docs/gcp)