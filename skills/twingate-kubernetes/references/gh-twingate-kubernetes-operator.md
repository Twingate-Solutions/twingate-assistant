---
source: https://github.com/Twingate/kubernetes-operator
type: github
fetched: 2026-08-06
source_version: 10ea93fc897133a71bf4aebbbfab4fdff91795a8
---

# Twingate Kubernetes Operator

## Summary
A custom Kubernetes controller that automates management of Twingate resources within a Kubernetes cluster. It bridges Kubernetes-native workflows with Twingate's Zero Trust Network by syncing Kubernetes assets to Twingate configuration via CRDs.

## Key Information
- Deployed via Helm; OCI registry is the recommended installation path
- Manages Twingate resources (Remote Networks, Resources, etc.) declaratively through Kubernetes custom resources
- Recent additions: Helm adoption of generated Kubernetes Resources; preserves Kubernetes Resources when Service annotation is removed
- Docker images published to [Docker Hub](https://hub.docker.com/r/twingate/kubernetes-operator)
- Helm chart published to `oci://ghcr.io/twingate/helmcharts/twingate-operator`

## Prerequisites
- Kubernetes 1.16+
- Twingate account with a configured Remote Network for the cluster
- Twingate connectors deployed (available via the [Twingate Helm charts](https://github.com/Twingate/helm-charts))
- Twingate API token with **Read/Write/Provision** permissions (generated in the Twingate Admin Console)

## Installation

### Via OCI (Recommended)
```bash
helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator \
  --install --wait -f ./values.yaml
```

### Via Git Clone
```bash
cp ./deploy/twingate-operator/values.yaml ./deploy/twingate-operator/values.local.yaml
# Edit values.local.yaml, specifically the twingateOperator section
helm upgrade twop ./deploy/twingate-operator \
  --install --wait -f ./deploy/twingate-operator/values.local.yaml
```

Add `-n [namespace]` to either command to target a specific namespace.

## Configuration Values
- **`twingateOperator`** — primary Helm values section; configure API token, account name, and operator settings here
- Reference the [default values.yaml](https://github.com/Twingate/kubernetes-operator/blob/main/deploy/twingate-operator/values.yaml) as a starting point

Full API reference: [Wiki API Reference](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference)

## Gotchas
- **CRDs are not auto-updated on Helm upgrade** (Helm v3 limitation); CRDs must be manually updated when upgrading the chart
- API token must have all three permissions: Read, Write, and Provision — missing any will cause failures
- Removing a Service annotation now preserves the associated Kubernetes Resource (changed in latest release)

## Related Docs
- [Getting Started Guide](https://github.com/Twingate/kubernetes-operator/wiki/Getting-Started)
- [API Reference](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference)
- [Full Wiki](https://github.com/Twingate/kubernetes-operator/wiki)
- [CHANGELOG](https://github.com/Twingate/kubernetes-operator/blob/main/CHANGELOG.md)
- [Developer Guide](https://github.com/Twingate/kubernetes-operator/blob/main/DEVELOPER.md)
- [Helm CRD upgrade docs](https://helm.sh/docs/chart_best_practices/custom_resource_definitions)