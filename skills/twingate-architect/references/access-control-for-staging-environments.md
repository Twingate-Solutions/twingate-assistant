---
source: https://www.twingate.com/docs/access-control-for-staging-environments
type: docs
fetched: 2026-08-14
source_version: 16605c5156e207c8e3e99cc1f1c90a3bebf3068d73984d8dcc0567825b5a5faa
---

# Best Practices for Non-production Environment Access

## Summary
Twingate routes private traffic based on destination FQDN **before** DNS resolution, enabling transparent routing to separate environments (dev/staging/prod) without user reconfiguration. Resources are coupled to Remote Networks, so the address field determines which subnet handles DNS resolution. Users never need to manually switch between environments.

## Key Information
- Routing decision happens pre-DNS resolution, using FQDN as the routing key
- Each environment needs Twingate Connectors deployed in its subnet (deploy in pairs for load balancing)
- Local DNS on each subnet resolves the FQDN to the correct internal IP
- Environments remain completely hidden from the public internet when using private DNS
- Granular access can be granted per Resource (e.g., `staging.example.com` only), not entire networks

## Prerequisites
- Twingate Connectors deployed in each target subnet
- Local/private DNS configured per subnet (see: Private DNS Best Practices)
- Resources created in Twingate and mapped to corresponding Remote Networks

## Step-by-Step Configuration

1. Deploy Connector pairs in each environment subnet (dev, staging, prod)
2. Create a Remote Network in Twingate for each subnet
3. Create Resources with environment-specific FQDNs:
   - `dev.example.com` → mapped to dev Remote Network
   - `staging.example.com` → mapped to staging Remote Network
4. Assign user/group access policies per Resource
5. Users connect once to Twingate; routing is automatic based on requested FQDN

## Configuration Values
| Component | Value/Notes |
|-----------|-------------|
| Resource address | FQDN (e.g., `staging.example.com`) |
| Remote Network | Maps to specific subnet |
| DNS resolution | Handled by local DNS on target subnet |
| Connectors per subnet | Minimum 2 (load balancing) |

## Gotchas
- **No local DNS?** Private DNS must be configured per subnet for this pattern to work — consult Private DNS Best Practices guide
- **Publicly hosted environments:** If an environment is public, this routing approach doesn't apply — use the Whitelisting Traffic to Public Services approach instead
- Routing is FQDN-based, so consistent naming conventions across environments are critical

## Benefits Summary
- Users connect once; no manual environment switching
- External users (contractors, vendors) and internal non-technical users get scoped access without seeing backend topology
- No public DNS exposure = no accidental resource exposure
- No whitelist management overhead

## Related Docs
- Private DNS Best Practices
- Whitelisting Traffic to Public Services
- Getting Started with Twingate on AWS
- Getting Started with Twingate on GCP
- Twingate Starter (free tier, ~3-4 min setup)