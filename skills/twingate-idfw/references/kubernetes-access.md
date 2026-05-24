# Twingate Privileged Access for Kubernetes Overview

## Summary
Twingate Privileged Access for Kubernetes provides Zero Trust, auditable access to Kubernetes clusters via a Layer 7 reverse proxy (Twingate Gateway) that propagates user identity to clusters. It integrates with Kubernetes RBAC and logs all user activity to stdout in asciicast v2 format. Free for up to 5 resources.

## Key Information
- Introduces a **Twingate Gateway** (L7 reverse proxy) deployed inside your environment
- User identity forwarded to cluster; configure access via `ClusterRoleBindings` or `RoleBindings`
- All actions logged to `stdout`, tied to user identity; logs are **not** uploaded to Twingate
- New Resource type "Kubernetes Cluster" appears in Admin Console after setup
- Session replay available at `https://www.twingate.com/sessionplayer` (asciicast v2 format)
- Available on macOS, Windows, and Linux only

## Prerequisites
- Connector version **≥ 1.82.0** for all Connectors associated with Kubernetes Resources
- Client version **≥ 2025.175** for all users
- Existing `.kube` folder on user machines (create manually or run `kubectl` if absent)

## Setup Steps
1. Deploy via the **Twingate Kubernetes Operator** (recommended for ease and updates)
2. Configure Kubernetes RBAC (`ClusterRoleBindings`/`RoleBindings`) to authorize forwarded identities
3. Grant users access to the Kubernetes Cluster Resource in Admin Console
4. Users sync kubeconfig: sync specific Resource, all Resources, or enable auto-sync

## Configuration Values
| Item | Value |
|------|-------|
| Log format | asciicast v2 |
| Log destination | `stdout` only |
| Session player URL | `https://www.twingate.com/sessionplayer` |
| Min Connector version | 1.82.0 |
| Min Client version | 2025.175 |

## Gotchas
- `.kube` folder **must exist** before syncing kubeconfig; create it manually if `kubectl` has never been run
- Logs are infrastructure-local only — no Twingate cloud storage; admins must configure their own export/storage pipeline
- Privileged Access is **not available** on mobile platforms
- Pricing beyond 5 resources requires contacting Twingate sales

## Related Docs
- Twingate Kubernetes Operator setup
- Twingate Gateway configuration
- kubeconfig sync documentation
- Kubernetes RBAC (`ClusterRoleBindings`/`RoleBindings`) — Kubernetes official docs