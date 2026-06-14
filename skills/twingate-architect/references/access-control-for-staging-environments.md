# Best Practices for Non-production Environment Access

## Summary
Twingate enables transparent routing to separate development/staging/production environments using FQDN-based routing decided before DNS resolution. Users connect to different environments simply by using different hostnames, with no manual VPN switching required. Resources are coupled to Remote Networks, so the destination address determines which private network handles the request.

## Key Information
- Routing decisions happen **before DNS resolution**, using the FQDN in the user's request
- Each environment gets its own Twingate Resource tied to its own Remote Network/subnet
- Local DNS on each subnet resolves hostnames to private IPs (e.g., `dev.example.com` → `10.0.2.77`)
- Connectors should be deployed in pairs per subnet for load balancing
- Environments remain invisible to the public internet (no public DNS exposure)
- Granular access: users/groups can be restricted to specific Resources (e.g., only `staging.example.com`)

## Prerequisites
- Twingate Connectors deployed in each target subnet (pairs recommended)
- Local/private DNS configured per subnet for hostname resolution
- Separate Remote Networks defined per environment in Twingate admin

## Step-by-Step Configuration

1. Deploy Connector pairs in each environment subnet (dev, staging, prod)
2. Create a Remote Network in Twingate for each subnet
3. Create Resources mapped to each Remote Network:
   - `dev.example.com` → dev Remote Network
   - `staging.example.com` → staging Remote Network
4. Configure local DNS in each subnet to resolve the FQDN to the private IP
5. Assign user/group access policies to each Resource as needed

## Configuration Values
| Component | Example Value |
|-----------|--------------|
| Dev Resource address | `dev.beamreachinc.com` |
| Staging Resource address | `staging.beamreachinc.com` |
| Private IP (resolved locally) | `10.0.2.77` |

## Gotchas
- **Local DNS required**: Each subnet needs its own DNS to resolve private hostnames; without it, routing won't work as expected → see *Private DNS Best Practices*
- **Publicly hosted environments**: If an environment is publicly accessible, FQDN-based routing alone isn't sufficient—use the *Whitelisting Traffic to Public Services* approach instead
- Resources must be explicitly scoped; users with access to one environment Resource do not automatically get access to others

## Related Docs
- [Private DNS Best Practices](https://www.twingate.com/docs/private-dns-best-practices)
- [Whitelisting Traffic to Public Services](https://www.twingate.com/docs/whitelisting-traffic-to-public-services)
- [Getting Started with Twingate on AWS](https://www.twingate.com/docs/aws)
- [Getting Started with Twingate on GCP](https://www.twingate.com/docs/gcp)