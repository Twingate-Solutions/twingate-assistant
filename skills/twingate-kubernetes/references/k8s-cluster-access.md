# Route Traffic from Kubernetes (GKE) via Twingate Headless Client

## Summary
This guide configures a GCP VM running the Twingate headless client as a network router for a GKE cluster, enabling pods to reach Twingate-protected resources. Traffic from the cluster is routed through the VM via static VPC routes and iptables NAT rules. The VM uses a Twingate service account for authentication.

## Key Information
- Architecture: GKE pods → VPC static route → Router VM (Twingate headless client) → Remote resource
- Router VM must be in the same VPC/subnet as the GKE cluster
- IP forwarding must be enabled on both the OS (`sysctl`) and the GCP VM instance level
- Twingate interface on the VM is `sdwan0`; VM network interface is typically `ens4` (verify yours)

## Prerequisites
- GCP project with VPC network and subnet created
- Twingate admin access to create service accounts and resources
- GKE cluster in same VPC/subnet as router VM
- `gcloud` CLI and `kubectl` configured locally

## Step-by-Step

### Router VM Setup
1. Create Ubuntu x86/64 VM in same region/subnet as GKE; enable **IP Forwarding** checkbox in networking
2. Create Twingate service account → generate service key → copy Key Object JSON
3. Add firewall rule: TCP port 22, source `0.0.0.0/0`, all instances in network

### Install & Configure Twingate
```bash
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
nano /tmp/service_key.json          # paste Key Object JSON
sudo twingate setup --headless /tmp/service_key.json
sudo twingate start                 # verify "online"
```

### Enable Routing
```bash
sudo nano /etc/sysctl.conf          # uncomment net.ipv4.ip_forward=1
sudo sysctl -p

sudo iptables --append FORWARD --in-interface ens4 --out-interface sdwan0 --jump ACCEPT
sudo iptables --append FORWARD --in-interface sdwan0 --out-interface ens4 --match state --state RELATED,ESTABLISHED --jump ACCEPT
sudo iptables -t nat --append POSTROUTING --out-interface sdwan0 --jump MASQUERADE
sudo apt install iptables-persistent -y
```

### GKE Integration
1. Add static VPC route: destination = Twingate resource IP/range, next hop = router VM instance
2. Add firewall rules allowing inbound traffic from GKE node IPs and pod IP CIDR to router VM
3. Grant service account access to the Twingate resource in Admin console

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Twingate interface | `sdwan0` |
| VM network interface | `ens4` (verify with `ip link`) |
| Service key path | `/tmp/service_key.json` |
| sysctl param | `net.ipv4.ip_forward=1` |

## Gotchas
- **Interface name**: `ens4` may differ on your VM — verify before running iptables commands
- **Permission propagation**: After granting service account resource access, wait several minutes before testing
- **iptables-persistent**: Without this, rules are lost on VM restart
- **Firewall rules**: Must cover both GKE node IPs and pod CIDR separately
- **Pod security context**: Test pods need `NET_ADMIN` capability if running network tools

## Related Docs
- [Twingate Headless Client](https://www.twingate.com/docs/headless-clients)
- [Remote Network Setup](https://www.twingate.com/docs/remote-networks)
- [GCP SSH restriction guide](https://cloud.google.com/compute/docs/connect/ssh-using-iap)