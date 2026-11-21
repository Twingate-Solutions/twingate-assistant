---
source: https://github.com/Twingate/kubernetes-operator
type: github
fetched: 2026-11-19
source_version: c40e60e5b6eccd0688b3f94b611a57623ba13528
trust: official
---

# Twingate Kubernetes Operator

## Summary
The Twingate Kubernetes Operator is a custom controller that lets you configure and manage Twingate resources using Kubernetes assets. It integrates Kubernetes clusters with the Twingate Zero Trust Network. It is open source and installed via a Helm chart.

## Key Information
- Repo: Twingate/kubernetes-operator (default branch: `main`).
- Helm chart is published to the OCI repository `oci://ghcr.io/twingate/helmcharts/twingate-operator` (recommended install method).
- Chart source lives in `./deploy/twingate-operator`; default values are in `deploy/twingate-operator/values.yaml`.
- Container images are on Docker Hub: `twingate/kubernetes-operator`.
- Documentation is in the GitHub wiki: Wiki, Getting Started, and API Reference pages.
- Latest release is v3.1.0 (2026-11-18). It contains CRD changes, so update to the latest CRDs (see the upgrading-chart note in the README). Highlights:
  - Feature: the `TwingateGateway` address can now be set explicitly (PR #1243).
  - Performance: integration test runtime cut by 42% (PR #1232).
  - Chores: many dependency bumps, including gateway 2.0.1 to 2.1.0 in `/deploy/twingate-operator`, croniter 7.0.0, kopf 1.45.2, kubernetes 37.0.2, pydantic 2.14.3; docs for kvz as the macOS local cluster; markdownlint pre-commit hook fix.
- Previous release: v3.0.2 (2026-10-21), a chore release (certifi bump).
- Changelog: `CHANGELOG.md`. Developer guide: `DEVELOPER.md`.

## Prerequisites
- Kubernetes cluster, version 1.16+.
- Twingate account and resources (Gateways, Networks, Applications, etc.).
- A Twingate `Remote Network` for the cluster, with connectors deployed (see the Twingate Helm charts repo: https://github.com/Twingate/helm-charts).
- Twingate API token with `Read/Write/Provision` permissions, generated in the Twingate Admin Console.
- Helm.

## Usage / Step-by-Step

**Install via OCI (recommended)**
1. Create a custom `values.yaml`, starting from the default values file.
2. Edit the settings, specifically `twingateOperator`.
3. Deploy (add `-n [namespace]` for a specific namespace):
```bash
helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator --install --wait -f ./values.yaml
```

**Install from a cloned repo**
1. Clone the repository.
2. Copy the defaults:
```bash
cp ./deploy/twingate-operator/values.yaml ./deploy/twingate-operator/values.local.yaml
```
3. Edit `twingateOperator` settings in `values.local.yaml`.
4. Deploy:
```bash
helm upgrade twop ./deploy/twingate-operator --install --wait -f ./deploy/twingate-operator/values.local.yaml
```

## Configuration Values
- `twingateOperator` section of `values.yaml`: the main settings to edit (the README does not list individual keys; consult the default `values.yaml` for them, such as API token and network details).
- `-n [namespace]`: optional Helm flag to install into a specific namespace.
- Helm release name used in examples: `twop`.

## Gotchas
- With Helm v3, CRDs created by this chart are not updated on upgrade by default; they must be updated manually. See the Helm documentation on CRDs and `helm upgrade`. This matters for v3.1.0, which includes CRD changes.
- The API token must have `Read/Write/Provision` permissions, otherwise resource management will fail.
- Connectors and a Remote Network must already exist for the cluster.

## Related Docs
- Wiki: https://github.com/Twingate/kubernetes-operator/wiki
- Getting Started: https://github.com/Twingate/kubernetes-operator/wiki/Getting-Started
- API Reference: https://github.com/Twingate/kubernetes-operator/wiki/API-Reference
- Twingate Helm charts: https://github.com/Twingate/helm-charts
- Default values: https://github.com/Twingate/kubernetes-operator/blob/main/deploy/twingate-operator/values.yaml
- Support: GitHub issues, Twingate forum (https://forum.twingate.com/), or support tickets (https://help.twingate.com/)