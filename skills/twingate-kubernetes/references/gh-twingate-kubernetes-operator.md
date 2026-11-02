---
source: https://github.com/Twingate/kubernetes-operator
type: github
fetched: 2026-11-01
source_version: 8b5565516874ac54960ebd5c313142d2c5906b4e
trust: official
---

# Twingate Kubernetes Operator

## Summary
A custom Kubernetes controller that automates management of Twingate resources within a Kubernetes cluster. It integrates Kubernetes with the Twingate Zero Trust Network by reconciling custom resources against the Twingate API.

## Key Information
- Container images published to [Docker Hub](https://hub.docker.com/r/twingate/kubernetes-operator)
- Helm chart published to OCI registry: `oci://ghcr.io/twingate/helmcharts/twingate-operator`
- CRDs are **not** automatically updated on `helm upgrade` (Helm v3 behavior)
- Full API reference and getting-started guide available on the [repo wiki](https://github.com/Twingate/kubernetes-operator/wiki)

## Prerequisites
- Kubernetes 1.16+
- Twingate account with a Remote Network configured for the cluster
- Twingate connectors deployed (available via the [Twingate Helm charts repo](https://github.com/Twingate/helm-charts))
- Twingate API token with **Read/Write/Provision** permissions (generated in the Admin Console)

## Installation (Helm via OCI — recommended)

1. Download and copy the [default `values.yaml`](https://github.com/Twingate/kubernetes-operator/blob/main/deploy/twingate-operator/values.yaml) as a starting point.
2. Edit the `twingateOperator` section with your account details and API token.
3. Install or upgrade:

```bash
helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator \
  --install --wait -f ./values.yaml
```

Add `-n <namespace>` to target a specific namespace.

## Installation (Helm from cloned repo)

```bash
git clone https://github.com/Twingate/kubernetes-operator
cp ./deploy/twingate-operator/values.yaml ./deploy/twingate-operator/values.local.yaml
# Edit values.local.yaml
helm upgrade twop ./deploy/twingate-operator \
  --install --wait -f ./deploy/twingate-operator/values.local.yaml
```

## Configuration Values
Primary configuration lives in `values.yaml` under the `twingateOperator` key. Refer to the default values file for all available fields. Minimum required settings include:
- Twingate account/network name
- API token (Read/Write/Provision)

## Gotchas
- **CRDs are not auto-upgraded by Helm v3.** After a chart version bump, manually apply updated CRD manifests before running `helm upgrade`.
- Connectors must already be deployed into the target Remote Network before the operator can manage resources against it.

## Related Docs
- [Wiki](https://github.com/Twingate/kubernetes-operator/wiki)
- [Getting Started](https://github.com/Twingate/kubernetes-operator/wiki/Getting-Started)
- [API Reference](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference)
- [Changelog](https://github.com/Twingate/kubernetes-operator/blob/main/CHANGELOG.md)
- [Developer Guide](https://github.com/Twingate/kubernetes-operator/blob/main/DEVELOPER.md)
- [Twingate Helm Charts](https://github.com/Twingate/helm-charts)