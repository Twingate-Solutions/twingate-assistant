# Twingate Site-to-Site Connections

## Summary
Configures bidirectional routing between two cloud networks (e.g., Azure and GCP) using Twingate Connectors and headless Twingate Clients acting as router VMs. Each site runs a Connector for inbound access and a headless Client VM with IP forwarding/iptables masquerading to route subnet traffic outbound through Twingate.

## Key Information
- Each site requires two VMs: one running the Connector, one running the headless Twingate Client (router VM)
- Headless Clients authenticate via Service Account keys (JSON)
- Router VMs need no public IP; use NAT gateway (Azure) or Cloud NAT (GCP) for internet access
- Peer-to-peer connections recommended to reduce bandwidth under Fair Use Policy
- Test VMs are added as Twingate Resources assigned to the opposing site's Service Account

## Prerequisites
- Twingate Admin Console access
- Two Remote Networks created (one per site)
- Two Connectors deployed (one per Remote Network)
- Two Service Accounts created with generated keys (stored securely)
- Cloud routing tables configured between subnets
- IP forwarding enabled on router VMs (GCP requires this at VM creation time)

## Step-by-Step

1. Create Remote Networks for each site in Admin Console
2. Deploy Connector tokens for each site; deploy Connector on Linux VM (no public IP)
3. Create two Service Accounts; generate and save JSON keys
4. On each router VM, install headless Client:
   ```bash
   curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
   nano /tmp/service_key.json        # paste service account key
   sudo twingate setup --headless /tmp/service_key.json
   sudo twingate start
   ```
5. Enable IP forwarding:
   ```bash
   sudo nano /etc/sysctl.conf        # uncomment net.ipv4.ip_forward=1
   sudo sysctl -p
   ```
6. Configure iptables (replace interface names as needed):
   ```bash
   sudo iptables -A FORWARD -i ens4 -o sdwan0 -j ACCEPT
   sudo iptables -A FORWARD -i sdwan0 -o ens4 -m state --state RELATED,ESTABLISHED -j ACCEPT
   sudo iptables -t nat -A POSTROUTING -o sdwan0 -j MASQUERADE
   sudo apt install iptables-persistent -y   # persist rules across reboots
   ```
7. Add test VMs as Resources; assign each to the opposing site's Service Account
8. Configure cloud routing tables to direct subnet traffic to the router VM

## Configuration Values
| Parameter | Value/Note |
|-----------|------------|
| Internal interface | `ens4` (Azure) / `eth0` (GCP) — verify per VM |
| Twingate virtual interface | `sdwan0` |
| Service key path | `/tmp/service_key.json` |
| sysctl forwarding key | `net.ipv4.ip_forward=1` |

## Gotchas
- GCP requires IP forwarding enabled **at VM creation**, not just via sysctl
- Azure Connector VM must have public IP disabled; configure NAT gateway before deploying
- Interface names (`ens4`, `eth0`, `sdwan0`) vary — verify before running iptables commands
- Cloud NAT must be active before router VM deployment or Twingate install will fail
- Service Account key is shown only once — save immediately on generation

## Related Docs
- [Headless/Service Accounts](https://www.twingate.com/docs/services)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)