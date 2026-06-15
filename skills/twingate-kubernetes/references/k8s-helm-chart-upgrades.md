# How to Upgrade Connectors Running in Kubernetes with Helm

## Summary
Guide for upgrading Twingate Connectors deployed in Kubernetes via Helm. Covers checking current connector version, updating the Helm chart, and updating the Connector image. Image updates require a pod restart due to the `Always` pull policy.

## Key Information
- Updating the Helm chart does **not** automatically update the Connector image
- Official Helm chart uses `pullPolicy: Always` — pod restart triggers image pull
- Helm chart updates are infrequent but recommended when updating Connectors
- Latest version info available in Connector Release Notes

## Prerequisites
- Connector deployed in Kubernetes using Helm
- `kubectl` and `helm` CLI access to the cluster

## Step-by-Step

### Check Current Connector Version
```bash
kubectl exec <pod-name> -- ./connectord --version
```
Replace `<pod-name>` with the actual Pod name (e.g., `connector-1`).

### Update the Helm Chart
```bash
helm repo update -n twingate
```

### Update the Connector Image
Restart the Pod to trigger image pull (due to `pullPolicy: Always`):
```bash
kubectl rollout restart deployment/<connector-deployment-name> -n twingate
```
Or delete the pod to force recreation:
```bash
kubectl delete pod <pod-name> -n twingate
```

## Configuration Values
| Field | Value | Effect |
|-------|-------|--------|
| `image.pullPolicy` | `Always` | Pulls latest image on pod restart |

## Gotchas
- **Helm chart update ≠ image update**: Running `helm repo update` only updates the chart definition, not running pod images
- Pod must be restarted to pull and apply the latest Connector image
- Namespace flag `-n twingate` assumes default namespace; adjust if deployed elsewhere

## Related Docs
- Connector Release Notes (for version numbers and update notes)
- [Official Twingate Helm Chart](https://www.twingate.com/docs/k8s-helm-chart-upgrades)