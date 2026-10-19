---
source: https://www.twingate.com/docs/kubernetes-agent-access
type: docs
fetched: 2026-10-18
source_version: 921f6bb57c7699740262a0259e698cda9ced98f68751b8ea52541c1cc485b839
trust: official
---

# Secure Kubernetes Sandbox Access for AI Agents

## Page Title
Secure Kubernetes Sandbox Access for AI Agents

## Summary
Provides a pattern for giving AI agents access to Kubernetes clusters through Twingate's Privileged Access Gateway instead of storing credentials on agent hosts. The agent host runs a Twingate Headless Client; the Gateway injects a cluster identity tied to the Service Account, and Kubernetes RBAC enforces permissions. This prevents agents from holding credentials, escalating privileges, or reaching the API server through alternate network paths.

## Key Information
- Gateway injects identity into every request: `Username` = Service Key ID, `Group` = Service Account name (e.g., `agent-readonly`)
- RBAC bindings should target **Service Account name** (Group), not Service Key ID — survives key rotation
- Renaming a Service Account changes which RBAC binding applies; update subjects accordingly
- **Never grant** `rbac.authorization.k8s.io` verbs (`bind`, `escalate`) — prevents privilege escalation
- Gateway logs every API call and records `kubectl exec` sessions outside the agent's reach
- Revocation options: revoke a single Service Key (one host) or remove Service Account's Resource access (all keys)

## Prerequisites
- Kubernetes Identity Firewall deployment: Kubernetes Operator, Gateway, ≥1 Connector, Kubernetes Resource configured
- Kubernetes API server with **no public endpoint**; Connector is the only network path
- Connector version **1.82.0+**
- Twingate Client version **2025.175+** installed in headless mode on each agent host
- `kubectl` **1.26+** on each agent host
- Admin access to the cluster for RBAC object creation
- Agent host must have no alternate routes to API server (no shared VPC, VPC peering, VPN, cloud IAM roles, or leftover kubeconfig/credentials)

## Step-by-Step

### 1. Create Service Accounts and Keys (Terraform)
```hcl
locals {
  agents = {
    readonly = "agent-readonly"
    platform = "agent-platform"
  }
}
resource "twingate_service_account" "agent" { for_each = local.agents; name = each.value }
resource "twingate_service_account_key" "agent" {
  for_each = local.agents
  service_account_id = twingate_service_account.agent[each.key].id
  name = "${each.value} Headless Client"
}
```

### 2. Grant Service Accounts Access to Kubernetes Resource
Create a `TwingateResourceAccess` CR per Service Account referencing the `TwingateResource` and `principalId` (Service Account ID).

### 3. Configure Kubernetes RBAC
- `ClusterRole: agent-reader` — get/list/watch pods, logs, services, namespaces, deployments, replicasets
- `ClusterRole: agent-operator` — above + delete pods, scale deployments, exec into pods
- `ClusterRoleBinding` → `agent-readonly` group → `agent-reader`
- `RoleBinding` (namespace-scoped) → `agent-platform` group → `agent-operator`

### 4. Configure Agent Hosts
```bash
sudo twingate setup --headless /path/to/service_key.json
sudo twingate start
mkdir -p ~/.kube
twingate kube config sync
kubectl config use-context <context>
```

### 5. Verify
```bash
kubectl auth whoami                                          # confirm Group injection
kubectl auth can-i create clusterrolebindings               # should return "no"
kubectl create clusterrolebinding self-admin --clusterrole=cluster-admin --group=agent-platform --dry-run=server  # should fail
```

## Configuration Values
| Parameter | Value/Notes |
|---|---|
| Service Key token field | Service Key JSON; pass to `twingate setup --headless` |
| kubeconfig token placeholder | `void` (literal) — authentication is via Twingate, not kubeconfig credential |
| `principalId` in TwingateResourceAccess | Use Service Account **ID**, not name |
| Group name in RBAC subjects | Must match Service Account name exactly |

## Gotchas