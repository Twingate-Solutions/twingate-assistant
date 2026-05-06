# Best Practices for Whitelisting Traffic to Public Resources

## Summary
Twingate replaces legacy IP whitelisting for public resources by routing authorized user traffic through Connectors with static IPs. Access control is managed centrally via the Admin Console, eliminating per-user IP management. Works for staging sites, SaaS apps with source IP whitelisting, or any public resource requiring access control.

## Key Information
- Connectors act as the egress point; their static IPs are what get whitelisted at the resource
- Users can work from any location without admin IP list updates
- Access is tied to authenticated identity (via IdP), not device/network IP
- Provides audit visibility into who has access

## Problems Solved vs. Legacy IP Whitelisting
- No more per-user dynamic IP tracking
- No location-dependent access failures
- Eliminates overly broad shared IP grants (e.g., entire office NAT)
- No large IP list maintenance burden
- Clear access revocation path

## Prerequisites
- Twingate Remote Network configured
- Connectors deployed in a cloud environment with static external IP support
- Access to the target public resource's whitelist settings
- Twingate Admin Console access

## Step-by-Step

**Step 1: Whitelist Connector IPs at the public resource**
1. Deploy Connectors in a Remote Network
2. Assign static external IP(s) to the Connector hosts (typically the NAT gateway public IP)
3. Add those static IPs to the whitelist in your public resource or SaaS application

**Step 2: Restrict access via Twingate Admin Console**
1. Create a Resource in Twingate pointing to the public resource URL/address
2. Associate the Resource with the Remote Network from Step 1
3. Create a Group containing authorized users
4. Associate the Group with the Resource

## Configuration Notes
- Static IP assignment method depends on cloud provider (AWS NAT Gateway example in linked guide)
- Resource definition: use the public hostname/IP of the target service
- Remote Network: logical grouping that ties Connectors to Resources

## Gotchas
- The static IP to whitelist is the **NAT gateway IP**, not the Connector instance's private IP
- All authorized users share the Connector egress IPs — the whitelisting is at the Connector level, not per-user
- Users must be **both** connected to Twingate **and** in an authorized Group to reach the resource
- Connector redeployment or cloud changes may alter the public IP — re-whitelist if Connectors are rebuilt

## Related Docs
- Configuring static public IP addresses in AWS (linked in source)
- Remote Networks setup
- Resources configuration
- Groups and access control