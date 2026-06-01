# How to Cloak a Bastion Server

## Summary
Removes public internet exposure from a bastion server by routing all access through a Twingate Connector deployed on the same private subnet. Users retain the same workflow (same DNS name, same SSH commands) while the bastion becomes inaccessible without Twingate authentication.

## Key Information
- Connector is deployed on the same private subnet as the bastion
- Firewall rules restrict bastion ingress to Connector IP only
- Users authenticate via Twingate client before connecting
- Public DNS removal is optional but recommended for full cloaking

## Prerequisites
- Existing bastion server on a private subnet with a public DNS record
- Twingate admin console access
- Ability to modify firewall/security group rules for the bastion
- Ability to modify DNS records (public and private)

## Step-by-Step

### 1. Deploy Twingate Connector
- Deploy Connector on the **same private subnet** as the bastion (`10.1.0.0/24`)
- Recommend multiple Connectors for failover redundancy
- Note the Connector's private IP (e.g., `10.1.0.50`)

### 2. Add Firewall Allow Rule
- Add ingress allow rule on bastion's **public IP network interface**
- Source: Connector private IP (`10.1.0.50`)
- Port: `22`
- Account for routing since users still resolve to public IP at this stage

### 3. Add Bastion as Twingate Resource
- In admin console, create Resource using the public DNS name (e.g., `bastion.beamreachinc.com`)
- DNS resolution of the bastion name must work from the Connector host

### 4. Authorize Users
- Create or use existing Group (e.g., "Bastion Access")
- Add the bastion Resource to the Group
- Add authorized users to the Group

### 5. Verify Connectivity
- Confirm users can reach bastion via Twingate before proceeding

### 6. Block All Other Public Ingress
- Remove/deny all other ingress rules to the bastion
- Keep only the Connector allow rule from step 2

### 7. [Optional] Transition to Private DNS
1. Enable private DNS for the subnet (`10.1.0.0/24`)
2. Create private DNS record: `bastion.beamreachinc.com` → `10.1.0.214`
3. Delete the public DNS record for `bastion.beamreachinc.com`
4. Release the bastion's public IP assignment

## Configuration Values
| Parameter | Example Value |
|-----------|---------------|
| Private subnet | `10.1.0.0/24` |
| Bastion private IP | `10.1.0.214` |
| Connector private IP | `10.1.0.50` |
| Bastion DNS name | `bastion.beamreachinc.com` |
| SSH port | `22` |

## Gotchas
- Firewall rule must allow traffic from Connector to bastion's **public IP interface** until private DNS transition is complete
- DNS resolution of the bastion resource name must work **from the Connector host**, not just from users' machines
- Do not block public ingress until connectivity through Twingate is verified
- If deploying multiple Connectors for redundancy, add firewall allow rules for each Connector IP

## Related Docs
- [Create a new Remote network](https://www.twingate.com/docs)
- [Create a new Resource](https://www.twingate.com/docs)
- [Create a new Group](https://www.twingate.com/docs)