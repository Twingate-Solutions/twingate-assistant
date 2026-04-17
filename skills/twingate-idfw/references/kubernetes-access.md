Looking at the untracked files in git status, this belongs in `skills/twingate-idfw/references/`. Let me produce the summary.

## Privileged Access for Kubernetes

**Page Title:** Privileged Access for Kubernetes

**Summary:** Twingate Privileged Access for Kubernetes extends Zero Trust to Layer 7 Kubernetes operations via a Gateway (reverse proxy) deployed inside your cluster. It propagates user identity to Kubernetes RBAC, eliminating separate cluster credentials. Session activity is recorded and attributed to specific identities via asciicast logs exported to stdout.

**Key Information:**
- Free for up to 5 resources; contact Twingate for additional pricing
- Introduces a **Twingate Gateway** — an L7 reverse proxy that handles identity propagation and session recording
- User identity forwarded to the cluster; authorize via `ClusterRoleBindings` or `RoleBindings`
- Session logs exported to `stdout` in **asciicast v2 format** — not uploaded to Twingate, stays on your infrastructure
- Sessions replayable at `https://www.twingate.com/sessionplayer` (paste log or upload file)
- After setup, a new **Kubernetes Cluster** resource type appears in the Admin Console

**Prerequisites:**
- Connector version **≥ 1.77.0** on all Connectors associated with Kubernetes resources
- Client version **≥ 2025.175** on all end-user machines
- Client platform: macOS, Windows, or Linux only (no mobile)
- Kubernetes Operator deployed in cluster

**Setup:**
1. Deploy via the **Kubernetes Operator** (recommended — easiest path and simplifies upgrades)
2. Configure Kubernetes RBAC (`ClusterRoleBindings`/`RoleBindings`) to authorize users by propagated identity
3. Grant users access to the Kubernetes Cluster Resource in the Admin Console
4. Users sync kubeconfig: sync a specific resource, all resources, or enable auto-sync

**Configuration Values:**
- No explicit env vars documented on this page
- Kubeconfig sync options: single resource / all resources / auto-sync

**Gotchas:**
- Logs are **not** stored by Twingate — export/storage is your responsibility
- Connector version requirement (1.77.0) applies to all Connectors tied to Kubernetes resources, not just a single one
- Privileged Access is unavailable on iOS/Android clients

**Related Docs:**
- Kubernetes Operator setup
- Twingate Gateway configuration
- Session player: `https://www.twingate.com/sessionplayer`