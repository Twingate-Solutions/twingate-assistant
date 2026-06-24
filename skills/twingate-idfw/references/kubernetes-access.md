# Privileged Access for Kubernetes Overview

## Page Title
Twingate Privileged Access for Kubernetes Overview

## Summary
Twingate Privileged Access for Kubernetes extends Zero Trust to Layer 7 Kubernetes operations via an application-level reverse proxy (Gateway) deployed in your environment. It propagates user identity to Kubernetes clusters, enabling RBAC authorization without separate credentials. All activity is logged to stdout in asciicast v2 format with session replay capability.

## Key Information
- Free for up to 5 resources; contact Twingate for additional pricing
- Introduces a **Twingate Gateway** (L7 reverse proxy) deployed in-cluster
- Creates a new **Kubernetes Cluster** Resource type in Admin Console
- Identity propagated to cluster; configure access via `ClusterRoleBindings` or `RoleBindings`
- Logs exported to `stdout` only — **not uploaded to Twingate**, stored on your infrastructure
- Log format: **asciicast v2**, replayable at `https://www.twingate.com/sessionplayer`
- Available on macOS, Windows, and Linux only

## Prerequisites
- Connector version **≥ 1.82.0** for all Connectors associated with Kubernetes Resources
- Twingate Client version **≥ 2025.175** for end users
- Existing `.kube` folder on user machines (create manually or run `kubectl` if absent)

## Step-by-Step Setup
1. Deploy via **Kubernetes Operator** (recommended for ease of setup and updates)
2. Configure Kubernetes RBAC (`ClusterRoleBindings`/`RoleBindings`) using propagated Twingate identity
3. Grant users access to the Kubernetes Cluster Resource in Admin Console
4. Users sync kubeconfig on their machine:
   - Sync specific Resource
   - Sync all Resources
   - Enable auto-sync

## Configuration Values
| Item | Value |
|------|-------|
| Minimum Connector version | `1.82.0` |
| Minimum Client version | `2025.175` |
| Log output | `stdout` |
| Log format | asciicast v2 |
| Session player URL | `https://www.twingate.com/sessionplayer` |
| Supported platforms | macOS, Windows, Linux |

## Gotchas
- `.kube` folder **must exist** before syncing kubeconfig — create it manually if no prior `kubectl` usage
- Logs are **not** stored by Twingate; you are responsible for exporting/storing from stdout
- Privileged Access is **not available** on mobile platforms
- All Connectors tied to Kubernetes Resources must meet minimum version requirement

## Related Docs
- Kubernetes Operator setup (linked in-page as "here")
- Gateway documentation (linked in-page)
- Twingate session player: `https://www.twingate.com/sessionplayer`