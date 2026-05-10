# How to Upgrade Connectors Running in Kubernetes with Helm

## Summary
Covers checking the current Connector version in Kubernetes and upgrading both the Helm chart and Connector container image. Helm chart updates and Connector image updates are separate operations.

## Key Information
- Helm chart update does **not** automatically update the running Connector image
- Default `imagePullPolicy` is set to `Always` in the official Twingate Helm chart
- Restarting the pod triggers a fresh image pull, effectively upgrading the Connector
- Release notes available in Connector Release Notes documentation

## Prerequisites
- `kubectl` access to the cluster
- `helm` CLI configured with Twingate repo
- Connectors deployed via official Twingate Helm chart

## Step-by-Step

### Check Current Connector Version
```bash
kubectl exec connector-1 -- ./connectord --version
```
Replace `connector-1` with the actual Pod name.

### Update Helm Chart
```bash
helm repo update -n twingate
```

### Update Connector Image
Restart the pod to pull the latest image (leverages `pullPolicy: Always`):
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
| `imagePullPolicy` | `Always` | Official Twingate Helm chart default |

## Gotchas
- **Two separate update steps**: Helm chart update and Connector image update must be done independently
- Updating the Helm chart alone leaves existing pods running the old Connector version
- Pod must be restarted to trigger image pull — no automatic rolling updates on chart update
- Recommended practice: update Helm chart every time you update Connectors

## Related Docs
- Connector Release Notes
- Official Twingate Helm Chart
- Kubernetes Connector deployment documentation