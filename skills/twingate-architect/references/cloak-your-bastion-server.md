---
source: https://www.twingate.com/docs/cloak-your-bastion-server
type: docs
fetched: 2026-08-14
source_version: 05b87ca37ecf481dba8bfe8d28651aa7fadb2094516284806dfae1d364630a79
---

# How to Cloak a Bastion Server

## Summary
Step-by-step guide to hide a bastion server from public internet access using Twingate. Replaces public IP exposure with Connector-mediated access, requiring users to authenticate via Twingate client before connecting. Users experience no workflow change throughout the transition.

## Key Information
- Connector deployed on same private subnet as bastion handles all inbound traffic
- Firewall rules restrict bastion access to Connector IP only (port 22)
- Public DNS can be replaced with private DNS as final hardening step
- Deploy multiple Connectors on same subnet for failover redundancy

## Prerequisites
- Twingate admin console access
- Ability to modify bastion firewall/security group rules
- Ability to manage DNS records (public and optionally private)
- Twingate client deployed to end users

## Example Environment
| Component | Value |
|-----------|-------|
| Private subnet | `10.1.0.0/24` |
| Bastion private IP | `10.1.0.214` |
| Bastion public DNS | `bastion.beamreachinc.com` |
| Connector IP | `10.1.0.50` |
| SSH port | `22` |

## Step-by-Step

1. **Deploy Connector** on same private subnet as bastion (`10.1.0.0/24`)
2. **Add firewall allow rule** on bastion: permit inbound TCP port 22 from Connector IP (`10.1.0.50`)
3. **Create Resource** in admin console using bastion's DNS name (`bastion.beamreachinc.com`) — Connector must be able to resolve this name
4. **Create/assign Group** (e.g., "Bastion Access"), add bastion Resource and authorized users
5. **Verify connectivity** via Twingate client before proceeding
6. **Block all public ingress** to bastion except the Connector allow rule
7. *(Optional)* **Transition to private DNS:**
   - Enable private DNS on `10.1.0.0/24` subnet
   - Create private DNS record: `bastion.beamreachinc.com` → `10.1.0.214`
   - Delete public DNS record for `bastion.beamreachinc.com`
   - Release bastion's public IP assignment

## Gotchas
- During transition (before private DNS), traffic still routes via public DNS/IP — ensure firewall rules account for this routing path
- Connector must be able to resolve the Resource's DNS name; private DNS must be accessible from the Connector host
- Do not remove public ingress rules until Twingate connectivity is verified
- If deploying multiple Connectors for redundancy, add a firewall allow rule for each Connector IP

## Related Docs
- [Create a new Remote Network](https://www.twingate.com/docs/create-a-remote-network)
- [Create a new Resource](https://www.twingate.com/docs/create-a-resource)
- [Create a new Group](https://www.twingate.com/docs/create-a-group)