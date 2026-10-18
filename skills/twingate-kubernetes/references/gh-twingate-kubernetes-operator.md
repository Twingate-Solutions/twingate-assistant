---
source: https://github.com/Twingate/kubernetes-operator
type: github
fetched: 2026-10-18
source_version: fe5bde8727e6832aa79c38ff7addd685cbe927ec
trust: official
---

# Twingate Kubernetes Operator

## Summary
A custom Kubernetes controller that manages Twingate resources (Resources, Groups, Users, Connectors) via Kubernetes CRDs. It syncs the desired state declared in Kubernetes manifests with the Twingate API. The operator is distributed as a Helm chart via OCI registry.

## Key Information
- Custom Resource Definitions (CRDs) for `TwingateResource`, `TwingateGroup`, `TwingateUser`, `TwingateConnector`, and related binding types
- Communicates with Twingate's GraphQL API using an API token
- Container image published to Docker Hub: `twingate/kubernetes-operator`
- Helm chart published to `oci://ghcr.io/twingate/helmcharts/twingate-operator`
- CRDs are **not** automatically updated on `helm upgrade` (Helm v3 limitation — manual update required)
- Latest release: **v3.0.0** (breaking changes — see [v2 → v3 migration guide](https://github.com/Twingate/kubernetes-operator/wiki/Migration-v2-to-v3))

## Prerequisites
- Kubernetes 1.16+
- Twingate account with a Remote Network configured for the cluster
- Twingate Connectors deployed (Helm chart: `github.com/Twingate/helm-charts`)
- Twingate API token with **Read/Write/Provision** permissions (generated in the Admin Console)

## Installation

### Via OCI Helm chart (recommended)
1. Download and customize `values.yaml` from `deploy/twingate-operator/values.yaml`
2. Set values under the `twingateOperator` key (API token, account name, etc.)
3. Install:
```bash
helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator --install --wait -f ./values.yaml
```

### Via cloned repository
1. Clone the repo and copy the values file:
```bash
cp ./deploy/twingate-operator/values.yaml ./deploy/twingate-operator/values.local.yaml
```
2. Edit `twingateOperator` settings in the copied file
3. Install:
```bash
helm upgrade twop ./deploy/twingate-operator --install --wait -f ./deploy/twingate-operator/values.local.yaml
```

Add `-n <namespace>` to either command to target a specific namespace.

## Configuration Values
Key settings live under `twingateOperator` in `values.yaml`:
- `apiToken` — Twingate API token (Read/Write/Provision)
- `accountName` (or equivalent) — Twingate account/network name
- Refer to [default values file](https://github.com/Twingate/kubernetes-operator/blob/main/deploy/twingate-operator/values.yaml) for the full list

## Breaking Changes in v3.0.0
- Gateway subchart updated to 2.0.0 with a breaking TLS values schema change
- `protocols` field is now only allowed on Network-type `TwingateResources` (not other resource types)
- See the [v2 → v3 migration guide](https://github.com/Twingate/kubernetes-operator/wiki/Migration-v2-to-v3) before upgrading

## Gotchas
- **CRD upgrades are manual**: Helm v3 does not upgrade CRDs automatically during `helm upgrade`; apply updated CRD manifests separately before upgrading the chart
- Connectors must already exist in the cluster (via the Twingate Helm chart) before the operator can manage them
- API token must have **Provision** permission, not just Read/Write

## Related Docs
- [Wiki](https://github.com/Twingate/kubernetes-operator/wiki)
- [Getting Started](https://github.com/Twingate/kubernetes-operator/wiki/Getting-Started)
- [API Reference](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference)
- [Twingate Connector Helm Charts](https://github.com/Twingate/helm-charts)
- [CHANGELOG](https://github.com/T