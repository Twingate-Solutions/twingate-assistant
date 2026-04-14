---
name: twingate-architect
description: |
  Core Twingate ZTNA architecture and design guidance. Use this skill whenever
  the user asks how Twingate works, wants to plan a Twingate deployment, needs
  to understand Twingate components, or is comparing Twingate to VPNs or other
  ZTNA solutions. Also trigger when the user mentions 'zero trust', 'ZTNA',
  'remote access architecture', or 'network design with Twingate'.
---

# Twingate Architect

## When to Use This Skill

Trigger this skill when the user:

- Asks how Twingate works, what its components are, or how it differs from a VPN
- Wants to plan a new Twingate deployment or evaluate Twingate for their environment
- Needs to understand remote network design, resource definition strategy, or connector placement
- Is comparing Twingate to other ZTNA products, mesh VPNs, or traditional perimeter access
- Mentions zero trust network access, ZTNA, least-privilege remote access, or microsegmentation
- Asks about Twingate's DNS model, encryption, NAT traversal, or P2P communication
- Needs a deployment sequence or rollout strategy
- Is troubleshooting why a resource is unreachable and the issue might be architectural

## Quick Reference

| Component | Where it runs | Role |
|---|---|---|
| Controller | Twingate cloud (SaaS) | Management plane — auth, authorization, policy |
| Client | User device | Intercepts DNS for managed resources, establishes tunnels |
| Connector | Customer's private network | Brokers access to resources, never exposes inbound ports |
| Relay | Twingate's global PoPs | NAT traversal assistance and encrypted fallback path |

**Default connection path:** P2P (direct, encrypted, lower latency)
**Fallback path:** Via Relay (encrypted, used when P2P NAT traversal fails)
**DNS scope:** Twingate only intercepts DNS for resources it explicitly manages — all other DNS resolves normally through the system resolver.

## Evergreen Knowledge

### The Four Components

**Controller**
The Controller is Twingate's cloud-hosted management plane. It hosts the admin console and GraphQL API, handles user authentication (federated to the customer's IdP), enforces authorization policy, and orchestrates key exchange between Clients and Connectors. The Controller never carries application data — it is a signaling and policy plane only. Customers interact with the Controller through the admin console at `<tenant>.twingate.com` or via the GraphQL API.

**Clients**
The Twingate Client runs on end-user devices (Windows, macOS, Linux, iOS, Android, ChromeOS). Its primary job is split DNS interception: when the OS resolves a hostname that belongs to a managed Twingate Resource, the Client intercepts that query, contacts the Controller to confirm the user is authorized, and initiates a tunnel to the appropriate Connector. For all other hostnames the Client is transparent — DNS passes through to the system resolver unchanged. The Client is the enforcement point for device-level security policy (device trust, posture checks).

**Connectors**
Connectors run inside the customer's private networks — in a VPC, on-premises data center, branch office, or any environment that can reach the resources being protected. Each Connector makes outbound connections only: it dials out to the Twingate Controller (for control plane signaling) and to Relays (for data plane coordination). No inbound firewall rules are needed. The Connector proxies traffic from authorized Clients to the backend Resources and is the data plane enforcement point at the network edge. Deploy at least two Connectors per Remote Network for high availability; Clients automatically fail over between them.

**Relays**
Relays are Twingate-operated infrastructure distributed globally across cloud PoPs. They serve two roles: (1) assisting with NAT traversal so that P2P connections can be established through restrictive NATs and firewalls, and (2) providing an encrypted fallback relay path when direct P2P is not possible. Relays never terminate application traffic in cleartext — all data passing through a Relay remains end-to-end encrypted between the Client and Connector. Customers do not deploy or manage Relays.

### Connection Flow

1. The user accesses a resource (e.g., opens SSH to `db.internal.corp` or browses to `https://internal-app.corp`)
2. The OS issues a DNS query; the Twingate Client intercepts it because it matches a managed Resource
3. The Client contacts the Controller to verify the user's identity and confirm the access policy permits this connection
4. If authorized, the Controller orchestrates key material exchange between the Client and the target Connector
5. The Client attempts to establish a direct P2P connection to the Connector using NAT traversal (STUN/ICE-like protocols, assisted by the Relay)
6. If P2P succeeds: traffic flows directly, encrypted, between Client and Connector — the Relay is no longer in the path
7. If P2P fails (e.g., symmetric NAT, restrictive firewall): traffic flows through the Relay, still encrypted end-to-end
8. The Connector proxies the traffic to the backend Resource on the customer's private network
9. The Controller continuously enforces policy — if the user's session or device trust state changes, access is revoked in real time

The Controller is only in the critical path for the handshake, not for ongoing data flow. Once the tunnel is established, data moves between Client and Connector without the Controller involved per-packet.

### Split DNS Model

Twingate's DNS model is one of its most important architectural properties. Understand it before designing any deployment.

- The Client registers itself as a DNS resolver with the OS, but only for the specific hostnames and domains that correspond to defined Twingate Resources.
- All other DNS queries are forwarded to the system's normal resolver (DHCP-assigned, manually configured, or DoH provider).
- This means Twingate is entirely invisible to traffic that doesn't match a managed Resource — no split tunneling configuration required, no proxy for internet traffic, no performance impact on non-managed hosts.
- Resources can be defined as FQDNs, CIDR ranges, or wildcard DNS patterns. FQDN and wildcard resources use DNS interception; CIDR resources use routing interception.
- The split DNS model also prevents "scope creep" problems common in VPNs where adding a route accidentally captures too much traffic.

### P2P vs. Relay Connections

Both paths are encrypted using modern cryptography (WireGuard-derived key exchange, AES-256-GCM or ChaCha20-Poly1305 symmetric encryption). P2P is preferred because it offers lower latency and does not route traffic through a third-party PoP. The Relay path is automatic fallback — customers do not configure it.

NAT traversal success depends on the NAT types on both the Client and Connector sides. Cone NATs (full cone, restricted cone, port-restricted cone) allow P2P. Symmetric NATs on both sides simultaneously block P2P and force Relay fallback. Most corporate networks use port-restricted cone NAT, which allows P2P in most cases.

If customers are consistently falling back to Relay and latency is a concern, check whether the Connector is behind symmetric NAT and consider adjusting network topology (e.g., using a cloud Connector in a VPC with a predictable NAT gateway).

### Remote Network Design Principles

A **Remote Network** in Twingate is a logical grouping of Connectors and Resources that represents a real network boundary. Map Remote Networks to actual trust boundaries, not to arbitrary groupings.

**Good mappings:**
- One Remote Network per AWS VPC
- One Remote Network per GCP VPC / Azure VNet
- One Remote Network per physical data center
- One Remote Network per branch office

**Avoid:**
- One mega Remote Network for the entire organization (couples unrelated environments, makes blast radius larger if a Connector is misconfigured)
- One Remote Network per individual server or application (creates management overhead with no security benefit; use Resource-level access policies instead for granularity)

Each Remote Network should have 2 or more Connectors for HA. Connectors within the same Remote Network are interchangeable — Clients load-balance and fail over automatically.

### Resource Definition Strategies

Define Resources at the narrowest scope that satisfies the use case. Prefer specificity.

**FQDN (recommended when DNS is reliable)**
Use when the resource has a stable, resolvable hostname. Most reliable for applications. Example: `postgres.internal.corp`, `gitlab.internal.corp`. The Client intercepts the DNS query, so the resource backend IP can change without reconfiguring Twingate.

**Wildcard DNS**
Use for dynamic subdomains or service meshes where hostnames follow a pattern. Example: `*.internal.corp`, `*.svc.cluster.local`. Scope wildcards as tightly as possible to avoid inadvertently capturing traffic you don't intend to manage.

**CIDR**
Use for subnets where you want to grant access to a range of IPs. Scope as tightly as possible — avoid `/16` or larger unless there is a genuine reason. CIDR resources are handled by routing interception, not DNS interception, so they work even without a hostname. Useful for legacy systems without DNS entries.

**IP address (last resort)**
Use only when the resource has no hostname and is a single, stable IP. IP resources are the least flexible and the hardest to maintain. Prefer FQDN or CIDR.

### Recommended Deployment Sequence

Follow this sequence for a clean rollout. Deviating from it (especially deploying Clients before Connectors and Resources are configured) creates a poor first-impression experience.

1. **Deploy Connectors** — Two or more per Remote Network, in the target environment. Verify they show as "Connected" in the admin console before proceeding.
2. **Define Resources** — Start with a small, well-understood set (e.g., a single internal app or service). Use FQDN where possible.
3. **Create Groups and assign Resources** — Map access to existing IdP groups where possible. Assign resources to groups, not to individual users.
4. **Configure Security Policies** — Set session duration, device trust requirements, MFA enforcement. Start with sensible defaults and tighten iteratively.
5. **Integrate IdP** — Configure SAML SSO and SCIM provisioning. SCIM ensures groups and users stay synchronized.
6. **Enroll test devices** — Install the Client on a small set of pilot devices. Confirm policy, DNS, and tunnel behavior.
7. **Validate access** — Test each Resource from the pilot device set. Confirm P2P vs. Relay behavior, DNS resolution, and revocation.
8. **Expand scope** — Add more Resources, Groups, and Connectors. Migrate users from VPN in cohorts.

### Encryption

All Twingate data-plane traffic is encrypted using a WireGuard-derived approach:
- Elliptic curve Diffie-Hellman (ECDH) for key exchange
- ChaCha20-Poly1305 or AES-256-GCM for symmetric encryption
- Keys are ephemeral and rotated per session
- The Relay, even as a fallback path, never sees plaintext application traffic

Control plane communication (Client ↔ Controller, Connector ↔ Controller) uses TLS 1.2+ over HTTPS/WSS.

### Comparing Twingate to VPNs

| Property | Traditional VPN | Twingate |
|---|---|---|
| Access scope | Network-level (once in, access all) | Resource-level (per-resource policy) |
| Client traffic | Often full-tunnel (all traffic goes through VPN) | Split — only managed resources intercepted |
| Inbound firewall rules | Required (VPN concentrator must accept inbound) | Not required (Connectors make outbound connections only) |
| Lateral movement risk | High — VPN grants broad network access | Low — policy enforced per resource, per group |
| Scalability | Concentrator is a bottleneck | Connectors scale horizontally, no single bottleneck |
| IdP integration | Often bolt-on or limited | Native SAML + SCIM, device trust baked in |
| Zero trust posture | No — perimeter model | Yes — identity + device + policy enforced per connection |

### When NOT to Use Twingate

- **Server-to-server communication within the same private network.** If two services are in the same VPC and can reach each other natively, don't route that traffic through Twingate. Use native networking. Twingate is for access from outside the network boundary.
- **General internet egress/proxying.** Twingate is not a web proxy or SASE platform. Exit Networks provide specific egress patterns (e.g., fixed egress IP for SaaS allowlisting), not general internet proxying for all traffic.
- **High-bandwidth bulk data transfer between cloud regions.** For large inter-region transfers, use cloud-native solutions (e.g., AWS Transit Gateway, Direct Connect). Twingate tunnels add overhead that is not justified for high-throughput storage workloads.

## Current Documentation

Reference files in `./references/` are auto-generated by the update pipeline and contain summaries of current Twingate documentation. Read them for up-to-date deployment steps, configuration syntax, and CLI commands.

If a reference file is missing or appears outdated, fetch the canonical doc directly:

```
curl -s https://www.twingate.com/docs/how-twingate-works
curl -s https://www.twingate.com/docs/architecture
curl -s https://www.twingate.com/docs/how-dns-works-with-twingate
curl -s https://www.twingate.com/docs/p2p-communication
curl -s https://www.twingate.com/docs/encryption
```

Key doc slugs for this skill:
- `how-twingate-works` — component overview and connection flow
- `architecture` — detailed system architecture
- `how-dns-works-with-twingate` — split DNS model deep dive
- `p2p-communication` — NAT traversal and P2P mechanics
- `encryption` — cryptographic details
- `twingate-vs-vpn` — comparison for evaluation conversations
- `quick-start` — first-deployment walkthrough
- `automated-deployment` — scripted and IaC deployment patterns

## Common Patterns

**Hub-and-spoke multi-cloud deployment**
One Remote Network per cloud VPC/VNet/project. Connectors deployed in each. Resources defined per network. A single IdP integration covers all networks — Groups and Security Policies apply consistently across environments.

**On-premises + cloud hybrid**
On-prem data center is its own Remote Network. Cloud environments are separate Remote Networks. Users get seamless access to resources across both without VPN split tunneling complexity.

**Replacing a legacy VPN**
Deploy Connectors in parallel with the existing VPN. Define Twingate Resources that mirror current VPN-accessible services. Migrate users in cohorts (by team or department). Validate Twingate before decommissioning VPN routes. This avoids a "big bang" cutover.

**Contractor / third-party access**
Create a dedicated Group for contractors. Assign only the specific Resources they need. Set a short session duration and strict device trust policy. SCIM ensures contractor accounts are deprovisioned when removed from the IdP.

**Service account / headless access**
For servers or CI/CD systems that need to access Twingate Resources programmatically, use the Twingate Client in headless/service mode with a service account key. Define the service account as a member of the appropriate Group.

## Anti-Patterns and Gotchas

**Over-broad CIDR resources**
Defining a `/16` or `/8` CIDR resource captures more traffic than intended and grants more access than the least-privilege principle requires. Always prefer the smallest CIDR that satisfies the use case, or use FQDNs.

**Single Connector per Remote Network**
One Connector is a single point of failure. Deploy two or more per Remote Network in different availability zones or hosts. The Client automatically load-balances and fails over.

**Deploying Clients before Connectors are healthy**
Users who install the Client and attempt access before Connectors are connected and Resources are defined will have a broken experience. Always validate the Connector and Resource configuration first.

**Assuming Relay traffic is unencrypted**
Relay fallback is encrypted end-to-end between Client and Connector. Twingate infrastructure cannot read application data in transit. Do not treat Relay vs. P2P as a security decision — treat it as a latency consideration only.

**Using Twingate as a general internet proxy**
Clients only intercept traffic matching managed Resources. Twingate does not proxy general internet traffic unless Exit Networks are explicitly configured for specific egress use cases.

**Conflating Remote Networks with security zones**
Remote Networks define connectivity scope (which Connectors serve which Resources), not security policy. Security policy is defined at the Group and Resource level. Do not attempt to implement access control purely through Remote Network topology.

**Not integrating SCIM**
Without SCIM, user and group provisioning is manual. When employees leave or change roles, their Twingate access must be updated separately from the IdP. SCIM ensures the IdP is the authoritative source of truth and deprovisioning is automatic.

**DNS split-brain conflicts**
If internal FQDNs overlap with public DNS names (e.g., `app.example.com` resolves publicly and also exists internally), ensure the Twingate Resource definition covers the right scope. The Client will intercept the query and route it to the Connector — if the Connector can't reach the backend, the connection fails. Design internal DNS namespaces to be distinct from public names where possible.

## Related Skills

- [twingate-connectors](../twingate-connectors/SKILL.md) — Connector deployment across all platforms (Docker, Linux, Kubernetes, cloud marketplaces), HA configuration, upgrades, metrics, and logging
- [twingate-identity](../twingate-identity/SKILL.md) — IdP integration (Okta, Azure AD, Google, etc.), SCIM setup, security policies, device trust, and group management
- [twingate-troubleshoot](../twingate-troubleshoot/SKILL.md) — Systematic diagnostics for connectivity failures: device, DNS, Connector, and firewall layers
- [twingate-terraform](../twingate-terraform/SKILL.md) — Terraform provider for automating Remote Network, Resource, Group, and Connector configuration as code
