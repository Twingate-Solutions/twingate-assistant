# Cloak a Bastion Server with Twingate

## Summary
Remove a bastion server from public internet exposure by routing all access through a Twingate Connector on the same private subnet. Users retain their existing workflow (same DNS name, same SSH commands) while access becomes restricted to Twingate-authenticated users only.

## Key Information
- Connector must be on the **same private subnet** as the bastion
- Deploy multiple Connectors for failover redundancy
- Users experience zero workflow disruption throughout transition
- Private DNS transition is optional but strongly recommended

## Prerequisites
- Existing bastion server with public DNS and IP
- Twingate admin console access
- Ability to modify bastion firewall/security group rules
- Ability to manage DNS records

## Step-by-Step

### 1. Deploy Twingate Connector
- Deploy Connector on same subnet as bastion (`10.1.0.0/24`)
- Note the Connector's private IP (e.g., `10.1.0.50`)
- Add ingress allow rule on bastion: source = Connector IP, port = 22

### 2. Add Bastion as Resource
- Create Resource using the bastion's public DNS name (`bastion.beamreachinc.com`)
- DNS resolution of the resource name must be available from the Connector host
- Create or assign a Group (e.g., "Bastion Access")
- Add authorized users to the Group

### 3. Block Public Ingress
- Verify Twingate access works first
- Remove all public ingress rules **except** the Connector allow rule
- Bastion is now only reachable via Twingate

### 4. [Optional] Transition to Private DNS
1. Enable private DNS for the bastion's subnet
2. Create private DNS record: `bastion.beamreachinc.com` → `10.1.0.214`
3. Delete the public DNS record
4. Release the public IP from the bastion

## Configuration Values
| Item | Example Value |
|------|---------------|
| Private subnet | `10.1.0.0/24` |
| Bastion private IP | `10.1.0.214` |
| Connector IP | `10.1.0.50` |
| Bastion DNS | `bastion.beamreachinc.com` |
| Allowed port | `22` (SSH) |

## Gotchas
- **Firewall rules must account for routing**: Users still resolve public DNS during transition (before private DNS switch), so bastion's public IP interface needs the Connector allow rule
- **Order matters**: Verify Twingate connectivity *before* blocking public ingress
- **Connector DNS resolution**: The Connector host must be able to resolve the resource's DNS name
- **Multiple Connectors**: Apply the same firewall allow rules for each redundant Connector IP

## Related Docs
- [Create a new Remote Network](https://www.twingate.com/docs/create-a-remote-network)
- [Create a new Resource](https://www.twingate.com/docs/create-a-resource)
- [Create a new Group](https://www.twingate.com/docs/create-a-group)