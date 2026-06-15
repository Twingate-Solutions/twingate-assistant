# Route Traffic from Kubernetes (GKE) via Twingate

## Page Title
Route Traffic from Kubernetes Clusters Using Twingate Headless Client

## Summary
This guide configures a GCP VM as a Twingate headless client router, enabling GKE pods to reach Twingate-protected resources. Traffic from the cluster routes through the VM via static routes and iptables NAT rules. Requires a dedicated VPC, router VM, and GKE cluster in the same region/subnet.

## Key Information
- Twingate headless client runs on a dedicated Ubuntu VM acting as a network router
- GKE cluster and router VM must share the same VPC network and subnet
- Static VPC routes direct resource-bound traffic to the router VM
- Two firewall rules required: one for GKE node IPs, one for pod IP CIDR

## Prerequisites
- GCP project with VPC network and subnet already created
- Twingate admin access to create service accounts
- `gcloud` CLI and `kubectl` configured locally
- Remote network/resource configured in Twingate

## Step-by-Step

### 1. Create Service Account
- Twingate Admin → Team → Services → Create Service Account
- Generate service key, save the **Key Object** JSON

### 2. Create Router VM (GCP)
- Ubuntu x86/64, same region as VPC subnet
- Enable **IP Forwarding** checkbox under Networking
- Remove default NIC; add interface on your VPC/subnet
- Add firewall rule: TCP port 22, source `0.0.0.0/0`

### 3. Install & Configure Twingate on VM
```bash
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
nano /tmp/service_key.json          # paste Key Object JSON
sudo twingate setup --headless /tmp/service_key.json
sudo twingate start
```

### 4. Configure IP Forwarding & iptables
```bash
sudo nano /etc/sysctl.conf          # uncomment net.ipv4.ip_forward=1
sudo sysctl -p

sudo iptables --append FORWARD --in-interface ens4 --out-interface sdwan0 --jump ACCEPT
sudo iptables --append FORWARD --in-interface sdwan0 --out-interface ens4 --match state --state RELATED,ESTABLISHED --jump ACCEPT
sudo iptables -t nat --append POSTROUTING --out-interface sdwan0 --jump MASQUERADE

sudo apt install iptables-persistent -y
```

### 5. Add Static VPC Route
- Destination: Twingate resource IP/range
- Next hop: router VM instance

### 6. Add Firewall Rules
- Inbound from GKE node IPs → router VM
- Inbound from pod IP CIDR → router VM

### 7. Grant Service Account Resource Access
- Twingate Admin → Resource → Add Access → select service account

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Twingate interface | `sdwan0` |
| VM network interface | `ens4` (verify your actual interface name) |
| Service key file path | `/tmp/service_key.json` |
| sysctl setting | `net.ipv4.ip_forward=1` |

## Gotchas
- `ens4` may differ on your VM — verify with `ip link` before running iptables commands
- Permission propagation after granting resource access can take **several minutes**
- GKE cluster must be in the **same region/zone** as the router VM
- Pod spec requires `NET_ADMIN` capability for routing scenarios
- Static route must be added per-resource IP or CIDR — not automatic

## Related Docs
- [Twingate Headless Client](https://www.twingate.com/docs/headless-clients)
- [Remote Network Setup](https://www.twingate.com/docs/remote-networks)
- [GCP SSH firewall hardening](https://cloud.google.com/vpc/docs/firewalls)