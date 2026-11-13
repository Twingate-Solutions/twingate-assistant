---
source: https://www.twingate.com/docs/identity-firewall
type: docs
fetched: 2026-11-13
source_version: 8ba4dd9b70b77f100a97c07831738053f95d8a277bf4a128a7cb935db004632d
trust: official
---

# Twingate Identity Firewall (Overview)

## Summary
Identity Firewall is a Layer 7 access control layer that verifies user and AI agent identity on every Kubernetes API call, SSH session, and web app request. It relies on the Twingate Gateway, an open-source reverse proxy deployed in your own environment, which propagates identity to upstream services and records sessions. It has three components: Privileged Access for Kubernetes, SSH, and Web Apps.

## Key Information
- Available on all plans; free for up to 5 Resources.
- Traffic path: `Twingate Client → Connector → Twingate Gateway → Kubernetes API server / SSH server / web app`.
- Identity propagation per protocol:
  - **Kubernetes:** Gateway impersonates the authenticated user against the API server, so native RBAC and audit logs see the real identity. No kubeconfig tokens or cloud IAM credentials needed.
  - **SSH:** Gateway logs in to the target with a short-lived certificate issued by an SSH CA. Replaces bastion hosts and distributed SSH keys.
  - **Web apps:** Gateway injects a signed JWT or identity headers into each request and overwrites any client-supplied identity headers (prevents forgery). Adds SSO and group authorization to apps like Grafana and Jenkins without an OIDC integration.
- Every `kubectl` command and SSH session is audited. Logs and recordings stay on your infrastructure and are never uploaded to Twingate.
- Gateway is open source (Mozilla Public License 2.0); source, Helm chart, and release binaries are on GitHub.

## Prerequisites
| Requirement | Applies to | Minimum |
|---|---|---|
| Connector | Kubernetes and SSH Resources | 1.82.0 |
| Kubernetes | Clusters using the Twingate Kubernetes Operator | 1.31 |
| `kubectl` | AI agent hosts | 1.26 |
| Client, macOS | SSH | 2026.85 |
| Client, Windows | SSH | 2026.90 |
| Client, Linux | SSH | 2025.342 |
| Client platform | Kubernetes and SSH | macOS, Windows, Linux (no Android/iOS) |

## Step-by-Step
This overview page has no deployment steps. Follow the protocol-specific docs (Kubernetes, SSH, Web Apps). General model:
1. Deploy a Connector in the Remote Network.
2. Deploy a Gateway in that Remote Network.
3. Create Identity Firewall Resources bound to the Gateway.

## Configuration Values
- Gateway audit logs and recordings are written to `stderr` by default; it can be configured to write to a file instead (specific flag not given on this page).
- Recordings use asciicast v2 format.

## Gotchas
- The Gateway is required: every Identity Firewall Resource must be bound to one. One Gateway can serve multiple Resources in the same Remote Network.
- The Gateway does not replace the Connector. Each Remote Network with a Gateway needs at least one Connector.
- You are responsible for forwarding and retaining logs and recordings (e.g., SIEM or object storage).
- Mobile clients are unsupported for Kubernetes and SSH.
- Minimum client versions for SSH differ per OS.

## Related Docs
- Privileged Access for Kubernetes
- Privileged Access for SSH
- Privileged Access for Web Apps
- Twingate session player (replay asciicast v2 recordings by pasting or uploading)
- Twingate Gateway on GitHub (source, Helm chart, binaries)