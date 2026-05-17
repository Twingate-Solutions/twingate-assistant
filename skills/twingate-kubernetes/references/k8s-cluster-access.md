# Route Traffic from Kubernetes (GKE) via Twingate

## Page Title
Route Traffic from Kubernetes Clusters via Twingate Headless Client

## Summary
This guide configures a GCP VM running the Twingate headless client as a network router, enabling pods in a GKE cluster to reach Twingate-protected resources. Traffic from the cluster routes through the VM via static GCP routes and iptables NAT rules. The VM acts as a transparent gateway using a Twingate service account for authentication.

## Key Information
- Architecture: GKE Pod → Static Route → Router VM (Twingate headless) → Remote Resource
- All components (VM, GKE cluster) must be in the same VPC network and subnet
- VM requires IP Forwarding enabled at the GCP network interface level
- Twingate interface on the VM is `sdwan0`; VM NIC is typically `ens4` (verify yours)

## Prerequisites
- GCP project with a custom VPC network and subnet
- Twingate account with admin access
- Service account + service key created in Twingate admin (Team → Services)
- Remote network and resource configured in Twingate with access granted to the service account
- `gcloud` CLI and `kubectl` configured locally

## Step-by-Step

### Router VM Setup
1. Create Ubuntu x86/64 VM in same region/subnet as GKE; enable **IP Forwarding** on NIC
2. Add firewall rule: TCP port 22 from `0.0.0.0/0` (or restricted range)
3. Install Twingate: `curl https://binaries.twingate.com/client/linux/install.sh | sudo bash`
4. Save service key: `nano /tmp/service_key.json`
5. Configure headless: `sudo twingate setup --headless /tmp/service_key.json`
6. Start: `sudo twingate start` → verify `online` status
7. Enable IP forwarding in OS: uncomment `net.ipv4.ip_forward=1` in `/etc/sysctl.conf`, run `sudo sysctl -p`
8. Configure iptables (replace `ens4` with actual interface name):
```bash
sudo iptables --append FORWARD --in-interface ens4 --out-interface sdwan0 --jump ACCEPT
sudo iptables --append FORWARD --in-interface sdwan0 --out-interface ens4 --match state --state RELATED,ESTABLISHED --jump ACCEPT
sudo iptables -t nat --append POSTROUTING --out-interface sdwan0 --jump MASQUERADE
sudo apt install iptables-persistent -y  # persist rules across reboots
```

### GKE Configuration
1. Create GKE cluster in same VPC/subnet as router VM
2. Add static route: destination = Twingate resource IP/range, next hop = router VM instance
3. Add firewall rules allowing inbound traffic from GKE node IPs and pod CIDR to router VM

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Twingate interface | `sdwan0` |
| Default VM NIC | `ens4` (verify with `ip link`) |
| Service key path | `/tmp/service_key.json` |
| SSH firewall port | `tcp/22` |

## Gotchas
- **Interface name**: `ens4` may differ on your VM — verify with `ip link` before running iptables commands
- **Permission propagation**: After granting service account access to a resource, wait several minutes before testing
- **Pod security context**: Test pods need `NET_ADMIN` capability to run network tools
- **Firewall rules needed for both** GKE node IPs and pod CIDR range (found in GKE cluster info page)
- Service key is displayed once — copy it immediately upon generation

## Related Docs
- [Twingate Headless Client setup](https://www.twingate.com/docs/headless-client)
- [Remote Network configuration](https://www.twingate.com/docs/remote-networks)
- [GCP SSH restriction guide](https://cloud.google.com/compute/docs/instances/ssh)