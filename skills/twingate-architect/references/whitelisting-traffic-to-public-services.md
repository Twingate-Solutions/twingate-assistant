# Best Practices for Whitelisting Traffic to Public Resources

## Summary
Twingate replaces IP whitelisting for public resources by routing authorized user traffic through Connectors with static IPs. Admins whitelist Connector IPs at the resource level and control user access via Twingate Groups, eliminating per-user IP management.

## Key Information
- Solves IP whitelisting challenges: dynamic IPs, location changes, overly broad shared IPs, large IP list maintenance
- Traffic from authorized users egresses through known Connector IPs → whitelist those IPs, not individual users
- Works for any public resource supporting source IP whitelisting (staging sites, SaaS apps, etc.)
- Users can access from any network/location once authorized in Twingate

## Prerequisites
- Twingate Admin Console access
- Connectors deployed in a cloud environment (AWS, GCP, Azure, etc.)
- Ability to assign static public IPs to Connectors (e.g., via NAT gateway)
- Target resource must support IP-based or header-based access control

## Step-by-Step

### Step 1: Whitelist Connector IPs at the Target Resource
1. Create a **Remote Network** in Twingate Admin Console
2. Deploy Connectors within that Remote Network
3. Assign static external IP addresses to the Connectors (typically the NAT gateway public IP of the private network)
4. Add these static IPs to the whitelist on your public resource or SaaS application

### Step 2: Restrict Access via Twingate
1. Create a **Resource** in Twingate pointing to the public resource URL/address
2. Associate the Resource with the Remote Network from Step 1 (ensures traffic routes through whitelisted Connectors)
3. Create a **Group** with authorized users
4. Associate the Group with the Resource

## Configuration Values
| Component | Setting |
|-----------|---------|
| Remote Network | Logical container for Connectors with static IPs |
| Resource | Public hostname/IP of the target service |
| Group | Users authorized to access the Resource |
| Static IP | Assigned at cloud NAT gateway level, not Connector process level |

## Gotchas
- Static IP assignment is at the **cloud infrastructure level** (NAT gateway), not configured within Twingate itself — requires cloud provider configuration
- All traffic from authorized users egresses from shared Connector IPs; the target resource sees Connector IP, not user IP
- Users must be **both** connected to Twingate **and** in an authorized Group to access the resource
- If Connectors are in multiple Remote Networks, each network's IPs may need to be whitelisted

## Related Docs
- [Configuring static public IP addresses in AWS](https://www.twingate.com/docs) (referenced but URL not provided)
- Remote Networks configuration
- Resources configuration
- Groups and access control