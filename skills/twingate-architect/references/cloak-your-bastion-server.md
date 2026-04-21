## Page Title
How to Cloak a Bastion Server

## Summary
Step-by-step guide to removing a bastion server from public internet exposure while maintaining seamless user access through Twingate. After cloaking, the bastion has no public IP or DNS record; only authorized Twingate users can reach it via the Connector.

## Key Information
- **End state**: bastion firewall allows SSH only from the Connector's private IP; public DNS and public IP are removed; users continue to access via the same FQDN via private DNS
- **No user workflow change**: users still `ssh user@bastion.example.com` -- Twingate transparently routes via the Connector
- **Connector placement**: Connector must be on the same private subnet as the bastion (or have L3 routing to it)

## Prerequisites
- Twingate Remote Network and at least one Connector deployed on the same subnet as the bastion
- Private DNS available or configurable for the bastion's subnet

## Step-by-Step
1. Deploy Connector on the same subnet as the bastion (e.g., `10.1.0.50` in subnet `10.1.0.0/24`)
2. Add firewall ingress rule on the bastion: allow TCP 22 from Connector IP only
3. Create a Twingate Resource for `bastion.example.com`; add to a Group; grant users access
4. Verify users can connect via Twingate (before removing public access)
5. Remove all public ingress rules on the bastion firewall -- only Connector ingress remains
6. (Recommended) Enable private DNS for the subnet, create private DNS A record pointing to bastion private IP, delete the public DNS record, release the bastion's public IP

## Configuration Values
- Resource address: bastion FQDN (e.g., `bastion.example.com`) or private IP
- Firewall rule: TCP/22 from Connector private IP only

## Gotchas
- Do not remove public ingress until you have verified Twingate access works -- removing prematurely locks out all access
- If deploying multiple Connectors for redundancy, the firewall rule must allow ingress from each Connector's IP
- Private DNS record must be resolvable from the Connector host (not just from user devices)

## Related Docs
- `/docs/bastion-replacement` -- case for replacing bastion entirely with Twingate
- `/docs/private-dns-best-practices` -- private DNS configuration
- `/docs/connector-placement-best-practices` -- Connector placement guidance
