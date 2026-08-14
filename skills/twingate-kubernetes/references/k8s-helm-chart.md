---
source: https://www.twingate.com/docs/k8s-helm-chart
type: docs
fetched: 2026-08-14
source_version: 10bb4db15d3e8390d73fe234517fde4ed9968fff1fa0f899bb67cf6a088d1c0d
---

# Deploy Twingate Connector with K8s Helm Chart

## Summary
Deploys Twingate Connectors to Kubernetes clusters (GKE, EKS, MicroK8s, etc.) using the official Twingate Helm Chart. The chart bootstraps a Connector pod within your K8s cluster. Updating the Helm chart does not automatically update Connector images.

## Key Information
- Official chart hosted at: `https://twingate.github.io/helm-charts`
- GitHub repo: `https://github.com/twingate/helm-charts`
- Supports any Kubernetes distribution with Helm support
- Peer-to-peer connections recommended for bandwidth Fair Use Policy compliance

## Prerequisites
- Helm installed
- Kubernetes cluster access (kubectl configured)
- Twingate Connector tokens: `accessToken` and `refreshToken`
- Twingate network name

## Step-by-Step

### Install
```bash
# Add Twingate Helm repo
helm repo add twingate https://twingate.github.io/helm-charts

# Deploy connector
helm upgrade --install twingate-connector twingate/connector -n [namespace] \
  --set connector.network=[network] \
  --set connector.accessToken=[accessToken] \
  --set connector.refreshToken=[refreshToken]
```

### Uninstall
```bash
helm del twingate-connector -n [namespace]
```

## Configuration Values

| Parameter | Description |
|-----------|-------------|
| `connector.network` | Twingate network name |
| `connector.accessToken` | Connector access token |
| `connector.refreshToken` | Connector refresh token |

Additional parameters listed in the [chart's Parameters section](https://github.com/twingate/helm-charts).

## Gotchas
- **Helm chart updates ≠ Connector image updates** — updating the chart does not update the Connector Docker images; follow the separate [Helm Chart updating guide](https://www.twingate.com/docs/helm-chart-updating-guide)
- Namespace must exist or be created before install; specify with `-n [namespace]`
- Tokens (`accessToken`, `refreshToken`) should ideally be passed via Kubernetes Secrets rather than plain `--set` flags to avoid exposure in shell history

## Related Docs
- [Helm Chart GitHub Repository](https://github.com/twingate/helm-charts)
- [Helm Chart Updating Guide](https://www.twingate.com/docs/helm-chart-updating-guide)
- [Supporting Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)