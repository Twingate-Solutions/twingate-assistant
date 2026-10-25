---
source: https://github.com/Twingate/gateway/wiki
type: github
fetched: 2026-10-25
source_version: cf54f609917be8d18fa8f331339781f1f77f263b
trust: official
---

# Twingate Gateway

## Summary
The Twingate Gateway is an open-source Layer 7 reverse proxy deployed within your environment that enables identity propagation and auditing for privileged access to infrastructure. It integrates with Twingate's Zero Trust network to provide secure access to Kubernetes clusters, SSH servers, and web applications without storing credentials on end-user machines. All audit logs and session recordings remain within your infrastructure.

## Key Information
- **Supported protocols:** Kubernetes, SSH, Web App (Database coming soon)
- **Authentication:** Gateway Access Token (GAT) issued by Twingate control plane after policy evaluation (MFA, device trust, geo-location, JIT)
- **Identity propagation:** Forwards user identity to upstream services via impersonation headers (Kubernetes) or equivalent mechanisms
- **Session recording:** Asciicast v2 format, emitted as structured JSON to stderr; each log entry has `logger: "session_recording"` (renamed from `gateway.audit` in 2.0); routable via Vector, Fluentd, Fluent Bit, etc.
- **Metrics:** Prometheus endpoint on port 9090; supports PodMonitor, ServiceMonitor, PrometheusRule, and Grafana dashboards
- **Deployment:** Helm chart hosted at `ghcr.io/twingate/helmcharts/gateway`; recommended as subchart of Twingate Operator
- **Minimum client version:** 2025.175; Privileged Access available on macOS, Windows, Linux only
- **Releases:** Semantic versioning via `make cut-release` (dev) or `make cut-release-prod`

## Prerequisites
- Twingate account with admin privileges
- Twingate Client (≥2025.175) and Connector deployed
- Kubernetes deployments: Helm, kubectl, Kubernetes cluster v1.31+
- SSH deployments: Docker, Linux host reachable from Connector on port 8443
- Development: asdf, Docker, KinD, kubectl, helm-unittest, Caddy; add `127.0.0.1 acme.test` to `/etc/hosts`

## Usage / Step-by-Step (Kubernetes)

1. Create a Remote Network and API key in Twingate Admin Console
2. Install Gateway via Twingate Operator Helm chart with `gateway.enabled: true`
3. Annotate Gateway service to auto-create `TwingateResource` for the cluster API server
4. Deploy a `TwingateConnector` in the cluster
5. Assign user/group to the resource in Admin Console
6. In Twingate Client, click "Sync Kubernetes Configuration" — kubeconfig updated automatically
7. Verify: `kubectl --context twingate-<cluster> auth whoami` — output includes `twingate:authenticated` in the Groups field

## Web App Integration Spec (for Coding Agents)

A natural-language specification (`Web-App-Integration-Spec.md`) is provided for admins to share with developers or AI coding agents building internal web apps behind the Gateway. Admins fill in the "Settings from your admins" table before distributing it.

### Token verification rules
- The Gateway adds an `Authorization: Bearer <token>` header (a JWT signed by Twingate, type `GAT`) to every inbound request server-side; browsers never see it.
- Verify on every request in a single app-wide layer before routing; no per-route checks, no bypass flags or dev modes.
- Only exemption: `GET /healthz` (exact match), returns `ok`.
- Never log, store, display, or forward the token or `Authorization` header.
- Never trust `X-Twingate-*` headers for anything but display.

### Required configuration (read from environment, never hard-coded)

| Variable | Description |
|---|---|
| `TWINGATE_JWKS_URL` | `https://<twingate-address>/api/v1/jwk/ec` |
| `TWINGATE_AUDIENCE` | Network name (e.g. `acme`) |
| `TWINGATE_RESOURCE_ADDRESS` | This app's Twingate resource address(es), comma-separated |

Refuse to start if any value is unset, blank, or contains `<` or `>`.

### Verification requirements
- **Algorithm:** `ES256`