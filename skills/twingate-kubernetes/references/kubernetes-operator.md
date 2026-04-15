<!-- initial seed — to be refreshed by pipeline -->

## Page Title
Twingate Kubernetes Operator

## Summary
The Twingate Kubernetes Operator manages Twingate Connectors as native Kubernetes custom resources, handling the full lifecycle including deployment, configuration, and upgrades declaratively. It introduces three CRDs that allow teams to express Twingate network topology entirely through Kubernetes manifests.

## Key Information
- **Operator vs Helm chart:** The operator manages CRDs declaratively and supports multi-connector topologies with reconciliation loops; the Helm chart (`twingate/connector`) is simpler and preferred for single-connector deployments without CRD management
- **CRDs introduced:** `TwingateConnector` (connector lifecycle), `TwingateResource` (resource definitions), `TwingateResourceAccess` (access policy bindings between groups/service accounts and resources)
- **Reconciliation:** The operator continuously reconciles desired state — if a connector pod is deleted or drifts, the operator recreates it automatically
- **Connector credentials:** Stored as a Kubernetes `Secret` with keys `TWINGATE_ACCESS_TOKEN` and `TWINGATE_NETWORK`; the operator mounts these into connector pods automatically
- **Sidecar pattern:** The operator supports injecting a Twingate Connector as a sidecar into application pods, giving per-workload network identity and access without a cluster-wide connector
- **Image management:** The operator tracks the Twingate connector image and can roll out upgrades across all managed connectors when the desired version is updated in the CRD spec

## Prerequisites
- Kubernetes 1.24+ (1.26+ recommended)
- Helm 3.x installed for operator deployment
- A Twingate account with at least one Remote Network configured
- Connector tokens (access token + network name) generated from the Twingate Admin Console
- Appropriate RBAC permissions to create CRDs and cluster-scoped resources

## Step-by-Step
1. Add the Twingate Helm repository: `helm repo add twingate https://twingate.github.io/helm-charts && helm repo update`
2. Create a namespace for the operator: `kubectl create namespace twingate`
3. Create a Secret with connector credentials:
   ```
   kubectl create secret generic twingate-connector \
     --from-literal=TWINGATE_ACCESS_TOKEN=<token> \
     --from-literal=TWINGATE_NETWORK=<network-name>.twingate.com \
     -n twingate
   ```
4. Install the operator via Helm: `helm install twingate-operator twingate/connector -n twingate`
5. Apply a `TwingateConnector` manifest referencing the secret to register the connector with the operator
6. Verify the connector pod is running: `kubectl get pods -n twingate`
7. Check connector status via the CRD: `kubectl get twingateconnector -n twingate`
8. Apply `TwingateResource` manifests to define which internal resources are accessible through this connector
9. Apply `TwingateResourceAccess` manifests to bind groups or service accounts to resources

## Configuration Values
```
TWINGATE_ACCESS_TOKEN: <connector access token from Admin Console>
TWINGATE_NETWORK: <subdomain>.twingate.com
image.repository: twingate/connector
image.tag: <version or "latest">
resources.requests.cpu: "100m"
resources.requests.memory: "128Mi"
resources.limits.cpu: "500m"
resources.limits.memory: "256Mi"
```

## Gotchas
- **Token scope:** Each `TwingateConnector` CRD instance requires its own unique access token — tokens are not shared between connector instances; generate one per connector in the Admin Console
- **CRD upgrade ordering:** When upgrading the operator, apply CRD updates before upgrading the operator Helm release to avoid schema mismatches during reconciliation
- **Sidecar injection requires pod restart:** Enabling the sidecar injector webhook affects new pods only; existing pods must be restarted to receive the injected connector container
- **Namespace vs cluster scope:** `TwingateResource` and `TwingateResourceAccess` are namespace-scoped; `TwingateConnector` CRDs may be cluster-scoped depending on operator version — check the CRD manifest before applying
- **Resource limits matter:** Connectors under load (many concurrent tunnels) can spike CPU; set limits generously or use HPA if the operator version supports it
- **Operator vs Helm chart conflict:** Do not deploy both the operator and the standalone Helm chart managing the same connector token — they will compete and cause connector instability

## Related Docs
- `/docs/guides/kubernetes-operator` — Official operator installation and CRD reference
- `/docs/guides/kubernetes` — General Kubernetes connector deployment (Helm chart, no operator)
- `/docs/guides/connector-deployment` — Platform-agnostic connector deployment overview
- `/docs/reference/terraform-provider` — Terraform alternative for declarative Twingate resource management
- `/docs/guides/helm-chart` — Standalone Helm chart for single-connector deployments
