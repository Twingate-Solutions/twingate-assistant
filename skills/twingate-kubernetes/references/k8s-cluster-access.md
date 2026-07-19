# Route Traffic from Kubernetes via Twingate Headless Client

## Summary
This guide demonstrates using the Twingate headless client as a routing VM within a GCP VPC to enable GKE cluster pods to access Twingate-protected remote resources. A dedicated Ubuntu VM runs the Twingate client in headless mode and handles IP forwarding/NAT between the GKE cluster and Twingate resources.

## Key Information
- Architecture: GKE Cluster → VPC Static Route → Router VM (Twingate headless) → Remote Resource
- Router VM must be in the same VPC/subnet as the GKE cluster
- All traffic to Twingate resources is NATed through the `sdwan0` interface on the router VM
- Twingate interface name is always `sdwan0`; VM interface name may vary (e.g., `ens4`)

## Prerequisites
- GCP VPC with custom subnet (same region for VM and GKE cluster)
- Twingate service account + generated service key (JSON)
- Ubuntu VM with IP Forwarding enabled (GCP checkbox at creation time)
- `gcloud` CLI and `kubectl` configured locally
- Remote network/resource configured in Twingate admin; service account granted access

## Step-by-Step

### Router VM Setup
```bash
# Install Twingate client
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash

# Save service key
nano /tmp/service_key.json

# Configure headless mode
sudo twingate setup --headless /tmp/service_key.json

# Start client
sudo twingate start  # Expected output: "online"

# Enable IP forwarding
sudo nano /etc/sysctl.conf  # Uncomment: net.ipv4.ip_forward=1
sudo sysctl -p

# Configure iptables (replace ens4 with your VM's interface name)
sudo iptables --append FORWARD --in-interface ens4 --out-interface sdwan0 --jump ACCEPT
sudo iptables --append FORWARD --in-interface sdwan0 --out-interface ens4 --match state --state RELATED,ESTABLISHED --jump ACCEPT
sudo iptables -t nat --append POSTROUTING --out-interface sdwan0 --jump MASQUERADE

# Persist iptables rules
sudo apt install iptables-persistent -y
```

### GCP Networking Configuration
1. **Static Route**: Destination = Twingate resource IP/range; Next hop = Router VM instance
2. **Firewall Rules** (on VPC): Allow inbound from GKE node IPs AND pod IP CIDR range to router VM

### GKE Test Pod (`ubuntu.yaml`)
```yaml
spec:
  containers:
  - name: ubuntu
    image: ubuntu:22.04
    command: ["/bin/sleep", "3650d"]
    securityContext:
      capabilities:
        add: ["NET_ADMIN"]
```

## Configuration Values
| Parameter | Value/Location |
|-----------|---------------|
| Service key path | `/tmp/service_key.json` |
| Twingate interface | `sdwan0` |
| IP forward sysctl | `net.ipv4.ip_forward=1` in `/etc/sysctl.conf` |
| SSH firewall rule | TCP port 22, source `0.0.0.0/0` |

## Gotchas
- **VM interface name**: `ens4` in iptables commands may differ on your VM — verify with `ip link`
- **IP Forwarding checkbox** must be enabled at VM creation time in GCP, not after
- **Permissions propagation**: After granting service account resource access, wait several minutes before testing
- **Pod security context**: `NET_ADMIN` capability required on test pods using `curl`
- VM must be **deleted from default network interface** and added to your custom VPC subnet

## Related Docs
- [Twingate Headless Client setup](https://www.twingate.com/docs/headless-client)
- [Twingate Remote Networks](https://www.twingate.com/docs/remote-networks)
- [GCP SSH firewall hardening](https://cloud.google.com/vpc/docs/firewalls)