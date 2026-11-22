---
source: https://www.twingate.com/docs/site-2-site
type: docs
fetched: 2026-11-22
source_version: b95b5b0873cf564a0f6a86ae9ed4b1b3937bed479e1c85b8d93fb250dc5a1b19
trust: official
---

# Page Title
How to Secure Site-to-Site Connections with Twingate (https://www.twingate.com/docs/site-2-site)

## Summary
This guide shows how to route traffic between two sites (example: Azure and GCP) using Twingate. A Twingate Client in headless mode on a router VM in each site forwards traffic for the remote subnet to a Twingate Connector in the other site. Service Accounts authenticate the headless Clients.

## Key Information
- Each site needs: a Remote Network, a Connector, a Service Account, and a router VM running the headless Client.
- Test VMs in each site are added as Twingate Resources. Each Resource is assigned to the *other* site's Service Account (site 1 Resource → site 2 Service Account, and vice versa).
- Example subnets: site 1 (Azure) 10.0.1.0/24, site 2 (GCP) 172.16.1.0/24.
- Connector and router VMs need no public IP. Outbound internet access is via a NAT gateway (Azure) or Cloud NAT (GCP).
- Routing must be configured independently on each side (Azure route table, GCP route).
- Peer-to-peer connections help with user experience and Fair Use Policy bandwidth limits.

## Prerequisites
- Twingate Admin Console access
- Azure and GCP accounts (or equivalent two sites)
- Linux VMs for Connector and router in each site
- Two Service Accounts, with keys saved securely
- Connector deploy commands (with tokens) generated in the Admin Console

## Step-by-Step
1. In the Admin Console, create a Remote Network per site.
2. Deploy a Connector per site (choose Linux, generate tokens, copy the command). Run it on a Linux VM, via SSH or the VM's Run command option.
3. Create Service Accounts under Team → Services → Add Service. Save each key.
4. Create the network components (Azure: resource group, vnet, NAT gateway, subnet; GCP: VPC, subnet, Cloud NAT). Set up NAT before deploying the Connector.
5. Deploy a router VM per site with IP forwarding enabled. On GCP, enable it at VM creation.
6. Install the headless Client on the router VM using the Linux install script from binaries.twingate.com (see the source page for the exact command).
7. Save the service key to `/tmp/service_key.json`, then run `sudo twingate setup --headless /tmp/service_key.json` and `sudo twingate start`. Status should report `online`.
8. On Linux, uncomment `net.ipv4.ip_forward=1` in `/etc/sysctl.conf` and run `sudo sysctl -p`.
9. Add the iptables rules (below).
10. Optionally install `iptables-persistent` to keep the rules across reboots.
11. Add routes so the remote subnet goes via the router VM (Azure route table associated with the subnet; GCP route).
12. Test with `ping` between test VMs in both directions.

## Configuration Values
```
sudo iptables -A FORWARD -i <internal_if> -o sdwan0 -j ACCEPT
sudo iptables -A FORWARD -i sdwan0 -o <internal_if> -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -t nat -A POSTROUTING -o sdwan0 -j MASQUERADE
```
- `<internal_if>`: `ens4` in the Azure example, `eth0` in the GCP example. Replace with your own interface name.
- `sdwan0`: virtual interface created by the Twingate Client.
- `net.ipv4.ip_forward=1`: in `/etc/sysctl.conf`.

## Gotchas
- Interface names differ per VM, so verify them before running the iptables commands.
- IP forwarding must be enabled on the VM itself (GCP: at creation time) as well as in sysctl.
- Without NAT in place, the Connector cannot install on VMs without public IPs.
- Azure Connector uses a plain Linux VM rather than the Azure deployment option, because the ACS approach requires its own vnet.
- Without remote access to the router VM, add its private IP as a Twingate Resource to reach it.
- Service Account keys are shown only at generation, so store them securely.
- Routing and firewall needs vary. The example routes entire subnets both ways.

## Related Docs
- Peer-to-peer connections (https://www.twingate.com/docs/peer-to-peer-communication-in-twingate)
- Supporting peer-to-peer connections (https://www.twingate.com/docs/troubleshooting-p2p)
- Fair Use Policy (https://www.twingate.com/terms/sa)