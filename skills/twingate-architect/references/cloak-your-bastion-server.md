# How to Cloak a Bastion Server

## Summary
Removes public internet exposure of a bastion server by routing access through a Twingate Connector deployed on the same private subnet. Users retain the same SSH workflow while firewall rules restrict ingress to only the Connector's private IP. Optionally eliminates all public DNS/IP traces.

## Key Information
- Connector deployed on same private subnet as bastion handles all authorized traffic
- Users experience no workflow change (same hostname, same SSH commands)
- Process is staged to allow verification before blocking public access
- Multiple Connectors recommended for failover redundancy

## Prerequisites
- Existing bastion server with public DNS record and public IP
- Ability to modify bastion firewall/security group rules
- Twingate admin console access
- Ability to manage DNS records (public and optionally private)

## Step-by-Step

### 1. Deploy Twingate Connector
- Deploy Connector on same private subnet as bastion (`10.1.0.0/24`)
- Note the Connector's private IP (e.g., `10.1.0.50`)
- Add firewall **ingress allow rule** on bastion's public IP interface: source = Connector IP, port = 22

### 2. Add Bastion as Resource and Authorize Users
- Create Resource in Twingate admin console using the public DNS name (`bastion.beamreachinc.com`)
- DNS for the bastion hostname must resolve from the Connector host
- Create or reuse a Group (e.g., "Bastion Access"), add the Resource and authorized users

### 3. Verify and Block Public Ingress
- Confirm users can connect via Twingate before blocking
- Remove all bastion ingress rules **except** the allow rule for the Connector IP(s)

### 4. [Optional] Transition to Private DNS
1. Enable private DNS for the bastion's subnet
2. Create private DNS record: `bastion.beamreachinc.com` → `10.1.0.214`
3. Delete the public DNS record for `bastion.beamreachinc.com`
4. Release the bastion's public IP assignment

## Configuration Values
| Parameter | Example Value |
|-----------|--------------|
| Private subnet | `10.1.0.0/24` |
| Bastion private IP | `10.1.0.214` |
| Connector private IP | `10.1.0.50` |
| Bastion public DNS | `bastion.beamreachinc.com` |
| Allowed ingress port | `22` |

## Gotchas
- Firewall allow rule must target the bastion's **public IP interface** (not private) until private DNS transition is complete — routing must account for public DNS still resolving to public IP during transition
- If deploying multiple Connectors, add a separate firewall allow rule for **each** Connector IP
- Private DNS must be resolvable from the Connector host for the Resource definition to work

## Related Docs
- [Create a new Remote Network](https://www.twingate.com/docs/create-a-remote-network)
- [Create a new Resource](https://www.twingate.com/docs/create-a-resource)
- [Create a new Group](https://www.twingate.com/docs/create-a-group)