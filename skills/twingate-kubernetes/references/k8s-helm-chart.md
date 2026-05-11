# Deploy a Connector with K8s Helm Chart

## Summary
Deploys Twingate Connectors to Kubernetes clusters using the official Twingate Helm Chart. Supports GKE, EKS, MicroK8s, and any Helm-compatible cluster. The chart bootstraps a Connector pod in the specified namespace.

## Key Information
- Official chart hosted at: `https://twingate.github.io/helm-charts` (GitHub)
- Release name convention: `twingate-connector`
- Updating the Helm chart does **not** automatically update Connector images

## Prerequisites
- Helm installed and configured
- Access to a Kubernetes cluster
- Twingate Connector tokens (`accessToken`, `refreshToken`) and network name
- Namespace created in target cluster

## Step-by-Step: Install

```bash
# Add Twingate Helm repo
helm repo add twingate https://twingate.github.io/helm-charts

# Install/upgrade Connector
helm upgrade --install twingate-connector twingate/connector -n [namespace] \
  --set connector.network=[network] \
  --set connector.accessToken=[accessToken] \
  --set connector.refreshToken=[refreshToken]
```

## Step-by-Step: Uninstall

```bash
helm del twingate-connector -n [namespace]
```
Removes all Kubernetes components and deletes the release.

## Configuration Values

| Parameter | Description |
|-----------|-------------|
| `connector.network` | Twingate network name |
| `connector.accessToken` | Connector access token |
| `connector.refreshToken` | Connector refresh token |

Additional parameters documented in the chart's Parameters section on GitHub.

## Gotchas
- **Helm chart updates ≠ Connector image updates**: Must follow the separate Helm Chart updating guide to update Connector pod images
- Peer-to-peer connections should be enabled to avoid Fair Use Policy bandwidth limits — requires additional configuration

## Related Docs
- [Official Helm Chart (GitHub)](https://github.com/Twingate/helm-charts)
- Helm Chart updating guide (linked from Twingate docs)
- Peer-to-peer connections support guide