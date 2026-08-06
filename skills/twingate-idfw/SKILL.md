---
name: twingate-idfw
description: >
  Use when the user deploys the Twingate Gateway, configures SSH privileged access with
  short-lived certificates, implements session recording, manages privileged access,
  configures Certificate Authorities (X.509 or SSH CA, local or HashiCorp Vault),
  routes kubectl through the Twingate gateway, automates IDFW setup with Terraform or
  Ansible, sets up contractor or vendor SSH access, or asks about the Identity Firewall
  (IDFW). This skill owns protocol-level identity enforcement — not just network-level
  access. Also activate for: session-recording playback/archival (asciicast, .cast files),
  reviewing recorded SSH or kubectl sessions for dangerous commands or leaked secrets, or
  self-hosting a session-recording ingest/browse UI for Gateway audit logs.
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
- **The Gateway itself is the only production-supported component here.** Session-recording
  *playback/archival* tooling (e.g. `gh-twingate-solutions-gatorcast.md`) is explicitly an
  example/reference project with no warranty — recommend it for self-hosted review of
  existing recordings, but tell the user it is not a supported Twingate product before they
  put it in a compliance-critical path.

## Search References First

**Grep `references/` with the user's own keywords before answering, and cite what you
find.** Filenames reveal only the topic — Helm value names, env vars, and error strings
live in the file bodies, so a filename scan alone will miss them:

```
grep -ril "asciicast" references/      # -> gh-twingate-gateway-wiki.md, gh-twingate-gateway.md, gh-twingate-solutions-gatorcast.md
grep -ril "vault" references/          # -> ssh-privileged-access-overview.md, ssh-installation.md
grep -ril "prometheus" references/     # -> gh-twingate-gateway-wiki.md
```

Never answer from training-data memory for: gateway config YAML keys and structure
(recording, ssh.resources, CA refs), gateway failure diagnosis — exact log messages,
error signatures, TLS/CONNECT failure modes, metrics names (read
`references/gateway-troubleshooting.md`), admin console navigation paths and UI labels,
Vault secrets engine paths or policy syntax, Smallstep CA configuration syntax, Helm
chart values for kubectl proxy mode or session recording, or the supported SSH/protocol
matrix and IDFW roadmap. Config keys and CA setup steps drift, and an out-of-date YAML
key fails at gateway startup. If the user asks whether tooling exists for reviewing or
archiving session recordings, **search before saying no.**

For the **Gateway's own Helm chart values and deploy examples**, `gh-twingate-gateway-wiki.md`
and `gh-twingate-gateway.md` summarize the repo and its wiki; for exact current YAML keys,
inspect `https://github.com/Twingate/gateway` (`deploy/` directory) directly.

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

See [`references/`](./references/) for the current corpus, refreshed weekly. Two kinds
of file live there, plus one hand-authored field guide:

- **`gateway-troubleshooting.md`** — hand-authored field guide from real gateway testing.
  No public doc equivalent; never auto-regenerated.
- **`{slug}.md`** — summaries of `twingate.com/docs` pages (product documentation).
- **`gh-{org}-{repo}.md`** — summaries of the Gateway's own GitHub repo/wiki and
  community/SE tooling built on top of its session recordings.

| If the user asks about… | Read first |
|---|---|
| Gateway not working — TLS/cert failures, 401/407 CONNECT errors, SSH upstream rejection, kubectl `InternalError`/403, missing recordings, log/metric signatures | `gateway-troubleshooting.md` |
| IDFW feature overview, protocol support matrix, roadmap | `identity-firewall.md`, `identity-firewall-overview.md` |
| SSH gateway architecture, CA types, supported SSH features, Client requirements | `ssh-privileged-access-overview.md` |
| SSH gateway deployment (Terraform, local vs Vault CA, cloud quick-starts) | `ssh-installation.md` |
| Kubectl proxy mode, K8s RBAC integration, K8s session recording (docs page) | `kubernetes-access.md` |
| **Gateway repo/wiki** — protocol support (K8s/SSH/Web App coming soon), GAT auth flow, identity propagation, asciicast v2 session recording, Prometheus metrics, Helm chart values, Docker image | `gh-twingate-gateway.md`, `gh-twingate-gateway-wiki.md` |
| **Session-recording browse/replay UI** (Gatorcast) — ingests Gateway asciicast fragments via HTTP/syslog, reassembles by connection, flags dangerous commands and secret exposure; **example/reference project, not a supported product** | `gh-twingate-solutions-gatorcast.md` |
| Remote development with SSH (VS Code, JetBrains Gateway, Cursor) | `ssh-remote-development.md` |
| Smallstep CA integration | `ssh-smallstep.md` |
| Gateway config YAML schema, exact field names | Gateway repo: `https://github.com/Twingate/gateway` (`deploy/` directory) |

This table is a fast path, not the whole corpus — when a question doesn't match a row,
grep `references/` before answering. Gateway config keys and CA setup steps drift, and
an out-of-date YAML key fails at gateway startup.
