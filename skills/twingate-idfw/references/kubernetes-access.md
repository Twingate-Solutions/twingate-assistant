---
source: https://www.twingate.com/docs/kubernetes-access
type: docs
fetched: 2026-08-14
source_version: dd6c75dc1dad5ee0b398dad12d8f7ac71b956fa9953ada27f2a34482ff455ca0
---

# Twingate Privileged Access for Kubernetes Overview

## Summary
Twingate Privileged Access for Kubernetes extends Zero Trust to the application layer (Layer 7) within Kubernetes clusters, enabling identity propagation, least-privilege RBAC enforcement, and session recording. A Twingate Gateway (reverse proxy) is deployed inside your environment to handle identity forwarding and audit logging. Free for up to 5 resources.

## Key Information
- Introduces a **Twingate Gateway** — Layer 7 reverse proxy deployed in your environment
- User identity is forwarded to Kubernetes; configure RBAC via `ClusterRoleBindings`/`RoleBindings`
- All actions audited via `stdout` in **asciicast v2 format**; logs stay on your infrastructure (not uploaded to Twingate)
- Session replay available at `https://www.twingate.com/sessionplayer`
- Creates a new **Kubernetes Cluster** Resource type in the Admin Console

## Prerequisites
- **Connector version**: ≥ 1.82.0 for all Connectors associated with Kubernetes Resources
- **Client version**: ≥ 2025.175 for end users
- **Platforms**: macOS, Windows, Linux only
- Existing `.kube` folder on user machines (create manually or run `kubectl` if absent)

## Setup Steps
1. Deploy via the **Twingate Kubernetes Operator** (recommended for ease and updates)
2. Configure Kubernetes RBAC (`ClusterRoleBindings`/`RoleBindings`) using propagated user identity
3. Grant users access to the Kubernetes Cluster Resource in Admin Console
4. Users sync kubeconfig via Twingate Client:
   - Sync specific Resource
   - Sync all Resources
   - Enable auto-sync
5. For headless/CI-CD usage, see Kubernetes Kubeconfig Sync docs

## Configuration Values
| Item | Value/Notes |
|------|-------------|
| Log format | asciicast v2 |
| Log destination | `stdout` only |
| Session player URL | `https://www.twingate.com/sessionplayer` |
| Min Connector version | 1.82.0 |
| Min Client version | 2025.175 |

## Gotchas
- Logs are **not** stored by Twingate — export/storage is your responsibility
- `.kube` directory must exist before kubeconfig sync; create it manually if needed
- Privileged Access is **not available** on mobile platforms
- All Connectors tied to Kubernetes Resources must meet minimum version requirement

## Related Docs
- Twingate Kubernetes Operator setup
- Gateway configuration
- Kubernetes Kubeconfig Sync (headless/CI-CD usage)
- Twingate RBAC / Access Policies