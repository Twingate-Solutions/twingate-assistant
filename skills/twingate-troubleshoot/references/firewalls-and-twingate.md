## How Firewalls Work with Twingate

Conceptual reference comparing firewall roles in **VPN architectures** vs. **Twingate**. Useful for explaining to security teams why Twingate doesn't need the same firewall layer.

### Firewall Role with Traditional VPN

VPNs assign users a **local IP on the private network** -- effectively joining them to the LAN. VPNs handle **connectivity only**, not access control.

**Risk**: a user (or attacker on a compromised user device) connected via VPN has unrestricted lateral access on the network. They can:
- Port scan
- Catalog assets
- Move laterally to compromise more systems

**Mitigation**: firewalls layered on top of VPNs to enforce access controls:
- Block inbound traffic from user IPs to application/service IPs
- Allowlist specific user-IP-ranges to specific service-IP+port combos (e.g., dev team to SSH 22 on dev servers)
- Monitor outbound traffic from user IPs for scanning/anomalies

VPNs also rarely contribute to **anomaly detection** -- firewalls (and SecOps tools) handle that.

### Firewall Role with Twingate

Twingate handles **connectivity AND access control in one product**.

**Key difference**: when a user connects to Twingate, they are NOT joined to the network. The user's device gets no local IP on the private network. Instead:
- Twingate Client only allows traffic to Resources the user is **explicitly authorized** for
- Unauthorized Resource traffic **never leaves the user's device** -- it doesn't even hit the network
- Lateral attacks from a user device are virtually impossible (no presence on the network)

**Result**: Twingate replaces the firewall's role for **user-to-application flows** -- with stricter, identity-based gates than a network-IP-based firewall could provide.

### What Twingate Doesn't Replace

**Machine-to-machine flows** within the same network still benefit from firewalls:
- Application-to-application segmentation on the same subnet
- Preventing compromised app A from reaching app B
- These are handled by traditional firewalls + network segmentation

For **machine flows across networks**: Twingate **Service Accounts** + headless Client cover the same use case (e.g., CI/CD SaaS reaching on-prem service).

### SecOps & Anomaly Detection in Twingate

Twingate has **real-time connection logs** with rich detail:
- User identity (email, public IP, device info)
- Source: protocol, port, requested Resource
- Network path: Connector, Remote Network
- Context: timestamp, event type

**Recommendation**: feed these logs to a SIEM for real-time monitoring + investigative work. Twingate replaces the firewall's monitoring role for user-flow access -- but only for traffic that's authorized (denied attempts don't leave the device, so no log).

### Securing the Twingate Admin Console

Admin Console = critical surface (defines mappings between Users, Groups, Resources, Policies).

Twingate provides:
- **Dedicated Admin Console Security Policy** (separate from MAR; more frequent re-auth, mandatory 2FA -- per /docs/admin-console-security)
- **Admin Actions Report**: timestamped audit trail of every admin action -- create/delete/edit/connect across all object types

### Decision Notes

- **Firewalls + Twingate**: still valuable for machine-to-machine intra-network flows; less critical for user flows
- For greenfield deployments: design Twingate Resources tightly (specific protocols + ports) -- this is where firewall-equivalent enforcement happens
- For brownfield migrations: deploy Twingate alongside existing firewalls; tighten Resource definitions over time
- Always feed Twingate connection logs to a SIEM -- the audit trail is essential for incident response

### Gotchas

- "Twingate replaces firewalls" is half-true -- it replaces firewall-for-users, not firewall-for-machines
- Resource definitions that allow broad ports (`tcp policy=ALLOW_ALL`) lose the firewall-equivalent benefit -- always restrict to specific ports
- The Twingate Admin Actions Report is critical for compliance audits -- enable + retain accordingly

### Related Docs

- /docs/twingate-vs-vpn -- Detailed VPN vs Twingate comparison
- /docs/security-policies -- Resource Policies (the access control layer)
- /docs/security-policies-best-practices -- Risk-tier policy design
- /docs/admin-console-security -- Admin Console policy
- /docs/network-overview, /docs/exporting-network-traffic, /docs/syncing-data-to-s3 -- Connection logs + SIEM integration
- /docs/service-accounts-guide -- Machine-to-machine flows
