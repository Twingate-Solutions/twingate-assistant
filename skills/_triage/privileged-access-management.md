---
source: https://www.twingate.com/docs/privileged-access-management
type: docs
fetched: 2026-11-19
source_version: e41968eef3b68712dd443e42cdea5c40f0b95de34bc7a4db51641035d2bdd90b
trust: official
---

<!-- triage: unassigned -->

# Page Title
Twingate Privileged Access Management (Overview)

## Summary
Privileged Access Management (PAM) is a Layer 7 access control layer that verifies user and AI agent identity on every Kubernetes API call, SSH session, and web app request. It relies on the Twingate Gateway, an open-source reverse proxy you deploy in your own environment. It has three components: Privileged Access for Kubernetes, SSH, and Web Apps.

## Key Information
- **Traffic path:** Twingate Client → Connector → Twingate Gateway → Kubernetes API server / SSH server / web app.
- **Identity propagation:**
  - Kubernetes: Gateway impersonates the authenticated user, so native RBAC and audit logs see the real identity.
  - SSH: Gateway logs in to the target with a short-lived certificate from an SSH certificate authority.
  - Web apps: Gateway injects a signed JWT or identity headers, and overwrites any client-supplied identity headers to prevent forgery.
- **Use cases:** Kubernetes access without kubeconfig tokens or cloud IAM credentials; replacing SSH bastions and distributed SSH keys; adding SSO and group authorization to apps like Grafana and Jenkins without an OIDC integration; auditing every `kubectl` command and SSH session.
- Access is just-in-time, based on identity, device posture, location, and context.
- The Gateway is open source (Mozilla Public License 2.0). Source, Helm chart, and release binaries are on GitHub.
- Every PAM Resource must be bound to a Gateway. One Gateway can serve multiple Resources in the same Remote Network.
- The Gateway does not replace the Connector. Each Remote Network with a Gateway needs at least one Connector.

## Prerequisites (Minimum Versions)
| Item | Applies to | Minimum |
|---|---|---|
| Connector | Kubernetes, SSH | 1.82.0 |
| Kubernetes | Clusters set up with the Twingate Kubernetes Operator | 1.31 |
| kubectl | AI agent hosts | 1.26 |
| Client, macOS | SSH | 2026.85 |
| Client, Windows | SSH | 2026.90 |
| Client, Linux | SSH | 2025.342 |
| Client platform | Kubernetes, SSH | macOS, Windows, Linux (no Android or iOS) |

## Configuration Values
- Audit logs and session recordings are written to `stderr` by default. The Gateway can be configured to write them to a file instead.
- Session recordings use the asciicast v2 format.

## Gotchas
- Audit logs and recordings stay on your infrastructure and are never uploaded to Twingate. You are responsible for forwarding and retention (e.g., SIEM or object storage).
- Android and iOS clients are not supported for Kubernetes and SSH.
- A Connector is still required alongside the Gateway.
- Client minimum versions apply to SSH. Check the protocol-specific docs for other requirements.

## Replaying Sessions
Paste or upload an asciicast v2 recording into the Twingate session player.

## Related Docs
- Privileged Access for Kubernetes
- Privileged Access for SSH
- Privileged Access for Web Apps
- Twingate Gateway on GitHub (source, Helm chart, release binaries)
- Twingate session player