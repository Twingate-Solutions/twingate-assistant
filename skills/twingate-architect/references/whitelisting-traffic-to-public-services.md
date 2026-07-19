# Best Practices for Whitelisting Traffic to Public Resources

## Summary
Twingate replaces legacy IP whitelisting for public resources by routing authorized user traffic through Connectors with static IPs. Admins whitelist Connector IPs instead of individual user IPs, then control access via Twingate Groups and Resources.

## Key Information
- Solves IP whitelisting problems: dynamic user IPs, location changes, overly broad shared IPs, large IP list maintenance
- Traffic to public resources routes through Connector hosts with known static IPs
- Access control enforced via Twingate Groups + Identity Provider authentication
- Users can access from any location without admin IP list updates

## Prerequisites
- Twingate Admin Console access
- Connectors deployed in a cloud environment with static public IP support (e.g., AWS NAT gateway)
- Target public resource or SaaS app must support source IP whitelisting

## Step-by-Step

**Step 1: Whitelist Connector IPs with the public resource**
1. Create a Remote Network in Twingate Admin Console
2. Deploy Connectors within that Remote Network
3. Assign static external IP addresses to Connectors (typically via cloud NAT gateway)
4. Add those static IPs to the public resource's/SaaS app's allowlist

**Step 2: Restrict access to authorized users**
1. Create a Resource in Twingate for the public URL/service
2. Associate the Resource with the Remote Network from Step 1
3. Create a Group and add authorized users
4. Grant the Group access to the Resource

## Configuration Values
- **Remote Network**: logical grouping for Connectors; must be associated with the Resource
- **Static IP assignment**: configured at cloud infrastructure level (not within Twingate); see AWS NAT gateway guide for reference
- **Group**: used to grant/revoke user access to the Resource

## Gotchas
- Static IP assignment happens at the cloud provider level (NAT gateway), **not** inside Twingate — Twingate does not directly manage Connector IPs
- Both conditions must be true for access: user must be (1) connected to Twingate AND (2) authorized via Group membership
- If Connectors are in multiple Remote Networks, each network's IPs need to be whitelisted separately
- Connector must be in the same Remote Network as the Resource for traffic to route correctly

## Related Docs
- [Configuring static public IP addresses in AWS](https://www.twingate.com/docs) (linked in source)
- Remote Networks configuration
- Resources configuration
- Groups configuration