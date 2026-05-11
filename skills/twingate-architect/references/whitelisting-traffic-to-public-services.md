# Best Practices for Whitelisting Traffic to Public Resources

## Summary
Twingate replaces IP whitelisting for public resources by routing authorized user traffic through Connectors with static IPs. Access control is managed centrally via the Admin Console, eliminating per-user IP management. Users can access resources from any location without admin intervention.

## Key Information
- Solves IP whitelisting problems for public internet resources (staging sites, SaaS apps with source whitelisting)
- Traffic from authorized users routes through Connector hosts with known static IPs
- Access tied to identity provider authentication, not source IP
- Works regardless of user's physical location or network

## Problems Solved vs Legacy IP Whitelisting
- No per-user IP collection or updates needed
- Users can work from any location without admin changes
- Eliminates overly broad shared IPs (office NAT, coworking spaces)
- Single source of truth for access control (Admin Console vs IP lists)
- Easy revocation via group membership changes

## Step-by-Step Implementation

### Step 1: Configure Connector with Static IP
1. Create a **Remote Network** in Twingate Admin Console
2. Deploy Connectors in that Remote Network
3. Assign static external IP(s) to Connector hosts (e.g., static NAT gateway IP in AWS)
4. Whitelist those static IPs in your public resource or SaaS application

### Step 2: Restrict Access via Admin Console
1. Create a **Resource** in Twingate pointing to your public resource URL/address
2. Associate the Resource with the Remote Network from Step 1
3. Create a **Group** with authorized users
4. Associate the Group with the Resource

## Configuration Values
| Component | Value |
|-----------|-------|
| Remote Network | Maps to Connector deployment location |
| Static IP source | NAT gateway public IP of Connector's private network |
| Access control | Group membership in Admin Console |

## Prerequisites
- Twingate Connectors deployed in a cloud environment supporting static IPs
- Ability to configure IP whitelisting on target public resource/SaaS app
- Twingate Admin Console access
- Identity Provider configured in Twingate

## Gotchas
- Static IP must be assigned at the **NAT gateway level**, not the Connector instance itself — the Connector's egress IP is the gateway's public IP
- All authorized users share the same egress IPs (the Connector hosts); whitelist at resource must allow those IPs
- Users must be **both** connected to Twingate **and** in an authorized Group — connection alone is insufficient
- Cloud-specific configuration required for static IPs (see AWS guide for example)

## Related Docs
- [Configuring static public IP addresses in AWS](#) (referenced in page)
- Remote Networks configuration
- Resource creation
- Group management