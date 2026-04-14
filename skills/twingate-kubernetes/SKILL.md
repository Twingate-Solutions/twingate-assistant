---
name: twingate-kubernetes
description: |
  Twingate Kubernetes integration — Helm chart, operator, CRDs, traffic routing,
  kubectl access, and service access patterns. Use this skill when the user
  mentions Kubernetes, K8s, Helm, the Twingate operator, kubectl with Twingate,
  routing traffic from K8s clusters, or accessing private/public K8s services
  through Twingate.
---

# twingate-kubernetes

## When to Use

Activate this skill whenever the user's task involves any of the following:

- Deploying a Twingate connector inside a Kubernetes cluster
- Using the Twingate Helm chart or Kubernetes operator
- Managing Twingate resources via CRDs (`TwingateResource`, `TwingateRemoteNetwork`)
- Routing traffic from cluster workloads through Twingate to external private services
- Gating `kubectl` access to a cluster's API server through Twingate
- Exposing ClusterIP, headless, LoadBalancer, or Ingress services to Twingate users
- GitOps workflows that include Twingate configuration alongside K8s manifests

## Quick Reference

| Item | Value |
|---|---|
| Helm repo URL | `https://twingate.github.io/helm-charts` |
| Helm chart name | `twingate/connector` |
| Operator repo | `https://github.com/Twingate/kubernetes-operator` |
| Helm charts repo | `https://github.com/Twingate/helm-charts` |
| Values reference | `charts/connector/values.yaml` in helm-charts repo |
| CRD schemas | `config/crd/` directory in kubernetes-operator repo |
| Required Helm values | `connector.network`, `connector.accessToken`, `connector.refreshToken` |
| Token source | Terraform (`twingate_connector_tokens`), Pulumi, or Admin Console |
| Operator auth | K8s Secret containing Twingate API token (Provision permission) |

## Integration Pattern Decision Table

Choose the right pattern before writing any configuration. These patterns are not mutually exclusive — a cluster may use more than one, but each should serve a distinct purpose.

| Pattern | Use when | How it works |
|---|---|---|
| **Helm chart (connector in K8s)** | Deploying a connector inside a K8s cluster to expose cluster-internal services to Twingate users | Deploy the official Helm chart; connector runs as a Kubernetes Deployment inside the cluster |
| **Kubernetes Operator (CRD-based)** | Managing Twingate Resources and Remote Networks as K8s custom resources, especially for GitOps | Install the operator; declare `TwingateResource` / `TwingateRemoteNetwork` CRDs; operator reconciles state with the Twingate API |
| **Traffic routing (headless client as router)** | Routing traffic FROM cluster pods outbound through Twingate to reach private external services | Run the Twingate Linux client in headless/router mode as a dedicated pod or sidecar; cluster workloads route through it |

## Evergreen Knowledge

### Pattern 1 — Helm Chart (Most Common)

The Helm chart is the standard method for deploying a Twingate connector inside a Kubernetes cluster. Each Helm release corresponds to one logical connector instance registered in the Admin Console.

**How it works:**
- The chart deploys the connector as a Kubernetes `Deployment` with configurable replicas.
- The connector registers with the Twingate control plane using `accessToken` and `refreshToken`.
- Once registered, cluster-internal services (ClusterIP, headless) become addressable as Twingate resources for end users and devices.

**Token lifecycle:**
- Generate tokens in the Admin Console (Connectors → New Connector → Copy tokens) or via Terraform/Pulumi during IaC provisioning.
- Each Helm release requires its own unique token pair. Tokens from one release cannot be reused in another.
- To rotate tokens: delete the connector in the Admin Console, generate a new connector with new tokens, then update the Helm release with the new token values.

**High availability:**
- Deploy a minimum of two Helm releases per remote network in production. Each release is an independent connector instance; Twingate load-balances across healthy connectors.
- Use distinct Kubernetes namespaces or release names to keep releases independent (e.g., `connector-a`, `connector-b`).

**Secret management:**
- Never put `accessToken` or `refreshToken` as plaintext strings in a committed `values.yaml`.
- Store tokens in a Kubernetes `Secret` and reference them via `secretKeyRef` in the Helm values.

### Pattern 2 — Kubernetes Operator

The Kubernetes operator enables declarative, GitOps-friendly management of Twingate configuration directly from Kubernetes manifests.

**How it works:**
- The operator watches for `TwingateResource` and `TwingateRemoteNetwork` custom resource objects.
- When a CRD is created or updated, the operator calls the Twingate API to reconcile the declared state — creating, updating, or deleting the corresponding Twingate objects.
- This means Twingate resource definitions live alongside your K8s manifests in the same repo, following the same GitOps review and merge process.

**Authentication:**
- The operator requires a Kubernetes `Secret` containing a Twingate API token with the **Provision** permission scope.
- This token is not a connector token — it is a service account API key from the Admin Console.

**CRD schema:**
- The `TwingateResource` spec closely mirrors the Terraform `twingate_resource` and Pulumi `TwingateResource` schemas (address, protocols, port ranges, access policies).
- Check `config/crd/` in the `Twingate/kubernetes-operator` repo for current field definitions before writing manifests.

**When to prefer the operator over standalone Helm:**
- Teams already managing K8s infrastructure via GitOps (Argo CD, Flux).
- Twingate resource definitions need to co-deploy with the K8s services they expose.
- Multiple teams need to manage their own Twingate resources via PR workflow.

**Coordination note:** Do not use both the operator and a standalone Helm connector to manage the same remote network's resources without explicit coordination. The operator manages Twingate API objects (resources, remote networks); the Helm chart manages the connector instance. They are complementary, not interchangeable, but overlapping responsibilities cause duplicate or conflicting resource definitions.

### Pattern 3 — Traffic Routing (Headless Client as Router)

Use this pattern when cluster-resident workloads need to reach private external services that are protected by Twingate — the reverse of the Helm chart pattern.

**How it works:**
- Deploy the Twingate Linux client in headless (non-interactive) router mode as a Kubernetes `Deployment` or sidecar container.
- Configure the client with service credentials (headless client tokens) from the Admin Console.
- Route pod traffic through the client pod by setting it as the default gateway or using network policies / init containers to direct specific traffic.

**Common use cases:**
- CI/CD runner pods (e.g., GitHub Actions self-hosted runners, GitLab runners) need to reach private artifact stores, databases, or internal APIs.
- Application pods need to call private microservices in another environment protected by Twingate.
- Cluster workloads need to reach on-premises services without exposing those services to the public internet.

**Deployment options:**
- **Dedicated router deployment:** A single Twingate router pod serves the whole cluster or namespace. Other pods route traffic to it.
- **Sidecar:** A Twingate client container runs in the same pod as the workload that needs access. Simpler isolation, higher resource overhead per pod.

### kubectl Access Pattern

Treat the Kubernetes API server itself as a Twingate resource to eliminate VPN requirements for cluster management.

**How it works:**
1. Register the API server's private hostname or IP as a Twingate resource (e.g., `https://api.internal.cluster:6443`).
2. Apply access policies: only users/groups/devices with the appropriate Twingate policy can reach the API server.
3. Update `kubeconfig` to point `server:` at the private API server URL instead of a public endpoint.
4. Users authenticate through Twingate, the tunnel is established, and `kubectl` commands route through it transparently.

**Benefits:**
- No VPN client needed for cluster operators.
- Access policy enforced at the network layer before K8s RBAC is even reached (defense in depth).
- Works with all `kubectl` commands, `helm`, `k9s`, and any other Kubernetes tooling.

**Requirements:**
- The connector must be deployed in a network position where it can reach the API server on port 6443 (or whichever port the API server listens on).
- The API server must not be the only path by which the connector itself connects — the connector needs outbound internet access to the Twingate control plane.

### Private Services Pattern

Expose Kubernetes services that are intentionally internal (ClusterIP, headless) to Twingate users without creating a LoadBalancer or Ingress.

**How it works:**
- The connector runs inside the cluster (via Helm chart) and has network access to ClusterIP services by DNS name (e.g., `my-service.my-namespace.svc.cluster.local`).
- Register the ClusterIP DNS name and port as a Twingate resource.
- Authorized users connect through Twingate; their traffic routes through the connector to the in-cluster service.

**Address format:** Use the fully qualified cluster DNS name as the resource address — `service-name.namespace.svc.cluster.local` — to ensure stable resolution regardless of cluster configuration.

### Public Services Pattern

Gate LoadBalancer or Ingress services that have a public IP with identity-aware Twingate access control instead of relying solely on security groups or firewall rules.

**How it works:**
- Register the service's public or private hostname as a Twingate resource.
- Apply restrictive access policies (group membership, device trust, MFA).
- Users access the service through Twingate rather than directly; the connector proxies the connection.

**When to use:**
- Staging and QA environments deployed on public clusters that should not be open to the internet.
- Internal developer tools (Grafana, Argo CD, internal dashboards) deployed behind an Ingress but requiring stronger access control than HTTP basic auth.

### Runtime Repository Inspection

When configuring the Helm chart, clone `https://github.com/Twingate/helm-charts` and inspect `charts/connector/values.yaml` for the full options reference. The values schema is the authoritative source for resource limits, replica settings, image configuration, environment variable injection, and extra annotations.

When working with the operator, clone `https://github.com/Twingate/kubernetes-operator` and check the `config/crd/` directory for current CRD schemas. The operator wiki in that repository contains deployment instructions and field-level documentation.

## Common Patterns

### 1. Add Helm Repo and Install Connector

```bash
# Add the Twingate Helm repository
helm repo add twingate https://twingate.github.io/helm-charts
helm repo update

# Install a connector (inline values — for dev/testing only; use secrets in production)
helm install connector-a twingate/connector \
  --namespace twingate \
  --create-namespace \
  --set connector.network="your-tenant" \
  --set connector.accessToken="ACCESS_TOKEN_HERE" \
  --set connector.refreshToken="REFRESH_TOKEN_HERE"
```

### 2. Production Helm Values File

Store tokens in a Kubernetes Secret and reference them via `secretKeyRef`. Commit this values file — it contains no secrets.

```yaml
# values-production.yaml
connector:
  network: "acme"  # Your Twingate tenant name (no .twingate.com suffix)

  # Reference tokens from a pre-existing K8s Secret — never inline tokens here
  accessTokenSecretRef:
    name: twingate-connector-tokens
    key: accessToken
  refreshTokenSecretRef:
    name: twingate-connector-tokens
    key: refreshToken

replicaCount: 2  # Run 2 pods per release for pod-level redundancy

resources:
  requests:
    cpu: "100m"
    memory: "128Mi"
  limits:
    cpu: "500m"
    memory: "256Mi"

podAnnotations:
  prometheus.io/scrape: "true"
  prometheus.io/port: "9340"
```

Create the Secret separately (via Sealed Secrets, External Secrets Operator, or manual `kubectl create secret`):

```bash
kubectl create secret generic twingate-connector-tokens \
  --namespace twingate \
  --from-literal=accessToken="<access-token>" \
  --from-literal=refreshToken="<refresh-token>"

# Install using the values file
helm install connector-a twingate/connector \
  --namespace twingate \
  --values values-production.yaml
```

### 3. TwingateResource CRD Example (Operator)

```yaml
# twingate-resource-postgres.yaml
apiVersion: twingate.com/v1
kind: TwingateResource
metadata:
  name: postgres-internal
  namespace: twingate
spec:
  name: "PostgreSQL Internal"
  address: "postgres.data.svc.cluster.local"
  remoteNetworkName: "k8s-cluster-prod"
  protocols:
    allowIcmp: false
    tcp:
      policy: RESTRICTED
      ports:
        - start: 5432
          end: 5432
    udp:
      policy: DENY_ALL
  accessPolicy:
    - groupName: "db-engineers"
```

Apply the manifest using standard `kubectl` — the operator handles the Twingate API call:

```bash
kubectl apply -f twingate-resource-postgres.yaml
kubectl get twingateresource -n twingate  # Check reconciliation status
```

### 4. kubectl Access via Twingate Resource

Register the API server as a Twingate resource so engineers can use `kubectl` without a VPN:

```hcl
# Terraform example — use twingate-terraform skill for full provider setup
resource "twingate_resource" "k8s_api_server" {
  name              = "K8s API Server (prod)"
  address           = "api.internal.k8s.acme.internal"
  remote_network_id = twingate_remote_network.prod.id

  protocols {
    allow_icmp = false
    tcp {
      policy = "RESTRICTED"
      ports  = ["6443"]
    }
    udp {
      policy = "DENY_ALL"
    }
  }
}
```

Update `kubeconfig` to use the private address:

```yaml
# ~/.kube/config (relevant excerpt)
clusters:
  - cluster:
      server: https://api.internal.k8s.acme.internal:6443
      certificate-authority-data: <ca-data>
    name: prod-cluster
```

Users connect through Twingate before running any `kubectl` command. No public API server endpoint required.

### 5. Multi-Connector HA Deployment

Deploy two independent Helm releases per remote network. Each release has its own connector registration and token pair.

```bash
# Create separate secrets for each connector's tokens
kubectl create secret generic twingate-connector-a-tokens \
  --namespace twingate \
  --from-literal=accessToken="<access-token-a>" \
  --from-literal=refreshToken="<refresh-token-a>"

kubectl create secret generic twingate-connector-b-tokens \
  --namespace twingate \
  --from-literal=accessToken="<access-token-b>" \
  --from-literal=refreshToken="<refresh-token-b>"

# Install first connector
helm install connector-a twingate/connector \
  --namespace twingate \
  --values values-production.yaml \
  --set connector.accessTokenSecretRef.name=twingate-connector-a-tokens \
  --set connector.refreshTokenSecretRef.name=twingate-connector-a-tokens

# Install second connector
helm install connector-b twingate/connector \
  --namespace twingate \
  --values values-production.yaml \
  --set connector.accessTokenSecretRef.name=twingate-connector-b-tokens \
  --set connector.refreshTokenSecretRef.name=twingate-connector-b-tokens
```

Both connectors register to the same remote network. Twingate load-balances across them and fails over automatically if one becomes unhealthy. Use `podAntiAffinity` rules to ensure connectors land on separate nodes:

```yaml
# Add to values-production.yaml
affinity:
  podAntiAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchLabels:
            app.kubernetes.io/name: connector
        topologyKey: kubernetes.io/hostname
```

## Anti-Patterns

**Putting tokens directly in values.yaml**
Do not set `connector.accessToken` or `connector.refreshToken` as plaintext strings in a values file that is committed to source control. These are long-lived credentials. Store them in a Kubernetes Secret and reference with `secretKeyRef`. Use an operator like External Secrets Operator to sync from a secrets manager (AWS Secrets Manager, HashiCorp Vault) in production.

**Deploying only one connector per remote network in production**
A single connector is a single point of failure. If the pod restarts, is evicted, or the node goes down, all Twingate access to that remote network is interrupted. Always deploy a minimum of two connectors (two Helm releases) per remote network in production. Add pod anti-affinity rules to prevent both connectors from scheduling on the same node.

**Using the operator and Helm chart for the same remote network without coordination**
The Helm chart manages the connector process (registration, tunnel). The operator manages Twingate API objects (resources, remote networks). Using both for the same remote network is valid — the operator defines the resources, the Helm connector provides the data path — but do not let both manage the same Twingate objects. If the operator creates a `TwingateResource` pointing to a service, do not also manually create that resource in Terraform or the Admin Console, or you will end up with duplicates.

**Reusing tokens from one release in another**
Each connector registered in the Admin Console has unique token pairs. These tokens are cryptographically tied to that connector's identity. If you copy tokens from one Helm release into a second release, the second connector will fail to authenticate or will steal the identity of the first, causing instability. Always generate a fresh connector registration for each Helm release.

**Treating TwingateResource CRDs as analogous to Kubernetes Services**
`TwingateResource` is a Twingate API object that defines what is accessible through the Twingate network. It is not a Kubernetes network primitive. It does not configure DNS, kube-proxy, or any in-cluster routing. Creating a `TwingateResource` CRD does not expose a service to pods inside the cluster — it exposes it to Twingate users outside the cluster. Keep this distinction clear when designing access patterns.

**Forgetting to inspect the values.yaml schema before configuring**
The Helm chart values schema evolves between releases. Fields available in a newer chart version may not exist in an older one, and vice versa. Always inspect `charts/connector/values.yaml` in the `Twingate/helm-charts` repo at the target chart version before writing configuration. Do not rely on documentation or examples from third-party sources that may reference outdated field names.

## Related Skills

- [twingate-connectors](../twingate-connectors/SKILL.md) — connector fundamentals, upgrade procedures, HA patterns, metrics and logging
- [twingate-terraform](../twingate-terraform/SKILL.md) — Terraform-based connector token generation (`twingate_connector_tokens` resource), full IaC integration
- [twingate-pulumi](../twingate-pulumi/SKILL.md) — Pulumi-based connector token generation and resource management
- [twingate-idfw](../twingate-idfw/SKILL.md) — Kubernetes gateway for privileged access (SSH PAM, session recording, Identity Firewall)
- [twingate-architect](../twingate-architect/SKILL.md) — architecture fundamentals, remote network design, DNS and routing concepts
