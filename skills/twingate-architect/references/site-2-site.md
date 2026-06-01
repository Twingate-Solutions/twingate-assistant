# Twingate Site-to-Site Connections

## Summary
Configures bidirectional traffic routing between two network sites (e.g., Azure and GCP) using Twingate Connectors and headless Twingate Clients acting as software routers. Each site runs a Connector for inbound access and a headless Client on a router VM that forwards traffic to the remote site via iptables NAT.

## Key Information
- Each site requires: one Connector (inbound), one headless Client on a router VM (outbound routing), and a Service Account for headless auth
- Router VM uses `iptables` with `MASQUERADE` to NAT traffic through the `sdwan0` Twingate virtual interface
- Resources in each site are assigned to the Service Account of the **opposite** site
- Peer-to-peer connections recommended to reduce bandwidth under Fair Use Policy

## Prerequisites
- Two Remote Networks created in Twingate Admin Console (one per site)
- Connector tokens generated per site
- Two Service Accounts with keys generated (one per site)
- Router VMs must have internet access (via NAT gateway/Cloud NAT — no public IP required)
- IP forwarding enabled on router VMs

## Step-by-Step

### Per-Site Setup (repeat for each site)
1. Create Remote Network in Admin Console
2. Deploy Connector on a Linux VM (no public IP); use generated token command
3. Deploy second Linux VM as router (no public IP); enable IP forwarding
4. Install headless Twingate Client:
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
6. Configure iptables (replace `ens4`/`eth0` and `sdwan0` with actual interfaces):
   ```bash
   sudo iptables -A FORWARD -i ens4 -o sdwan0 -j ACCEPT
   sudo iptables -A FORWARD -i sdwan0 -o ens4 -m state --state RELATED,ESTABLISHED -j ACCEPT
   sudo iptables -t nat -A POSTROUTING -o sdwan0 -j MASQUERADE
   sudo apt install iptables-persistent -y  # persist rules
   ```
7. Add test VM as a Twingate Resource; assign to **opposite site's** Service Account
8. Configure cloud routing tables to direct subnet traffic through the router VM

## Configuration Values
| Item | Value |
|------|-------|
| Client install script | `https://binaries.twingate.com/client/linux/install.sh` |
| Headless setup command | `sudo twingate setup --headless <key_file.json>` |
| Twingate virtual interface | `sdwan0` |
| sysctl IP forward setting | `net.ipv4.ip_forward=1` |

## Gotchas
- **Interface names vary**: Replace `ens4` (Azure) / `eth0` (GCP) and verify `sdwan0` matches actual Twingate interface
- **GCP requires IP forwarding enabled at VM creation** (not just via sysctl post-deploy)
- **Cloud NAT must be configured before deploying router VM** in GCP, or Client/Connector install will fail
- **Cross-assign Resources**: Site 1 test VM → Site 2 Service Account; Site 2 test VM → Site 1 Service Account
- Connector VM should have no public IP; use Run Command (Azure) or automation scripts (GCP) if no SSH access

## Related Docs
- [Headless/Service Accounts](https://www.twingate.com/docs/services)
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
- [Linux Connector deployment](https://www.twingate.com/docs/linux)