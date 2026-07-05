# Kubernetes Overview - Twingate

## Summary
Twingate provides Kubernetes integration for securing cluster access and managing authorization within K8s workflows. The recommended approach uses the Twingate Kubernetes Operator to define and manage Twingate components directly from Kubernetes deployments. Privileged Access for Kubernetes adds identity propagation and session recording.

## Key Information
- Kubernetes Operator is the **recommended** deployment method for Twingate on K8s
- Operator allows managing Twingate config and access authorization in the same K8s deployment
- Privileged Access for Kubernetes enables identity propagation and session recording
- Users can sync kubeconfig via CLI to use `kubectl` without cloud provider CLIs
- Helm Chart available for deployment

## Prerequisites
- Kubernetes cluster
- Twingate account with appropriate permissions
- Kubernetes Operator installed (via GitHub repo or Helm Chart)

## Core Components

| Component | Purpose |
|---|---|
| Kubernetes Operator | Manage/deploy Twingate resources as K8s objects |
| Kubernetes Access Gateway | Open-source; enables Privileged Access |
| Kubeconfig Sync | Syncs kubeconfig for direct `kubectl` access |

## CLI Commands
```bash
# Sync kubeconfig for direct kubectl access
twingate kube config sync
```

## Available Guides
- [Kubernetes Operator GitHub Repo](https://github.com/Twingate) — Operator setup instructions
- Quick Start Guide
- Securely manage Kubernetes using `kubectl`
- Route traffic from a K8s cluster using Twingate Client
- Securely access private resources in a K8s cluster
- Securely access publicly exposed resources in a K8s cluster
- Helm Chart deployment

## Gotchas
- Operator configuration lives in the GitHub repo — primary docs are external to this page
- Privileged Access (session recording + identity propagation) requires the Kubernetes Access Gateway in addition to the Operator
- `twingate kube config sync` eliminates need for cloud provider CLIs (e.g., `aws eks update-kubeconfig`) — useful for CI/CD pipelines

## Related Docs
- Twingate Kubernetes Operator (GitHub)
- Kubernetes Access Guide
- Kubernetes Access Gateway (GitHub, open source)
- Kubernetes Kubeconfig Sync
- Helm Chart