# Deploy a Connector with K8s Helm Chart

## Summary
Deploys Twingate Connectors to Kubernetes clusters using Helm. Supports GKE, EKS, MicroK8s, and any Helm-compatible cluster. The chart bootstraps a Connector deployment with configurable parameters.

## Key Information
- Official chart hosted at: `https://twingate.github.io/helm-charts` (GitHub)
- Updating the Helm chart does NOT automatically update Connector pod images — requires separate update process
- Peer-to-peer connections recommended to improve performance and stay within Fair Use Policy bandwidth limits

## Prerequisites
- Helm installed and configured
- Access to a Kubernetes cluster (GKE, EKS, MicroK8s, or other)
- Twingate `accessToken` and `refreshToken` for the Connector
- Twingate network name/identifier

## Step-by-Step Installation

1. Add the Twingate Helm repo:
   ```bash
   helm repo add twingate https://twingate.github.io/helm-charts
   ```

2. Install/upgrade the chart:
   ```bash
   helm upgrade --install twingate-connector twingate/connector -n [namespace] \
     --set connector.network=[network] \
     --set connector.accessToken=[accessToken] \
     --set connector.refreshToken=[refreshToken]
   ```

3. Uninstall:
   ```bash
   helm del twingate-connector -n [namespace]
   ```

## Configuration Values

| Parameter | Description |
|---|---|
| `connector.network` | Twingate network name |
| `connector.accessToken` | Connector access token |
| `connector.refreshToken` | Connector refresh token |

> Full parameter list available in the chart's Parameters section on GitHub.

## Gotchas
- **Helm chart updates ≠ Connector image updates**: Upgrading the chart does not pull new Connector images. Follow the separate Helm Chart updating guide for full updates.
- Namespace must be specified with `-n [namespace]`; omitting it deploys to `default`

## Related Docs
- [Official Helm Chart (GitHub)](https://github.com/twingate/helm-charts)
- Helm Chart updating guide
- Peer-to-peer connections setup
- Twingate Fair Use Policy