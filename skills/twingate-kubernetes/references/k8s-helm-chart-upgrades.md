# How to Upgrade Connectors Running in Kubernetes with Helm

## Summary
Covers the process for checking Connector versions and upgrading Twingate Connectors deployed in Kubernetes via Helm. Helm chart updates and Connector image updates are separate operations. Restarting pods triggers a fresh image pull due to the default `pullPolicy: Always` setting.

## Key Information
- Helm chart update ≠ Connector image update; these are independent steps
- Default `pullPolicy` is `Always` in the official Twingate Helm chart
- Restarting the pod is sufficient to pull and run the latest Connector image
- Release notes available in Connector Release Notes documentation

## Prerequisites
- Twingate Connector deployed in Kubernetes using the official Helm chart
- `kubectl` and `helm` CLI access to the cluster
- Namespace `twingate` (used in examples)

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
Run before upgrading Connectors; recommended but does not update running Connector images.

### Update the Connector Image
Restart the pod to trigger an image pull:
```bash
kubectl rollout restart deployment/<connector-deployment-name> -n twingate
```
Or delete the pod to let it recreate:
```bash
kubectl delete pod <pod-name> -n twingate
```
The `pullPolicy: Always` setting ensures the latest image is pulled on restart.

## Configuration Values

| Field | Value | Location |
|-------|-------|----------|
| `pullPolicy` | `Always` | Official Twingate Helm chart (image spec) |

## Gotchas
- **Helm chart update does not update running pods** — must restart pods separately after updating the chart
- Helm chart changes are infrequent; image updates are the primary upgrade path
- Pod name must be specified exactly in `kubectl exec` commands

## Related Docs
- Connector Release Notes (for version numbers and changelog)
- Official Twingate Helm Chart repository