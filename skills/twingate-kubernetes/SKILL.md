---
name: twingate-kubernetes
description: >
  Use when the user deploys Twingate in Kubernetes, uses the Twingate Helm chart or
  operator, manages TwingateResource or TwingateRemoteNetwork CRDs, routes traffic from
  cluster pods outward through Twingate, gates kubectl access via Twingate, or integrates
  Twingate into a GitOps workflow. Also trigger when an existing K8s stack needs connector
  deployment, token secret management, or declarative Twingate resource definitions.
---

## Role

Twingate's Kubernetes integration specialist. Covers three distinct patterns — Helm chart
deployment of Connectors inside a cluster, Operator-based CRD management for GitOps
workflows, and traffic routing from cluster workloads outward through Twingate. Owns
connector token lifecycle in K8s and secret management for tokens. General Connector
mechanics belong in `twingate-connectors`; IDFW kubectl proxy mode belongs in
`twingate-idfw`.

## Decisions & Guidelines

- **Check for existing Twingate Kubernetes resources before generating.** When operating in a
  Kubernetes or Helm context, check for existing Twingate Helm releases (`helm list -A | grep
  twingate`) and existing `values.yaml` files with Twingate connector configuration before
  generating values or manifests. If a release exists, produce a `values-patch.yaml` or
  targeted changes to the existing values file rather than a full replacement. Check for
  existing `TwingateConnector` and `TwingateResource` CRDs before generating new operator
  manifests.

**Choose the right pattern before writing any configuration.** These patterns are
complementary, not mutually exclusive — each serves a distinct purpose:

- **Helm chart (connector in K8s)**: deploying a Connector *inside* the cluster to expose
  cluster-internal services *to* Twingate users — the inbound access pattern.
- **Kubernetes Operator (CRD-based)**: GitOps-driven management of Twingate Resources and
  Remote Networks as CRDs alongside K8s manifests, reconciled against the Twingate API.
- **Traffic routing / headless client**: routing traffic *from* cluster pods *outward*
  through Twingate to reach private external services — the reverse direction.

The Operator and Helm chart are complementary, not interchangeable — the Operator manages
Twingate API objects (Resources, Remote Networks); the Helm chart manages the Connector
process (data path). Do not let both manage the same Twingate objects or you will create
duplicates.

- **Never commit connector token values as plaintext in Helm values files** —
  store in a Kubernetes Secret and reference via `secretKeyRef`; in production,
  use External Secrets Operator to sync from a secrets manager (AWS Secrets
  Manager, HashiCorp Vault) rather than manual `kubectl create secret`. Helm
  chart field names evolve between versions — verify current values keys in
  `references/k8s-helm-chart.md` or the chart's published `values.yaml` before
  generating configuration.
- **Deploy a minimum of two Helm releases per Remote Network in production** — each release
  is an independent Connector; use pod anti-affinity rules to prevent both scheduling on
  the same node.
- **Each Helm release requires its own unique token pair** — tokens are tied to one
  Connector's identity; never copy tokens from one release to another.
- **`TwingateResource` is a Twingate API object, not a Kubernetes network primitive** — it
  does not configure DNS, kube-proxy, or in-cluster routing; it exposes a service to
  Twingate users *outside* the cluster, not to pods inside it.
- **Always inspect the Helm chart `values.yaml` at the target chart version before writing
  configuration** — the schema evolves between releases; do not rely on third-party docs
  that may reference outdated field names.

## When to Verify

This skill body covers patterns and decisions, not chart values or CRD
schemas. **Before answering questions involving any of the following, read
the relevant `references/` file first** — and cite it in your response:

- Specific Helm chart values keys (token field names, image tag, anti-affinity)
- CRD field names and schemas (`TwingateConnector`, `TwingateResource`, etc.)
- Helm install / upgrade commands and chart version compatibility
- Kubectl proxy mode configuration (when not in IDFW context)

For the **authoritative Helm chart values schema**, clone
`https://github.com/Twingate/helm-charts` and inspect
`charts/connector/values.yaml`. For **CRD schemas**, clone
`https://github.com/Twingate/kubernetes-operator` and check `config/crd/`.

Do not answer these from training-data memory — chart values keys and CRD
fields drift between releases.

## Routing

- **→ twingate-connectors**: for Connector fundamentals, upgrade procedures, HA patterns,
  metrics, and logging — Kubernetes-specific deployment is here, but general Connector
  mechanics are in `twingate-connectors`
- **→ twingate-terraform / twingate-pulumi**: for IaC-generated connector token management
  passed to Helm releases
- **→ twingate-idfw**: for the Kubernetes gateway (kubectl proxy mode with Twingate
  identity enforcement) — distinct from the Helm chart Connector pattern
- **→ twingate-architect**: for architectural questions about Remote Network topology and
  how K8s deployments fit into the broader network design
- **→ twingate-troubleshoot**: when the user reports connector registration failures, pod
  crashes, or K8s networking issues

## References

`references/` contains current Twingate doc summaries, refreshed weekly.
**Consult these before answering fact-shaped questions.**

| If the user asks about… | Read first |
|---|---|
| Helm chart deployment, values keys, install commands | `k8s-helm-chart.md` |
| Helm chart upgrades and chart version handling | `k8s-helm-chart-upgrades.md` |
| Operator CRDs, GitOps with `TwingateResource` / `TwingateRemoteNetwork` | `kubernetes-operator.md` |
| Cluster service exposure (private services to Twingate users) | `k8s-private-services.md`, `k8s.md` |
| Public service exposure patterns | `k8s-public-services.md` |
| kubectl access via Twingate (non-IDFW) | `k8s-cluster-access.md`, `k8s-kubectl.md` |
| Helm values schema (exact field names) | Helm chart repo: `charts/connector/values.yaml` |
| CRD schemas (exact field names) | Operator repo: `config/crd/` |

For comprehensive coverage, see [`references/`](./references/) for the full
set of doc summaries. **Default to checking** — chart values keys and CRD
schemas drift between versions.
