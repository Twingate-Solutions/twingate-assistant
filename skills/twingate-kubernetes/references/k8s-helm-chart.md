# Deploy a Connector with K8s Helm Chart

## Summary
Deploy Twingate Connectors to Kubernetes clusters using the official Helm Chart. Supports GKE, EKS, MicroK8s, and any Helm-compatible cluster. Chart bootstraps a Connector deployment with configurable parameters.

## Key Information
- Official chart hosted at `https://twingate.github.io/helm-charts` (GitHub)
- Updating the Helm chart does **not** automatically update Connector images/pods
- Supports peer-to-peer connections (recommended for Fair Use Policy compliance)

## Prerequisites
- Helm installed and configured
- Access to a Kubernetes cluster
- Twingate `accessToken` and `refreshToken` for the Connector
- Twingate network name

## Step-by-Step Installation

```bash
# Add the Twingate Helm repo
helm repo add twingate https://twingate.github.io/helm-charts

# Install/upgrade the connector
helm upgrade --install twingate-connector twingate/connector -n [namespace] \
  --set connector.network=[network] \
  --set connector.accessToken=[accessToken] \
  --set connector.refreshToken=[refreshToken]
```

## Uninstall

```bash
helm del twingate-connector -n [namespace]
```

## Configuration Values

| Parameter | Description |
|-----------|-------------|
| `connector.network` | Twingate network name |
| `connector.accessToken` | Connector access token |
| `connector.refreshToken` | Connector refresh token |

Additional parameters available in the chart's Parameters section on GitHub.

## Gotchas
- Upgrading the Helm chart does **not** update Connector container images — follow the separate [Helm Chart updating guide](https://www.twingate.com/docs) for full updates
- Namespace must be specified with `-n [namespace]`; no default namespace is assumed in the commands

## Related Docs
- [Official Helm Chart (GitHub)](https://github.com/Twingate/helm-charts)
- Helm Chart updating guide
- Peer-to-peer connections setup
- Fair Use Policy