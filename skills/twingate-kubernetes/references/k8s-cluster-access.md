# Route Traffic from Kubernetes (GKE) via Twingate Headless Client

## Summary
This guide configures a GKE cluster to route traffic to Twingate-protected resources using a headless Twingate client running on a GCP VM as a network router. The VM acts as a gateway between the GKE cluster and remote Twingate resources. Traffic is routed via static VPC routes and iptables NAT/forwarding rules.

## Key Information
- Architecture: GKE Cluster → Router VM (Twingate headless client) → Twingate Network → Remote Resource
- Requires a dedicated GCP VPC with custom subnet shared by both the router VM and GKE cluster
- Twingate headless client authenticates via service account key (JSON)
- Router VM must have IP forwarding enabled at both OS and GCP network interface level

## Prerequisites
- GCP project with VPC network and subnet created
- Twingate admin access to create service accounts
- `gcloud` CLI and `kubectl` configured locally
- Remote Twingate network and resource already configured
- GKE cluster in same region/zone and VPC as router VM

## Step-by-Step

### Router VM Setup
1. Create service account in Twingate Admin → Team → Services → Create Service Account; generate and save service key JSON
2. Create GCP VM (Ubuntu x86/64) in same region as VPC subnet with **IP Forwarding enabled**; remove default NIC, add NIC on custom VPC subnet
3. Add firewall rule: all instances, source `0.0.0.0/0`, TCP port 22
4. SSH into VM and install Twingate:
   ```bash
   curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
   nano /tmp/service_key.json   # paste key JSON
   sudo twingate setup --headless /tmp/service_key.json
   sudo twingate start
   ```
5. Enable IP forwarding:
   ```bash
   sudo nano /etc/sysctl.conf   # uncomment net.ipv4.ip_forward=1
   sudo sysctl -p
   ```
6. Configure iptables (replace `ens4` with actual interface name):
   ```bash
   sudo iptables --append FORWARD --in-interface ens4 --out-interface sdwan0 --jump ACCEPT
   sudo iptables --append FORWARD --in-interface sdwan0 --out-interface ens4 --match state --state RELATED,ESTABLISHED --jump ACCEPT
   sudo iptables -t nat --append POSTROUTING --out-interface sdwan0 --jump MASQUERADE
   sudo apt install iptables-persistent -y
   ```

### GKE + Routing Setup
1. Create GKE cluster in same VPC/subnet as router VM
2. Grant service account access to Twingate resource
3. Add VPC static route: destination = resource IP/range, next hop = router VM instance
4. Add two firewall rules allowing inbound traffic to router VM from: GKE node IPs + pod IP CIDR range

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Twingate interface | `sdwan0` |
| VM network interface | `ens4` (verify on your VM) |
| Headless setup flag | `--headless /tmp/service_key.json` |
| IP forwarding sysctl | `net.ipv4.ip_forward=1` |

## Gotchas
- `ens4` may differ on your VM — verify with `ip link` before running iptables commands
- iptables rules are lost on reboot unless `iptables-persistent` is installed
- Permission propagation after granting resource access can take **several minutes**
- Pod manifest requires `NET_ADMIN` capability to function correctly with routing
- GKE nodes and pods are on separate IP ranges — both require separate firewall rules to reach the router VM

## Related Docs
- [Twingate Headless Client setup](https://www.twingate.com/docs/headless-client)
- [Remote Network configuration](https://www.twingate.com/docs/remote-networks)
- [GCP SSH restriction guide](https://cloud.google.com/compute/docs/connect/