---
source: https://www.twingate.com/docs/k8s-helm-chart
type: docs
fetched: 2026-11-13
source_version: 41d97579d83289a1aa31f24679161afe7e630649c5159ca8f416bde780dc45e1
trust: official
---

# How to Deploy a Connector with the K8s Helm Chart

## Summary
The Twingate Helm Chart deploys a Twingate Connector into a Kubernetes cluster (GKE, EKS, MicroK8s, or any cluster supporting Helm). It bootstraps the Connector using tokens generated for a Connector in your Twingate network. The official chart is hosted on GitHub.

## Key Information
- Chart repo: `https://twingate.github.io/helm-charts`
- Chart name: `twingate/connector`; suggested release name: `twingate-connector`
- Default install uses the chart's default configuration; additional parameters are listed in the chart's Parameters section on GitHub.
- Peer-to-peer connections are recommended for better user experience and to stay within the Fair Use Policy on bandwidth.
- Updating the Helm chart does **not** update the Connector images used by pods.

## Prerequisites
- A Kubernetes cluster and `kubectl` access
- Helm installed
- A Twingate network name
- Connector access token and refresh token (generated when you add a Connector in the Twingate Admin Console)
- A target namespace

## Step-by-Step

**Install**
```
helm repo add twingate https://twingate.github.io/helm-charts
helm upgrade --install twingate-connector twingate/connector -n [namespace] \
  --set connector.network=[network] \
  --set connector.accessToken=[accessToken] \
  --set connector.refreshToken=[refreshToken]
```

**Uninstall**
```
helm del twingate-connector -n [namespace]
```
This removes all Kubernetes components associated with the chart and deletes the release.

**Update**
Follow the Helm Chart updating guide to update both the chart and the Connectors.

## Configuration Values
| Parameter | Purpose |
|---|---|
| `connector.network` | Your Twingate network name |
| `connector.accessToken` | Connector access token |
| `connector.refreshToken` | Connector refresh token |
| `-n [namespace]` | Kubernetes namespace for the release |

Further parameters are documented in the chart's GitHub Parameters section.

## Gotchas
- Chart updates and Connector image updates are separate; follow the updating guide to update both.
- Passing tokens via `--set` can leave them in shell history; consider a values file or secrets management.
- Ensure network settings allow peer-to-peer connectivity to avoid relayed traffic and bandwidth concerns.

## Related Docs
- Twingate Helm Chart on GitHub (official chart and Parameters section)
- Helm Chart updating guide
- Peer-to-peer connections / supporting peer-to-peer
- Twingate Fair Use Policy