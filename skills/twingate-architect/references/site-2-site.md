# Twingate Site-to-Site Connections

## Summary
Configures bidirectional traffic routing between two network sites (e.g., Azure and GCP) using Twingate Connectors and headless Twingate Clients acting as routers. Each site deploys a Connector for inbound access and a headless Client VM with IP forwarding/iptables for outbound routing. Resources are assigned to Service Accounts cross-site to enable bidirectional access.

## Key Information
- Each site requires: one Connector VM, one headless Client "router" VM, and optionally a test VM
- Headless Client uses Service Account key authentication (not user auth)
- Router VM uses `iptables` + IP forwarding to forward subnet traffic through Twingate (`sdwan0` interface)
- No public IPs needed on any VMs; use NAT gateway (Azure) or Cloud NAT (GCP) for internet access
- Peer-to-peer connections recommended to reduce bandwidth and comply with Fair Use Policy

## Prerequisites
- Twingate Admin Console access
- Two Remote Networks created (one per site)
- Two Service Accounts created (one per site, cross-assigned)
- Linux VMs with internet access via NAT in each site
- Cloud routing tables configured (Azure route table, GCP route)

## Step-by-Step

1. **Admin Console**: Create two Remote Networks, two Connectors (get deploy tokens), two Service Accounts (save keys)
2. **Each site**: Deploy Connector on Linux VM (no public IP), run generated deploy command
3. **Each site**: Deploy router VM (no public IP), install headless Twingate Client:
   ```bash
   curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
   nano /tmp/service_key.json   # paste service account key
   sudo twingate setup --headless /tmp/service_key.json
   sudo twingate start
   ```
4. **Enable IP forwarding** on router VM:
   ```bash
   sudo nano /etc/sysctl.conf   # uncomment net.ipv4.ip_forward=1
   sudo sysctl -p
   ```
5. **Configure iptables** (replace `ens4`/`eth0` and `sdwan0` with actual interface names):
   ```bash
   sudo iptables -A FORWARD -i ens4 -o sdwan0 -j ACCEPT
   sudo iptables -A FORWARD -i sdwan0 -o ens4 -m state --state RELATED,ESTABLISHED -j ACCEPT
   sudo iptables -t nat -A POSTROUTING -o sdwan0 -j MASQUERADE
   sudo apt install iptables-persistent -y   # optional: persist rules
   ```
6. **Add test VMs as Resources** in each site's Remote Network; assign to the *opposite* site's Service Account
7. **Configure cloud routing**: Azure route table + GCP route pointing subnets to router VM's private IP

## Configuration Values
| Parameter | Example Value |
|-----------|---------------|
| Site 1 subnet (Azure) | `10.0.1.0/24` |
| Site 2 subnet (GCP) | `172.16.1.0/24` |
| Twingate virtual interface | `sdwan0` |
| Azure internal interface | `ens4` |
| GCP internal interface | `eth0` |

## Gotchas
- GCP requires IP forwarding enabled **at VM creation time** (not just via sysctl)
- Cloud NAT must be configured **before** deploying router VM (needed to pull Twingate installer)
- Interface names (`ens4`, `eth0`, `sdwan0`) vary—verify with `ip a` before running iptables commands
- Service Account keys shown only once at creation—store immediately
- Each Resource must be assigned to the **other** site's Service Account (cross-assignment)

## Related Docs
- [Headless/Service Accounts setup](https://www.twingate.com/docs/services)
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
- [Linux Connector deployment