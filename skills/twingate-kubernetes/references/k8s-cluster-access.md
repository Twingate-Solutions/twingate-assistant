# Route Traffic from Kubernetes (GKE) via Twingate

## Summary
Uses a Twingate headless client on a GCP VM as a network router, enabling GKE cluster pods to access Twingate-protected remote resources. Traffic flows: GKE Pod → VPC static route → Router VM (iptables NAT) → Twingate → Remote Resource.

## Key Information
- Router VM must be in the same VPC/subnet as the GKE cluster
- Twingate runs in headless mode using a Service Account key
- VM interface `sdwan0` is created by Twingate; `ens4` is the VM's network interface (may differ)
- Static VPC route must point resource IP/range to the router VM instance
- Two firewall rules needed: one for GKE node IPs, one for pod IP range

## Prerequisites
- GCP project with VPC network and subnet created
- Twingate admin access to create Service Accounts
- Remote network and resource configured in Twingate
- `gcloud` CLI and `kubectl` configured locally
- Ubuntu VM with IP forwarding enabled at GCP level (checkbox in NIC settings)

## Step-by-Step

1. **Create Service Account** → Twingate Admin > Team > Services > Create Service Account → Generate service key → Copy Key Object JSON
2. **Create Router VM** (GCP): Ubuntu x86/64, same region as subnet, enable IP Forwarding checkbox, attach to custom VPC subnet, remove default NIC
3. **Add SSH firewall rule**: TCP port 22, source `0.0.0.0/0`, target all instances in network
4. **Install Twingate on VM**:
   ```bash
   curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
   nano /tmp/service_key.json        # paste Key Object JSON
   sudo twingate setup --headless /tmp/service_key.json
   sudo twingate start
   ```
5. **Enable IP forwarding on VM**:
   ```bash
   sudo nano /etc/sysctl.conf        # uncomment net.ipv4.ip_forward=1
   sudo sysctl -p
   ```
6. **Configure iptables** (replace `ens4` with actual interface name):
   ```bash
   sudo iptables --append FORWARD --in-interface ens4 --out-interface sdwan0 --jump ACCEPT
   sudo iptables --append FORWARD --in-interface sdwan0 --out-interface ens4 --match state --state RELATED,ESTABLISHED --jump ACCEPT
   sudo iptables -t nat --append POSTROUTING --out-interface sdwan0 --jump MASQUERADE
   sudo apt install iptables-persistent -y
   ```
7. **Grant Service Account access** to the Twingate resource via Add Access
8. **Add static VPC route**: Destination = resource IP/range, Next hop = router VM instance
9. **Add firewall rules**: Allow inbound from GKE node IPs AND pod IP CIDR to router VM
10. **Deploy test pod** with `NET_ADMIN` capability, exec in, test with `curl <resource-ip>`

## Configuration Values
| Item | Value |
|------|-------|
| Service key file path | `/tmp/service_key.json` |
| Twingate setup command | `sudo twingate setup --headless <key-file>` |
| sysctl parameter | `net.ipv4.ip_forward=1` |
| Twingate VPN interface | `sdwan0` |
| VM network interface | `ens4` (verify with `ip link`) |

## Gotchas
- `ens4` interface name varies by VM — verify before running iptables commands
- Service Account access to resources can take several minutes to propagate
- GKE nodes and pod CIDR require **separate** firewall rules to reach router VM
- Service key JSON must be stored securely; loss = re-generate key
- iptables rules are lost on reboot without `iptables-persistent`

## Related Docs
- [Twingate Headless Client setup](https://www.twingate.com/docs/)
- [Remote Network configuration](https://www.twingate.com/docs/)
- [