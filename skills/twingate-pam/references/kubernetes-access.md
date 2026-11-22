---
source: https://www.twingate.com/docs/kubernetes-access
type: docs
fetched: 2026-11-22
source_version: 8cec1d59779c8b92f12f41262e77dfe805d54ab2ac4c806de7ade6cf97228faa
trust: official
---

# Privileged Access for Kubernetes Overview

## Summary
Privileged Access for Kubernetes is the Kubernetes component of Twingate Privileged Access Management. It places a Twingate Gateway (Layer 7 reverse proxy) in front of the cluster API server so each `kubectl` request carries the user's Twingate identity and is authorized by native Kubernetes RBAC. It also provides auditing and session replay.

## Key Information
- Request path: `kubectl → Twingate Client → Connector → Twingate Gateway → Kubernetes API server`.
- The Gateway impersonates the user using a Kubernetes service account token plus impersonation headers. `kubectl` sends no bearer token or client cert.
- Identity sent to the cluster:
  - Username: Twingate username (usually email).
  - Groups: only the Twingate Groups granting access to this Resource, plus `twingate:authenticated` (Kubernetes adds `system:authenticated`).
- Verify identity with `kubectl --context twingate-<cluster> auth whoami`.
- Deployment options:
  - Connector and Gateway in-cluster: recommended, installed via the Twingate Kubernetes Operator.
  - Connector outside, Gateway inside: supported, but the Gateway must be exposed.
  - Both outside: manual configuration, contact Twingate Support.
- Gateway in-cluster uses the pod's service account (Helm chart creates it with impersonation permissions). Gateway outside the cluster needs a service account token with impersonation permissions.
- Audit logs go to `stderr` by default (can be written to a file), are tied to user identity, and are not uploaded to Twingate.
- Session recordings use asciicast v2 format and can be replayed in the Twingate session player web page.
- Supported client platforms: macOS, Windows, Linux.

## Prerequisites
- Twingate Privileged Access for Kubernetes enabled (contact Twingate for a free trial).
- Remote Network for the cluster, plus its ID.
- API key with Read, Write & Provision permissions.
- Connectors on version 1.82.0 or later.
- At least one Connector in the same Remote Network.
- Existing `.kube` folder on user machines (run `kubectl` once or create an empty folder).

## Step-by-Step
1. Create a Remote Network in the Admin Console and note its ID.
2. Create an API key with Read, Write & Provision permissions.
3. Install the Twingate Kubernetes Operator with the Gateway subchart enabled:
   `helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator --install --wait -f ./values.yaml`
   This deploys the Gateway, registers it, and creates a Kubernetes Cluster Resource.
4. Deploy at least one Connector in the Remote Network (e.g., a `TwingateConnector` custom resource).
5. Grant users or Groups access to the Resource in the Admin Console.
6. Create RoleBindings or ClusterRoleBindings for those usernames or Groups.
7. Users sync kubeconfig in the Twingate Client, then run `kubectl auth whoami`.

## Configuration Values
- Expose Gateway for external Connectors (GKE example):
  ```yaml
  service:
    type: LoadBalancer
    annotations:
      cloud.google.com/load-balancer-type: "Internal"
  ```
- Get the LoadBalancer address (standalone Helm chart; set it as the Resource's Gateway address):
  `kubectl get service gateway -o jsonpath='{.status.loadBalancer.ingress[0]}'`
- Custom address for indirect access (NodePort, proxy, ingress, private endpoint). Requires Gateway 2.1.0+ and Operator 3.1.0+:
  ```yaml
  twingateOperator:
    gateway:
      address:
        host: gateway.corp.internal
        port: 443
  ```

## Gotchas
- The default ClusterIP service is reachable only by in-cluster Connectors, and every Connector in the Remote Network must reach the Gateway.
- Multiple clusters can share the address `kubernetes.default.svc.cluster.local`. Give each Resource a unique alias (e.g., `cluster-a.int`) and include each alias in the Gateway TLS certificate.
- Session recording works only over the WebSocket streaming protocol (default for `kubectl` and Kubernetes 1.31+).
- The Groups list shows only Groups granting access to this Resource, not all of the user's Groups.

## Related Docs
- Privileged Access Management (https://www.twingate.com/docs/privileged-access-management)
- AI Agent Access (https://www.twingate.com/docs/kubernetes-agent-access#how-agent-access-works)
- Gateway TLS Certificates (https://www.twingate.com/docs/gateway-tls-certificates)
- Kubernetes Kubeconfig Sync (https://www.twingate.com/docs/kubernetes-kubeconfig-sync)
- Session Recordings (https://www.twingate.com/docs/gateway-session-recordings)
- Kubernetes Troubleshooting (https://www.twingate.com/docs/kubernetes-troubleshooting)
- Kubernetes Operator PAM user guide (https://github.com/Twingate/kubernetes-operator/wiki/Privileged-Access-Management-User-Guide)
- Gateway Kubernetes quick start guide (https://github.com/Twingate/gateway/wiki/Kubernetes-Quick-Start-Guide)