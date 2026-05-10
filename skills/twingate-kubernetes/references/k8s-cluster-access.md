# Route Traffic from Kubernetes (GKE) via Twingate

## Page Title
Route Traffic from Kubernetes Clusters via Twingate Headless Client

## Summary
This guide configures a Twingate headless Client on a GCP VM as a network router, enabling GKE cluster pods to reach Twingate-protected resources. Traffic from pods routes through the VM via static routes and iptables NAT rules. The setup uses a service account for headless authentication.

## Key Information
- Twingate headless client runs on a dedicated Ubuntu VM acting as a router
- All components (VM, GKE cluster) must be in the same GCP VPC network/subnet
- Static routes direct resource-bound traffic from GKE nodes/pods through the router VM
- IP forwarding must be enabled on both the OS and VM instance level
- Twingate interface is `sdwan0`; VM network interface may vary (commonly `ens4`)

## Prerequisites
- GCP project with VPC network and subnet created
- Twingate admin access to create service accounts
- `gcloud` CLI and `kubectl` configured locally
- GKE cluster in same region/zone as router VM

## Step-by-Step

1. **Create service account** in Twingate Admin → Team → Services → Create Service Account → Generate service key → Copy Key Object JSON
2. **Create Ubuntu VM** in GCP with IP Forwarding enabled, attached to your VPC subnet (remove default interface)
3. **Add SSH firewall rule**: TCP port 22, source `0.0.0.0/0`, all instances in network
4. **Install Twingate client** on VM:
   ```bash
   curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
   nano /tmp/service_key.json   # paste Key Object JSON
   sudo twingate setup --headless /tmp/service_key.json
   sudo twingate start
   ```
5. **Enable IP forwarding** on VM OS:
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
8. **Add static route** in VPC: destination = resource IP/range, next hop = router VM instance
9. **Add firewall rules** to allow inbound from GKE node IPs and pod IP CIDR to router VM
10. **Test** from a pod: `kubectl exec -it ubuntu /bin/bash` → `curl <resource-ip>`

## Configuration Values
| Parameter | Value/Notes |
|-----------|-------------|
| Twingate interface | `sdwan0` |
| VM network interface | `ens4` (verify on your VM) |
| Service key file path | `/tmp/service_key.json` |
| Sysctl parameter | `net.ipv4.ip_forward=1` |
| Pod test image | `ubuntu:22.04` |

## Gotchas
- **Interface name**: `ens4` in iptables commands may differ on your VM — verify before running
- **Permission propagation delay**: After granting resource access to service account, wait several minutes before testing
- **Firewall rules needed for both** GKE node IPs and pod IP CIDR — find pod CIDR in GKE cluster details page
- **Pod requires `NET_ADMIN` capability** in securityContext for network operations
- Guide uses smallest VM type — review sizing for production throughput requirements
- SSH firewall rule exposes port 22 publicly — restrict source IPs for production

## Related Docs
- [Twingate Headless Client setup](https://www.twingate.