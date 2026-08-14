---
source: https://github.com/Twingate/kubernetes-operator
type: github
fetched: 2026-08-14
source_version: d4bfd2b72cc2200f71c2559e08b298c1bc10440c
---

# Twingate Kubernetes Operator

## Summary
A Kubernetes custom controller that manages Twingate resources (Remote Networks, Resources, Groups, etc.) within a Kubernetes cluster using CRDs. It automates Twingate configuration via Kubernetes-native assets and integrates with the Twingate API. Licensed under Apache 2.0.

## Key Information
- **Latest release: v2.0.0** (breaking changes — see [v1 → v2 migration guide](https://github.com/Twingate/kubernetes-operator/wiki/Migration-v1-to-v2))
- Published as OCI Helm chart at `oci://ghcr.io/twingate/helmcharts/twingate-operator`
- Docker images available on [Docker Hub](https://hub.docker.com/r/twingate/kubernetes-operator)
- Supports Kubernetes Services annotation-based resource creation; removing annotations retains the Kubernetes Resource
- Helm can adopt operator-generated Kubernetes Resources
- CRDs are **not** auto-updated on `helm upgrade`; must be updated manually

## Prerequisites
- Kubernetes 1.16+ (deprecated Kubernetes versions removed in v2.0.0)
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

## v2.0.0 Breaking Changes
- **`twingate.com/resource` Service annotation removed**: Services annotated with `twingate.com/resource*` are no longer reconciled; migrate to `resource.twingate.com` equivalents.
- **Deprecated Kubernetes versions removed**.
- **Object-reference `namespace` defaults to the CR's own namespace** when not explicitly specified.
- **License changed to Apache 2.0**.

## Notable v2.0.0 Features
- `TwingateResourceAccess` is now reconciled when the referenced resource or principal ID changes.
- Kubernetes Resources left behind by the v1→v2 upgrade are automatically repaired.
- `remoteNetworkId` field added to `TwingateGateway`, `TwingateResource`, and `TwingateConnector` CRDs.
- `WebApp` resource type support added, including `requestHeaderRewrites` and k8s Service annotation.
- `TwingateGateway` and `TwingateCertificateAuthority` custom resources supported.