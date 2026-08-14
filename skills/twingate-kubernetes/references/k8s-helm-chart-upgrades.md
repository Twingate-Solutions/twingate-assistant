---
source: https://www.twingate.com/docs/k8s-helm-chart-upgrades
type: docs
fetched: 2026-08-14
source_version: 705d0bbb7b1d49c9d346897e70cb8457daffa9aaae4ce7b57bf3f2e2574982f3
---

# How to Upgrade Connectors Running in Kubernetes with Helm

## Summary
Covers checking the current Connector version and upgrading Twingate Connectors deployed via Helm in Kubernetes. Helm chart updates and Connector image updates are separate operations that must be performed independently.

## Key Information
- Helm chart update does **not** automatically update the Connector image/pods
- Default `pullPolicy` is set to `Always` in the official Twingate Helm Chart
- Restarting the pod triggers a pull of the latest Connector image
- Release notes available in Connector Release Notes documentation

## Prerequisites
- Twingate Connector deployed via Helm in Kubernetes
- `kubectl` and `helm` CLI access to the cluster

## Step-by-Step

### Check Current Connector Version
```bash
kubectl exec <pod-name> -- ./connectord --version
```
Replace `<pod-name>` with the actual Pod name (e.g., `connector-1`).

### Update Helm Chart
```bash
helm repo update -n twingate
```

### Update Connector Image
Restart the pod to trigger image pull (due to `pullPolicy: Always`):
```bash
# Force pod restart to pull latest image
kubectl rollout restart deployment/<deployment-name> -n twingate
```
Or delete the pod to allow it to be recreated with the latest image.

## Configuration Values

| Field | Value | Location |
|-------|-------|----------|
| `pullPolicy` | `Always` | Official Twingate Helm Chart |

## Gotchas
- **Two separate steps required**: Updating the Helm chart and updating the Connector image are independent — do both when upgrading
- Helm chart updates are infrequent, but recommended to run alongside any Connector image update
- The `-n twingate` flag in `helm repo update` targets the `twingate` namespace — adjust if deployed to a different namespace

## Related Docs
- Connector Release Notes
- [Official Twingate Helm Chart](https://www.twingate.com/docs/k8s-helm-chart-upgrades)
- Kubernetes Connector deployment documentation