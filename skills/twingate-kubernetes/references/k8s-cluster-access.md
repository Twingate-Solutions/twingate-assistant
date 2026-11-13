---
source: https://www.twingate.com/docs/k8s-cluster-access
type: docs
fetched: 2026-11-13
source_version: b2dcf78e914422419c27122c14999af78925f2849968f7e3ce501b9791c4ba0f
trust: official
---

# Route Traffic from Kubernetes (GKE) via Twingate Headless Client

## Summary
Guide to letting pods in a GKE cluster reach Twingate-protected remote resources. A dedicated GCP VM runs the Twingate headless Client and acts as a router/NAT gateway. A static VPC route sends traffic for the resource IP through that VM. It is a demo guide, not production-hardened.

## Key Information
- Architecture: GKE pods → VPC static route → router VM (Twingate headless client, IP forwarding, iptables NAT) → Twingate → remote resource.
- The VM authenticates using a Twingate **service account** and service key (headless mode).
- The Twingate interface on the VM is `sdwan0`; the VM's own NIC in the example is `ens4`.
- Router VM, VPC subnet, and GKE cluster should be in the same region/zone and the same VPC network/subnet.
- The example uses the smallest VM type; size for throughput in production.

## Prerequisites
- Twingate account with a Remote Network and Resource (example resource IP `10.43.40.159`)
- GCP project with a VPC and subnet already created
- `gcloud` CLI and `kubectl` configured
- Admin access to create Twingate service accounts

## Step-by-Step
1. **Service account**: Twingate Admin → Team → Services → Create Service Account → generate a service key and save the Key Object (JSON).
2. **Create VM**: Ubuntu x86/64, same region as the subnet. Enable **IP Forwarding**, delete the default NIC, and add a NIC on your VPC/subnet.
3. **Firewall rule for SSH**: TCP 22 on the VPC (the guide uses source `0.0.0.0/0`; restrict this).
4. **Install the client** on the VM using the official install script from `binaries.twingate.com` (`https://binaries.twingate.com/client/linux/install.sh`, run with sudo bash, per the page).
5. Save the key to `/tmp/service_key.json`, then run `sudo twingate setup --headless /tmp/service_key.json` and `sudo twingate start`. Status should show `online`.
6. **Enable forwarding**: uncomment `net.ipv4.ip_forward=1` in `/etc/sysctl.conf`, then run `sudo sysctl -p`.
7. **iptables**:
   ```
   sudo iptables --append FORWARD --in-interface ens4 --out-interface sdwan0 --jump ACCEPT
   sudo iptables --append FORWARD --in-interface sdwan0 --out-interface ens4 --match state --state RELATED,ESTABLISHED --jump ACCEPT
   sudo iptables -t nat --append POSTROUTING --out-interface sdwan0 --jump MASQUERADE
   sudo apt install iptables-persistent -y
   ```
8. In Twingate, grant the service account access to the Resource (via Add Access). Test from the VM with `curl <resource-ip>`. Permissions can take a few minutes to propagate.
9. **Create GKE cluster** (Standard) in the same region/zone, network, and subnet as the router.
10. **Static route**: VPC → Routes → Create. Destination is the resource IP/range, next hop is the router VM instance.
11. **Firewall rules**: allow inbound to the router from the GKE node IPs and from the pod/service IP ranges.
12. **Test**: `gcloud container clusters get-credentials twingate-demo --zone europe-west1-b`, deploy an Ubuntu 22.04 test pod (`ubuntu.yaml`, with `NET_ADMIN` capability), `kubectl exec` into it, install curl, and curl the resource.

## Configuration Values
- `net.ipv4.ip_forward=1` (`/etc/sysctl.conf`)
- Twingate commands: `twingate setup --headless <key.json>`, `twingate start`
- Interfaces: `ens4` (replace with your NIC name), `sdwan0`
- Pod securityContext: `capabilities.add: [NET_ADMIN]`

## Gotchas
- Check your actual NIC name (it may not be `ens4`) before running iptables commands.
- Without `iptables-persistent`, rules are lost on reboot.
- The service key authenticates the client, so protect it (and delete `/tmp/service_key.json` after setup).
- The SSH rule in the example is open to the internet; restrict it.
- GKE nodes and pods cannot reach the router until firewall rules are added.
- The route destination must match your resource IP/range.
- Access changes may take a few minutes to take effect.

## Related Docs
- Twingate Headless Client (Linux) installation guide
- Twingate Remote Networks and Resources setup
- Twingate service accounts and keys
- GCP VPC firewall rules and routes documentation