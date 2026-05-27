# Best Practices for Whitelisting Traffic to Public Resources

## Summary
Twingate replaces legacy IP whitelisting for public resources by routing authorized user traffic through Connectors with static IPs. This centralizes access control, eliminates per-user IP management, and enables location-independent access while maintaining visibility into who can access resources.

## Key Information
- Use case: controlling access to public internet resources (staging sites, SaaS apps with IP allowlisting)
- Twingate routes traffic through Connectors with known static IPs, replacing per-user IP whitelisting
- Access control managed via Groups + Resources in Admin Console rather than IP lists
- Works with any SaaS application that supports source IP whitelisting

## Prerequisites
- Twingate Remote Network configured with deployed Connectors
- Static external IP addresses assigned to Connector hosts (via cloud NAT gateway or equivalent)
- Admin access to Twingate Admin Console
- Ability to configure IP allowlist on target public resource/SaaS app

## Step-by-Step

### 1. Whitelist Connector IPs with the Public Resource
1. Deploy Connectors in a Remote Network
2. Assign static public IP addresses to the Connector hosts (typically the NAT gateway public IP for the private network)
3. Add those static IPs to the allowlist of the target public resource or SaaS application

### 2. Restrict Access via Twingate Admin Console
1. Create a **Resource** in Twingate representing the public resource URL/address
2. Associate the Resource with the Remote Network from Step 1
3. Create a **Group** and add authorized users to it
4. Associate the Group with the Resource

## Configuration Values
- **Remote Network**: logical grouping for Connectors; determines egress path
- **Resource**: defines the public resource (FQDN or IP) users access through Twingate
- **Group**: controls which users can access the Resource
- Static IP assignment method varies by cloud provider (see AWS NAT gateway guide for reference)

## Gotchas
- Static IPs must be assigned at the **NAT gateway / infrastructure level**, not directly to Connector software — Twingate does not manage external IPs itself
- All Connectors in the Remote Network share the same egress IP(s); scope Remote Networks appropriately if different resources need different IP allowlists
- Users must be **both** connected to Twingate **and** in an authorized Group — Twingate connection alone is insufficient
- Traffic routing through the Connector only applies when the Resource is defined in Twingate; public resources not defined as Resources bypass this path

## Related Docs
- Configuring static public IP addresses in AWS (NAT gateway guide)
- Remote Networks configuration
- Resources configuration
- Groups configuration
- Identity Provider integration