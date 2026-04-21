## Site-to-Site Connectivity with Twingate

Guide to building site-to-site network connectivity using a Twingate Connector + headless Client on a "router VM" at each site. Each site hosts a Connector (for incoming access) and a headless Client VM (for outbound routing via iptables/MASQUERADE), enabling bidirectional traffic between private subnets without site-to-site VPN tunnels. Demonstrated with Azure (site 1) and GCP (site 2).

**Key Information**
- Architecture per site: one Connector VM (no public IP; NAT/Cloud NAT for outbound) + one router VM running headless Twingate Client with IP forwarding
- Service Accounts authenticate the headless Clients; each site's Service Account is granted access to the other site's Resources
- IP forwarding on router VM: uncomment `net.ipv4.ip_forward=1` in `/etc/sysctl.conf`; run `sysctl -p`
- iptables on router VM: FORWARD and MASQUERADE rules on `sdwan0` (Twingate virtual interface)
- Cloud routing tables must be configured to route each site's subnet CIDR through the router VM
- Connector and router VMs do NOT need public IP addresses; use NAT gateway (Azure) or Cloud NAT (GCP) for outbound

**Prerequisites**
- Twingate account with Service Accounts support (Enterprise plan)
- Two separate cloud networks (or any two private networks)
- Linux VMs for Connector and router at each site

**Key iptables Commands (router VM)**
```bash
# Replace ens4/eth0 with internal interface, sdwan0 is Twingate's virtual interface
sudo iptables -A FORWARD -i <internal_iface> -o sdwan0 -j ACCEPT
sudo iptables -A FORWARD -i sdwan0 -o <internal_iface> -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -t nat -A POSTROUTING -o sdwan0 -j MASQUERADE
sudo apt install iptables-persistent -y   # persist across reboots
```

**Headless Client Setup**
```bash
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
sudo twingate setup --headless /path/to/service_key.json
sudo twingate start
```

**Gotchas**
- GCP requires IP forwarding enabled at VM creation time (not just via sysctl) -- check "IP forwarding" in VM settings
- Cloud NAT must be set up before deploying the router VM; without it the install commands won't reach the internet
- P2P connections are important for performance and Fair Use Policy compliance -- configure P2P support

**Related Docs**
- /docs/linux-headless
- /docs/service-accounts-guide
- /docs/local-peer-to-peer-best-practices
- /docs/connector-deployment
