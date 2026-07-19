# Secure Site-to-Site Connections with Twingate

## Summary
Configures bidirectional traffic routing between two cloud sites (Azure and GCP) using Twingate Connectors and headless Twingate Clients acting as router VMs. Each site runs a Connector for inbound access and a headless Client with iptables NAT rules to forward outbound traffic to the remote site.

## Key Information
- Each site requires two VMs: one running the Twingate Connector, one running the headless Twingate Client (router VM)
- Headless Client uses Service Account keys (not user auth) for authentication
- `sdwan0` is the virtual network interface created by the Twingate Client
- Resources in each site are assigned to the Service Account of the **opposite** site
- Peer-to-peer connections recommended to reduce bandwidth and comply with Fair Use Policy

## Prerequisites
- Twingate Admin Console access
- Two Remote Networks configured (one per site)
- Two Connectors deployed (one per site)
- Two Service Accounts created with keys saved
- NAT gateway (Azure) / Cloud NAT (GCP) configured before router VM deployment
- IP forwarding enabled on router VMs

## Step-by-Step

### Per Site (repeat for each)
1. Create Remote Network in Admin Console
2. Deploy Connector VM (no public IP, use NAT for internet access); run generated token command
3. Deploy router VM (no public IP); install headless Client:
```bash
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
nano /tmp/service_key.json   # paste Service Account key
sudo twingate setup --headless /tmp/service_key.json
sudo twingate start
```
4. Enable IP forwarding:
```bash
sudo nano /etc/sysctl.conf   # uncomment net.ipv4.ip_forward=1
sudo sysctl -p
```
5. Configure iptables (replace interface names):
```bash
sudo iptables -A FORWARD -i ens4 -o sdwan0 -j ACCEPT
sudo iptables -A FORWARD -i sdwan0 -o ens4 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -t nat -A POSTROUTING -o sdwan0 -j MASQUERADE
sudo apt install iptables-persistent -y   # optional: persist rules
```
6. Deploy test VM; add as Twingate Resource assigned to the **other site's** Service Account
7. Configure cloud routing tables to route remote subnet traffic through router VM

## Configuration Values
| Parameter | Site 1 (Azure) | Site 2 (GCP) |
|-----------|---------------|--------------|
| Internal interface | `ens4` | `eth0` |
| Twingate interface | `sdwan0` | `sdwan0` |
| Example subnet | `10.0.1.0/24` | `172.16.1.0/24` |

## Gotchas
- Interface names (`ens4`, `eth0`) vary by VM/OS — verify before running iptables commands
- GCP requires IP forwarding enabled at VM creation time (not just in OS)
- Cloud NAT must be configured **before** deploying router VM or it can't download packages
- Service Account key is shown once — copy immediately during generation
- Assign each site's Resource to the **opposite** site's Service Account (cross-assignment)
- iptables rules are lost on reboot unless `iptables-persistent` is installed

## Related Docs
- Peer-to-peer connections support
- Headless Client / Service Accounts documentation
- Twingate Fair Use Policy