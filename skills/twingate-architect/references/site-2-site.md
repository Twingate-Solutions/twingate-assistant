# Secure Site-to-Site Connections with Twingate

## Summary
Configures bidirectional traffic routing between two cloud sites (Azure and GCP) using Twingate Connectors and headless Twingate Clients acting as routers. Each site runs a Connector for inbound access and a headless Client VM that forwards traffic via iptables/NAT to the remote site's subnet.

## Key Information
- Architecture: Each site needs two VMs — one running the Connector, one running the headless Client (router VM)
- Traffic flow: VM in site → router VM (iptables FORWARD) → Twingate Client (`sdwan0`) → remote Connector → destination VM
- Service Accounts authenticate headless Clients (not user accounts)
- Resources must be assigned to the **opposing site's** Service Account (site 1 resource → site 2 service account, and vice versa)
- Peer-to-peer connections recommended to reduce bandwidth and stay within Fair Use Policy

## Prerequisites
- Two Remote Networks created in Twingate Admin Console (one per site)
- One Connector deployed per site
- Two Service Accounts created (one per site)
- Service Account keys saved securely
- NAT gateway (Azure) / Cloud NAT (GCP) configured before router VM deployment
- No public IPs required on any VMs (Connector or router)

## Step-by-Step

### Router VM Setup (both sites)
1. Install Twingate Client:
   ```bash
   curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
   ```
2. Create service key file: `nano /tmp/service_key.json` (paste key contents)
3. Configure headless mode: `sudo twingate setup --headless /tmp/service_key.json`
4. Start client: `sudo twingate start` — verify output shows `online`
5. Enable IP forwarding in `/etc/sysctl.conf` — uncomment `net.ipv4.ip_forward=1`
6. Apply: `sudo sysctl -p`
7. Configure iptables (replace interface names as needed):
   ```bash
   sudo iptables -A FORWARD -i ens4 -o sdwan0 -j ACCEPT
   sudo iptables -A FORWARD -i sdwan0 -o ens4 -m state --state RELATED,ESTABLISHED -j ACCEPT
   sudo iptables -t nat -A POSTROUTING -o sdwan0 -j MASQUERADE
   ```
8. Persist rules: `sudo apt install iptables-persistent -y`

## Configuration Values

| Parameter | Site 1 (Azure) | Site 2 (GCP) |
|---|---|---|
| Internal interface | `ens4` | `eth0` |
| Twingate interface | `sdwan0` | `sdwan0` |
| Example subnet | `10.0.1.0/24` | `172.16.1.0/24` |

## Gotchas
- **Interface names vary** — replace `ens4`/`eth0` and `sdwan0` with actual interface names from your VMs
- **GCP requires IP forwarding enabled at VM creation time** (not just via sysctl) — Azure does not
- **Cloud NAT must exist before router VM deployment** in GCP, or the Client install script won't reach the internet
- **Cross-assign Resources**: site 1 test VM resource → site 2 service account; site 2 test VM resource → site 1 service account
- Cloud routing tables must be configured in both cloud providers independently (Azure route table + GCP route) for subnet traffic to reach the router VMs

## Related Docs
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Headless Client / Service Accounts](https://www.twingate.com/docs/services)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)