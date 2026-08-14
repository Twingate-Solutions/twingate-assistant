---
source: https://www.twingate.com/docs/site-2-site
type: docs
fetched: 2026-08-14
source_version: 8f041cd36a4a6030530257594e5d72f57d948a9fbbbb434ae7438ad399fc957a
---

# Twingate Site-to-Site Connections

## Summary
Configures bidirectional traffic routing between two cloud sites (Azure and GCP) using Twingate Connectors and headless Twingate Clients acting as software routers. Each site requires a Connector for Twingate network presence and a separate "router VM" running the headless Client with iptables NAT rules. Traffic is routed through the `sdwan0` virtual interface created by the Twingate Client.

## Key Information
- Each site needs two VMs: one Connector VM, one router VM (headless Client)
- Headless Client authenticated via Service Account key (JSON file)
- Router VM uses iptables MASQUERADE on `sdwan0` interface to NAT traffic into Twingate
- Cloud routing tables must be configured to direct subnet traffic to the router VM
- Peer-to-peer connections recommended to reduce bandwidth and stay within Fair Use Policy
- Test VMs are added as Twingate Resources and assigned to the opposing site's Service Account

## Prerequisites
- Twingate Admin Console access
- Two Remote Networks created (one per site)
- One Connector deployed per site
- Two Service Accounts created (one per site)
- IP forwarding enabled on router VMs
- Cloud NAT configured so private VMs can reach the internet (required before Connector install)
- No public IPs required on Connector or router VMs

## Step-by-Step

### Per-Site Setup (repeat for each site)
1. Create Remote Network in Admin Console
2. Generate Connector token in Admin Console → Deploy Connector (Linux VM, no public IP, uses Cloud NAT)
3. Create Service Account → generate and save JSON key
4. Deploy router VM (Linux, no public IP)
5. Install headless Client:
   ```bash
   curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
   nano /tmp/service_key.json        # paste Service Account key
   sudo twingate setup --headless /tmp/service_key.json
   sudo twingate start
   ```
6. Enable IP forwarding:
   ```bash
   sudo nano /etc/sysctl.conf        # uncomment net.ipv4.ip_forward=1
   sudo sysctl -p
   ```
7. Configure iptables (replace `ens4`/`eth0` with local internal interface):
   ```bash
   sudo iptables -A FORWARD -i ens4 -o sdwan0 -j ACCEPT
   sudo iptables -A FORWARD -i sdwan0 -o ens4 -m state --state RELATED,ESTABLISHED -j ACCEPT
   sudo iptables -t nat -A POSTROUTING -o sdwan0 -j MASQUERADE
   sudo apt install iptables-persistent -y   # persist rules across reboots
   ```
8. Add test VM as Twingate Resource → assign to **opposite site's** Service Account
9. Add cloud routing table entry pointing remote subnet to router VM's private IP

## Configuration Values
| Item | Site 1 (Azure) | Site 2 (GCP) |
|------|---------------|--------------|
| Example subnet | `10.0.1.0/24` | `172.16.1.0/24` |
| Internal interface | `ens4` | `eth0` |
| Twingate interface | `sdwan0` | `sdwan0` |
| Service key path | `/tmp/service_key.json` | `/tmp/service_key.json` |

## Gotchas
- Interface names (`ens4`, `eth0`) vary by VM/cloud — verify before running iptables commands
- GCP requires IP forwarding enabled at VM creation time (not just in OS)
- Cloud NAT must be configured **before** deploying router VM or it cannot download Client
- Resource must be assigned to the **other** site's Service Account (cross-assignment enables routing)
- iptables rules are lost on reboot without `iptables-persistent`
- Connector VM should have no public IP; use "Run command" in Azure portal if no SSH access

## Related Docs
- [Headless Client / Service Accounts](https://www.twingate.com/docs/services)
- [Peer-to-Peer Connections](https://www.t