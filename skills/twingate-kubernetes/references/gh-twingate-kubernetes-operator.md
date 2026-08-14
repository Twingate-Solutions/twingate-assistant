---
source: https://github.com/Twingate/kubernetes-operator
type: github
fetched: 2026-08-14
source_version: 337b3d782df1c42ca782d29734b1436d4ea79ba6
---

# Twingate Kubernetes Operator

## Summary

Custom Kubernetes controller that automates management of Twingate resources (Resources, Connectors, Gateways, Certificate Authorities) declaratively via CRDs, integrating a cluster with the Twingate Zero Trust network. Installed as a Helm chart published to an OCI registry; also manages Twingate objects in response to Kubernetes Service annotations. OSS, Apache 2.0 licensed.

## Key Information

- Repo: `Twingate/kubernetes-operator`, default branch `main`, Dockerhub `twingate/kubernetes-operator`
- Helm chart (OCI): `oci://ghcr.io/twingate/helmcharts/twingate-operator`
- Documentation: repo Wiki, Getting Started, and API Reference wiki pages
- CRDs: `TwingateResource`, `TwingateConnector`, `TwingateGateway`, `TwingateCertificateAuthority`, `TwingateResourceAccess`; `WebApp` resource type with `requestHeaderRewrites` support
- Service annotation namespace is `resource.twingate.com` (the old `twingate.com/resource*` form is removed in v2)

## Prerequisites

- Kubernetes cluster 1.16+
- Twingate account with a Remote Network for the cluster and Connectors deployed (use `Twingate/helm-charts` if needed)
- Twingate API token with `Read/Write/Provision` permissions (generated in the Admin Console)

## Usage / Step-by-Step (Helm via OCI, recommended)

1. Copy the default `deploy/twingate-operator/values.yaml` to a custom `values.yaml`.
2. Edit settings, specifically the `twingateOperator` block.
3. Deploy (optionally scoped to a namespace with `-n [namespace]`):

```bash
helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator --install --wait -f ./values.yaml
```

Alternative: clone the repo and point `helm upgrade` at the local `./deploy/twingate-operator` chart.

## Configuration Values

- Primary config block: `twingateOperator` in `values.yaml` (API token, network settings)
- Install namespace: `helm -n [namespace]`
- API token requires `Read/Write/Provision` scope

## Gotchas

- **v2.0.0 is a breaking release** — read the [v1→v2 migration guide](https://github.com/Twingate/kubernetes-operator/wiki/Migration-v1-to-v2) before upgrading.
- **CRDs are not upgraded automatically** by Helm v3; update them manually on chart upgrade.
- Deprecated `twingate.com/resource*` Service annotations are no longer reconciled — migrate to `resource.twingate.com` equivalents.
- Object-reference `namespace` now defaults to the CR's own namespace (v2 behavior change).
- Deprecated Kubernetes versions removed in v2; changing a Service's `resource.twingate.com/type` value now recreates the `TwingateResource`.
- On uninstall, the gateway's Twingate CRs are deleted before the operator.
- License changed to Apache 2.0 in v2.

## Related Docs

- `Twingate/helm-charts` — Connector deployment (Remote Network prerequisite)
- Repo Wiki: Getting Started, API Reference, v1→v2 Migration
- Twingate forum and help center for support

---
Want this written to `skills/twingate-kubernetes/references/gh-twingate-kubernetes-operator.md` with the standard provenance frontmatter?