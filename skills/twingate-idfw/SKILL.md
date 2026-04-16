---
name: twingate-idfw
description: >
  Use when the user configures SSH with Twingate certificates, deploys the Twingate
  gateway, implements session recording, manages privileged access, installs the Twingate
  PAM module, routes kubectl through the Twingate gateway, automates Ansible with Twingate
  SSH certificates, sets up contractor or vendor SSH access, uses the
  twingate_gateway_config Terraform resource, or asks about the Identity Firewall (IDFW).
  This skill owns protocol-level identity enforcement — not just network-level access.
---

## Role

Twingate's Identity Firewall specialist. Owns the Twingate gateway — its deployment,
configuration, SSH certificate integration, Kubernetes kubectl proxy mode, session
recording, PAM setup, and contractor access patterns. The gateway enforces identity at the
protocol layer (SSH, K8s API), which is fundamentally different from connector-based
network-layer access. General Connector deployment belongs in `twingate-connectors`; IaC
generation of gateway config belongs in `twingate-terraform`.

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
- **Disable static SSH keys** alongside Twingate certificates — leaving
  `PubkeyAuthentication` enabled in `sshd_config` creates a credential bypass path that
  defeats the purpose of certificate-based authentication.
- **A single gateway instance is a SPOF** for all SSH and K8s access to the resources it
  serves — deploy at least two behind a load balancer.
- **The PAM module must be installed on every target SSH server** — the gateway validates
  the certificate before forwarding, but the target server needs PAM to complete the
  validation chain; servers without PAM may fall back to password or key auth, creating a
  bypass path.
- **The IDFW feature set is expansion-ready** — web application gating and additional
  protocols beyond SSH and K8s are on the roadmap; check the Twingate docs sitemap and
  `references/` for capabilities added since this skill was authored.

## Routing

- **→ twingate-terraform**: for `twingate_gateway_config` resource usage and provider
  setup
- **→ twingate-connectors**: for the distinction between the gateway (this skill) and
  Connectors (network layer) — and for general Connector deployment questions
- **→ twingate-kubernetes**: for K8s operator, Helm chart, and Resource routing patterns
  that complement the gateway's kubectl proxy mode
- **→ twingate-identity**: for Group membership management, JIT access, and time-bounded
  access patterns used in contractor SSH flows
- **→ twingate-architect**: for foundational questions about Remote Network topology and
  how the gateway fits into the broader Twingate deployment design
- **→ twingate-troubleshoot**: when the user reports failed SSH connections, certificate
  validation errors, or PAM configuration issues

## References

See [`references/`](./references/) for current doc summaries.
Key references: `identity-firewall-overview.md`

For gateway deployment examples, inspect `https://github.com/Twingate/gateway` — the
`deploy/` directory contains current Helm chart values, Docker Compose, and systemd
examples.
