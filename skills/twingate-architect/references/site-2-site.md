# Twingate Site-to-Site Connections

## Summary
Configures bidirectional traffic routing between two cloud sites (Azure and GCP) using Twingate Connectors and headless Twingate Clients acting as routers. Each site deploys a Connector for inbound access and a headless Client VM with iptables NAT rules to forward outbound traffic to the remote site.

## Key Information
- Each site requires: one Connector VM, one headless Client "router" VM, one test/workload VM
- Headless Clients authenticate via Service Account keys (JSON)
- Router VMs need IP forwarding enabled and iptables MASQUERADE rules
- No public IPs needed on any VMs; use NAT gateway (Azure) or Cloud NAT (GCP)
- Resources are cross-assigned: site 1 resources → site 2 Service Account, and vice versa

## Prerequisites
- Twingate Admin Console access
- Two Remote Networks created (one per site)
- Two Connectors deployed (one per Remote Network)
- Two Service Accounts with generated JSON keys
- Cloud routing tables configured (Azure route table + GCP route) pointing subnet traffic to router VM private IP

## Step-by-Step

### Headless Client Setup (both sites)
```bash
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
nano /tmp/service_key.json          # paste Service Account JSON key
sudo twingate setup --headless /tmp/service_key.json
sudo twingate start
```

### Enable IP Forwarding
```bash
sudo nano /etc/sysctl.conf          # uncomment net.ipv4.ip_forward=1
sudo sysctl -p
```

### iptables Rules (replace interface names as needed)
```bash
# Azure: ens4=internal, sdwan0=Twingate virtual interface
sudo iptables -A FORWARD -i ens4 -o sdwan0 -j ACCEPT
sudo iptables -A FORWARD -i sdwan0 -o ens4 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -t nat -A POSTROUTING -o sdwan0 -j MASQUERADE

# GCP: eth0=internal
sudo iptables -A FORWARD -i eth0 -o sdwan0 -j ACCEPT
sudo iptables -A FORWARD -i sdwan0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -t nat -A POSTROUTING -o sdwan0 -j MASQUERADE

# Persist rules
sudo apt install iptables-persistent -y
```

## Configuration Values
| Parameter | Example Value |
|-----------|--------------|
| Site 1 subnet (Azure) | `10.0.1.0/24` |
| Site 2 subnet (GCP) | `172.16.1.0/24` |
| Twingate virtual interface | `sdwan0` |
| Azure internal interface | `ens4` |
| GCP internal interface | `eth0` |
| Service key path | `/tmp/service_key.json` |

## Gotchas
- **GCP**: IP forwarding must be enabled at VM creation time (instance setting), not just via `sysctl`
- **Azure**: Disable public IP on Connector and router VMs; configure NAT gateway before deployment
- **GCP**: Cloud NAT must be set up before deploying the router VM or it cannot install packages
- **Resource assignment**: Site 1 test VM must be assigned to the **site 2** Service Account (and vice versa) for cross-site access
- iptables rules are lost on reboot without `iptables-persistent`
- Interface names (`ens4`, `eth0`) vary by cloud/distro—verify before running commands

## Related Docs
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
- Twingate headless Client documentation
- Service Accounts documentation