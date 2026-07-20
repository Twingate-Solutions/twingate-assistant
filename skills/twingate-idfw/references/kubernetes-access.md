# Privileged Access for Kubernetes Overview

## Summary
Twingate Privileged Access for Kubernetes extends Zero Trust to the application layer (Layer 7) for Kubernetes clusters, enabling identity propagation, least-privilege RBAC enforcement, and session auditing. It deploys a Gateway (reverse proxy) inside your environment that forwards authenticated user identity to clusters and records all commands. Free for up to 5 resources.

## Key Information
- Introduces a **Twingate Gateway** (L7 reverse proxy) deployed in your environment
- User identity propagated to cluster; configure access via Kubernetes `ClusterRoleBindings` or `RoleBindings`
- All session activity logged to **stdout** in **asciicast v2 format**; logs stay on your infrastructure (not uploaded to Twingate)
- Session replay available at `https://www.twingate.com/sessionplayer`
- New Resource type **"Kubernetes Cluster"** appears in Admin Console after setup
- Setup recommended via **Kubernetes Operator** (easiest, auto-updates)

## Prerequisites
- Connector version **≥ 1.82.0** for all Connectors associated with Kubernetes Resources
- Twingate Client version **≥ 2025.175** for end users
- Supported platforms: **macOS, Windows, Linux** only
- Existing `.kube` folder on user machines (create manually or run `kubectl` if missing)

## Step-by-Step (High Level)
1. Deploy Twingate Gateway via the **Kubernetes Operator**
2. Configure Kubernetes RBAC (`ClusterRoleBindings`/`RoleBindings`) using propagated user identities
3. Grant users access to the Kubernetes Cluster Resource in Admin Console
4. Users sync `kubeconfig` on their machines (manual, selective, or auto-sync)

## Configuration Values
| Item | Value/Note |
|------|-----------|
| Minimum Connector version | `1.82.0` |
| Minimum Client version | `2025.175` |
| Log format | asciicast v2 |
| Log destination | `stdout` only |
| Session player URL | `https://www.twingate.com/sessionplayer` |
| kubeconfig location | `~/.kube/` (standard kubeconfig) |

## Gotchas
- Logs are **not** stored by Twingate — you must configure your own export/storage pipeline from `stdout`
- The `.kube` directory **must exist** before kubeconfig sync; create it manually if `kubectl` has never been run
- Privileged Access is **not available** on mobile/other platforms (macOS, Windows, Linux only)
- All Connectors tied to Kubernetes Resources must meet the minimum version requirement

## Related Docs
- Kubernetes Operator setup
- Gateway configuration
- Kubernetes Kubeconfig Sync (includes headless/CI/CD usage)
- Twingate RBAC/access policy configuration