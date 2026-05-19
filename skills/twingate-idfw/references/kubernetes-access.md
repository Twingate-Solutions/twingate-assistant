# Privileged Access for Kubernetes Overview

## Summary
Twingate Privileged Access for Kubernetes is a Layer 7 reverse proxy solution that extends Zero Trust access controls to Kubernetes cluster operations. It propagates user identity to clusters, enables RBAC integration, and provides session recording/auditing. Free for up to 5 resources.

## Key Information
- Deploys a **Twingate Gateway** (L7 reverse proxy) inside your environment
- Passes authenticated user identity to Kubernetes clusters—no separate K8s credentials needed
- RBAC configured via `ClusterRoleBindings` or `RoleBindings` using propagated identity
- Session logs exported to `stdout` in **asciicast v2 format**; logs stay on your infrastructure (not uploaded to Twingate)
- Creates a new Resource type "Kubernetes Cluster" in Admin Console
- Platforms: macOS, Windows, Linux only

## Prerequisites
- Connector version **≥ 1.82.0** for all Connectors associated with Kubernetes Resources
- Client version **≥ 2025.175** for all users accessing Privileged Access
- Kubernetes Operator deployed (recommended setup method)

## Setup Steps
1. Deploy via the **Kubernetes Operator** (recommended for easiest setup and updates)
2. Configure Kubernetes RBAC (`ClusterRoleBindings`/`RoleBindings`) using Twingate-propagated user identities
3. Grant users access to the Kubernetes Cluster Resource in Admin Console
4. Users sync `kubeconfig` on their machines (manual per-resource, all resources, or auto-sync)

## Configuration Values
| Item | Value |
|------|-------|
| Log format | asciicast v2 |
| Log destination | `stdout` |
| Session player URL | `https://www.twingate.com/sessionplayer` |
| Min Connector version | 1.82.0 |
| Min Client version | 2025.175 |

## Gotchas
- Logs are **not** stored by Twingate—admins must configure their own export/storage pipeline from `stdout`
- Privileged Access is **not** available on mobile platforms
- All Connectors tied to Kubernetes Resources must meet the minimum version requirement—older Connectors will not work
- Users must explicitly sync kubeconfig after being granted access; it is not automatic unless auto-sync is enabled

## Related Docs
- Kubernetes Operator setup guide
- Gateway configuration reference
- kubeconfig sync instructions
- [Session Player](https://www.twingate.com/sessionplayer)