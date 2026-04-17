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
- **Two CAs are required, not one** — an X.509 CA secures the Client↔Gateway TLS
  connection; a separate SSH CA issues and validates user certificates. Both must be
  configured under Settings → Certificate Authorities before the Gateway will function.
- **A single gateway instance is a SPOF** for all SSH and K8s access to the resources it
  serves — deploy at least two behind a load balancer.
- **The IDFW feature set is actively expanding** — HTTPS, databases, and MCP are on the
  roadmap beyond SSH and K8s. Check `references/identity-firewall.md` and the live docs
  for protocols added since this skill was authored.

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
- **→ twingate-troubleshoot**: when the user reports failed SSH connections or certificate
  validation errors

## References

See [`references/`](./references/) for current doc summaries.

Key references:

- `identity-firewall.md` — IDFW feature overview, protocol support matrix, roadmap
- `ssh-privileged-access-overview.md` — Gateway architecture, CA types, supported SSH features, Client version requirements
- `ssh-installation.md` — Terraform-based deployment, local vs Vault CA modes, cloud quick-starts
- `kubernetes-access.md` — kubectl proxy mode, K8s RBAC integration, session recording
- `ssh-remote-development.md` — VS Code, JetBrains Gateway, Cursor IDE setup
- `ssh-smallstep.md` — Smallstep CA integration for certificate signing

For gateway deployment examples, inspect `https://github.com/Twingate/gateway` — the
`deploy/` directory contains current Helm chart values, Docker Compose, and systemd
examples.
