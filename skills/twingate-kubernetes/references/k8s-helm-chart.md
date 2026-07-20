# Deploy Twingate Connector with K8s Helm Chart

## Summary
Deploy Twingate Connectors to Kubernetes clusters using the official Helm Chart. Supports GKE, EKS, MicroK8s, and any Helm-compatible cluster. Chart bootstraps a Connector deployment with configurable parameters.

## Key Information
- Official chart hosted at: `https://twingate.github.io/helm-charts` (GitHub)
- Release name convention: `twingate-connector`
- Updating the Helm chart does NOT automatically update Connector images/pods

## Prerequisites
- Kubernetes cluster (GKE, EKS, MicroK8s, or other Helm-compatible)
- Helm installed
- Twingate `network`, `accessToken`, and `refreshToken` values
- Target namespace created

## Step-by-Step Installation

```bash
# 1. Add Twingate Helm repo
helm repo add twingate https://twingate.github.io/helm-charts

# 2. Install/upgrade connector
helm upgrade --install twingate-connector twingate/connector -n [namespace] \
  --set connector.network=[network] \
  --set connector.accessToken=[accessToken] \
  --set connector.refreshToken=[refreshToken]
```

## Uninstallation

```bash
helm del twingate-connector -n [namespace]
# Removes all K8s components and deletes the release
```

## Configuration Values

| Parameter | Description |
|---|---|
| `connector.network` | Twingate network name |
| `connector.accessToken` | Connector access token |
| `connector.refreshToken` | Connector refresh token |

> Full parameter list available in the chart's Parameters section on GitHub.

## Gotchas
- **Image updates are decoupled**: Upgrading the Helm chart does not update Connector pod images — follow the separate [Helm Chart updating guide](https://www.twingate.com/docs) for both chart and image updates
- Peer-to-peer connections should be configured to avoid Fair Use Policy bandwidth issues — requires additional setup

## Related Docs
- [Official Helm Chart (GitHub)](https://github.com/Twingate/helm-charts)
- Helm Chart updating guide
- Peer-to-peer connections setup
- Fair Use Policy