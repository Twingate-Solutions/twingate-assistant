# Deploy Twingate Connector with K8s Helm Chart

## Summary
Deploys Twingate Connectors to Kubernetes clusters using the official Twingate Helm Chart. Supports GKE, EKS, MicroK8s, and any Helm-compatible cluster. Bootstraps a Connector pod within the specified namespace.

## Key Information
- Official chart hosted at: `https://twingate.github.io/helm-charts` (GitHub)
- Chart name: `twingate/connector`
- Updating the Helm chart does NOT automatically update Connector images/pods
- Peer-to-peer connections recommended for bandwidth Fair Use Policy compliance

## Prerequisites
- Helm installed and configured
- Access to a Kubernetes cluster (GKE, EKS, MicroK8s, etc.)
- Twingate `accessToken` and `refreshToken` (from Twingate Admin Console)
- Twingate network name

## Step-by-Step

**Install:**
```bash
# Add Twingate Helm repo
helm repo add twingate https://twingate.github.io/helm-charts

# Deploy connector
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

Additional parameters available in the [chart's Parameters section](https://github.com/Twingate/helm-charts).

## Gotchas
- **Helm chart updates ≠ Connector image updates** — must follow separate [Helm Chart updating guide](https://www.twingate.com/docs/helm-chart-update) to update Connector pod images
- Namespace (`-n [namespace]`) must be specified consistently across install/uninstall commands
- Release name (`twingate-connector`) is used for deletion — track this name

## Related Docs
- [Official Helm Chart on GitHub](https://github.com/Twingate/helm-charts)
- [Helm Chart Updating Guide](https://www.twingate.com/docs/helm-chart-update)
- [Peer-to-Peer Connections Guide](https://www.twingate.com/docs/peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)