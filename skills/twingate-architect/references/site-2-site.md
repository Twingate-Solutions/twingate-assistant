# Secure Site-to-Site Connections with Twingate

## Summary
Configures bidirectional traffic routing between two cloud sites (Azure and GCP) using Twingate Connectors and headless Twingate Clients acting as router VMs. Each site deploys a Connector for inbound access and a headless Client VM with iptables NAT rules to forward outbound traffic to the remote site.

## Key Information
- Architecture: Each site needs both a **Connector** (receives traffic) and a **headless Client VM** (routes traffic out)
- Service Accounts authenticate the headless Clients — not user accounts
- Router VMs require no public IP; use NAT gateway (Azure) or Cloud NAT (GCP) for internet access
- Twingate Resources are cross-assigned: site 1's test VM assigned to site 2's Service Account, and vice versa
- Enable peer-to-peer connections to stay within Fair Use Policy bandwidth limits

## Prerequisites
- Twingate Admin Console access
- Azure: Resource group, VNet, NAT gateway, subnet
- GCP: VPC, subnet, Cloud NAT configured before VM deployment
- Two Remote Networks created in Admin Console (one per site)
- Two Service Accounts created in Admin Console (one per site)

## Step-by-Step

### Per Site (repeat for both):
1. Create Remote Network in Admin Console → deploy Connector token
2. Deploy Connector on Linux VM (no public IP), paste generated install command
3. Create Service Account → generate and save key as `/tmp/service_key.json`
4. Deploy router Linux VM (no public IP), install headless Client:
```bash
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
sudo twingate setup --headless /tmp/service_key.json
sudo twingate start
```
5. Enable IP forwarding:
```bash
sudo nano /etc/sysctl.conf  # uncomment net.ipv4.ip_forward=1
sudo sysctl -p
```
6. Configure iptables (replace interface names as needed):
```bash
sudo iptables -A FORWARD -i ens4 -o sdwan0 -j ACCEPT
sudo iptables -A FORWARD -i sdwan0 -o ens4 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -t nat -A POSTROUTING -o sdwan0 -j MASQUERADE
sudo apt install iptables-persistent -y
```
7. Deploy test VM → add as Twingate Resource → assign to **opposite site's** Service Account
8. Configure cloud routing tables to direct subnet traffic to router VM's private IP

## Configuration Values
| Parameter | Site 1 (Azure) | Site 2 (GCP) |
|-----------|---------------|--------------|
| Internal interface | `ens4` | `eth0` |
| Twingate interface | `sdwan0` | `sdwan0` |
| Example subnet | `10.0.1.0/24` | `172.16.1.0/24` |

## Gotchas
- **GCP only**: Enable IP forwarding at VM creation time (not just in sysctl)
- Cloud NAT must be configured **before** deploying the router VM in GCP, or it can't install packages
- Interface names (`ens4`, `eth0`, `sdwan0`) vary — verify with `ip link` before running iptables commands
- Without `iptables-persistent`, NAT rules reset on reboot
- If no SSH access to a VM, add its private IP as a Twingate Resource first to gain access

## Related Docs
- [Headless Client / Service Accounts](https://www.twingate.com/docs/services)
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)