# Twingate Site-to-Site Connections

## Summary
Configures bidirectional traffic routing between two network sites (e.g., Azure and GCP) using Twingate Connectors and headless Twingate Clients acting as router VMs. Each site runs a Connector for inbound access and a headless Client VM that forwards traffic via iptables/NAT to the remote site's subnet.

## Key Information
- Each site requires: one Connector, one headless Client (router VM), one Service Account
- Router VM uses `iptables` + IP forwarding to NAT traffic through the `sdwan0` Twingate interface
- Resources (test VMs) are assigned to the **opposite** site's Service Account to enable cross-site access
- Enable peer-to-peer connections to reduce bandwidth and stay within Fair Use Policy

## Prerequisites
- Twingate Admin Console access
- Two Remote Networks created (one per site)
- Linux VMs with no public IPs (use NAT gateway/Cloud NAT for internet access)
- SSH or VM run-command access for deployment

## Step-by-Step

### Twingate Admin Console
1. Create two Remote Networks (site 1, site 2)
2. Generate Connector tokens for each Remote Network (Linux deployment)
3. Create two Service Accounts under **Team → Services**; save keys securely

### Each Site (repeat for both)
1. Deploy Connector VM → paste generated connector command
2. Deploy router VM → install headless Twingate Client:
```bash
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
nano /tmp/service_key.json          # paste Service Account key
sudo twingate setup --headless /tmp/service_key.json
sudo twingate start
```
3. Enable IP forwarding:
```bash
sudo nano /etc/sysctl.conf          # uncomment net.ipv4.ip_forward=1
sudo sysctl -p
```
4. Configure iptables (replace `ens4`/`eth0` and `sdwan0` with actual interface names):
```bash
sudo iptables -A FORWARD -i ens4 -o sdwan0 -j ACCEPT
sudo iptables -A FORWARD -i sdwan0 -o ens4 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -t nat -A POSTROUTING -o sdwan0 -j MASQUERADE
sudo apt install iptables-persistent -y   # persist rules across reboots
```
5. Add test VM as a Resource; assign to **opposite** site's Service Account
6. Configure cloud routing tables to direct subnet traffic to the router VM's private IP

## Configuration Values
| Parameter | Example Value |
|---|---|
| Azure subnet | `10.0.1.0/24` |
| GCP subnet | `172.16.1.0/24` |
| Twingate virtual interface | `sdwan0` |
| Azure internal interface | `ens4` |
| GCP internal interface | `eth0` |
| Service key file | `/tmp/service_key.json` |

## Gotchas
- **GCP only**: Enable IP forwarding at VM creation time (not just in sysctl)
- Connector VM must have no public IP; configure Cloud NAT/Azure NAT Gateway **before** deploying router VM
- Interface names (`ens4`, `eth0`, `sdwan0`) vary by environment — verify before running iptables commands
- Each site's Resource is assigned to the *other* site's Service Account (not its own)
- Cloud routing tables must be configured independently on each side for bidirectional routing

## Related Docs
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Headless Client deployment](https://www.twingate.com/docs/linux-headless)
- [Service Accounts](https://www.twingate.com/docs/service-accounts)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)