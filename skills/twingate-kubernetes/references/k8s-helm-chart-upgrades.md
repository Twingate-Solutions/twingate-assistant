# How to Upgrade Connectors Running in Kubernetes with Helm

## Summary
Guide for upgrading Twingate Connectors deployed in Kubernetes via Helm. Covers version checking, Helm chart updates, and Connector image updates. Updating the Helm chart and updating the Connector image are separate operations.

## Key Information
- Helm chart updates do **not** automatically update the Connector image in running Pods
- The official Helm chart sets `pullPolicy: Always`, so restarting a Pod pulls the latest Connector image
- Helm chart changes are infrequent; update chart whenever updating Connectors

## Prerequisites
- Connectors deployed via Twingate official Helm chart
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
Restart the Pod to trigger image pull (due to `pullPolicy: Always`):
```bash
kubectl rollout restart deployment/<connector-deployment-name> -n twingate
```
Or delete the Pod to force recreation:
```bash
kubectl delete pod <pod-name> -n twingate
```

## Configuration Values
| Field | Value | Effect |
|-------|-------|--------|
| `pullPolicy` | `Always` | Pulls latest image on every Pod restart |

## Gotchas
- **Two-step process**: Must update Helm chart AND restart Pods separately to get latest Connector version
- Restarting the Pod is required to apply the new image — chart update alone is insufficient
- Check [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes) before upgrading to review breaking changes

## Related Docs
- [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes)
- [Official Twingate Helm Chart](https://github.com/Twingate/helm-charts)
- Kubernetes Connector deployment documentation