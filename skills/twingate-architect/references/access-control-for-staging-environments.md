# Best Practices for Non-production Environment Access

## Summary
Twingate enables logical separation of development, staging, and production environments without requiring users to switch VPN connections or reconfigure networks. Routing decisions are made based on destination FQDN **before** DNS resolution, allowing transparent environment separation. Users access the correct environment simply by using the appropriate hostname.

## Key Information
- Routing is determined by FQDN **before** DNS resolution occurs
- Resources are coupled to Remote Networks; the resource **address** determines target network routing
- DNS resolution happens locally on the target subnet after routing
- Multiple environments can share identical internal hostnames resolved differently per subnet
- Environments remain invisible to the public internet when using private DNS

## Prerequisites
- Twingate Connectors deployed in each target subnet (pairs recommended for load balancing)
- Local/private DNS configured per subnet
- Resources defined in Twingate mapped to appropriate Remote Networks
- See [Private DNS Best Practices](https://www.twingate.com/docs/private-dns-best-practices) if no local DNS exists

## Configuration Pattern

| Component | Dev Environment | Staging Environment |
|-----------|----------------|---------------------|
| Resource Address | `dev.example.com` | `staging.example.com` |
| Remote Network | Dev subnet | Staging subnet |
| DNS Resolution | Local dev DNS → `10.0.2.77` | Local staging DNS → separate IP |
| Connector Pair | Deployed in dev subnet | Deployed in staging subnet |

## Step-by-Step
1. Deploy Connector pairs in each environment's subnet
2. Create a Remote Network in Twingate for each subnet
3. Define Resources with environment-specific FQDNs (e.g., `dev.example.com`, `staging.example.com`)
4. Associate each Resource with its corresponding Remote Network
5. Grant user/group access to specific Resources (not entire networks)
6. Users connect to Twingate once — routing is automatic based on hostname used

## Gotchas
- If an environment is **publicly hosted** (not private subnet), this approach doesn't apply — see [Whitelisting Traffic to Public Services](https://www.twingate.com/docs/whitelisting-traffic-to-public-services)
- No local DNS per subnet = routing works but resolution will fail; private DNS is required
- Connector deployment in pairs is for load balancing — single connectors create a SPOF
- Users must use the correct FQDN; IP-based access bypasses Twingate routing logic

## Benefits Summary
- No user action required to switch environments
- Granular access: grant contractors/vendors access to `staging.example.com` only
- Environments fully hidden from public internet
- Eliminates VPN connect/disconnect workflow

## Related Docs
- [Private DNS Best Practices](https://www.twingate.com/docs/private-dns-best-practices)
- [Whitelisting Traffic to Public Services](https://www.twingate.com/docs/whitelisting-traffic-to-public-services)
- Getting Started: AWS / GCP tutorials