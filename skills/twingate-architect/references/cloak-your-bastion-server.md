# How to Cloak a Bastion Server

## Summary
Removes public internet exposure of a bastion server by routing all access through a Twingate Connector on the same private subnet. Users retain the same workflow (same DNS name, same SSH commands) while the bastion becomes inaccessible without Twingate authentication.

## Key Information
- Connector must be deployed on the **same private subnet** as the bastion
- Deploy multiple Connectors for failover redundancy
- Users experience zero workflow disruption throughout migration
- Private DNS transition is optional but strongly recommended

## Prerequisites
- Existing bastion server on a private subnet with a public DNS record
- Twingate admin console access
- Ability to modify firewall/security group rules for the bastion
- Ability to manage DNS records (public and optionally private)

## Step-by-Step

### 1. Deploy Twingate Connector
- Deploy Connector on same private subnet as bastion (e.g., `10.1.0.0/24`)
- Note the Connector's private IP (e.g., `10.1.0.50`)
- Repeat all steps for each redundant Connector

### 2. Update Bastion Firewall (Initial)
- Add ingress **allow** rule: traffic from Connector IP (`10.1.0.50`) on port `22`
- Keep existing public ingress rules active during testing

### 3. Create Resource and Authorize Users
- In admin console, create Resource using the bastion's DNS name (e.g., `bastion.beamreachinc.com`)
- DNS resolution of the resource name must work from the Connector host
- Create or reuse a Group (e.g., "Bastion Access"), attach the Resource, add authorized users

### 4. Verify Access via Twingate
- Confirm users can SSH to bastion through Twingate client before blocking public access

### 5. Block Public Ingress
- Remove all bastion firewall ingress rules **except** the Connector allow rule
- Bastion is now only reachable via Twingate-authorized connections

### 6. [Optional] Transition to Private DNS
1. Enable private DNS for the subnet (`10.1.0.0/24`)
2. Create private DNS record: `bastion.beamreachinc.com` → `10.1.0.214`
3. Delete the public DNS record for `bastion.beamreachinc.com`
4. Release the bastion's public IP assignment

## Configuration Values
| Item | Example Value |
|------|--------------|
| Private subnet | `10.1.0.0/24` |
| Bastion private IP | `10.1.0.214` |
| Connector private IP | `10.1.0.50` |
| Bastion DNS name | `bastion.beamreachinc.com` |
| Allowed port | `22` (SSH) |

## Gotchas
- Firewall rules must account for routing when bastion still has a public IP (traffic hits public IP, must route correctly to allow Connector's private IP)
- DNS resolution of the Resource name must be available **from the Connector host**, not just from clients
- Do not block public ingress until Twingate access is verified working
- Private DNS must cover the full subnet where both Connector and bastion reside

## Related Docs
- Create a new Remote Network
- Create a new Resource
- Create a new Group