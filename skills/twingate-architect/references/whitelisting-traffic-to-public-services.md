# Best Practices for Whitelisting Traffic to Public Resources

## Summary
Twingate replaces IP-based whitelisting for public resources by routing authorized user traffic through Connectors with known static IPs. Admins whitelist Connector IPs instead of individual user IPs, then control access via Twingate Groups. This eliminates dynamic IP management and provides identity-based access control.

## Key Information
- Addresses limitations of traditional IP whitelisting (dynamic IPs, location changes, broad shared IPs, large IP lists)
- Traffic from authorized users egresses through Connector's static IP, which is what gets whitelisted
- Access control enforced via Twingate Groups + Identity Provider authentication
- Works for any public resource supporting source IP whitelisting (staging sites, SaaS apps, etc.)

## Prerequisites
- Twingate Admin Console access
- One or more Connectors deployed in a cloud environment (AWS, GCP, Azure, etc.)
- Ability to assign static public IPs to Connector hosts (e.g., via NAT gateway)
- Ability to configure source IP allowlists on the target public resource/SaaS app

## Step-by-Step

### Step 1: Whitelist Connector IPs with the Public Resource
1. Create a **Remote Network** in Twingate Admin Console
2. Deploy Connectors within that Remote Network
3. Assign static external IPs to Connector hosts (typically via cloud NAT gateway)
4. Add those static IPs to the allowlist of the target public resource or SaaS application

### Step 2: Restrict Access via Twingate Admin Console
1. Create a **Resource** in Twingate pointing to the public resource URL/address
2. Associate the Resource with the Remote Network from Step 1
3. Create a **Group** in Twingate
4. Add authorized users to the Group
5. Grant the Group access to the Resource

## Configuration Values
| Component | Value/Setting |
|-----------|--------------|
| Remote Network | Associates Connectors that provide egress IPs |
| Resource | Public hostname/IP to protect; linked to Remote Network |
| Group | Contains authorized users; assigned to Resource |
| Static IP | NAT gateway public IP of Connector host (cloud-provider-specific) |

## Gotchas
- Static IP assignment is **not automatic** — requires cloud infrastructure configuration (see AWS static IP guide separately)
- The Connector's **NAT gateway IP** (not the Connector's private IP) is what external services see and should whitelist
- All authorized users share the same egress IPs — the public resource sees Connector IPs, not individual user IPs
- Users must be both **connected to Twingate** AND in an authorized Group to reach the resource

## Related Docs
- Configuring static public IP addresses in AWS
- Remote Networks setup
- Resources configuration
- Groups management