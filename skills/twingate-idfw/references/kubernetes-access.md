## Privileged Access for Kubernetes (IDFW)

Twingate IDFW for Kubernetes -- adds Layer-7 identity propagation, RBAC integration, and session recording on top of network-level access to a K8s cluster.

**Availability:**
- Free for up to 5 Resources

**Architecture:**
- The **Twingate Gateway** (open source: github.com/Twingate/kubernetes-access-gateway) is a Layer 7 reverse proxy deployed inside the cluster
- Sits between the Connector and the K8s API server
- Authenticates the user (via Twingate -> IdP), then forwards the authenticated identity to the K8s API server
- Records all `kubectl` commands and tags them with the user identity

**Identity Propagation -> RBAC:**
- The Gateway forwards the user's IdP identity to K8s
- Configure K8s authorization with `ClusterRoleBinding` / `RoleBinding` referencing the user identity (or a Group claim)
- No more shared `kubeconfig` files -- each user's commands appear in the K8s audit log under their actual identity

**Setup:**
- **Recommended**: deploy via the **Twingate Kubernetes Operator** (easier setup, easier updates)
  - Operator + Gateway repos referenced from this doc
- After setup, a new Admin Console **Resource** appears with type "Kubernetes Cluster" -- includes Gateway-specific details

**Version Requirements:**
- **Connectors**: 1.77.0 or later (any Connector associated with a Kubernetes Resource)
- **Twingate Client**: 2025.175 or later (users accessing the K8s Resource)
- **Platforms**: macOS, Windows, Linux only -- mobile clients not supported for IDFW K8s

**End-User Flow:**
1. Admin grants user access to the Kubernetes Cluster Resource in Twingate
2. User syncs their kubeconfig from the Twingate Client:
   - Sync a single Resource, sync all, or enable auto-sync (recommended)
3. `kubectl` runs normally -- traffic goes through Twingate Client -> Connector -> Gateway -> API server
4. K8s audit log shows the user's IdP identity for every action

**Session Recording:**
- All `kubectl` commands and their output exported to **stdout** of the Gateway pod
- Logs are **not** uploaded to Twingate -- they stay on customer infrastructure (stream to your SIEM, S3, etc.)
- Format: **asciicast v2**
- Replay options:
  - Standalone web player at https://www.twingate.com/sessionplayer (paste log content or upload a file)
  - Any asciicast-compatible player (e.g., `asciinema play`)

**RBAC Tip:**
- Map Twingate Group membership to K8s RBAC by creating `ClusterRoleBinding` per Group
- For finer-grained access, use namespace-scoped `RoleBinding`s tied to user identity

**Vs. Plain kubectl-over-Twingate (/docs/k8s-kubectl):**

| Pattern | Identity in K8s Audit | Session Recording | Setup Effort |
|---|---|---|---|
| Plain kubectl-over-Twingate | Whoever owns the kubeconfig (often shared) | None native | Low |
| **IDFW (this doc)** | Actual IdP user | asciicast v2 to stdout | Medium (Operator + Gateway) |

**Gotchas:**
- Connector and Client version requirements are non-negotiable -- older versions silently fall back to plain kubectl-over-Twingate without identity propagation
- Gateway logs to stdout only -- you must configure log shipping (Fluent Bit / Vector / etc.) to durably store sessions
- asciicast format includes terminal output, including potentially sensitive data -- treat session logs as confidential

**Related Docs:**
- /docs/identity-firewall -- IDFW overview
- /docs/k8s -- K8s deployment overview
- /docs/k8s-kubectl -- Plain kubectl-over-Twingate (no IDFW)
- Operator: github.com/Twingate/kubernetes-operator
- Gateway: github.com/Twingate/kubernetes-access-gateway
