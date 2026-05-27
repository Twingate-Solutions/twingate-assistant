# How to Upgrade Connectors Running in Kubernetes with Helm

## Summary
Guide for upgrading Twingate Connectors deployed in Kubernetes via Helm. Covers checking current connector version, updating the Helm chart, and updating the Connector image. Image updates require a pod restart due to the `Always` pull policy.

## Key Information
- Updating the Helm chart does **not** automatically update the running Connector image
- The official Twingate Helm chart sets `pullPolicy: Always` — pod restart triggers image pull
- Helm chart updates are infrequent but recommended when upgrading Connectors
- Release notes available in Connector Release Notes documentation

## Prerequisites
- Kubernetes cluster with Twingate Connector deployed via Helm
- `kubectl` and `helm` CLI tools configured
- Access to the `twingate` namespace

## Step-by-Step

### 1. Check Current Connector Version
```bash
kubectl exec connector-1 -- ./connectord --version
```
Replace `connector-1` with the actual Pod name.

### 2. Update the Helm Chart
```bash
helm repo update -n twingate
```

### 3. Update the Connector Image
Restart the pod to trigger image pull (due to `pullPolicy: Always`):
```bash
kubectl rollout restart deployment/<connector-deployment-name> -n twingate
```
Or delete the pod to force recreation:
```bash
kubectl delete pod connector-1 -n twingate
```

## Configuration Values
| Field | Value | Location |
|-------|-------|----------|
| `pullPolicy` | `Always` | Official Twingate Helm Chart |

## Gotchas
- **Helm chart update ≠ image update**: Running `helm repo update` only updates chart metadata; the Connector binary is not upgraded until pods are restarted
- Pod name in `kubectl exec` must match the actual running pod name — verify with `kubectl get pods -n twingate`
- The `-n twingate` flag assumes the `twingate` namespace; adjust if deployed elsewhere

## Related Docs
- Connector Release Notes
- Official Twingate Helm Chart