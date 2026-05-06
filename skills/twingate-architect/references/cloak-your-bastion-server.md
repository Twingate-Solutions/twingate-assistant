# How to Cloak a Bastion Server

## Summary
Removes public internet exposure from a bastion server by routing all access through a Twingate Connector deployed on the same private subnet. Users retain their existing workflow (same DNS name, same SSH commands) while the bastion becomes inaccessible without Twingate authentication.

## Key Information
- Connector must be on the same private subnet as the bastion
- Deploy multiple Connectors for failover redundancy
- Users experience zero workflow disruption throughout transition
- Private DNS transition is optional but recommended to eliminate all public traces

## Prerequisites
- Existing bastion server on a private subnet with a public DNS record
- Twingate admin console access
- Ability to modify firewall rules and DNS records for the bastion

## Step-by-Step

**1. Deploy Twingate Connector**
- Deploy Connector on same private subnet as bastion (e.g., `10.1.0.50` on `10.1.0.0/24`)
- Add firewall ingress rule on bastion's public IP interface: allow traffic from Connector IP (`10.1.0.50`) on port 22

**2. Designate Bastion as Resource**
- Create Resource in Twingate admin console using the public DNS name (e.g., `bastion.beamreachinc.com`)
- DNS resolution of the bastion name must be available from the Connector host
- Create or assign a Group (e.g., "Bastion Access") and add authorized users

**3. Block Global Ingress Traffic**
- Verify Twingate access works first
- Remove all public ingress rules except the Connector allow rule
- Bastion is now only reachable via Twingate-authorized connections

**4. [Optional] Transition to Private DNS**
- Enable private DNS for the subnet (`10.1.0.0/24`)
- Create private DNS record: `bastion.beamreachinc.com` → `10.1.0.214`
- Delete the public DNS record
- Release the public IP assignment from the bastion

## Configuration Values
| Parameter | Example Value |
|-----------|---------------|
| Private subnet | `10.1.0.0/24` |
| Bastion private IP | `10.1.0.214` |
| Connector IP | `10.1.0.50` |
| Bastion DNS | `bastion.beamreachinc.com` |
| Allowed port | `22` (SSH) |

## Gotchas
- **Firewall routing**: While users still use the public DNS name, ensure firewall rules account for traffic resolving to the public IP—don't block this before private DNS is configured
- **DNS resolution from Connector**: The Connector host must be able to resolve the bastion's DNS name; verify before completing setup
- **Order matters**: Verify Twingate connectivity *before* blocking public ingress traffic

## Related Docs
- Create a new Remote Network
- Create a new Resource
- Create a new Group