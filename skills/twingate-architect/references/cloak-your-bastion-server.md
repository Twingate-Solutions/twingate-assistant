# How to Cloak a Bastion Server

## Summary
Removes public internet exposure of a bastion server by routing all access through a Twingate Connector on the same private subnet. Users retain the same workflow (same hostname) while firewall rules restrict ingress to Connector traffic only.

## Key Information
- Connector deployed on same private subnet as bastion
- Firewall modified to allow only Connector IP on port 22
- Public DNS optionally replaced with private DNS (recommended)
- Zero workflow disruption for end users throughout transition

## Prerequisites
- Existing bastion server with public DNS and IP
- Twingate admin console access
- Ability to modify bastion firewall/security group rules
- Ability to manage DNS records (public and private)

## Step-by-Step

**1. Deploy Twingate Connector**
- Deploy Connector on same private subnet as bastion (`10.1.0.0/24`)
- Deploy multiple Connectors for failover redundancy
- Add firewall ingress rule: allow Connector IP (`10.1.0.50`) → bastion port 22

**2. Add Bastion as Resource**
- Create Resource in Twingate admin console using bastion's DNS name (`bastion.beamreachinc.com`)
- DNS name must be resolvable from the Connector host
- Assign Resource to a Group; add authorized users to that Group

**3. Verify Access via Twingate**
- Confirm users can connect through Twingate client before blocking public access

**4. Block Public Ingress**
- Remove all public ingress firewall rules except the Connector allow rule
- Only Twingate-authorized users can now initiate connections

**5. [Optional] Transition to Private DNS**
- Enable private DNS for the subnet (`10.1.0.0/24`)
- Create private DNS record: `bastion.beamreachinc.com` → `10.1.0.214`
- Delete public DNS record for `bastion.beamreachinc.com`
- Release the bastion's public IP assignment

## Configuration Values (Example)
| Parameter | Value |
|-----------|-------|
| Private subnet | `10.1.0.0/24` |
| Bastion private IP | `10.1.0.214` |
| Connector IP | `10.1.0.50` |
| Bastion hostname | `bastion.beamreachinc.com` |
| Allowed port | `22` (SSH) |

## Gotchas
- During transition (before private DNS), bastion's public DNS still resolves to public IP — ensure routing/firewall rules account for this
- Do not block public ingress until Twingate access is verified working
- Private DNS must be resolvable from the Connector host for the Resource to function
- All redundant Connectors need identical firewall allow rules on the bastion

## Related Docs
- [Create a new Remote Network](https://www.twingate.com/docs)
- [Create a new Resource](https://www.twingate.com/docs)
- [Create a new Group](https://www.twingate.com/docs)