# How to Cloak a Bastion Server

## Summary
Removes public internet exposure of a bastion server by routing all access through a Twingate Connector deployed on the same private subnet. Users retain their existing workflow (same hostname) while the bastion becomes inaccessible without Twingate authentication.

## Key Information
- Connector must be on the same private subnet as the bastion
- Deploy multiple Connectors for failover redundancy
- Users continue using the same DNS name throughout transition
- Final state: no public IP, no public DNS, firewall allows only Connector traffic

## Prerequisites
- Existing bastion server on a private subnet with a public DNS record
- Twingate admin console access
- Ability to modify firewall rules and DNS records for the bastion

## Step-by-Step

**1. Deploy Twingate Connector**
- Deploy Connector on same subnet as bastion (e.g., `10.1.0.50` on `10.1.0.0/24`)
- Add firewall ingress rule: allow traffic from Connector IP (`10.1.0.50`) to bastion public IP on port 22

**2. Add Bastion as Resource**
- Create Resource in admin console using the public DNS name (e.g., `bastion.beamreachinc.com`)
- Connector host must be able to resolve the bastion DNS name
- Create or assign a Group (e.g., "Bastion Access") and add authorized users

**3. Verify and Block Public Traffic**
- Confirm users can reach bastion via Twingate client
- Remove all ingress rules except the Connector allow rule
- Bastion is now inaccessible from public internet

**4. [Optional] Transition to Private DNS**
- Enable private DNS for the subnet (`10.1.0.0/24`)
- Create private DNS record: `bastion.beamreachinc.com` → `10.1.0.214`
- Delete public DNS record for `bastion.beamreachinc.com`
- Release the bastion's public IP assignment

## Configuration Values
| Parameter | Example Value |
|-----------|--------------|
| Private subnet | `10.1.0.0/24` |
| Bastion private IP | `10.1.0.214` |
| Connector IP | `10.1.0.50` |
| Bastion public DNS | `bastion.beamreachinc.com` |
| Firewall allow port | `22` |

## Gotchas
- During initial transition, users still use public DNS — firewall rules must account for routing via public IP until private DNS is switched
- Private DNS must be resolvable from the Connector host, not just the bastion
- Do not block public ingress before verifying Twingate connectivity works
- If deploying multiple Connectors for redundancy, add firewall allow rules for each Connector IP

## Related Docs
- [Create a new Remote network](https://www.twingate.com/docs/create-a-new-remote-network)
- [Create a new Resource](https://www.twingate.com/docs/create-a-new-resource)
- [Create a new Group](https://www.twingate.com/docs/create-a-new-group)