---
source: https://github.com/Twingate/kubernetes-operator
type: github
fetched: 2026-08-30
source_version: f439cbc49ce64b3e517e1d4df6169e419b657094
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
- **EKS compatibility (v2.0.1 / v1.3.1):** `ssl.VERIFY_X509_STRICT` was relaxed so the operator can reach the Kubernetes API server on EKS (fixes issue #1128).

## Recent Releases

- **v2.0.1 / v1.3.1 (2026-08-24):** Bug fix — relaxed `ssl.VERIFY_X509_STRICT` to restore connectivity to the API server on EKS clusters. Dependency bumps only otherwise.
- **v1.3.0 (2026-07-30):** The Kubernetes Resource is now retained when a Service annotation is removed; Helm can adopt operator-generated Kubernetes Resources.
- **v2.0.0 (2026-08-12):** Breaking release — see migration guide.

## Related Docs

- `Twingate/helm-charts` — Connector deployment (Remote Network prerequisite)
-