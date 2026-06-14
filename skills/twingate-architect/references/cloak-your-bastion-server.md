# How to Cloak a Bastion Server

## Summary
Removes public internet exposure from a bastion server by routing all access through a Twingate Connector deployed on the same private subnet. Users retain the same workflow (same DNS name, same SSH commands) while the bastion becomes inaccessible without Twingate authentication.

## Key Information
- Connector is deployed on the same private subnet as the bastion
- Firewall rules are updated to allow traffic only from the Connector's private IP
- Optional but recommended: transition from public DNS to private DNS to eliminate all public traces

## Prerequisites
- Existing bastion server with a public DNS record and public IP
- Access to firewall/security group configuration for the bastion
- Twingate admin console access
- Ability to manage DNS records (public and private)

## Step-by-Step

1. **Deploy Connector** on the same private subnet as the bastion (`10.1.0.0/24`). Deploy multiple Connectors for failover redundancy.

2. **Add firewall rule** on the bastion's public IP interface: allow ingress from Connector IP (`10.1.0.50`) on port 22.

3. **Create Resource** in Twingate admin console using the bastion's DNS name (`bastion.beamreachinc.com`). The Connector host must be able to resolve this DNS name.

4. **Create/assign Group** (e.g., "Bastion Access"), add the bastion Resource to it, and add authorized users.

5. **Verify connectivity** through Twingate before proceeding.

6. **Block all public ingress** to the bastion except the Connector allow rule.

7. **[Optional] Transition to private DNS:**
   - Enable private DNS for the subnet
   - Create private DNS record: `bastion.beamreachinc.com` → `10.1.0.214`
   - Delete the public DNS record
   - Release the public IP from the bastion

## Configuration Values
| Item | Example Value |
|------|--------------|
| Private subnet | `10.1.0.0/24` |
| Bastion private IP | `10.1.0.214` |
| Connector IP | `10.1.0.50` |
| Bastion DNS | `bastion.beamreachinc.com` |
| Allowed port | `22` (SSH) |

## Gotchas
- During the public DNS phase, firewall rules must account for the bastion resolving to its public IP — the Connector allow rule must target the public interface, not just the private IP
- Do not block public ingress until after verifying Twingate connectivity works
- Private DNS must be resolvable from the Connector host for the Resource to function
- All redundant Connectors need the same firewall allow rules on the bastion

## Related Docs
- [Create a new Remote Network](https://www.twingate.com/docs/create-a-remote-network)
- [Create a new Resource](https://www.twingate.com/docs/create-a-resource)
- [Create a new Group](https://www.twingate.com/docs/create-a-group)