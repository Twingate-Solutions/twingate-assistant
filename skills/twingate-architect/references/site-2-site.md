# Twingate Site-to-Site Connections

## Summary
Configure bidirectional traffic routing between two cloud sites (e.g., Azure and GCP) using Twingate Connectors and headless Twingate Clients acting as router VMs. Each site requires a Connector (for inbound access), a headless Client VM (for outbound routing), and iptables NAT rules to forward subnet traffic through the Twingate tunnel.

## Key Information
- Each site needs: Remote Network, Connector, Service Account, headless Client VM, and test VM
- Router VMs require no public IP; use cloud NAT (Azure NAT Gateway / GCP Cloud NAT) for internet access
- Twingate Client creates a virtual interface `sdwan0` that traffic is masqueraded through
- Resources must be assigned to the opposing site's Service Account for cross-site access
- Peer-to-peer connections recommended to reduce bandwidth and stay within Fair Use Policy

## Prerequisites
- Twingate Admin Console access
- Two cloud environments (guide uses Azure + GCP)
- Linux VMs with internet access via NAT (no public IPs required)
- IP forwarding capability on router VMs (GCP requires enabling at VM creation time)

## Step-by-Step

### Twingate Admin Setup
1. Create two Remote Networks (one per site)
2. Create a Connector in each Remote Network; generate and save deployment tokens
3. Create two Service Accounts under **Team → Services**; generate and save keys as JSON

### Per-Site Deployment (repeat for each site)
1. Deploy Connector VM (no public IP), run generated install command via SSH or Run Command
2. Deploy router VM (no public IP), install headless Client:
```bash
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
nano /tmp/service_key.json          # paste service account key
sudo twingate setup --headless /tmp/service_key.json
sudo twingate start
```
3. Enable IP forwarding:
```bash
sudo nano /etc/sysctl.conf          # uncomment net.ipv4.ip_forward=1
sudo sysctl -p
```
4. Configure iptables (replace `ens4`/`eth0` with actual internal interface):
```bash
sudo iptables -A FORWARD -i ens4 -o sdwan0 -j ACCEPT
sudo iptables -A FORWARD -i sdwan0 -o ens4 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -t nat -A POSTROUTING -o sdwan0 -j MASQUERADE
sudo apt install iptables-persistent -y   # persist rules across reboots
```
5. Deploy test VM; add as Twingate Resource; assign to **opposing site's** Service Account

### Routing
- Azure: Create route table → associate with subnet → add route to remote CIDR via router VM
- GCP: Add VPC route pointing remote CIDR to router VM

## Configuration Values
| Parameter | Site 1 (Azure) | Site 2 (GCP) |
|---|---|---|
| Internal interface | `ens4` | `eth0` |
| Twingate interface | `sdwan0` | `sdwan0` |
| Example subnet | `10.0.1.0/24` | `172.16.1.0/24` |

## Gotchas
- GCP requires IP forwarding enabled **at VM creation time**, not just in sysctl
- Azure Connector deployment via portal uses ACS (separate vnet required); use plain Linux deployment instead
- Service Account key is only shown once—store securely before closing
- Cloud NAT must be configured **before** deploying router VM or it cannot install packages
- Internal interface names (`ens4`, `eth0`) vary by cloud/OS—verify before running iptables commands
- Without `iptables-persistent`, rules are lost on reboot

## Related Docs
- [Headless Client / Service Accounts](https://www.twingate.com/docs/services)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
- [Connector