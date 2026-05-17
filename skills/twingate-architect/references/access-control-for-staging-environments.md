# Best Practices for Non-Production Environment Access

## Summary
Twingate routes private traffic based on destination FQDN **before** DNS resolution, enabling transparent routing to separate environments (dev/staging/prod) without user reconfiguration. Resources are coupled to Remote Networks, so the address field determines which private network handles the request and performs local DNS resolution.

## Key Information
- Traffic routing decisions occur before DNS resolution — FQDN alone determines target network
- Resources map to Remote Networks; the Resource address drives routing, not client-side config
- Local DNS on each subnet resolves hostnames to internal IPs (e.g., `dev.beamreachinc.com` → `10.0.2.77`)
- Users never need to switch VPN connections or know which backend network they're hitting
- Environments remain invisible to the public internet when using private DNS

## Prerequisites
- Twingate Connectors deployed in each target subnet (deploy in pairs for load balancing)
- Local/private DNS configured per subnet (see [Private DNS Best Practices](https://www.twingate.com/docs/private-dns))
- Separate Remote Networks defined in Twingate admin for each environment

## Configuration Pattern

| Component | Dev Example | Staging Example |
|-----------|-------------|-----------------|
| Resource address | `dev.beamreachinc.com` | `staging.beamreachinc.com` |
| Remote Network | Development subnet | Staging subnet |
| DNS resolution | Local DNS on dev subnet | Local DNS on staging subnet |
| Connector placement | Dev subnet (×2) | Staging subnet (×2) |

## Step-by-Step
1. Deploy Connector pairs in each environment subnet
2. Create a Remote Network in Twingate admin for each environment
3. Create Resources using environment-specific FQDNs, coupled to the correct Remote Network
4. Assign user/group access policies per Resource (narrow access as needed)
5. Configure local DNS on each subnet to resolve internal hostnames

## Access Control Notes
- Grant granular access: contractors/vendors can get access to `staging.beamreachinc.com` only, not the entire subnet
- Internal non-technical teams (product, marketing) can review staging without broad network access
- For **publicly hosted** resources where whitelist management is the concern, see [Whitelisting Traffic to Public Services](https://www.twingate.com/docs/whitelisting-traffic)

## Gotchas
- Requires local/private DNS per subnet — without it, hostname resolution won't work correctly
- Resource address must be the FQDN users request; Twingate intercepts before any DNS lookup
- No support for this pattern if environments share the same FQDN (routing cannot differentiate)

## Related Docs
- [Private DNS Best Practices](https://www.twingate.com/docs/private-dns)
- [Whitelisting Traffic to Public Services](https://www.twingate.com/docs/whitelisting-traffic)
- [Getting Started on AWS](https://www.twingate.com/docs/aws)
- [Getting Started on GCP](https://www.twingate.com/docs/gcp)