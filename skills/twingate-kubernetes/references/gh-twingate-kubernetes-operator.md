---
source: https://github.com/Twingate/kubernetes-operator
type: github
fetched: 2026-08-09
source_version: a0bbe14f40916e18a9ca05d1b0df82242b142e54
---

# Twingate Kubernetes Operator

## Summary
A Kubernetes custom controller that manages Twingate resources (Remote Networks, Resources, Groups, etc.) within a Kubernetes cluster using CRDs. It automates Twingate configuration via Kubernetes-native assets and integrates with the Twingate API.

## Key Information
- Published as OCI Helm chart at `oci://ghcr.io/twingate/helmcharts/twingate-operator`
- Docker images available on [Docker Hub](https://hub.docker.com/r/twingate/kubernetes-operator)
- Supports Kubernetes Services annotation-based resource creation; removing annotations retains the Kubernetes Resource
- Helm can adopt operator-generated Kubernetes Resources (recent feature)
- CRDs are **not** auto-updated on `helm upgrade`; must be updated manually

## Prerequisites
- Kubernetes 1.16+
- Active Twingate account with at least one Remote Network configured for the cluster
- Twingate connectors deployed (use [twingate/helm-charts](https://github.com/Twingate/helm-charts))
- Twingate API token with **Read/Write/Provision** permissions (generated in Twingate Admin Console)

## Installation

### Via OCI (recommended)
```bash
# 1. Download and edit default values
curl -O https://github.com/Twingate/kubernetes-operator/blob/main/deploy/twingate-operator/values.yaml
# Edit twingateOperator section

# 2. Install
helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator \
  --install --wait -f ./values.yaml
```

### Via Git Clone
```bash
git clone https://github.com/Twingate/kubernetes-operator
cp ./deploy/twingate-operator/values.yaml ./deploy/twingate-operator/values.local.yaml
# Edit values.local.yaml

helm upgrade twop ./deploy/twingate-operator \
  --install --wait -f ./deploy/twingate-operator/values.local.yaml
```

Add `-n [namespace]` to either command to target a specific namespace.

## Configuration Values
Primary configuration lives in `values.yaml` under the `twingateOperator` key:

| Key | Description |
|-----|-------------|
| `twingateOperator.apiToken` | Twingate API token (Read/Write/Provision) |
| `twingateOperator.account` | Twingate account name/URL |
| `twingateOperator.remoteNetwork` | Target Remote Network name |

See [default values.yaml](https://github.com/Twingate/kubernetes-operator/blob/main/deploy/twingate-operator/values.yaml) and the [API Reference](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference) for full options.

## Gotchas
- **CRDs are not upgraded automatically by Helm v3.** After a chart upgrade, CRDs must be applied manually per [Helm CRD documentation](https://helm.sh/docs/chart_best_practices/custom_resource_definitions).
- Connectors must be deployed separately before the operator can route traffic; the operator manages Twingate resource definitions, not connector deployment.
- Removing a Service annotation no longer deletes the associated Twingate Kubernetes Resource (behavior changed in latest release).

## Related Docs
- [Wiki / Getting Started](https://github.com/Twingate/kubernetes-operator/wiki/Getting-Started)
- [API Reference](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference)
- [CHANGELOG](https://github.com/Twingate/kubernetes-operator/blob/main/CHANGELOG.md)
- [Developer Guide](https://github.com/Twingate/kubernetes-operator/blob/main/DEVELOPER.md)
- [Twingate Helm Charts](https://github.com/Twingate/helm-charts) (connector deployment)