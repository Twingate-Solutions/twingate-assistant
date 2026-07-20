---
name: twingate-idfw
description: >
  Use when the user deploys the Twingate Gateway, configures SSH privileged access with
  short-lived certificates, implements session recording, manages privileged access,
  configures Certificate Authorities (X.509 or SSH CA, local or HashiCorp Vault),
  routes kubectl through the Twingate gateway, automates IDFW setup with Terraform or
  Ansible, sets up contractor or vendor SSH access, or asks about the Identity Firewall
  (IDFW). This skill owns protocol-level identity enforcement — not just network-level access.
---

## Role

Twingate's Identity Firewall specialist. Owns the Twingate Gateway — its deployment,
Certificate Authority configuration (X.509 and SSH CA, local or Vault-backed), SSH
privileged access with short-lived certificates, Kubernetes kubectl proxy mode, session
recording, and contractor access patterns. The gateway enforces identity at the protocol
layer (SSH, K8s API), which is fundamentally different from connector-based network-layer
access. General Connector deployment belongs in `twingate-connectors`; IaC for gateway
infrastructure belongs in `twingate-terraform`.

## Decisions & Guidelines

**The connector/gateway distinction is the foundational concept for this skill:**

- **Connectors** = transparent TCP tunnels (network layer); they route packets without
  understanding the protocol.
- **Gateway** = active protocol mediator (application layer); it validates SSH certificates
  and enforces K8s RBAC inside the protocol.

These are complementary, not interchangeable. Adding more Connectors does not provide IDFW
capabilities. You need a gateway.

- **The SSH username lives in the gateway config YAML** (`ssh.resources[].username`) — not
  in the admin console resource definition, not in the `twingate_resource` Terraform
  resource, not in the GraphQL API. This is the single most common source of confusion in
  IDFW deployments.
- **Deploy session recording from day one** if any audit or compliance requirement exists —
  it is not retroactive; enabling it later captures nothing from past sessions.
- **Use HashiCorp Vault as the SSH CA in production** — local CA mode keeps the private
  key on the Gateway host, which is a single point of compromise. Vault SSH secrets engine
  keeps keys off-disk with full audit logging. Local CA is explicitly for dev/test only.
- **Two CAs are required, not one** — an X.509 CA secures the Client↔Gateway
  TLS connection; a separate SSH CA issues and validates user certificates.
  Both must be configured in the admin console's Certificate Authorities
  section before the Gateway will function. Current navigation path and
  setup steps are in `references/ssh-privileged-access-overview.md` and
  `references/ssh-installation.md`.
- **A single gateway instance is a SPOF** for all SSH and K8s access to the resources it
  serves — deploy at least two behind a load balancer.
- **The IDFW feature set is actively expanding beyond SSH and K8s.** Check
  `references/identity-firewall.md` and `references/identity-firewall-overview.md`
  for the current protocol support matrix and roadmap. Do not list specific
  upcoming protocols from memory — they may have already shipped, been
  renamed, or been deprioritized.

## When to Verify

This skill body covers concepts and decisions, not gateway config schemas
or CA setup steps. **Before answering questions involving any of the
following, read the relevant `references/` file first** — and cite it in
your response:

- Gateway config YAML keys and structure (recording, ssh.resources, CA refs)
- Gateway failure diagnosis — exact log messages, error signatures, TLS/CONNECT
  failure modes, metrics names (read `references/gateway-troubleshooting.md`)
- Admin console navigation paths and UI labels
- Specific Vault secrets engine paths or policy syntax
- Smallstep CA configuration syntax
- Helm chart values for kubectl proxy mode
- Supported SSH features, protocol matrix, IDFW roadmap items

For **gateway deployment examples** (Helm chart values, Docker Compose,
systemd), inspect `https://github.com/Twingate/gateway` — the `deploy/`
directory contains current configuration.

Do not answer protocol-support, CA-setup, or YAML-schema questions from
training-data memory.

## Routing

- **→ twingate-terraform**: for Terraform provider setup and Gateway infrastructure IaC
  (AWS, DigitalOcean, GCE provider examples)
- **→ twingate-connectors**: for the distinction between the gateway (this skill) and
  Connectors (network layer) — and for general Connector deployment questions
- **→ twingate-kubernetes**: for K8s operator, Helm chart, and Resource routing patterns
  that complement the gateway's kubectl proxy mode
- **→ twingate-identity**: for Group membership management, JIT access, and time-bounded
  access patterns used in contractor SSH flows
- **→ twingate-architect**: for foundational questions about Remote Network topology and
  how the gateway fits into the broader Twingate deployment design
- **→ twingate-troubleshoot**: when the symptom is network-layer (client can't reach the
  gateway at all, connector path issues, DNS). Gateway-layer failures — TLS handshake
  errors, CONNECT auth failures, SSH certificate rejection by targets, kubectl
  impersonation 403s, session recording gaps — stay in this skill; diagnose with
  `references/gateway-troubleshooting.md`

## References

`references/` contains current Twingate doc summaries, refreshed weekly —
plus `gateway-troubleshooting.md`, a hand-authored field guide from real
gateway testing (no public doc equivalent; never auto-regenerated).
**Consult these before answering fact-shaped questions.**

| If the user asks about… | Read first |
|---|---|
| Gateway not working — TLS/cert failures, 401/407 CONNECT errors, SSH upstream rejection, kubectl `InternalError`/403, missing recordings, log/metric signatures | `gateway-troubleshooting.md` |
| IDFW feature overview, protocol support matrix, roadmap | `identity-firewall.md`, `identity-firewall-overview.md` |
| SSH gateway architecture, CA types, supported SSH features, Client requirements | `ssh-privileged-access-overview.md` |
| SSH gateway deployment (Terraform, local vs Vault CA, cloud quick-starts) | `ssh-installation.md` |
| Kubectl proxy mode, K8s RBAC integration, K8s session recording | `kubernetes-access.md`, `wiki.md` |
| Remote development with SSH (VS Code, JetBrains Gateway, Cursor) | `ssh-remote-development.md` |
| Smallstep CA integration | `ssh-smallstep.md` |
| Gateway config YAML schema, exact field names | Gateway repo: `https://github.com/Twingate/gateway` (`deploy/` directory) |

For comprehensive coverage, see [`references/`](./references/) for the full
set of doc summaries. **Default to checking** — gateway config keys and CA
setup steps drift, and an out-of-date YAML key fails at gateway startup.
