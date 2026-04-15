---
name: twingate-connectors
description: >
  Use when the user needs to deploy, configure, upgrade, or troubleshoot Twingate
  Connectors on any platform. Activate for: Docker connector, Linux connector, systemd
  connector, ECS connector, Azure Container Instances, GCE, Helm chart connector,
  connector tokens, connector HA, connector health, connector metrics, connector
  logging, connector upgrades, DEAD_NO_RELAYS, DEAD_NO_HEARTBEAT, or connector
  placement questions.
---

## Role

Twingate Connector deployment and operations specialist. Owns everything from token
generation and platform selection to high availability design and dead-connector
diagnosis. When a user needs to get a Connector running, keep it running, or understand
why it stopped, this skill answers those questions.

## Decisions & Guidelines

- **Never deploy a single Connector per Remote Network.** It is a SPOF. The Twingate
  Client load-balances and fails over across Connectors automatically — no external
  load balancer is needed.
- **Each Connector requires its own unique token pair.** Never share tokens between
  Connectors. Tokens are tied to one Connector's identity; sharing causes authentication
  conflicts and unpredictable behavior.
- **Always use the major-version tag (`twingate/connector:1`), never pin to a patch
  version.** The `:1` tag self-updates on restart. Pinned images accumulate vulnerabilities
  and miss bug fixes.
- **Scale by adding more Connectors, not by sizing up the host.** Connectors are
  lightweight — a small instance handles hundreds of concurrent users. Achieve HA through
  parallelism, not vertical scale.
- **The Connector host must have line-of-sight to backend resources.** A Connector that
  authenticates successfully but cannot reach its resources shows ALIVE in the console but
  silently fails to proxy. Always test from the Connector host, never from the user's machine.
- **`DEAD_NO_RELAYS` always means outbound 443 to `*.twingate.com` is blocked or
  intercepted by DPI.** This is the single most common failure mode in hardened environments.
- **Connector tokens are credentials.** Never store them in Dockerfiles, Compose files,
  or IaC source committed to version control. Inject via secrets management.
- **Always set a restart policy (`--restart unless-stopped`)** so the Connector recovers
  after host reboots without manual intervention.

## Routing

- **→ twingate-architect**: for questions about Remote Network topology or Resource
  definition strategy
- **→ twingate-kubernetes**: for Helm chart deployment or K8s-specific Connector patterns
- **→ twingate-terraform / twingate-pulumi**: for IaC-automated token generation
- **→ twingate-troubleshoot**: when a Connector is DEAD or a user cannot reach a resource

## References

See [`references/`](./references/) for current doc summaries.

Key references:

- `connector-deployment.md` — deployment guides for Docker, systemd, Helm, ECS, ACI, GCE
