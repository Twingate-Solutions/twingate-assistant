---
source: https://github.com/Twingate/kubernetes-operator
type: github
fetched: 2026-11-08
source_version: 9acf3a353e1fd56e956dd225998d07c7a61047b5
trust: official
---

# Twingate Kubernetes Operator

## Summary
A custom Kubernetes controller that manages Twingate resources (Resources, Resource Access policies, etc.) via Kubernetes CRDs. It bridges Kubernetes-native workflows with the Twingate Zero Trust Network using the Twingate API.

## Key Information
- Published Docker image: `twingate/kubernetes-operator` on Docker Hub
- Helm chart published to OCI registry: `oci://ghcr.io/twingate/helmcharts/twingate-operator`
- CRDs are **not** automatically updated on `helm upgrade` (Helm v3 limitation — must be updated manually)
- Full API reference and getting-started guide available on the [repo wiki](https://github.com/Twingate/kubernetes-operator/wiki)

## Prerequisites
- Kubernetes 1.16+
- Twingate account with a configured Remote Network and deployed connectors (see [Twingate Helm charts](https://github.com/Twingate/helm-charts))
- Twingate API token with **Read/Write/Provision** permissions (generated in the Twingate Admin Console)
- Helm v3

## Installation (Helm via OCI — recommended)

1. Copy the [default `values.yaml`](https://github.com/Twingate/kubernetes-operator/blob/main/deploy/twingate-operator/values.yaml) to a local file.
2. Edit the `twingateOperator` section with your account details and API token.
3. Install or upgrade:

```bash
helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator \
  --install --wait -f ./values.yaml
```

Add `-n <namespace>` to target a specific namespace.

## Installation (Helm from cloned repo)

```bash
git clone https://github.com/Twingate/kubernetes-operator.git
cp ./deploy/twingate-operator/values.yaml ./deploy/twingate-operator/values.local.yaml
# Edit values.local.yaml, then:
helm upgrade twop ./deploy/twingate-operator \
  --install --wait -f ./deploy/twingate-operator/values.local.yaml
```

## Configuration Values
Key settings live under the `twingateOperator` key in `values.yaml`. Refer to the default values file for the full list; at minimum configure:

| Field | Description |
|---|---|
| `twingateOperator.apiToken` | Twingate API token (Read/Write/Provision) |
| `twingateOperator.network` | Twingate account/network name |
| `twingateOperator.remoteNetwork` | Name of the Remote Network representing the cluster |

## Gotchas
- **CRD upgrades are manual.** Helm v3 does not upgrade CRDs automatically on `helm upgrade`. Apply updated CRD manifests manually before upgrading the chart.
- Connectors must be deployed to the Remote Network before the operator can route traffic; the operator does not deploy connectors itself.

## Related Docs
- [Wiki](https://github.com/Twingate/kubernetes-operator/wiki)
- [Getting Started](https://github.com/Twingate/kubernetes-operator/wiki/Getting-Started)
- [API Reference](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference)
- [Changelog](https://github.com/Twingate/kubernetes-operator/blob/main/CHANGELOG.md)
- [Developer Guide](https://github.com/Twingate/kubernetes-operator/blob/main/DEVELOPER.md)
- [Twingate Helm Charts](https://github.com/Twingate/helm-charts)