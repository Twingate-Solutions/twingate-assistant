# Privileged Access for Kubernetes Overview

## Page Title
Twingate Privileged Access for Kubernetes Overview

## Summary
Twingate Privileged Access for Kubernetes extends Zero Trust to the application layer (L7) for Kubernetes clusters, propagating user identity to enable RBAC-based authorization without separate Kubernetes credentials. It deploys a reverse proxy Gateway within your environment for identity propagation and session recording. Free for up to 5 resources.

## Key Information
- Introduces a **Layer 7 reverse proxy Gateway** deployed inside your environment
- User identity forwarded to Kubernetes; configure access via `ClusterRoleBindings` or `RoleBindings`
- All actions audited, exported via `stdout` in **asciicast v2 format**
- Session replay available at `https://www.twingate.com/sessionplayer`
- Logs stay on your infrastructure — **not uploaded to Twingate**
- New Resource type appears in Admin Console: **Kubernetes Cluster**
- Recommended setup path: **Kubernetes Operator**

## Prerequisites
- **Connector version**: ≥ 1.82.0 (all Connectors associated with Kubernetes Resources)
- **Client version**: ≥ 2025.175
- **Supported platforms**: macOS, Windows, Linux only (no mobile)
- Twingate account with Privileged Access feature enabled

## Step-by-Step Setup
1. Deploy via **Kubernetes Operator** (recommended for ease and updates)
2. Configure Kubernetes RBAC (`ClusterRoleBinding`/`RoleBinding`) using propagated Twingate user identities
3. Grant users access to the Kubernetes Cluster Resource in Admin Console
4. Users sync kubeconfig on their machine:
   - Sync specific Resource
   - Sync all Resources
   - Enable auto-sync

## Configuration Values
| Item | Value/Notes |
|------|-------------|
| Log format | asciicast v2 |
| Log destination | `stdout` (self-managed export/storage) |
| Session player URL | `https://www.twingate.com/sessionplayer` |
| Min Connector version | 1.82.0 |
| Min Client version | 2025.175 |

## Gotchas
- Logs are **not** stored by Twingate — you must configure export/storage pipeline yourself
- Users must manually sync or enable auto-sync for kubeconfig; access won't work without it
- Only macOS, Windows, Linux clients supported — no iOS/Android
- All Connectors for Kubernetes Resources must meet minimum version requirement

## Related Docs
- Kubernetes Operator setup guide (linked in page as "here")
- Gateway configuration (linked in page as "here")
- Twingate RBAC/access policy documentation
- Session player: `https://www.twingate.com/sessionplayer`