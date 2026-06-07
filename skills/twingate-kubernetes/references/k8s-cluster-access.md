# Route Traffic from Kubernetes (GKE) via Twingate Headless Client

## Summary
Uses a Twingate headless client on a GCP VM as a network router, allowing GKE cluster pods to access Twingate-protected remote resources. The VM acts as a NAT gateway between the GKE cluster subnet and Twingate's `sdwan0` interface.

## Key Information
- Architecture: GKE Cluster → VPC Subnet → Router VM (Twingate headless) → Remote Resource
- All components (VM, GKE cluster) must be in the **same VPC network and subnet**
- VM requires **IP Forwarding enabled** at both GCP network interface level and OS level
- Static VPC routes direct resource-bound traffic through the router VM
- Twingate interface on VM is `sdwan0`; VM network interface typically `ens4` (verify yours)

## Prerequisites
- GCP project with VPC network and subnet created
- Twingate admin access to create Service Accounts and Service Keys
- Ubuntu VM with IP forwarding enabled in GCP networking settings
- GKE cluster in same VPC/subnet as router VM
- `gcloud` CLI and `kubectl` configured locally

## Step-by-Step

### Router VM Setup
1. Create Twingate Service Account → generate Service Key → copy Key Object JSON
2. Create Ubuntu x86/64 VM in same region as subnet; enable **IP Forwarding** checkbox; attach to custom VPC subnet
3. Add firewall rule: TCP port 22, source `0.0.0.0/0`, all instances in network
4. SSH into VM and install Twingate:
   ```bash
   curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
   nano /tmp/service_key.json   # paste Key Object JSON
   sudo twingate setup --headless /tmp/service_key.json
   sudo twingate start
   ```
5. Enable IP forwarding at OS level:
   ```bash
   sudo nano /etc/sysctl.conf   # uncomment net.ipv4.ip_forward=1
   sudo sysctl -p
   ```
6. Configure iptables (replace `ens4` with your actual interface):
   ```bash
   sudo iptables --append FORWARD --in-interface ens4 --out-interface sdwan0 --jump ACCEPT
   sudo iptables --append FORWARD --in-interface sdwan0 --out-interface ens4 --match state --state RELATED,ESTABLISHED --jump ACCEPT
   sudo iptables -t nat --append POSTROUTING --out-interface sdwan0 --jump MASQUERADE
   sudo apt install iptables-persistent -y
   ```

### GKE + Routing Setup
1. Create GKE cluster in same VPC network and subnet as router VM
2. Add VPC static route: destination = resource IP/range, next hop = router VM instance
3. Add two firewall rules allowing inbound traffic to router VM from:
   - GKE node IPs
   - Pod IP CIDR range (found in GKE cluster info page)
4. Grant Service Account access to the Twingate resource via **Add Access** in admin console

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Service key file path | `/tmp/service_key.json` |
| Twingate setup command | `twingate setup --headless <key_file>` |
| OS sysctl setting | `net.ipv4.ip_forward=1` |
| Twingate network interface | `sdwan0` |
| VM network interface | `ens4` (verify—may differ) |

## Gotchas
- `ens4` is example interface name—verify actual name before running iptables commands
- Access permission changes after adding Service Account to resource can take **several minutes** to propagate
- Firewall rules must cover both **node IPs** and **pod CIDR** separately
- `iptables-persistent` required to survive VM reboots; answer YES to both prompts during install
- Pod spec requires `NET_ADMIN` capability if pods need network manipulation

## Related Docs
- [Twingate Headless Client](https://www.twingate.com/docs/linux-headless)