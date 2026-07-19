# How to Cloak a Bastion Server

## Summary
Removes public internet exposure of a bastion server by routing access through a Twingate Connector on the same private subnet. Users retain their existing workflow (same hostname) while the bastion becomes inaccessible without Twingate authentication.

## Key Information
- Connector must be deployed on the **same private subnet** as the bastion
- Users continue using the same DNS name throughout transition (no workflow disruption)
- Final state: bastion has no public IP, no public DNS, only reachable via Twingate-authorized users

## Prerequisites
- Existing bastion server on a private subnet with a public DNS record
- Twingate admin console access
- Ability to modify firewall rules and DNS records for the bastion

## Step-by-Step

### 1. Deploy Twingate Connector
- Deploy Connector on the same private subnet as bastion (`10.1.0.0/24`)
- Recommended: deploy multiple Connectors for failover redundancy
- Note the Connector's private IP (e.g., `10.1.0.50`)

### 2. Update Bastion Firewall
- Add ingress **allow** rule on bastion's public IP interface: source = Connector IP (`10.1.0.50`), port = 22
- Ensure routing rules account for users still resolving the public DNS name at this stage

### 3. Add Bastion as Twingate Resource
- Create Resource using the public DNS name (`bastion.beamreachinc.com`)
- DNS resolution of this name must be available from the Connector host

### 4. Authorize Users
- Create or reuse a Group (e.g., "Bastion Access")
- Assign the bastion Resource to the Group
- Add authorized users to the Group

### 5. Verify Access via Twingate
- Confirm users can connect through Twingate before blocking public access

### 6. Block All Other Public Ingress
- Remove/disable all ingress rules **except** the Connector allow rule
- Bastion is now unreachable from public internet but still has public DNS

### 7. [Optional] Transition to Private DNS
- Enable private DNS for the `10.1.0.0/24` subnet
- Create private DNS record: `bastion.beamreachinc.com` → `10.1.0.214`
- Delete the public DNS record
- Release the bastion's public IP assignment

## Configuration Values
| Item | Example Value |
|------|--------------|
| Private subnet | `10.1.0.0/24` |
| Bastion private IP | `10.1.0.214` |
| Connector private IP | `10.1.0.50` |
| Resource definition | `bastion.beamreachinc.com` |
| Firewall allow port | `22` |

## Gotchas
- The Connector and bastion must be on the same subnet for private DNS to resolve correctly
- Routing rules must account for the public IP path during the transition period (before private DNS cutover)
- Do not block public ingress until Twingate access is verified working
- All redundant Connectors need the same firewall allow rule on the bastion

## Related Docs
- Create a new Remote Network
- Create a new Resource
- Create a new Group