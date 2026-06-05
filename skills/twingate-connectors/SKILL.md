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
- **Always use the rolling major-version tag, never pin to a patch version.**
  The rolling tag self-updates on restart. Pinned images accumulate
  vulnerabilities and miss bug fixes. Current tag string is in
  `references/connector-deployment.md`.
- **Scale by adding more Connectors, not by sizing up the host.** Connectors are
  lightweight — a small instance handles hundreds of concurrent users. Achieve HA through
  parallelism, not vertical scale.
- **The Connector host must have line-of-sight to backend resources.** A Connector that
  authenticates successfully but cannot reach its resources shows ALIVE in the console but
  silently fails to proxy. Always test from the Connector host, never from the user's machine.
- **`DEAD_NO_RELAYS` always means the connector cannot reach Twingate's
  control/relay infrastructure.** The most common cause is DPI/SSL inspection
  on `*.twingate.com`, but it can also be one of the required outbound ports
  being blocked. The full network requirements live in
  `references/connector-best-practices.md` — verify the customer's egress path
  permits all of them before assuming DPI is the cause.
- **Connector tokens are credentials.** Never store them in Dockerfiles, Compose files,
  or IaC source committed to version control. Inject via secrets management.
- **Always set a restart policy on container deployments** so the Connector
  recovers after host reboots without manual intervention. Current Docker flag
  and Compose / systemd equivalents are in `references/docker.md`,
  `references/deploy-connector-with-docker-compose.md`, and
  `references/systemd-service.md`.

## When to Verify

This skill body contains opinions and guidelines, not authoritative technical
facts. **Before answering questions involving any of the following, read the
relevant `references/` file first** — values change between releases and the
references are the source of truth:

- Outbound port numbers, protocols, or firewall/SG/NSG rules
- Container image tags, Helm chart values keys, or environment variable names
- Platform-specific deployment commands or Terraform/IaC field syntax
- Hardware sizing recommendations
- Connector log paths, metric names, or monitoring endpoints
- Specific upgrade or shutdown procedures

Do not answer these from training-data memory or from this skill body alone.
Open the reference, confirm the current value, and cite the file in your
response so the user can verify.

## Routing

- **→ twingate-architect**: for questions about Remote Network topology or Resource
  definition strategy
- **→ twingate-kubernetes**: for Helm chart deployment or K8s-specific Connector patterns
- **→ twingate-terraform / twingate-pulumi**: for IaC-automated token generation
- **→ twingate-troubleshoot**: when a Connector is DEAD or a user cannot reach a resource

## References

`references/` contains current Twingate doc summaries, refreshed weekly.
**Consult these before answering fact-shaped questions** — your loaded context
may be incomplete or stale.

| If the user asks about… | Read first |
|---|---|
| Network requirements, ports, firewall/SG/NSG rules, egress | `connector-best-practices.md` |
| AWS-specific deployment (ECS, EC2, EKS) | `aws-connector-patterns.md`, `aws.md`, `aws-ecs-headless-configurations.md` |
| Azure-specific deployment (ACI, VMs, AKS) | `azure-connector-patterns.md`, `azure.md` |
| GCP-specific deployment (GCE, GKE, Cloud Run, MIG) | `gcp-connector-patterns.md`, `gcp.md` |
| Docker / Docker Compose deployment | `docker.md`, `deploy-connector-with-docker-compose.md` |
| Linux / systemd deployment | `connectors-on-linux.md`, `systemd-service.md` |
| NAS, homelab, on-prem (Synology, QNAP, TrueNAS, Proxmox, Unraid, Firewalla, CasaOS, ZimaOS, Ubiquiti) | `how-to-set-up-twingate-on-a-synology-nas-dsm-7.md`, `nas-qnap-install.md`, `truenas-container-deployment.md`, `proxmox-container-deployment.md`, `unraid-getting-started.md`, `deploy-connector-on-firewalla.md`, `casaos-getting-started.md`, `zimaos-getting-started.md`, `deploy-connector-on-ubiquiti.md` |
| Connector image tag, container env vars, deployment commands | `connector-deployment.md`, `connector-metadata.md` |
| Connector upgrades | `upgrading-connectors.md` |
| `DEAD_NO_RELAYS`, `DEAD_NO_HEARTBEAT`, health diagnosis | `connector-real-time-logs.md`, `connector-monitoring.md`, `connector-health-checks.md` |
| Logs, metrics, monitoring, SIEM integration | `connector-metrics.md`, `connector-monitoring.md`, `connector-real-time-logs.md`, `siem-guide.md` |
| Hardware sizing, HA topology | `connector-best-practices.md` |
| Headless / service account clients | `services-headless-clients.md`, `aws-ecs-headless-configurations.md` |
| Connector shutdown, restart, lifecycle | `connector-shutdown-process.md`, `advanced-connector-management.md` |

For comprehensive coverage, see [`references/`](./references/) for the full
set of doc summaries. **Default to checking** — do not answer port-level,
command-syntax, or version questions from memory.
