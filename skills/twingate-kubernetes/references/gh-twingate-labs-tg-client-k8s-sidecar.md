---
source: https://github.com/Twingate-Labs/tg-client-k8s-sidecar
type: github
fetched: 2026-08-06
source_version: 47fe25a003baacb04f678911adbcae93e808bc3f
---

<!-- triage: unassigned -->

# tg-client-k8s-sidecar

## Summary
Demonstrates how to run the Twingate headless client as a Kubernetes sidecar container, giving pods access to Twingate-protected resources. Uses a service account key injected as a Kubernetes Secret. Intended as a copy-paste starting point for adding to existing deployments.

## Key Information
- Sidecar pattern: Twingate client runs as an additional container in the same pod as the workload
- Supports access to any Twingate resource (databases, web services, monitoring, etc.)
- Requires a Twingate service account and service key (not a user account)
- Sidecar container requires `privileged: true` (needed by the Twingate headless client for network configuration)
- Service key must be base64-encoded before storing in the Kubernetes Secret

## Prerequisites
- A running Kubernetes cluster with `kubectl` configured
- Twingate account with admin access to create service accounts
- `openssl` or equivalent tool for base64 encoding
- Twingate service account and downloaded service key (JSON)

## Usage / Step-by-Step
1. Create a service account in the Twingate Admin UI and generate a service key
2. Assign the desired Twingate resources to the service account
3. Base64-encode the key file:
   ```
   openssl base64 -in key.json -out key.base64
   ```
4. Paste the encoded content into `secret.yaml`
5. Merge the sidecar container definition and volume sections from `deployment.yaml` into your existing deployment manifest
6. Deploy both resources to the same namespace:
   ```
   kubectl create -f secret.yaml
   kubectl apply -f deployment.yaml
   ```

## Configuration Values

| Item | Location | Notes |
|------|----------|-------|
| Base64 service key | `secret.yaml` | Content of `key.base64` |
| Sidecar container spec | `deployment.yaml` → `spec.template.spec.containers` | Add alongside existing containers |
| Shared volume | `deployment.yaml` → `spec.template.spec.volumes` | Required for sidecar communication |
| `privileged: true` | Sidecar container `securityContext` | Mandatory; cannot be removed |

## Gotchas
- `privileged: true` is required and non-negotiable for the headless client; clusters with restrictive Pod Security Standards/Admission may block this
- The Secret **must** be in the same namespace as the Deployment
- The service key is base64-encoded at the file level (not just standard Kubernetes Secret base64); ensure double-encoding does not occur
- This is an example repo—not a production-hardened Helm chart or operator; adapt manifests to your own security and lifecycle requirements

## Related Docs
- [Twingate Service Accounts](https://www.twingate.com/docs/services)
- [Twingate Headless Client](https://www.twingate.com/docs/linux-headless-client)
- Kubernetes [Sidecar Containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/)
- Kubernetes [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)