---
source: https://www.twingate.com/docs/k8s
type: docs
fetched: 2026-10-04
source_version: a1c808f8eb7474595b2b27a87c8d1844ff1cc0dc69b3dca9572636550205cd6a
trust: official
---

# Kubernetes Overview — Twingate

## Summary
Twingate integrates with Kubernetes to secure cluster access and manage service authorization within K8s workflows. The recommended approach uses the Twingate Kubernetes Operator to define and manage Twingate components declaratively. Privileged Access for Kubernetes adds identity propagation and session recording for sensitive infrastructure.

## Key Information
- **Kubernetes Operator** is the recommended deployment method — manages Twingate components and access authorizations as K8s resources
- **Privileged Access for Kubernetes** enables identity propagation and session recording for auditable cluster interactions
- **Kubernetes Access Gateway** is open source, available on GitHub
- `twingate kube config sync` syncs kubeconfig for direct `kubectl` access without cloud provider CLIs
- CI/CD workflows are supported via kubeconfig sync

## Prerequisites
- A running Kubernetes cluster
- Twingate account with appropriate permissions
- Helm (for Helm Chart deployment path)

## Core Components

| Component | Purpose |
|---|---|
| Kubernetes Operator | Declarative management of Twingate resources in K8s |
| Kubernetes Access Gateway | Open-source gateway enabling privileged access |
| Helm Chart | Alternative/supplemental deployment method |

## CLI Reference
```bash
twingate kube config sync    # Sync kubeconfig for kubectl access
```

## Related Docs / Resources
- [Twingate Kubernetes Operator (GitHub)](https://github.com/Twingate/kubernetes-operator)
- [Kubernetes Access Gateway (GitHub)](https://github.com/Twingate/kubernetes-access-gateway)
- [Kubernetes Operator Quick Start Guide](https://www.twingate.com/docs/k8s-operator-quick-start)
- [Kubernetes Kubeconfig Sync](https://www.twingate.com/docs/k8s-kubeconfig-sync)
- [Privileged Access for Kubernetes](https://www.twingate.com/docs/k8s-access)
- [Helm Chart](https://www.twingate.com/docs/k8s-helm)
- How to Securely Manage Kubernetes using kubectl
- How to Route Traffic from a Kubernetes Cluster Using the Twingate Client
- How to Securely Access Private Resources in a Kubernetes Cluster
- How to Securely Access Publicly Exposed Resources in a Kubernetes Cluster

## Gotchas
- Operator configuration and cluster access config are co-located by design — plan your GitOps/IaC structure accordingly
- `twingate kube config sync` eliminates the need for cloud provider CLIs (e.g., `aws eks update-kubeconfig`) — verify this fits your auth model before adopting
- Privileged Access requires the Kubernetes Access Gateway to be deployed separately