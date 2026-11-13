---
source: https://www.twingate.com/docs/kubernetes-agent-access
type: docs
fetched: 2026-11-13
source_version: 43ebe139339ed244278d6b5b63debec5e77abc59a679b16220e059168ef06a30
trust: official
---

# AI Agent Access for Kubernetes

## Summary
Describes how to sandbox AI agents so they reach a private Kubernetes API server only through the Twingate Gateway, with no cluster credential on the agent host. Access is authorized outside the agent's environment via Twingate Service Accounts and Kubernetes RBAC. The guide sets up two agents: one read-only, one that can delete pods, scale deployments, and `kubectl exec`.

## Key Information
- Agent host runs a Twingate Headless Client with a Service Key. The Gateway injects the identity tied to the key's Service Account.
- Injected identity: Username = Service Key ID. Groups = Service Account name (e.g. `agent-readonly`), Service Account ID, `twingate:service-accounts`, `twingate:authenticated`. Kubernetes also adds `system:authenticated`.
- Bind RBAC to the Service Account name (Group subject), not the Service Key, so key rotation doesn't break access.
- The Gateway logs every request (stderr by default, or a file) and records `kubectl exec` sessions.
- Revocation happens before RBAC evaluation.

## Prerequisites
- Privileged Access for Kubernetes deployment: Operator, Gateway, at least one Connector, and a Kubernetes Resource.
- API server with no public endpoint. The Connector is the only network path from agent hosts.
- Connector 1.82.0+; Twingate Client 2025.175+ in headless mode; kubectl 1.26+ on agent hosts.
- Cluster admin access to create RBAC objects.
- Isolated agent host: no other route to the API server (shared VPC, peering, VPN), no cloud identity with cluster permissions, no leftover kubeconfigs or cloud CLI credentials.

## Step-by-Step
1. **Create Service Accounts and keys** (Terraform `twingate_service_account` and `twingate_service_account_key`, or the Admin Console): `agent-readonly`, `agent-platform`. The key's `token` is the Service Key JSON.
2. **Grant resource access**: create one `TwingateResourceAccess` CR (`twingate.com/v1beta`) per Service Account. Set `spec.resourceRef.name` to the cluster's `TwingateResource` and `spec.principalId` to the Service Account ID.
3. **Apply RBAC**:
   - ClusterRole `agent-reader`: get/list/watch on pods, pods/log, services, namespaces, deployments, replicasets.
   - ClusterRole `agent-operator`: the read verbs plus delete pods, get/patch/update `deployments/scale`, create/get `pods/exec`.
   - `agent-readonly`: ClusterRoleBinding to `agent-reader`, Group subject.
   - `agent-platform`: RoleBinding (one per namespace) to `agent-operator`, Group subject.
4. **Configure each host**:
   ```
   sudo twingate setup --headless /path/to/service_key.json
   sudo twingate start
   twingate status
   ```
   Then, as the agent's user:
   ```
   mkdir -p ~/.kube
   twingate kube config sync
   kubectl config get-contexts
   kubectl config use-context <context>
   ```
5. **Verify**: `kubectl auth whoami` shows the expected group. Read-only: `get pods` succeeds, `delete pod --dry-run=server` is Forbidden. Elevated: delete succeeds in the workload namespace, is Forbidden elsewhere, and creating a clusterrolebinding is Forbidden (`kubectl auth can-i create clusterrolebindings` returns `no`).

## Configuration Values
- `twingate setup --headless <key.json>`, `twingate start`, `twingate status`, `twingate kube config sync`
- `TwingateResourceAccess`: `spec.resourceRef.name`, `spec.principalId`
- Placeholders: `<operator-namespace>`, `<workload-namespace>`, `<kubernetes-cluster-twingateresource-name>`

## Gotchas
- Never grant `bind` or `escalate` verbs on `rbac.authorization.k8s.io`. Omitting them prevents privilege escalation.
- Renaming a Service Account changes which RBAC binding applies, so update the subjects.
- Existing bindings using the same group name also apply. Pick unique Service Account names.
- `kube config sync` doesn't set the current context. Without `use-context`, kubectl falls back to `localhost:8080`.
- The synced kubeconfig token is the placeholder `void`, which is expected.
- Use `principalId`, not a name reference, because the ID survives renames.
- Twingate can't close other network or IAM paths from the host. You must do that yourself.
- Protect Service Keys (secrets manager, file permissions, rotation). A key grants network access, not cluster access.
- A revoked key can't be reactivated. Issue a new one.

## Revocation
- **Revoke Service Key**: cuts off Clients using that key across all Resources of the account. The account, access, and RBAC remain.
- **Remove Service Account access to the Kubernetes Resource**: cuts off every key on the account from the cluster only.

## Related Docs
- Privileged Access for Kubernetes
- Kubernetes Kubeconfig Sync
- How Service Accounts Work
- Linux Headless Client