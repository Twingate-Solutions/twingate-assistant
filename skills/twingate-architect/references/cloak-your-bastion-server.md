# How to Cloak a Bastion Server

## Summary
Step-by-step guide to remove a bastion server from public internet exposure while maintaining user workflow. Users continue connecting via the same hostname; Twingate handles authentication and network authorization. Traffic is restricted to originate only from Twingate Connectors.

## Key Information
- Bastion remains accessible via same DNS name throughout transition (no user workflow disruption)
- Connector must be deployed on the same private subnet as the bastion
- Deploy multiple Connectors for failover redundancy
- Final state: no public IP, no public DNS, only Connector-originated traffic allowed

## Prerequisites
- Existing bastion server on a private subnet with a public DNS record
- Twingate admin console access
- Ability to modify firewall rules and DNS records for the bastion
- Twingate Connector deployable on the same subnet as the bastion

## Step-by-Step

### 1. Deploy Twingate Connector
- Deploy Connector on the same private subnet as bastion (e.g., `10.1.0.0/24`)
- Note the Connector's private IP (e.g., `10.1.0.50`)
- Add firewall **ingress allow rule**: source `10.1.0.50`, destination bastion public IP interface, port `22`

### 2. Designate Bastion as a Resource
- In admin console, create Resource using the public DNS name (e.g., `bastion.beamreachinc.com`)
- DNS resolution of the bastion name must be available from the Connector host
- Create or assign a Group (e.g., "Bastion Access") and add authorized users

### 3. Block Global Ingress Traffic
- Verify user connectivity via Twingate first
- Remove all public ingress rules **except** the Connector allow rule
- Result: only traffic from Twingate Connector(s) can reach the bastion

### 4. [Optional] Transition to Private DNS (Recommended)
- Enable private DNS for the bastion's subnet (`10.1.0.0/24`)
- Create private DNS record: `bastion.beamreachinc.com` → `10.1.0.214` (private IP)
- Delete the public DNS record for `bastion.beamreachinc.com`
- Release the bastion's public IP assignment

## Configuration Values
| Parameter | Example Value |
|---|---|
| Private subnet | `10.1.0.0/24` |
| Bastion private IP | `10.1.0.214` |
| Connector private IP | `10.1.0.50` |
| Bastion public DNS | `bastion.beamreachinc.com` |
| SSH port (firewall rule) | `22` |

## Gotchas
- During the public DNS phase, routing/firewall rules must account for traffic resolving to the bastion's **public IP** (users still use public DNS name until private DNS is configured)
- Connector must have DNS resolution access to the bastion's hostname when defining the Resource
- Do not block public ingress until Twingate connectivity is verified
- All redundant Connectors need the same firewall allow rule added

## Related Docs
- [Create a new Remote Network](https://www.twingate.com/docs/create-a-remote-network)
- [Create a new Resource](https://www.twingate.com/docs/create-a-resource)
- [Create a new Group](https://www.twingate.com/docs/create-a-group)