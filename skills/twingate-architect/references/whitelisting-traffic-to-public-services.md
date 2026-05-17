# Best Practices for Whitelisting Traffic to Public Resources

## Summary
Twingate replaces legacy IP whitelisting for public resources by routing authorized user traffic through Connectors with static IPs. Access control is managed centrally in the Admin Console, eliminating per-user IP management.

## Key Information
- Use case: Restrict access to public internet resources (staging sites, SaaS apps with source IP whitelisting)
- Traffic is routed through Connector hosts with known static IPs, which are whitelisted at the resource
- Users can access from any location without admin IP updates
- Access tied to identity (via IdP) rather than device/network IP

## Problems This Solves
- User IPs are dynamic (especially remote/home workers)
- IP changes require admin intervention per user
- Shared IPs (office NAT) grant overly broad access
- Large IP lists are hard to maintain and audit
- No clear signal for when to revoke IP access

## Step-by-Step

**Step 1: Whitelist Connector IPs at the target resource**
1. Create a Remote Network in Twingate Admin Console
2. Deploy Connectors in that Remote Network
3. Assign static external IPs to Connector hosts (e.g., via AWS NAT Gateway Elastic IP)
4. Add those static IPs to the whitelist of your public resource or SaaS app

**Step 2: Restrict access via Twingate RBAC**
1. Create a Resource in Twingate pointing to the public resource's address
2. Associate the Resource with the Remote Network from Step 1
3. Create a Group with authorized users
4. Assign the Group access to the Resource

## Configuration Values
| Component | Value/Action |
|-----------|-------------|
| Remote Network | Logical grouping for Connectors with static IPs |
| Resource | Public URL/IP of the target service |
| Static IP source | NAT gateway public IP (cloud provider dependent) |
| Access control | Group membership in Admin Console |

## Prerequisites
- Twingate Admin Console access
- Connectors deployed in a cloud environment supporting static public IPs
- Ability to configure IP whitelisting on target resource/SaaS app
- Identity Provider configured in Twingate (for user authentication)

## Gotchas
- Static IP must be assigned at the **network/NAT gateway level**, not the Connector instance itself — Connector sees private IP
- Multiple Connectors in one Remote Network may have different public IPs; whitelist **all** of them
- See separate AWS guide for configuring Elastic IPs on NAT gateways

## Related Docs
- [Configuring Static Public IPs in AWS](#) (linked in source)
- Remote Networks configuration
- Groups and Resource access control
- Identity Provider integration