---
source: https://www.twingate.com/docs/k8s
type: docs
fetched: 2026-08-14
source_version: 65f60c40c69a2f58232eb9a400a592baedc5dc57939928efb0392836b7822ffb
---

# Kubernetes Overview - Twingate

## Summary
Twingate provides Kubernetes integration for securing cluster access and managing resource permissions within K8s workflows. The recommended approach uses the Twingate Kubernetes Operator to manage Twingate components declaratively. Privileged Access features add identity propagation and session recording for sensitive infrastructure.

## Key Information
- Kubernetes Operator is the recommended deployment method for Twingate on K8s
- Operator enables managing Twingate components and access authorizations within K8s manifests
- Privileged Access for K8s adds identity propagation and session recording
- Users can sync kubeconfig via CLI to use `kubectl` without cloud provider CLIs
- Helm Chart available for deployment

## Prerequisites
- Kubernetes cluster
- Twingate account
- Kubernetes Operator installed (via GitHub repo)

## Core Components

| Component | Purpose |
|---|---|
| Kubernetes Operator | Deploy/manage Twingate on K8s declaratively |
| Kubernetes Access Gateway | Open-source gateway for privileged access (GitHub) |
| Helm Chart | Alternative deployment method |

## Key Workflows

### Standard Access Setup
1. Deploy Twingate via Kubernetes Operator (see GitHub repo for instructions)
2. Define Twingate resources and access policies as K8s manifests
3. Configure access to private or public resources within cluster

### Privileged Access Setup
1. Configure Kubernetes Operator for privileged access
2. Set up Kubernetes Access Gateway (open source, GitHub)
3. Users run `twingate kube config sync` to sync kubeconfig
4. Access clusters via `kubectl` directly (no cloud provider CLI required)

## CLI Commands
```bash
twingate kube config sync   # Sync kubeconfig for kubectl access
```

## Available Guides
- Kubernetes Operator Quick Start Guide
- How to Securely Manage Kubernetes using kubectl
- How to Route Traffic from a Kubernetes Cluster Using the Twingate Client
- How to Securely Access Private Resources in a Kubernetes Cluster
- How to Securely Access Publicly Exposed Resources in a Kubernetes Cluster
- Kubernetes Kubeconfig Sync (includes CI/CD examples)

## Gotchas
- Operator configuration lives in K8s manifests—cluster config and access control are co-located by design
- Privileged Access requires separate Kubernetes Access Gateway setup (open source, not bundled)
- `twingate kube config sync` requires Privileged Access to be configured first
- CI/CD kubeconfig usage has specific requirements—see Kubeconfig Sync docs

## Related Docs
- Twingate Kubernetes Operator (GitHub)
- Kubernetes Access Gateway (GitHub)
- Kubernetes Kubeconfig Sync
- Kubernetes Access Guide (Privileged Access)
- Helm Chart docs