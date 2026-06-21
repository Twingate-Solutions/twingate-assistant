# How to Upgrade Connectors Running in Kubernetes with Helm

## Summary
Covers how to check the current Connector version, update the Helm chart, and upgrade the Connector image in Kubernetes deployments. Helm chart updates and Connector image updates are separate operations.

## Key Information
- Helm chart update does **not** automatically update the Connector image in running Pods
- Default `imagePullPolicy: Always` means restarting a Pod pulls the latest Connector image
- Check release notes for version details before upgrading

## Prerequisites
- Connector deployed via Twingate Helm chart in Kubernetes
- `kubectl` and `helm` CLI access to the cluster

## Step-by-Step

### 1. Check Current Connector Version
```bash
kubectl exec <pod-name> -- ./connectord --version
```
Replace `<pod-name>` with the actual Pod name (e.g., `connector-1`).

### 2. Update the Helm Chart
```bash
helm repo update -n twingate
```

### 3. Update the Connector Image
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
| `image.pullPolicy` | `Always` | Pulls latest image on every Pod restart |

## Gotchas
- Updating the Helm chart (`helm repo update`) does **not** upgrade running Connector Pods — you must restart the Pod separately
- Helm chart changes are infrequent; image updates are the primary upgrade path
- Always check [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes) before upgrading

## Related Docs
- [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes)
- [Official Twingate Helm Chart](https://hub.docker.com/r/twingate/connector)
- Twingate Kubernetes deployment documentation