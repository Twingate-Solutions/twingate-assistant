---
source: https://github.com/Twingate/kubernetes-operator
type: github
fetched: 2026-09-20
source_version: 7c63ac598efa37793653962cc54b702c5a819b8c
---

The changes are minor CI workflow pin updates (QEMU and Buildx actions bumped to v4.4.0) with no impact on the summary's content. The summary remains accurate as-is.

---

# Twingate Kubernetes Operator

## Summary
A Kubernetes custom controller (operator) that manages Twingate Zero Trust Network resources through Kubernetes CRDs. It bridges Kubernetes clusters with the Twingate API, allowing Twingate resources (networks, connectors, applications) to be declared and managed as Kubernetes objects.

## Key Information
- Written in Python; images published to Docker Hub (`twingate/kubernetes-operator`)
- Helm chart published to OCI registry: `oci://ghcr.io/twingate/helmcharts/twingate-operator`
- CRDs are **not** auto-updated on `helm upgrade` — manual CRD updates required
- Active dependency maintenance via Dependabot

## Prerequisites
- Kubernetes 1.16+
- Twingate account with a configured Remote Network for the cluster
- Twingate connectors deployed (Helm chart: `github.com/Twingate/helm-charts`)
- Twingate API token with **Read/Write/Provision** permissions (generated in Admin Console)

## Installation (Helm via OCI — recommended)

1. Download the default values file from `deploy/twingate-operator/values.yaml`
2. Edit `twingateOperator` section with your account details and API token
3. Install:
   ```bash
   helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator \
     --install --wait -f ./values.yaml
   ```
   Add `-n <namespace>` to target a specific namespace.

## Installation (Git clone)

```bash
cp ./deploy/twingate-operator/values.yaml ./deploy/twingate-operator/values.local.yaml
# Edit values.local.yaml
helm upgrade twop ./deploy/twingate-operator --install --wait \
  -f ./deploy/twingate-operator/values.local.yaml
```

## Configuration Values
Set in `values.yaml` under the `twingateOperator` key:

| Key | Description |
|-----|-------------|
| `twingateOperator.apiToken` | Twingate API token (Read/Write/Provision) |
| `twingateOperator.account` | Twingate account name/URL |

Full reference: [API Reference wiki](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference) and [default values.yaml](https://github.com/Twingate/kubernetes-operator/blob/main/deploy/twingate-operator/values.yaml)

## Gotchas
- **CRD upgrades are manual**: Helm v3 does not update CRDs on `helm upgrade`. You must apply CRD changes manually before upgrading the chart.
- Connectors and a Remote Network must exist in Twingate **before** deploying the operator.
- API token must have Provision-level permissions, not just Read/Write.

## Related Docs
- [Wiki / Getting Started](https://github.com/Twingate/kubernetes-operator/wiki/Getting-Started)
- [API Reference](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference)
- [Developer Guide](./DEVELOPER.md)
- [Changelog](./CHANGELOG.md)
- [Twingate Connector Helm Charts](https://github.com/Twingate/helm-charts)
- [Twingate Community Forum](https://forum.twingate.com/)