## How to Protect Your Home Lab with Twingate

End-to-end homelab setup guide covering Remote Network and Connector deployment, Resource creation (CIDR or DNS pattern), user/group organization, and Security Policies. Demonstrates moving from a single broad "Everything" resource to per-service Resources scoped by group role, replacing port forwarding and VPN server entirely.

**Key Information**
- Connector footprint: 2GB RAM, 2 vCPUs; can run on NAS (Docker/systemd), Raspberry Pi, Linux VM, or Windows (Docker/Hyper-V)
- Two Connectors per Remote Network recommended for HA and load balancing; only one is required
- Resources can be defined as: IP address, CIDR range (e.g. `192.168.100.0/24`), or DNS wildcard pattern (e.g. `*.int`)
- Use IP-style Resources if users connect by IP; use DNS-style if they use FQDNs; use both if needed
- Groups as roles pattern: Standard Users, Power Users, Admin Users -- each with different Resource access
- Security Policies control: re-auth frequency, 2FA requirement, device verification requirements
- Default policy is auto-applied to all groups; custom policies can override per group

**Prerequisites**
- Twingate account (free tier sufficient for homelabs)
- Twingate Client installed on admin device
- At least one device in the home network to host the Connector

**Step-by-Step**
1. Create Remote Network (On Premise location) in Admin Console
2. Deploy Connector on a device inside the home network (NAS, Pi, Linux VM, etc.)
3. Create a broad "Everything" Resource (CIDR or DNS pattern) assigned to Everyone group -- verify access
4. Invite family/friend users; create Groups (Standard Users, Power Users, Admin Users); add users to groups
5. Map each service (host:port) to appropriate groups; create per-service Resources; remove "Everything"
6. Optionally configure custom Security Policies per group for 2FA and device trust

**Gotchas**
- No need to create one Connector per Resource -- a single Connector serves all Resources in the Remote Network
- After deploying the Connector and creating Resources, remove all router port forwarding rules and shut down the VPN server
- Combine services on the same host into one Resource when the port ranges and group access are identical

**Related Docs**
- /docs/resources
- /docs/remote-networks
- /docs/security-policies
- /docs/connector-deployment
- /docs/private-dns-best-practices
