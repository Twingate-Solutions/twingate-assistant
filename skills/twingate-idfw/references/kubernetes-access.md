---
source: https://www.twingate.com/docs/kubernetes-access
type: docs
fetched: 2026-08-05
source_version: e16838d0a5c4bfe367e004ec9d461ad6d1f53f37a60174c61993fe44f0d087d4
---

# Privileged Access for Kubernetes Overview

## Summary
Twingate Privileged Access for Kubernetes extends Zero Trust to the application layer (L7) for Kubernetes clusters, enabling identity propagation, least-privilege RBAC enforcement, and session auditing. It deploys a Gateway reverse proxy within your environment that forwards authenticated user identity to Kubernetes and records all cluster interactions.

## Key Information
- Free for up to 5 resources; contact Twingate for additional pricing
- Introduces a **Twingate Gateway** (L7 reverse proxy) deployed in your environment
- User identity passed through to Kubernetes — no separate Kubernetes credentials needed
- All activity logged to `stdout` in **asciicast v2 format**; logs stay on your infrastructure (not uploaded to Twingate)
- Session replay available at `https://www.twingate.com/sessionplayer`
- Creates a new Resource type **"Kubernetes Cluster"** in the Admin Console

## Prerequisites
- **Connector version**: ≥ 1.82.0 for all Connectors associated with Kubernetes Resources
- **Client version**: ≥ 2025.175 for end users
- **Platforms**: macOS, Windows, Linux only
- Existing `.kube` folder on user machines (create manually or run `kubectl` if missing)

## Setup Steps
1. Deploy via the **Twingate Kubernetes Operator** (recommended for ease and updates)
2. Configure Kubernetes RBAC using `ClusterRoleBindings` or `RoleBindings` mapped to Twingate-propagated user identities
3. Grant users access to the Kubernetes Cluster Resource in the Admin Console
4. Users sync kubeconfig on their machines (manual sync, per-resource sync, or auto-sync)

## Configuration Values
| Item | Value/Notes |
|------|-------------|
| Minimum Connector version | 1.82.0 |
| Minimum Client version | 2025.175 |
| Log format | asciicast v2 |
| Log destination | `stdout` only |
| Session player URL | `https://www.twingate.com/sessionplayer` |

## Gotchas
- Logs are **not** stored by Twingate — you must configure your own log export/storage pipeline from `stdout`
- `.kube` folder must exist before kubeconfig sync; it is not created automatically
- Privileged Access is **not** available on mobile platforms
- All Connectors tied to Kubernetes Resources must meet the minimum version requirement

## Related Docs
- Kubernetes Operator setup
- Gateway configuration
- [Kubernetes Kubeconfig Sync](https://www.twingate.com/docs/) (headless/CI/CD usage covered there)