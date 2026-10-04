---
source: https://github.com/Twingate/kubernetes-operator
type: github
fetched: 2026-10-04
source_version: 705382e376f319c2f527ef4ed30288b8f8b20603
trust: official
---

# Twingate Kubernetes Operator

## Summary
A custom Kubernetes controller that manages Twingate resources (Resources, Groups, Connectors) via Kubernetes CRDs. It syncs Kubernetes object state to the Twingate API, enabling GitOps-style management of Twingate Zero Trust Network configuration.

## Key Information
- Manages Twingate resources declaratively through Kubernetes custom resources
- Published as a Helm chart at `oci://ghcr.io/twingate/helmcharts/twingate-operator`
- Container image available on Docker Hub: `twingate/kubernetes-operator`
- CRDs are **not** auto-updated on `helm upgrade`; manual CRD updates required

## Prerequisites
- Kubernetes 1.16+
- Active Twingate account with a Remote Network configured for the cluster
- Twingate Connectors deployed (via the [Twingate Helm charts](https://github.com/Twingate/helm-charts))
- Twingate API token with **Read/Write/Provision** permissions (generated in the Twingate Admin Console)

## Installation

### Via OCI Helm Chart (recommended)
1. Download the default `values.yaml` from `deploy/twingate-operator/values.yaml`.
2. Edit `twingateOperator` settings, including the API token and account details.
3. Install:
   ```bash
   helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator --install --wait -f ./values.yaml
   ```

### Via Cloned Repository
1. Clone the repository.
2. Copy and edit the values file:
   ```bash
   cp ./deploy/twingate-operator/values.yaml ./deploy/twingate-operator/values.local.yaml
   ```
3. Install:
   ```bash
   helm upgrade twop ./deploy/twingate-operator --install --wait -f ./deploy/twingate-operator/values.local.yaml
   ```

Add `-n <namespace>` to either command to target a specific namespace.

## Configuration Values
| Key | Description |
|-----|-------------|
| `twingateOperator` | Top-level Helm values block for operator settings |
| Twingate API token | Set in `values.yaml`; requires Read/Write/Provision scope |

See the [default values file](https://github.com/Twingate/kubernetes-operator/blob/main/deploy/twingate-operator/values.yaml) and [API Reference](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference) for the full list.

## Gotchas
- Helm v3 does **not** upgrade CRDs automatically; manually apply CRD updates after each chart upgrade.
- Connectors must be pre-deployed and a Remote Network must exist in Twingate before the operator can manage resources.

## Related Docs
- [Wiki](https://github.com/Twingate/kubernetes-operator/wiki)
- [Getting Started](https://github.com/Twingate/kubernetes-operator/wiki/Getting-Started)
- [API Reference](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference)
- [CHANGELOG](https://github.com/Twingate/kubernetes-operator/blob/main/CHANGELOG.md)
- [Twingate Helm Charts](https://github.com/Twingate/helm-charts)