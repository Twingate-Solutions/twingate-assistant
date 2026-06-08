# Best Practices for Whitelisting Traffic to Public Resources

## Summary
Twingate replaces legacy IP whitelisting for public resources by routing authorized user traffic through Connectors with static IPs. Access control is managed centrally via Groups and Resources in the Admin Console, eliminating per-user IP management.

## Key Information
- Solves the problem of controlling access to public internet resources (staging sites, SaaS apps with source IP whitelisting)
- Connector hosts serve as the static egress points that get whitelisted at the destination
- Users can work from any location without admin IP list updates
- Access tied to identity provider authentication, not source IP

## Prerequisites
- Twingate Remote Network configured with one or more Connectors
- Connectors deployed with static external IP addresses (e.g., via NAT gateway with Elastic IP in AWS)
- Access to the target public resource/SaaS app's IP whitelist configuration
- Twingate Admin Console access

## Step-by-Step

### Step 1: Whitelist Connector IPs at the destination
1. Deploy Connectors in a Remote Network with static public IP addresses (typically the NAT gateway public IP)
2. Add those static IPs to the allowlist of the public resource or SaaS application

### Step 2: Configure access control in Twingate
1. Create a **Resource** in the Admin Console pointing to the public resource's address
2. Associate the Resource with the Remote Network from Step 1
3. Create a **Group** and add authorized users to it
4. Grant the Group access to the Resource

## Configuration Values
- **Remote Network**: logical grouping containing the Connectors with static IPs
- **Resource**: the public URL/IP of the target service
- **Group**: set of authorized Twingate users
- Static IP assignment: cloud-provider dependent (see AWS NAT gateway guide for reference)

## Gotchas
- Static IP must be assigned at the **NAT gateway** level, not the Connector instance itself — the Connector's traffic egresses through the NAT
- All Connectors in the Remote Network share the NAT gateway IP; whitelist all gateway IPs if multiple NAT gateways are used
- Users must be both connected to Twingate **and** in an authorized Group — satisfying one condition alone is insufficient
- Connector IP changes (e.g., infrastructure redeployment) require updating the destination whitelist

## Related Docs
- [Configuring static public IP addresses in AWS](#) (NAT gateway guide)
- Remote Networks configuration
- Resources configuration
- Groups and access control