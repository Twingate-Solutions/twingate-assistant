---
source: https://www.twingate.com/docs/privileged-access-management
type: docs
fetched: 2026-11-22
source_version: 839a703616452137a3957b9f3d87ef95317423a88de048088651ee45cc814ed2
trust: official
---

# Privileged Access Management Overview

## Summary
Twingate Privileged Access Management (PAM) is a Layer 7 access control layer that verifies user and AI agent identity on every Kubernetes API call, SSH session, and web app request. It relies on the Twingate Gateway, an open-source reverse proxy you deploy in your own environment. It has three protocol components: Kubernetes, SSH, and Web Apps.

## Key Information
- **Traffic flow:** Twingate Client → Connector → Twingate Gateway → Kubernetes API server, SSH server, or web app.
- **Identity propagation by protocol:**
  - Kubernetes: the Gateway impersonates the authenticated user against the API server, so RBAC and audit logs see the real identity.
  - SSH: the Gateway signs in to the target with a short-lived certificate from an SSH certificate authority.
  - Web apps: the Gateway injects a signed JWT or identity headers into every request and overwrites client-sent identity headers, so forged headers can't reach the app.
- **Use cases:** kubeconfig-token-free Kubernetes access, replacing SSH bastions and distributed keys, adding SSO and group authorization to apps like Grafana and Jenkins, and auditing every `kubectl` command and SSH session.
- **Gateway is required.** Every PAM Resource is bound to a Gateway. One Gateway can serve multiple Resources in the same Remote Network.
- **Gateway does not replace the Connector.** Each Remote Network with a Gateway needs at least one Connector.
- **Licensing/availability:** Available now. Contact Twingate to start a free trial.
- **Gateway license:** Mozilla Public License 2.0. Source, Helm chart, and release binaries are on GitHub (https://github.com/Twingate/gateway).
- **Audit logs and recordings** stay on your infrastructure and are never uploaded to Twingate.

## Prerequisites (Minimum Versions)
| Requirement | Applies to | Minimum |
|---|---|---|
| Connector | Kubernetes and SSH Resources | 1.82.0 |
| Kubernetes | Clusters set up with the Twingate Kubernetes Operator | 1.31 |
| `kubectl` | AI agent hosts | 1.26 |
| Client for macOS | SSH | 2026.85 |
| Client for Windows | SSH | 2026.90 |
| Client for Linux | SSH | 2025.342 |
| Client platform | Kubernetes and SSH | macOS, Windows, or Linux (no Android or iOS) |

## Step-by-Step
This overview page has no deployment steps. The general order is:
1. Deploy a Gateway in the Remote Network.
2. Ensure a Connector (1.82.0+) exists in that Remote Network.
3. Create the PAM Resource bound to the Gateway.
4. Follow the protocol-specific docs.

## Configuration Values
- Gateway audit logs and session recordings are written to `stderr` by default. They can be configured to write to a file instead.
- Recordings use the asciicast v2 format.

## Gotchas
- Mobile clients (Android, iOS) are not supported for Kubernetes and SSH.
- You are responsible for forwarding and retaining logs and recordings (for example in a SIEM or object storage), since Twingate doesn't store them.
- Without a Connector in the Remote Network, clients cannot reach the Gateway.
- SSH requires specific minimum Client versions on each OS.

## Related Docs
- Privileged Access for Kubernetes (https://www.twingate.com/docs/kubernetes-access)
- Privileged Access for SSH (https://www.twingate.com/docs/ssh-privileged-access-overview)
- Privileged Access for Web Apps (https://www.twingate.com/docs/web-app-access)
- Twingate Gateway (https://www.twingate.com/docs/gateway): TLS certificates, session recordings, monitoring, upgrades
- Twingate session player (https://www.twingate.com/sessionplayer): replay recordings by pasting or uploading them