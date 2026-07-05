# How to Upgrade Connectors Running in Kubernetes with Helm

## Summary
Guide for upgrading Twingate Connectors deployed in Kubernetes via Helm. Covers version checking, Helm chart updates, and Connector image updates. Updating the Helm chart and updating the Connector image are separate operations.

## Key Information
- Helm chart updates do **not** automatically update the running Connector image
- The official Twingate Helm Chart sets `imagePullPolicy: Always` by default
- Restarting the pod triggers a pull of the latest Connector image
- Release notes available in Connector Release Notes documentation

## Prerequisites
- Twingate Connector deployed in Kubernetes via Helm
- `kubectl` access to the cluster
- Helm installed and Twingate repo configured

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
Restart the pod to pull the latest image (leverages `imagePullPolicy: Always`):
```bash
kubectl rollout restart deployment/<deployment-name> -n twingate
```
Or delete/restart the specific pod to force image pull.

## Configuration Values

| Field | Value | Effect |
|-------|-------|--------|
| `imagePullPolicy` | `Always` | Pulls latest image on every pod restart |

## Gotchas
- **Helm chart update ≠ image update**: Running `helm repo update` only updates the chart definition, not the running Connector binary. Must restart pods separately.
- Recommend updating the Helm chart every time you update Connectors, even though chart changes are infrequent.
- The `-n twingate` flag assumes the Twingate namespace; adjust if deployed elsewhere.

## Related Docs
- Connector Release Notes (for version numbers and change details)
- Official Twingate Helm Chart