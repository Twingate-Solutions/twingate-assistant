# Route Traffic from Kubernetes (GKE) via Twingate Headless Client

## Summary
This guide configures a GCP VM as a Twingate headless client router, enabling pods within a GKE cluster to access Twingate-protected remote resources. Traffic from the cluster is routed through the VM, which runs the Twingate client in headless (service account) mode and performs IP masquerading via iptables.

## Key Information
- Architecture: GKE pods → static VPC route → Router VM (Twingate headless client) → remote Twingate resource
- Router VM must be in the same VPC network/subnet as the GKE cluster
- IP forwarding must be enabled on the VM at both OS and GCP levels
- Twingate interface on the VM is `sdwan0`; VM network interface is typically `ens4` (verify yours)

## Prerequisites
- GCP project with a custom VPC network and subnet
- Twingate account with admin access
- Remote network and resource already configured in Twingate
- `gcloud` CLI and `kubectl` installed locally
- GKE cluster in same region/zone as router VM

## Step-by-Step

### 1. Create Service Account
- Admin console → Team → Services → Create Service Account
- Generate a service key; copy the full **Key Object** JSON

### 2. Create Router VM
- OS: Ubuntu x86/64
- Same region/subnet as GKE cluster
- Enable **IP Forwarding** checkbox in Networking section
- Remove default NIC; add NIC on your custom VPC subnet

### 3. Configure Firewall Rules
- SSH access: TCP port 22, source `0.0.0.0/0`, all instances in network
- Inbound from GKE node IPs (find on VM instances page)
- Inbound from pod IP CIDR range (find on GKE cluster info page)

### 4. Install & Configure Twingate on Router VM
```bash
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
nano /tmp/service_key.json          # paste Key Object JSON
sudo twingate setup --headless /tmp/service_key.json
sudo twingate start
```

### 5. Configure IP Routing on VM
```bash
# Enable IP forwarding
sudo nano /etc/sysctl.conf          # uncomment net.ipv4.ip_forward=1
sudo sysctl -p

# iptables rules (replace ens4 if your interface differs)
sudo iptables --append FORWARD --in-interface ens4 --out-interface sdwan0 --jump ACCEPT
sudo iptables --append FORWARD --in-interface sdwan0 --out-interface ens4 --match state --state RELATED,ESTABLISHED --jump ACCEPT
sudo iptables -t nat --append POSTROUTING --out-interface sdwan0 --jump MASQUERADE

sudo apt install iptables-persistent -y   # persist rules across reboots
```

### 6. Add Static VPC Route
- VPC Network → Routes → Create Route
- Destination IP: remote resource IP/range
- Next hop: Router VM instance

### 7. Grant Service Account Resource Access
- Twingate Admin → Resource → Add Access → select the service account

### 8. Deploy Test Pod to GKE
```bash
kubectl apply -f ubuntu.yaml        # see pod spec in docs
kubectl exec -it ubuntu /bin/bash
curl <resource-ip>
```

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Twingate install script | `https://binaries.twingate.com/client/linux/install.sh` |
| Service key path | `/tmp/service_key.json` |
| Twingate network interface | `sdwan0` |
| VM network interface | `ens4` (verify) |
| sysctl key | `net.ipv4.ip_forward=1` |

## Gotchas
- Interface name `ens4` may differ on your VM — verify before running iptables commands
- Resource access permissions can take **a few minutes** to propagate after granting
- Static route must be added for **each** resource IP/range you want reachable from the cluster
- Pod spec requires `NET_ADMIN