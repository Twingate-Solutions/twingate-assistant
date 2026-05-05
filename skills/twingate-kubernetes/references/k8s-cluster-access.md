## Route Traffic from Kubernetes (Headless Client as Router)

How to give every pod in a Kubernetes cluster outbound access to private Twingate Resources -- without installing a Twingate Client in each pod. Pattern: a dedicated VM in the same VPC runs the Twingate headless Client, the cluster sends traffic to that VM via static route + iptables NAT.

**Architecture:**
- **Router VM** -- Ubuntu VM in the same VPC/subnet as the cluster, runs Twingate headless Client + iptables NAT, has IP forwarding enabled
- **Static route** in the VPC -- destination = Twingate Resource IP/range, next hop = router VM
- **Firewall rules** -- allow GKE node IPs and pod CIDR to reach the router VM

**Setup Walkthrough (GKE Example):**

**1. Service Account + Service Key**
- Twingate Admin Console -> Team -> Services -> Create Service Account
- Generate service key; save the Key Object JSON (used for headless auth)

**2. Router VM**
- New GCP VM (smallest instance for testing; size up for production throughput)
- Ubuntu x86/64 image
- **Enable IP Forwarding** (Networking section -> tick the IP Forwarding checkbox; cannot be changed after creation)
- Place in the **same VPC + subnet** as the GKE cluster
- Allow SSH (firewall rule, port 22, restrict source ranges in production)

**3. Install Twingate Headless Client**
```
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
nano /tmp/service_key.json   # paste the Key Object content
sudo twingate setup --headless /tmp/service_key.json
sudo twingate start
```
Verify: status shows `online`.

**4. Enable IP Forwarding (Linux)**
- Edit `/etc/sysctl.conf` -- uncomment `net.ipv4.ip_forward=1`
- `sudo sysctl -p` to apply

**5. iptables NAT (replace `ens4` with your interface name)**
```
sudo iptables --append FORWARD --in-interface ens4 --out-interface sdwan0 --jump ACCEPT
sudo iptables --append FORWARD --in-interface sdwan0 --out-interface ens4 \
  --match state --state RELATED,ESTABLISHED --jump ACCEPT
sudo iptables -t nat --append POSTROUTING --out-interface sdwan0 --jump MASQUERADE
sudo apt install iptables-persistent -y   # persist across reboots
```
- `ens4` = VM's network interface (check with `ip addr`)
- `sdwan0` = the Twingate Client tun interface (created when `twingate start` runs)

**6. Twingate Resource + Group Access**
- Create a Resource in Twingate for the target private IP (e.g. `10.43.40.159`)
- Add the **service account** to a Group with access to that Resource
- Test from the router VM: `curl 10.43.40.159` should hit the Resource

**7. GCP VPC Static Route**
- Destination IP range = Twingate Resource IP/range
- Next hop = the router VM instance
- Network = same VPC as the GKE cluster

**8. Firewall Rules (GKE -> Router VM)**
- Allow inbound from GKE **node IPs** to the router VM
- Allow inbound from the **pod CIDR** to the router VM
- Find these on the GKE cluster info page

**9. Test from a Pod**
```
kubectl apply -f ubuntu.yaml   # pod with NET_ADMIN capability + sleep
kubectl exec -it ubuntu /bin/bash
apt update && apt install curl -y
curl 10.43.40.159   # should hit the Twingate Resource through the router
```

**Gotchas:**
- Network interface name on the VM is **not** always `ens4` -- check before applying iptables rules
- IP Forwarding must be enabled on the **VM (GCP setting)** AND in **Linux sysctl** -- both required
- Static route covers only the IPs in the destination range -- expand the range when adding more Twingate Resources, or create multiple routes
- Connection setup may take a few minutes after granting service account access -- wait before declaring failure
- For production, consider the **Twingate Kubernetes Operator** + Connector-in-cluster pattern instead -- the router VM is a single-VM SPOF and adds operational overhead

**Related Docs:**
- /docs/services-headless-clients -- Headless Client overview
- /docs/k8s -- K8s deployment options (Operator vs Helm vs router)
- /docs/service-accounts-guide -- Service account key management
- /docs/k8s-private-services -- Connector-in-cluster alternative for inbound access
