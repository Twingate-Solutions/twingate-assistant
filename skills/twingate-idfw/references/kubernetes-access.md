# Privileged Access for Kubernetes Overview

## Summary
Twingate Privileged Access for Kubernetes extends Zero Trust to Layer 7, enabling identity propagation, RBAC integration, and session recording for Kubernetes clusters. It deploys a Gateway (reverse proxy) within your environment that audits all user actions and ties them to authenticated identities. Free for up to five resources.

## Key Information
- Introduces a **Twingate Gateway** — Layer 7 reverse proxy deployed in your environment
- Forwards authenticated user identity to Kubernetes clusters (no separate K8s credentials needed)
- Supports Kubernetes RBAC via `ClusterRoleBindings` or `RoleBindings` using propagated identity
- Session logs exported to **stdout** in **asciicast v2 format** — not uploaded to Twingate
- New resource type **"Kubernetes Cluster"** appears in Admin Console after setup
- Recommended setup method: **Kubernetes Operator**

## Prerequisites
- Connector version **≥ 1.82.0** for all Connectors associated with Kubernetes Resources
- Client version **≥ 2025.175** for end users
- Platforms: **macOS, Windows, Linux only** (no mobile)
- Existing `.kube` folder on user machines (create manually or run `kubectl` if missing)

## Step-by-Step
1. Deploy via the Kubernetes Operator (recommended for ease and updates)
2. Configure Kubernetes RBAC (`ClusterRoleBindings`/`RoleBindings`) using propagated Twingate user identities
3. After setup, verify new "Kubernetes Cluster" resource appears in Admin Console
4. Users sync kubeconfig: sync specific resource, all resources, or enable auto-sync

## Configuration Values
| Item | Value/Notes |
|------|-------------|
| Log format | asciicast v2 |
| Log destination | `stdout` only |
| Session replay URL | `https://www.twingate.com/sessionplayer` |
| Min Connector version | 1.82.0 |
| Min Client version | 2025.175 |

## Gotchas
- Logs are **not** stored by Twingate — you are responsible for exporting/storing from `stdout`
- `.kube` folder must exist before users sync kubeconfig; it is **not** auto-created
- Privileged Access is **not available** on mobile platforms
- All Connectors tied to K8s resources must meet the minimum version requirement — older connectors will not work

## Related Docs
- Kubernetes Operator setup guide (referenced in docs)
- Gateway configuration reference (referenced in docs)
- Twingate session player: `https://www.twingate.com/sessionplayer`