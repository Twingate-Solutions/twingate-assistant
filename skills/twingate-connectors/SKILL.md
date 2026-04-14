---
name: twingate-connectors
description: |
  Twingate connector deployment, management, and troubleshooting. Use this skill
  whenever the user needs to deploy, upgrade, monitor, or troubleshoot Twingate
  connectors. Trigger on mentions of: connectors, connector deployment, Docker
  connector, Linux connector, systemd connector, Helm chart connector,
  AWS/Azure/GCP connector, connector tokens, connector health, connector metrics,
  connector logging, connector upgrades, or high availability.
---

# Twingate Connectors

## When to Use This Skill

- User needs to deploy a connector on any platform (Docker, Linux, Kubernetes, AWS, Azure, GCP)
- User asks how connectors work, how they authenticate, or how they connect to the control plane
- User is debugging a connector that shows DEAD, is not reachable, or is failing to connect
- User asks about connector HA, load balancing, or failover
- User needs to upgrade connectors or manage connector versions
- User wants to monitor connector health, metrics, or logs
- User asks about connector tokens, token generation, or token rotation
- User is automating connector deployment with Terraform, Ansible, or other tooling
- User asks about connector placement, network requirements, or firewall rules

## Quick Reference

| Property | Value |
|---|---|
| Docker image | `twingate/connector:1` |
| Image tag policy | Always use major-version tag (`:1`), never pin to patch |
| Required env vars | `TWINGATE_NETWORK`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN` |
| Inbound ports required | None — connectors are outbound-only |
| Outbound requirement | HTTPS (443) to `*.twingate.com` |
| Minimum per remote network | 2 connectors for HA |
| Token source | `connectorGenerateTokens` GraphQL mutation or admin console |
| Connector states | `ALIVE`, `DEAD_NO_HEARTBEAT`, `DEAD_HEARTBEAT_TOO_OLD`, `DEAD_NO_RELAYS` |

## Evergreen Knowledge

### Stateless and Outbound-Only Architecture

Connectors are stateless. They initiate only outbound connections — to the Twingate Controller for control plane operations, and to Twingate Relays for data plane coordination. No inbound firewall rules are ever required on the connector host or its network. This is architecturally significant: customers can deploy connectors behind NAT, in locked-down cloud VPCs, or on-premises without opening any firewall ports inbound. This is a key selling point when customers push back on firewall complexity.

Because the connector is stateless, it holds no session state itself. Sessions are brokered by the Controller. If a connector restarts, clients reconnect automatically.

### High Availability: Always Deploy 2+ Connectors

A single connector is a single point of failure. Always deploy at least two connectors per Remote Network. The Twingate client performs automatic load balancing across available connectors and fails over transparently when a connector goes unreachable. Customers often ask whether they need a load balancer in front of connectors — they do not. The client handles this natively.

For production environments recommend named, labeled connector pairs with monitoring on both.

### Connector Tokens

Each connector requires its own unique access token and refresh token pair. Tokens are generated via:

- The `connectorGenerateTokens` mutation in the Twingate GraphQL API (preferred for automation)
- The Twingate admin console (manual, for one-off deployments)

Tokens are sensitive credentials. Treat them with the same care as API keys or passwords. Use secrets management tooling (AWS Secrets Manager, HashiCorp Vault, Kubernetes Secrets) to inject tokens at runtime — never hardcode them in Dockerfiles, scripts, or IaC source files committed to version control.

Token pairs cannot be retrieved after initial generation. If a token is lost, generate a new pair and redeploy.

### Deployment Methods

Connectors are distributed as a Docker container image and support multiple deployment patterns:

| Method | Use Case |
|---|---|
| Docker container | Most common; any host with Docker installed |
| Linux systemd service | Native Linux install without Docker |
| Kubernetes via Helm chart | K8s-native environments |
| AWS ECS task | Teams already using ECS; runs in target VPC |
| Azure Container Instances (ACI) | Azure-native deployments |
| GCE instance or Cloud Run | GCP environments |

The Docker container is the most widely used and recommended approach for its simplicity and portability. Platform-specific deployment guides exist for all supported targets — see Current Documentation below.

### Key Environment Variables

| Variable | Required | Description |
|---|---|---|
| `TWINGATE_NETWORK` | Yes | Tenant name — e.g. `mycompany` for `mycompany.twingate.com` |
| `TWINGATE_ACCESS_TOKEN` | Yes | Access token from `connectorGenerateTokens` |
| `TWINGATE_REFRESH_TOKEN` | Yes | Refresh token from `connectorGenerateTokens` |
| `TWINGATE_LABEL_DEPLOYED_BY` | No | Label for tracking deployment source (e.g. `terraform`, `ansible`) |
| `TWINGATE_TIMESTAMP_FORMAT` | No | Set to `2` for human-readable log timestamps (recommended) |

Labels set via `TWINGATE_LABEL_DEPLOYED_BY` and other `TWINGATE_LABEL_*` variables appear in the admin console and are queryable via the API. Use labels consistently to distinguish connectors by environment, region, or deployment method.

### Docker Deployment

Standard single-host Docker deployment:

```bash
docker run -d \
  --name twingate-connector \
  -e TWINGATE_NETWORK="<tenant>" \
  -e TWINGATE_ACCESS_TOKEN="<access-token>" \
  -e TWINGATE_REFRESH_TOKEN="<refresh-token>" \
  --restart unless-stopped \
  twingate/connector:1
```

Always include `--restart unless-stopped` so the connector automatically recovers after host reboots or container crashes.

### Image Tag Policy

Use `twingate/connector:1` — the major-version tag. This tag always resolves to the latest stable patch within the major version. Twingate pushes patch updates automatically, so connectors on the `:1` tag self-update on restart or `docker pull`. Do not pin to a specific patch version (e.g., `twingate/connector:1.2.3`) unless debugging a regression — pinned images accumulate security vulnerabilities and miss bug fixes.

### Connector States

The Twingate admin console and GraphQL API report connector state:

| State | Meaning |
|---|---|
| `ALIVE` | Healthy; connector is connected and sending heartbeats |
| `DEAD_NO_HEARTBEAT` | Connector process is not sending heartbeats — likely down or unreachable |
| `DEAD_HEARTBEAT_TOO_OLD` | Last heartbeat is stale — possible network interruption or process crash |
| `DEAD_NO_RELAYS` | Connector cannot reach any Twingate Relay — outbound path to `*.twingate.com:443` is blocked |

`DEAD_NO_RELAYS` is the most common state when outbound connectivity is restricted. Check that the connector host can reach Twingate infrastructure on port 443.

### Network Requirements

- **Outbound HTTPS (443)** to `*.twingate.com` — required for both control plane (Controller) and data plane (Relays)
- **No inbound ports** — connectors never accept inbound connections
- **Line-of-sight to backend resources** — the connector host must be able to route to the private IPs or FQDNs of the Resources it serves

The line-of-sight requirement is the most commonly missed placement issue. A connector placed in a DMZ that cannot reach internal services will authenticate successfully but fail to proxy traffic. Place the connector in the same network segment as the resources, or ensure routing exists between the connector host and those resources.

### Connector Placement

Design connector placement around resource reachability:

- **VPC/VNet resources**: Deploy the connector as an instance or container inside the VPC/VNet with access to private subnets
- **On-premises resources**: Deploy the connector on the corporate LAN or a segment with routes to internal services
- **Multi-region**: Deploy a separate Remote Network and connector pair per region — do not use a single connector to proxy resources across WAN links (adds latency and creates a chokepoint)
- **Kubernetes workloads**: Use the Helm chart to deploy the connector inside the cluster so it can reach cluster-internal services via `ClusterIP` or DNS

## Current Documentation

For current deployment steps, configuration syntax, and CLI commands, read the reference files in `./references/`.

If a reference file is missing or appears outdated, fetch the doc directly:

```bash
curl -s https://www.twingate.com/docs/connector
curl -s https://www.twingate.com/docs/connector-deployment
curl -s https://www.twingate.com/docs/connector-upgrades
curl -s https://www.twingate.com/docs/connector-health
curl -s https://www.twingate.com/docs/connector-metrics
curl -s https://www.twingate.com/docs/connector-logging
curl -s https://www.twingate.com/docs/connector-best-practices
```

Key doc slugs:

| Slug | Content |
|---|---|
| `connector` | Overview, quickstart, architecture |
| `connector-deployment` | Platform-specific deployment guides (Docker, Linux, K8s, AWS, Azure, GCP) |
| `connector-upgrades` | Upgrade procedures and version management |
| `connector-health` | Health metrics, monitoring, and status checks |
| `connector-metrics` | Prometheus-compatible metrics endpoint |
| `connector-logging` | Log configuration, formats, and log levels |
| `connector-best-practices` | HA design, labeling conventions, naming standards |

## Common Patterns

### 1. Docker with Restart Policy (Standard Single-Host)

The baseline deployment for any host with Docker:

```bash
docker run -d \
  --name twingate-connector \
  -e TWINGATE_NETWORK="mycompany" \
  -e TWINGATE_ACCESS_TOKEN="<access-token>" \
  -e TWINGATE_REFRESH_TOKEN="<refresh-token>" \
  -e TWINGATE_TIMESTAMP_FORMAT=2 \
  -e TWINGATE_LABEL_DEPLOYED_BY=docker \
  --restart unless-stopped \
  twingate/connector:1
```

Deploy this command twice (with separately generated token pairs) to achieve HA.

### 2. Kubernetes via Helm Chart

For K8s-native environments, use the official Helm chart from the `Twingate/helm-charts` repository:

```bash
helm repo add twingate https://twingate.github.io/helm-charts
helm repo update

helm install twingate-connector twingate/connector \
  --set connector.network="mycompany" \
  --set connector.accessToken="<access-token>" \
  --set connector.refreshToken="<refresh-token>"
```

Deploy two Helm releases (with separate token pairs) for HA. Consider placing them on separate nodes using pod anti-affinity rules to prevent both failing on a single node failure. See `twingate-kubernetes` skill for full K8s-specific guidance.

### 3. AWS ECS Fargate Task

For teams using ECS, run the connector as a Fargate task in the target VPC. Store tokens in AWS Secrets Manager and inject them as environment variables via the ECS task definition's `secrets` field. The task runs in the private subnet with outbound internet access via NAT Gateway.

Key task definition settings:
- `networkMode: awsvpc`
- `requiresCompatibilities: [FARGATE]`
- Assign to private subnet(s) with NAT Gateway for outbound `*.twingate.com:443`
- Use `secrets` referencing Secrets Manager ARNs for `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN`

### 4. Terraform-Automated Token Generation

Use the `twingate_connector` and `twingate_connector_tokens` resources to fully automate connector creation:

```hcl
resource "twingate_connector" "main" {
  remote_network_id = twingate_remote_network.vpc.id
  name              = "prod-connector-1"
}

resource "twingate_connector_tokens" "main" {
  connector_id = twingate_connector.main.id
}
```

Pass `twingate_connector_tokens.main.access_token` and `.refresh_token` directly into ECS task definitions, EC2 user data, or ACI environment variables. Never write token values to state output blocks — keep them internal to the module. See `twingate-terraform` skill for full provider usage.

### 5. HA Pair with Labels

Deploy two connectors with consistent labels for tracking and monitoring:

```bash
# Connector 1
docker run -d \
  --name twingate-connector-1 \
  -e TWINGATE_NETWORK="mycompany" \
  -e TWINGATE_ACCESS_TOKEN="<token-1-access>" \
  -e TWINGATE_REFRESH_TOKEN="<token-1-refresh>" \
  -e TWINGATE_LABEL_DEPLOYED_BY=ansible \
  -e TWINGATE_LABEL_REGION=us-east-1 \
  --restart unless-stopped \
  twingate/connector:1

# Connector 2 — separate token pair
docker run -d \
  --name twingate-connector-2 \
  -e TWINGATE_NETWORK="mycompany" \
  -e TWINGATE_ACCESS_TOKEN="<token-2-access>" \
  -e TWINGATE_REFRESH_TOKEN="<token-2-refresh>" \
  -e TWINGATE_LABEL_DEPLOYED_BY=ansible \
  -e TWINGATE_LABEL_REGION=us-east-1 \
  --restart unless-stopped \
  twingate/connector:1
```

Query both connector states via the GraphQL API or monitor in the admin console to ensure both remain `ALIVE`.

## Anti-Patterns and Gotchas

**Single connector per Remote Network.** A single connector is a single point of failure. If it goes down, all access to that Remote Network's resources is lost. Always deploy at least two connectors per Remote Network.

**Reusing tokens across connectors.** Each connector must have its own unique token pair generated by a separate `connectorGenerateTokens` call. Sharing tokens between two connectors causes authentication conflicts and unpredictable behavior.

**Pinning to a patch version tag.** Using `twingate/connector:1.2.3` instead of `twingate/connector:1` means the connector never receives security patches or bug fixes unless manually updated. Use the major-version tag.

**Connector placed without resource line-of-sight.** A connector in a DMZ, isolated subnet, or separate VPC without routes to the backend resources will show `ALIVE` in the admin console but fail to proxy traffic. Always verify the connector host can reach target resources before declaring the deployment complete.

**Outbound port 443 blocked.** Many hardened environments restrict outbound HTTPS. If the connector shows `DEAD_NO_RELAYS`, check that `*.twingate.com:443` is reachable from the connector host. This includes wildcard DNS resolution — some environments block wildcard TLS or use split-horizon DNS that breaks resolution of Twingate relay hostnames.

**Storing tokens in plaintext.** Never hardcode tokens in Dockerfiles, shell scripts, `docker-compose.yml` files committed to version control, or Terraform source files. Use secrets management: AWS Secrets Manager, HashiCorp Vault, Kubernetes Secrets, GCP Secret Manager, or Azure Key Vault. Leaked tokens grant persistent access until rotated.

**Not setting `--restart unless-stopped`.** Without a restart policy, the connector does not recover after a host reboot or container crash. Always set a restart policy in production.

**Using `docker-compose` without secrets management.** Inline environment variable values in `docker-compose.yml` are stored in plaintext. Use `.env` files excluded from version control, or reference external secrets directly.

## Related Skills

- [twingate-architect](../twingate-architect/SKILL.md) — overall ZTNA architecture, Remote Network design, Resource and Group definitions
- [twingate-kubernetes](../twingate-kubernetes/SKILL.md) — Helm chart deployment, Kubernetes-specific connector patterns, pod anti-affinity, operator usage
- [twingate-terraform](../twingate-terraform/SKILL.md) — automating connector creation, token generation, and IaC lifecycle management
- [twingate-troubleshoot](../twingate-troubleshoot/SKILL.md) — diagnosing dead connectors, relay failures, DNS issues, and client connectivity problems
