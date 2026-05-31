# Best Practices for Whitelisting Traffic to Public Resources

## Summary
Twingate replaces IP whitelisting for public resources by routing authorized user traffic through Connectors with static IPs. Admins whitelist Connector IPs at the resource/SaaS level and control user access via Twingate Groups, eliminating per-user IP management.

## Key Information
- Solves IP whitelisting pain points: dynamic user IPs, location changes, overly broad shared IPs, large IP list maintenance
- Traffic to public resources is routed through Twingate Connectors with known static IPs
- Access control enforced at two layers: network (Connector IPs) + identity (Twingate Groups + IdP)
- Users can access from any location without admin IP updates

## Prerequisites
- Twingate Admin Console access
- Connectors deployed in cloud infrastructure (AWS, GCP, Azure, etc.)
- Static public IP assigned to Connector's NAT gateway in your cloud provider
- Target public resource or SaaS app must support source IP whitelisting

## Step-by-Step

1. **Assign static IPs to Connectors**
   - Provision static public IPs via your cloud provider (e.g., AWS Elastic IP on NAT gateway)
   - Ensure Connector egress traffic routes through the static IP

2. **Create a Remote Network**
   - Define a Remote Network in Twingate Admin Console
   - Assign Connectors with static IPs to this Remote Network

3. **Whitelist Connector IPs at the resource**
   - Add the static public IP(s) of the Connector's NAT gateway to the target resource's IP allowlist

4. **Create a Twingate Resource**
   - Add the public resource (URL/hostname) as a Resource in Twingate
   - Associate it with the Remote Network from step 2

5. **Create a Group and assign users**
   - Create a Group in Twingate Admin Console
   - Add authorized users to the Group
   - Grant the Group access to the Resource

## Configuration Values
| Item | Details |
|------|---------|
| Remote Network | Maps to deployment where static-IP Connectors live |
| Resource address | Public hostname/IP of the target service |
| Static IP source | NAT gateway public IP (cloud-provider-assigned) |

## Gotchas
- The static IP is typically the **NAT gateway IP**, not the Connector instance IP directly—verify egress path in your cloud setup
- Multiple Connectors in a Remote Network may have different egress IPs; whitelist all of them
- Users must be **both** connected to Twingate **and** in an authorized Group—neither condition alone grants access
- If Connectors are redeployed or NAT gateways change, whitelisted IPs must be updated at the resource

## Related Docs
- [Configuring static public IPs in AWS](https://www.twingate.com/docs) (referenced in page)
- Remote Networks configuration
- Resources configuration
- Groups and access control
- Identity Provider integration