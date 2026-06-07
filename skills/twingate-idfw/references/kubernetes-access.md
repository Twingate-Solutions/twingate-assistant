# Privileged Access for Kubernetes Overview

## Summary
Twingate Privileged Access for Kubernetes adds Layer 7 zero-trust access control to Kubernetes clusters by deploying a reverse proxy Gateway that propagates user identity, enforces RBAC, and records sessions. It extends network-level access policies to in-cluster operations without requiring separate Kubernetes credentials. Free for up to five resources.

## Key Information
- Introduces a **Twingate Gateway** (L7 reverse proxy) deployed in your environment
- Passes authenticated user identity to Kubernetes; configure access via `ClusterRoleBindings`/`RoleBindings`
- All user actions audited and tied to identity; logs exported via `stdout` in **asciicast v2 format**
- Logs are **not** uploaded to Twingate — stored solely on your infrastructure
- New Resource type "Kubernetes Cluster" appears in Admin Console after setup
- Session replay available at `https://www.twingate.com/sessionplayer`

## Prerequisites
- **Connector version**: ≥ 1.82.0 (all Connectors associated with Kubernetes Resources)
- **Client version**: ≥ 2025.175
- **Platforms**: macOS, Windows, Linux only
- Existing `.kube` folder on user machines (create manually or run `kubectl` once if missing)

## Step-by-Step Setup
1. Deploy via the **Kubernetes Operator** (recommended for setup and updates)
2. Configure Gateway (see Gateway documentation)
3. Assign users access to the Kubernetes Cluster Resource in Admin Console
4. Users sync kubeconfig on their machines:
   - Sync specific Resource
   - Sync all Resources
   - Enable auto-sync

## Configuration Values
| Item | Value/Notes |
|------|-------------|
| Log format | asciicast v2 |
| Log destination | `stdout` (self-managed export) |
| RBAC integration | `ClusterRoleBindings` or `RoleBindings` |
| Resource type in console | `Kubernetes Cluster` |

## Gotchas
- `.kube` folder must exist before syncing kubeconfig — create it manually if `kubectl` has never been run
- Logs are self-hosted only; Twingate never stores session recordings
- Privileged Access is **not** available on mobile platforms
- All associated Connectors must be updated to ≥ 1.82.0 before use
- Pricing beyond 5 resources requires contacting Twingate sales

## Related Docs
- Kubernetes Operator setup guide
- Gateway configuration guide
- Kubeconfig sync (user configuration)
- Twingate Session Player: `https://www.twingate.com/sessionplayer`