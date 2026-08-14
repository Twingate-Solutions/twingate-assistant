---
source: https://www.twingate.com/docs/k8s-cluster-access
type: docs
fetched: 2026-08-14
source_version: a1db8f356d5bce63e8738dbe1a289ffdc2cf636490cdcb71efa9f3637f4eab93
---

# Route Traffic from Kubernetes (GKE) via Twingate Headless Client

## Summary
This guide configures a Twingate headless client on a GCP VM as a network router, enabling GKE cluster pods to access Twingate-protected remote resources. Traffic is routed from GKE pods → router VM (running Twingate headless client) → remote resources via Twingate tunnel.

## Key Information
- Architecture: GKE Cluster → Static Route → Router VM (Twingate headless) → Remote Resource
- Router VM uses IP forwarding + iptables NAT (MASQUERADE) to proxy traffic
- Service account + service key used for headless authentication (no UI interaction)
- Twingate interface on VM is `sdwan0`; LAN interface may vary (example uses `ens4`)
- Static VPC route directs resource IPs to the router VM instance as next hop

## Prerequisites
- GCP project with VPC, subnet, and GKE cluster in same region
- Twingate admin access to create service accounts and resources
- Remote network and resource already configured in Twingate
- `gcloud` CLI and `kubectl` configured locally

## Step-by-Step

1. **Create Twingate Service Account** → Admin → Team → Services → Create Service Account → Generate service key → copy Key Object JSON
2. **Create Ubuntu VM** in same region/subnet as GKE cluster; enable **IP Forwarding** checkbox; use custom VPC network interface
3. **Firewall rule**: Allow TCP port 22 from `0.0.0.0/0` to SSH into VM
4. **Install Twingate headless client** on VM:
   ```bash
   curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
   nano /tmp/service_key.json   # paste Key Object JSON
   sudo twingate setup --headless /tmp/service_key.json
   sudo twingate start
   ```
5. **Enable IP forwarding** on VM:
   ```bash
   sudo nano /etc/sysctl.conf   # uncomment net.ipv4.ip_forward=1
   sudo sysctl -p
   ```
6. **Configure iptables** (replace `ens4` with actual interface name):
   ```bash
   sudo iptables --append FORWARD --in-interface ens4 --out-interface sdwan0 --jump ACCEPT
   sudo iptables --append FORWARD --in-interface sdwan0 --out-interface ens4 --match state --state RELATED,ESTABLISHED --jump ACCEPT
   sudo iptables -t nat --append POSTROUTING --out-interface sdwan0 --jump MASQUERADE
   sudo apt install iptables-persistent -y
   ```
7. **Grant service account access** to Twingate resource via Add Access
8. **Add VPC static route**: Destination = resource IP/range, Next hop = router VM instance
9. **Add firewall rules** allowing inbound from GKE node IPs and pod IP range to router VM
10. **Test from GKE pod**: Deploy ubuntu pod, `kubectl exec`, `curl <resource-ip>`

## Configuration Values
| Parameter | Value/Notes |
|-----------|-------------|
| Twingate interface | `sdwan0` |
| VM LAN interface | `ens4` (verify; may differ) |
| Service key file | `/tmp/service_key.json` |
| sysctl setting | `net.ipv4.ip_forward=1` |
| Pod manifest capabilities | `NET_ADMIN` required |

## Gotchas
- **Interface name**: `ens4` is example only — verify actual interface name before running iptables commands
- **Permission propagation delay**: After granting resource access to service account, wait several minutes before testing
- **GKE firewall rules**: Both node IPs and pod CIDR ranges need separate firewall rules to reach the router VM
- **iptables-persistent**: Must be installed to survive VM reboots; answer YES to both prompts
- Service key JSON must be kept secure — treat as credentials

## Related Docs
- [Twingate Headless Client setup](https://www.twingate.com/docs/linux-headless)
- [Remote network configuration](https://www.t