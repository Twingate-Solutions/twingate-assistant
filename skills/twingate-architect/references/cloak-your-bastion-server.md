# How to Cloak a Bastion Server

## Summary
Removes public internet exposure of a bastion server by routing access exclusively through a Twingate Connector on the same private subnet. Users retain their existing workflow (same hostname) while the bastion becomes inaccessible from the public internet.

## Key Information
- Connector must be deployed on the **same private subnet** as the bastion
- Firewall rules restrict bastion ingress to Connector IP only (port 22)
- Users authenticate via Twingate client; workflow unchanged (same hostname)
- Optional but recommended: migrate from public to private DNS to eliminate all public traces

## Prerequisites
- Twingate admin console access
- Ability to modify bastion firewall/security group rules
- Ability to modify DNS records (public and optionally private)
- Bastion on a private subnet with a public DNS record resolving to a public IP

## Step-by-Step

### 1. Deploy Twingate Connector
- Deploy Connector on same private subnet as bastion (e.g., `10.1.0.50` on `10.1.0.0/24`)
- Recommend deploying multiple Connectors for failover redundancy
- Add ingress allow rule on bastion: permit traffic from Connector IP (`10.1.0.50`) on **port 22**

### 2. Designate Bastion as a Resource
- In admin console, create Resource using bastion's DNS name (e.g., `bastion.beamreachinc.com`)
- DNS for the resource name must resolve from the Connector host
- Create or assign a Group (e.g., "Bastion Access"), add the Resource and authorized users

### 3. Block Global Ingress Traffic
- Verify Twingate access works first
- Remove all public ingress rules **except** the Connector allow rule
- Bastion now only accepts connections originating from the Connector

### 4. [Optional] Transition to Private DNS
1. Enable private DNS for the bastion's subnet (`10.1.0.0/24`)
2. Create private DNS record: `bastion.beamreachinc.com` → `10.1.0.214`
3. Delete the public DNS record for `bastion.beamreachinc.com`
4. Release the bastion's public IP assignment

## Configuration Values
| Parameter | Example Value |
|-----------|---------------|
| Private subnet | `10.1.0.0/24` |
| Bastion private IP | `10.1.0.214` |
| Connector IP | `10.1.0.50` |
| Bastion hostname | `bastion.beamreachinc.com` |
| Allowed port | `22` (SSH) |

## Gotchas
- Verify Twingate connectivity **before** blocking public ingress—no rollback path once public access is removed
- If bastion has a public IP on its network interface, firewall rules must account for routing via public IP even when using public DNS
- Private DNS must be resolvable from the Connector host, not just end-user machines
- Apply Connector firewall allow rules to **all** redundant Connectors, not just one

## Related Docs
- [Create a new Remote Network](https://www.twingate.com/docs/create-a-remote-network)
- [Create a new Resource](https://www.twingate.com/docs/create-a-resource)
- [Create a new Group](https://www.twingate.com/docs/create-a-group)