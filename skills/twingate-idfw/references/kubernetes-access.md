# Twingate Privileged Access for Kubernetes Overview

## Summary
Twingate Privileged Access for Kubernetes extends Zero Trust to the application layer (L7) for Kubernetes clusters, enabling identity propagation, RBAC integration, and session recording. A Twingate Gateway (reverse proxy) is deployed within your environment to handle identity forwarding and audit logging. Free for up to five resources.

## Key Information
- Introduces a **Twingate Gateway** — L7 reverse proxy deployed in your environment
- User identity propagated to Kubernetes clusters; no separate Kubernetes credentials needed
- RBAC configured via `ClusterRoleBindings` or `RoleBindings` based on propagated identity
- All actions logged to `stdout` in **asciicast v2 format**, tied to user identity
- Logs are **not uploaded to Twingate** — stored solely on your infrastructure
- Session replay available at `https://www.twingate.com/sessionplayer`
- Creates a new **Kubernetes Cluster** resource type in the Admin Console

## Prerequisites
- **Connector version**: ≥ 1.82.0 for all Connectors associated with Kubernetes Resources
- **Client version**: ≥ 2025.175 for end users
- **Platforms**: macOS, Windows, Linux only (no mobile)
- Existing `.kube` folder on user machines (create manually or run `kubectl` if absent)

## Setup Steps
1. Deploy via the **Twingate Kubernetes Operator** (recommended for ease and updates)
2. Configure Kubernetes RBAC (`ClusterRoleBindings`/`RoleBindings`) to authorize propagated identities
3. Grant users access to the Kubernetes Cluster Resource in Admin Console
4. Users sync kubeconfig on their machine:
   - Sync a specific Resource
   - Sync all Resources
   - Enable auto-sync

## Configuration Values
| Item | Value/Notes |
|------|-------------|
| Log format | asciicast v2 |
| Log destination | `stdout` (self-managed export) |
| Session player URL | `https://www.twingate.com/sessionplayer` |
| Min Connector version | 1.82.0 |
| Min Client version | 2025.175 |

## Gotchas
- `.kube` folder must exist before syncing kubeconfig — create it manually if `kubectl` has never been run
- Logs are infrastructure-side only; Twingate does not store or have access to session recordings
- Privileged Access is unavailable on mobile platforms
- All Connectors tied to Kubernetes Resources must meet the minimum version requirement

## Related Docs
- Kubernetes Operator setup guide (linked in source as "here")
- Gateway configuration (linked in source as "here")
- Twingate kubeconfig sync documentation
- Twingate Connector versioning