---
source: https://www.twingate.com/docs/k8s-helm-chart-upgrades
type: docs
fetched: 2026-08-05
source_version: c105dfd487c942ab0365cbe19140956d8f3179b9b071b092e71e5c8bf16f0769
---

# Upgrading Twingate Connectors in Kubernetes with Helm

## Summary
Guide for checking and upgrading Twingate Connector versions running in Kubernetes via Helm. Helm chart updates and Connector image updates are separate operations. Restarting the pod triggers a fresh image pull due to the `Always` pull policy.

## Key Information
- Helm chart updates do **not** automatically update the Connector container image
- Default `imagePullPolicy: Always` means pod restart = latest image pulled
- Check release notes before upgrading: [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes)

## Prerequisites
- Helm installed and configured
- `kubectl` access to the cluster
- Twingate Helm repo added

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
Restart the pod to trigger image pull (leverages `pullPolicy: Always`):
```bash
kubectl rollout restart deployment/<connector-deployment-name> -n twingate
```
Or delete the pod to force recreation:
```bash
kubectl delete pod connector-1 -n twingate
```

## Configuration Values
| Field | Value | Effect |
|-------|-------|--------|
| `image.pullPolicy` | `Always` (default) | Pulls latest image on every pod start |

## Gotchas
- **Helm chart update ≠ image update** — must restart pods separately after `helm repo update`
- Helm chart changes are infrequent; image updates are more common
- Pod name in `kubectl exec` must match actual running pod name

## Related Docs
- [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes)
- [Official Twingate Helm Chart](https://artifacthub.io/packages/helm/twingate/connector)
- Kubernetes Connector deployment guide