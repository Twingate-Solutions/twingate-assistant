# Best Practices for Whitelisting Traffic to Public Resources

## Summary
Twingate replaces legacy IP whitelisting for public resources by routing authorized user traffic through Connectors with static IPs. Access control is managed centrally via the Admin Console, eliminating per-user IP management. Users can access resources from any location without admin intervention.

## Key Information
- Replaces source IP whitelisting for public internet resources (staging sites, SaaS apps with IP allowlists)
- Traffic routes through Connector hosts with known static IPs — whitelist the Connector IPs, not user IPs
- Access controlled via Twingate Groups + Identity Provider authentication
- Works from any user location/network without IP list updates

## Problems Solved vs. Legacy IP Whitelisting
- Users' home/roaming IPs are dynamic — Connector IPs are static
- No per-user IP submissions or admin updates when users change locations
- Eliminates overly broad shared office IPs granting access to unauthorized devices
- Centralizes access list management (no sprawling IP lists)
- Access removal is explicit (remove user from Group) vs. guessing stale IPs

## Step-by-Step Implementation

### Step 1: Whitelist Connector IPs with the public resource
1. Create a **Remote Network** in Twingate Admin Console
2. Deploy Connectors in that Remote Network with **static external IPs** (e.g., via NAT gateway static IP in AWS)
3. Add those static IPs to the allowlist of the target public resource or SaaS application

### Step 2: Restrict access to authorized users
1. Create a **Resource** in Twingate pointing to the public resource URL/address
2. Associate the Resource with the Remote Network from Step 1
3. Create a **Group**, add authorized users to it, and grant the Group access to the Resource

## Configuration Values
| Component | Value/Note |
|-----------|------------|
| Remote Network | Logical grouping for Connectors routing traffic |
| Connector static IP | Public IP of NAT gateway for the cloud network |
| Resource | Public URL or address of the target service |
| Group | Controls which Twingate users can access the Resource |

## Prerequisites
- Connectors deployed in a cloud environment supporting static public IPs (AWS, GCP, Azure, etc.)
- Ability to configure IP allowlists on the target resource/SaaS app
- Identity Provider configured in Twingate Admin Console

## Gotchas
- Static IP must be assigned at the **NAT gateway/egress level**, not directly to the Connector instance
- All authorized user traffic egresses from Connector IPs — ensure Connector capacity handles the load
- If multiple Connectors exist in the Remote Network, whitelist **all** their static IPs (load balancing may use any)
- Users must be **both** connected to Twingate **and** in an authorized Group — either condition alone is insufficient

## Related Docs
- [Configuring Static Public IPs in AWS](https://www.twingate.com/docs) (referenced in page)
- Remote Networks configuration
- Groups and Resource access control
- Identity Provider integration