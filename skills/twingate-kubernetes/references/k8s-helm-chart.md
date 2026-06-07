# Deploy a Connector with K8s Helm Chart

## Summary
Deploys Twingate Connectors to Kubernetes clusters using an official Helm Chart. Supports GKE, EKS, MicroK8s, and any Helm-compatible cluster. Chart bootstraps the Connector but does not automatically update Connector images on chart updates.

## Key Information
- Official chart hosted at: `https://twingate.github.io/helm-charts` (GitHub)
- Chart name: `twingate/connector`
- Updating the Helm chart does NOT update Connector pod images — requires separate update process
- Peer-to-peer connections recommended for better UX and Fair Use Policy compliance

## Prerequisites
- Kubernetes cluster (GKE, EKS, MicroK8s, or any Helm-supported cluster)
- Helm installed
- Twingate access token and refresh token
- Target namespace created

## Step-by-Step Installation

```bash
# Add Twingate Helm repo
helm repo add twingate https://twingate.github.io/helm-charts

# Install/upgrade Connector
helm upgrade --install twingate-connector twingate/connector -n [namespace] \
  --set connector.network=[network] \
  --set connector.accessToken=[accessToken] \
  --set connector.refreshToken=[refreshToken]
```

## Configuration Values

| Parameter | Description |
|---|---|
| `connector.network` | Twingate network name |
| `connector.accessToken` | Connector access token |
| `connector.refreshToken` | Connector refresh token |

Additional parameters available in the chart's Parameters section on GitHub.

## Uninstall

```bash
helm del twingate-connector -n [namespace]
```
Removes all associated Kubernetes components and deletes the release.

## Gotchas
- **Chart updates ≠ image updates**: Upgrading the Helm chart does not pull new Connector images; follow the separate [Helm Chart updating guide](https://www.twingate.com/docs) for full updates
- Namespace must be specified with `-n [namespace]` on both install and delete commands

## Related Docs
- [Official Helm Chart (GitHub)](https://github.com/Twingate/helm-charts)
- Helm Chart updating guide
- Peer-to-peer connections setup
- Fair Use Policy