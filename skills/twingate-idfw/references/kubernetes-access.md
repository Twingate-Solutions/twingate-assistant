# Privileged Access for Kubernetes Overview

## Summary
Twingate Privileged Access for Kubernetes extends Zero Trust to Layer 7, enabling identity-propagated, auditable access to Kubernetes clusters without separate cluster credentials. It deploys a reverse proxy Gateway within your environment that handles identity forwarding, RBAC integration, and session recording. Free for up to 5 resources.

## Key Information
- Layer 7 reverse proxy (Twingate Gateway) deployed inside your environment
- Identity propagated to cluster; configure RBAC via `ClusterRoleBindings`/`RoleBindings`
- All actions logged to `stdout` in **asciicast v2 format**, tied to user identity
- Logs stay on your infrastructure (not uploaded to Twingate)
- Session replay available at `https://www.twingate.com/sessionplayer`
- Creates a new Resource type "Kubernetes Cluster" in Admin Console

## Prerequisites
- Connector version **≥ 1.82.0** on all Connectors associated with Kubernetes Resources
- Client version **≥ 2025.175** for end users
- Platforms: macOS, Windows, Linux only
- Existing `.kube` folder on user machines (create manually or run `kubectl` if absent)

## Setup Steps
1. Deploy via **Kubernetes Operator** (recommended for ease and updates)
2. Configure Kubernetes RBAC (`ClusterRoleBindings`/`RoleBindings`) using propagated user identity
3. Users sync kubeconfig via Twingate Client:
   - Sync specific Resource
   - Sync all Resources
   - Enable auto-sync
4. For headless/CI/CD usage, see Kubernetes Kubeconfig Sync docs

## Configuration Values
| Item | Value/Detail |
|------|-------------|
| Log format | asciicast v2 |
| Log destination | `stdout` (self-managed export) |
| Session player URL | `https://www.twingate.com/sessionplayer` |
| Min Connector version | 1.82.0 |
| Min Client version | 2025.175 |

## Gotchas
- `.kube` folder **must exist** before syncing kubeconfig; create it manually if `kubectl` has never been run
- Logs are **not** stored by Twingate — you must configure your own export/storage pipeline
- Privileged Access is **not available** on mobile platforms
- All Connectors linked to Kubernetes Resources must meet the minimum version requirement

## Related Docs
- Kubernetes Operator setup
- Gateway configuration
- Kubernetes Kubeconfig Sync (headless/CI/CD usage)