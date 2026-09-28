---
source: https://github.com/Twingate/kubernetes-operator
type: github
fetched: 2026-09-27
source_version: 8518a54a8dc038894cf9d162fa8f8e8520b684bf
---

# Twingate Kubernetes Operator

## Summary
A Kubernetes custom controller that manages Twingate resources (Resources, Groups, Connectors) via Kubernetes CRDs. It automates provisioning and lifecycle management of Twingate objects by reconciling Kubernetes manifests against the Twingate API.

## Key Information
- Distributed as a Helm chart via OCI: `oci://ghcr.io/twingate/helmcharts/twingate-operator`
- Docker image: `twingate/kubernetes-operator` (Docker Hub)
- CRDs are **not** auto-updated on `helm upgrade`; manual CRD updates required
- Latest release: v1.3.2 (chores/dependency bumps only)

## Prerequisites
- Kubernetes 1.16+
- Twingate account with a configured Remote Network for the cluster
- Twingate Connectors deployed (Helm chart: `github.com/Twingate/helm-charts`)
- Twingate API token with **Read/Write/Provision** permissions (generated in Admin Console)

## Usage / Step-by-Step

### Install via OCI (recommended)
```bash
# 1. Copy and edit values
cp <default-values.yaml> ./values.yaml
# Edit twingateOperator section

# 2. Deploy
helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator \
  --install --wait -f ./values.yaml
```

### Install by cloning repo
```bash
cp ./deploy/twingate-operator/values.yaml ./deploy/twingate-operator/values.local.yaml
# Edit values.local.yaml

helm upgrade twop ./deploy/twingate-operator \
  --install --wait -f ./deploy/twingate-operator/values.local.yaml
```

### Upgrade
```bash
# Manually apply CRDs first, then:
helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator -f ./values.yaml
```

## Configuration Values
Set under `twingateOperator` in `values.yaml`:

| Key | Description |
|-----|-------------|
| `twingateOperator.apiToken` | Twingate API token (Read/Write/Provision) |
| `twingateOperator.network` | Twingate account network name |
| `twingateOperator.remoteNetwork` | Target Remote Network name |

Full defaults: `deploy/twingate-operator/values.yaml` in repo.

## Gotchas
- **CRDs are not upgraded automatically by Helm v3.** Manually update CRDs before running `helm upgrade`.
- Namespace scoping requires explicitly passing `-n [namespace]` to Helm commands.
- Connectors must be deployed separately before the operator can function; the operator does not deploy connectors itself.

## Related Docs
- [Wiki](https://github.com/Twingate/kubernetes-operator/wiki)
- [Getting Started](https://github.com/Twingate/kubernetes-operator/wiki/Getting-Started)
- [API Reference](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference)
- [CHANGELOG](./CHANGELOG.md)
- [Developer Guide](./DEVELOPER.md)
- [Twingate Helm Charts](https://github.com/Twingate/helm-charts)