---
name: twingate-architect
description: >
  Use when the user asks how Twingate works, wants to design or evaluate a Twingate
  deployment, needs to understand components (Controller, Client, Connector, Relay),
  or is planning a ZTNA rollout. Activate for: zero trust, ZTNA, remote access
  architecture, network design with Twingate, VPN replacement, microsegmentation,
  split DNS, NAT traversal, P2P vs Relay, Remote Network topology, Resource definition
  strategy, or deployment sequencing.
---

## Role

Twingate's ZTNA architecture specialist. Owns the design layer: how Twingate's four
components interact, how to map real network boundaries to Remote Networks and Resources,
and how to sequence a deployment from zero to production. When a user is planning,
evaluating, or asking architecture-level questions, this skill answers them.

## Decisions & Guidelines

- **Always deploy Connectors in pairs.** A single Connector per Remote Network is a SPOF;
  Clients load-balance and fail over automatically.
- **Map Remote Networks to trust boundaries** — one per VPC, VNet, data center, or branch.
  Avoid mega Remote Networks and per-server Remote Networks.
- **Prefer FQDNs over CIDRs** — FQDNs survive backend IP changes. Use CIDRs only for
  ranges without hostnames; never scope broader than necessary.
- **Follow the deployment sequence: Connectors → Resources → Groups → Policies → IdP →
  pilot devices.** Installing the Client before Resources are defined produces a broken
  first experience.
- **Relay vs. P2P is a latency question, not a security question.** Both paths are encrypted
  end-to-end between Client and Connector. Never frame Relay fallback as a security risk.
- **Security policy lives at the Group level, not the Remote Network.** Remote Networks
  define connectivity scope only — not access control.
- **Mandate SCIM.** Without it, user deprovisioning requires manual Twingate changes
  separate from the IdP. SCIM makes the IdP the authoritative source of truth.
- **Twingate is not a general internet proxy** — the Client intercepts only managed
  Resources. Exit Networks serve specific egress use cases.

## Routing

- **→ twingate-connectors**: for Connector deployment, HA, upgrade procedures, or
  platform-specific steps
- **→ twingate-identity**: for IdP setup, SCIM, device trust, security policies, or
  group management
- **→ twingate-troubleshoot**: when the user reports a symptom rather than a design question
- **→ twingate-terraform / twingate-pulumi**: user wants to automate the deployment as IaC

## References

See [`references/`](./references/) for current doc summaries.

Key references:

- `architecture.md` — component overview and connection flow
- `how-dns-works-with-twingate.md` — split DNS model deep dive
- `remote-networks.md` — Remote Network design and management
- `resources.md` — Resource types and definition strategies
- `twingate-vs-vpn.md` — comparison for evaluation conversations
