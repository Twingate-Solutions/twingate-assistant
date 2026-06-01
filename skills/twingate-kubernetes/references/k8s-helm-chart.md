# Deploy Twingate Connector with K8s Helm Chart

## Summary
Deploy Twingate Connectors to Kubernetes clusters (GKE, EKS, MicroK8s, etc.) using the official Twingate Helm Chart. The chart bootstraps a Connector pod in the specified namespace with minimal configuration required.

## Key Information
- Official chart hosted at: `https://twingate.github.io/helm-charts`
- GitHub repo contains full parameter documentation
- Updating the Helm chart does NOT automatically update Connector images/pods
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits

## Prerequisites
- Helm installed and configured
- `kubectl` access to target K8s cluster
- Twingate Connector tokens: `accessToken` and `refreshToken`
- Twingate network name

## Step-by-Step Installation

```bash
# 1. Add Twingate Helm repo
helm repo add twingate https://twingate.github.io/helm-charts

# 2. Install/upgrade Connector
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
- **Chart updates ≠ image updates**: Upgrading the Helm chart version does not update the Connector Docker images — follow the separate Helm Chart updating guide for full upgrades
- Namespace must be specified with `-n [namespace]`; no default namespace is assumed in the examples

## Related Docs
- Official Helm Chart (GitHub)
- Helm Chart updating guide
- Peer-to-peer connections setup
- Fair Use Policy