# How to Upgrade Connectors Running in Kubernetes with Helm

## Summary
Guide for upgrading Twingate Connectors deployed in Kubernetes via Helm. Covers version checking, Helm chart updates, and Connector image updates. Updating the Helm chart and updating the Connector image are separate operations.

## Key Information
- Helm chart updates do **not** automatically update the running Connector image
- Official Helm chart sets `imagePullPolicy: Always` — pod restart pulls latest image
- Connector release notes available separately for version/changelog info

## Prerequisites
- Twingate Connector deployed in Kubernetes using Helm
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
Restart the pod — `imagePullPolicy: Always` ensures the latest image is pulled on restart:
```bash
kubectl rollout restart deployment/<connector-deployment-name> -n twingate
```
*(Standard Kubernetes restart method; not explicitly stated in docs but follows from `Always` pull policy)*

## Configuration Values

| Field | Value | Effect |
|-------|-------|--------|
| `imagePullPolicy` | `Always` | Pulls latest Connector image on every pod restart |

## Gotchas
- **Helm chart update ≠ image update**: Running `helm repo update` only updates the chart definition, not the running pod's image
- Recommended practice: update Helm chart **every time** you update Connectors, even though chart changes are infrequent
- Must explicitly restart pods to apply a new Connector image version

## Related Docs
- [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes) — latest build versions and update notes
- [Official Twingate Helm Chart](https://artifacthub.io/packages/helm/twingate/connector) — chart source and configuration reference