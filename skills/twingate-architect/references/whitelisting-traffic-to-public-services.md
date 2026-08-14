---
source: https://www.twingate.com/docs/whitelisting-traffic-to-public-services
type: docs
fetched: 2026-08-14
source_version: dbf61bbcdd72fdefaf914bb6fbd31ccdd81f0a721e9e76064f4d164e13050f21
---

# Best Practices for Whitelisting Traffic to Public Resources

## Summary
Twingate replaces legacy IP whitelisting for public resources by routing authorized user traffic through Connectors with static IPs. Access control is managed centrally via the Admin Console, eliminating per-user IP management. Users can access resources from any location without admin intervention.

## Key Information
- Solves IP whitelisting problems for public internet resources (staging sites, SaaS apps with source whitelisting)
- Traffic from authorized users exits through Connector IPs, which are whitelisted at the resource
- Identity Provider authentication provides visibility into who accessed what
- Works regardless of user's physical location or ISP

## Prerequisites
- Twingate account with Admin Console access
- One or more Connectors deployed in cloud infrastructure (AWS, GCP, Azure, etc.)
- Ability to assign static public IPs to Connectors' NAT gateway
- Target resource/SaaS app must support IP or header-based whitelisting

## Step-by-Step

### Step 1: Whitelist Connector IPs at the target resource
1. Deploy Connectors in a Remote Network
2. Assign static external IP addresses to the Connectors (typically via NAT gateway in cloud provider)
3. Add those static IPs to the allowlist in your public resource or SaaS application

### Step 2: Configure access control in Twingate Admin Console
1. Create a **Resource** pointing to the public resource's URL/address
2. Associate the Resource with the Remote Network from Step 1 (ensures traffic routes through whitelisted Connectors)
3. Create a **Group** of authorized users
4. Associate the Group with the Resource

## Configuration Values
| Component | Value |
|-----------|-------|
| Remote Network | Container for Connectors with static IPs |
| Resource | Public resource URL/address tied to that Remote Network |
| Group | Set of authorized Twingate users |
| Static IP source | NAT gateway public IP of Connector host |

## Gotchas
- Static IP assignment depends on deployment platform — must be configured at infrastructure level (e.g., AWS Elastic IP on NAT Gateway), not within Twingate itself
- All authorized users share the Connector's outbound IP — resource logs will show Connector IP, not individual user IPs (use Twingate logs for user-level audit)
- Connectors must be in the same Remote Network as the Resource for traffic routing to work correctly
- If multiple Connectors are used for HA, all their IPs must be whitelisted at the target resource

## Related Docs
- [Configuring static public IP addresses in AWS](#) (linked in source)
- Remote Networks configuration
- Resources configuration
- Groups configuration
- Identity Provider integration