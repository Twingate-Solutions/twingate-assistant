---
source: https://www.twingate.com/docs/kubernetes-access
type: docs
fetched: 2026-10-25
source_version: 6c615a901fb258275ae7d2cf6d2a42e2f2790cfa583a7a630ad8cc6dd6929ac3
trust: official
---

# Privileged Access for Kubernetes Overview

## Page Title
Twingate Privileged Access for Kubernetes Overview

## Summary
Twingate Privileged Access for Kubernetes extends Zero Trust to application-layer Kubernetes operations via a Layer 7 reverse proxy (Twingate Gateway) deployed in your environment. It propagates user identity to clusters, enables Kubernetes RBAC integration, and records all session activity. Currently free for up to five resources.

## Key Information
- Introduces a **Twingate Gateway** (L7 reverse proxy) deployed inside your environment
- User identity forwarded to Kubernetes cluster; map to RBAC via `ClusterRoleBindings` or `RoleBindings`
- All activity logged to `stdout` in **asciicast v2 format**; logs stay on your infrastructure (not uploaded to Twingate)
- Session replay available at `https://www.twingate.com/sessionplayer`
- Creates a new **Kubernetes Cluster** Resource type in the Admin Console
- Platform support: **macOS, Windows, Linux only**

## Prerequisites
- Connector version **≥ 1.82.0** for all Connectors associated with Kubernetes Resources
- Existing `.kube` folder on user machines (create manually or run `kubectl` once if absent)
- Twingate Client installed on end-user machines

## Setup (Step-by-Step)
1. Deploy via the **Kubernetes Operator** (recommended for ease and updates)
   - Follow: [Kubernetes Operator Identity Firewall user guide]
   - Follow: [Gateway Kubernetes quick start guide]
2. Configure Kubernetes RBAC (`ClusterRoleBindings`/`RoleBindings`) to authorize identities forwarded by Twingate
3. Grant users access to the Kubernetes Cluster Resource in Admin Console
4. Users sync `kubeconfig` on their machines:
   - Sync a specific Resource, all Resources, or enable auto-sync
   - See: [Kubernetes Kubeconfig Sync] for headless/CI-CD usage

## Configuration Values
| Item | Value/Note |
|---|---|
| Minimum Connector version | `1.82.0` |
| Log format | asciicast v2 |
| Log destination | `stdout` (self-managed export) |
| Session player URL | `https://www.twingate.com/sessionplayer` |
| kubeconfig location | Standard `.kube` folder |

## Gotchas
- `.kube` folder **must exist** before syncing kubeconfig; create it manually if `kubectl` has never been run
- Logs are **not** sent to Twingate — storage and export are entirely operator-managed
- Privileged Access is **not available** on mobile or other platforms beyond macOS/Windows/Linux
- All Connectors tied to Kubernetes Resources must be upgraded to ≥ 1.82.0 or access will fail

## Related Docs
- Kubernetes Operator Identity Firewall user guide
- Gateway Kubernetes Quick Start guide
- Kubernetes Kubeconfig Sync (including headless/CI-CD)
- Twingate Connector version management