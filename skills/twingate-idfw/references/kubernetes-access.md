---
source: https://www.twingate.com/docs/kubernetes-access
type: docs
fetched: 2026-10-11
source_version: bc5b332070eb239d1c6487e2644542bc5751e4c9d8af648077007fe2722a0df8
trust: official
---

# Twingate Privileged Access for Kubernetes Overview

## Summary
Twingate Privileged Access for Kubernetes extends Zero Trust principles to application-layer Kubernetes operations via a Layer 7 reverse proxy (Twingate Gateway) deployed in your environment. It propagates user identity to Kubernetes clusters, enabling RBAC-based authorization without separate Kubernetes credentials. All user actions are logged and attributed to specific identities with session replay support.

## Key Information
- Free for up to 5 resources; contact Twingate for additional pricing
- Introduces a **Twingate Gateway** (L7 reverse proxy) deployed inside your environment
- Identity is forwarded to the cluster; use `ClusterRoleBindings`/`RoleBindings` for RBAC authorization
- Audit logs exported to `stdout` in **asciicast v2 format**; logs stay on your infrastructure (not uploaded to Twingate)
- Session replay available at `https://www.twingate.com/sessionplayer` (paste log or upload file)
- Creates a new Resource type **"Kubernetes Cluster"** visible in the Admin Console with Gateway-specific details

## Prerequisites
- **Connector version**: ≥ 1.82.0 (all Connectors associated with Kubernetes Resources)
- **Client version**: ≥ 2025.175
- **Supported platforms**: macOS, Windows, Linux only
- Existing `.kube` folder on user machines (create manually or run `kubectl` once if absent)

## Setup Steps
1. Deploy via the **Kubernetes Operator** (recommended for ease of setup and updates)
   - Follow the [Kubernetes Operator Identity Firewall user guide](#)
   - Follow the [Gateway Kubernetes quick start guide](#)
2. Configure Kubernetes RBAC (`ClusterRoleBindings` or `RoleBindings`) using propagated Twingate user identities
3. Grant users access to the Kubernetes Cluster Resource in the Admin Console
4. Users sync kubeconfig on their machines (see [Kubernetes Kubeconfig Sync](#)):
   - Sync a specific Resource
   - Sync all Resources
   - Enable auto-sync

## Configuration Values
| Parameter | Value/Notes |
|---|---|
| Audit log format | asciicast v2 |
| Log destination | `stdout` (self-managed export/storage) |
| kubeconfig location | Standard `.kube` folder |
| Resource type in Admin Console | `Kubernetes Cluster` |

## Gotchas
- `.kube` folder must exist before syncing kubeconfig — create it manually if `kubectl` has never been run
- Logs are **not** stored by Twingate; you must configure your own export/storage pipeline from `stdout`
- Privileged Access is **not available** on mobile platforms
- All associated Connectors must be upgraded to ≥ 1.82.0 or Kubernetes Resources will not function

## Related Docs
- Kubernetes Operator Identity Firewall user guide
- Gateway Kubernetes quick start guide
- Kubernetes Kubeconfig Sync (includes headless/CI-CD usage)
- Twingate Session Player: `https://www.twingate.com/sessionplayer`