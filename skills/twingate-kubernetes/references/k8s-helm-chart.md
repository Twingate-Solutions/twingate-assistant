# Deploy a Connector with K8s Helm Chart

## Summary
Deploys Twingate Connectors to Kubernetes clusters using Helm. Supports GKE, EKS, MicroK8s, and any Helm-compatible cluster. The chart bootstraps a Connector pod in the target namespace.

## Key Information
- Official chart hosted at: `https://twingate.github.io/helm-charts` (GitHub)
- Updating the Helm chart does **not** automatically update Connector images
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits

## Prerequisites
- Helm installed and configured
- Access to a Kubernetes cluster (GKE, EKS, MicroK8s, etc.)
- Twingate Connector credentials: `network`, `accessToken`, `refreshToken`

## Step-by-Step

**Install:**
```bash
helm repo add twingate https://twingate.github.io/helm-charts

helm upgrade --install twingate-connector twingate/connector -n [namespace] \
  --set connector.network=[network] \
  --set connector.accessToken=[accessToken] \
  --set connector.refreshToken=[refreshToken]
```

**Uninstall:**
```bash
helm del twingate-connector -n [namespace]
```

## Configuration Values

| Parameter | Description |
|---|---|
| `connector.network` | Twingate network name |
| `connector.accessToken` | Connector access token |
| `connector.refreshToken` | Connector refresh token |

Full parameter list available in the chart's Parameters section on GitHub.

## Gotchas
- Updating the Helm chart version does **not** update the Connector Docker images — follow the separate Helm Chart updating guide for full updates
- Namespace must be specified with `-n [namespace]`; no default namespace is assumed in docs

## Related Docs
- [Official Helm Chart (GitHub)](https://github.com/twingate/helm-charts)
- Helm Chart updating guide (linked in docs)
- Peer-to-peer connections setup guide
- Fair Use Policy