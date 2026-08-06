---
source: https://www.twingate.com/docs/k8s
type: docs
fetched: 2026-08-05
source_version: 3b220db1fadb21a1ca2ca0ba3e6bd2243dd578303d468c125a2f937bdd5149e1
---

# Kubernetes Overview - Twingate

## Summary
Twingate provides Kubernetes integration for securing K8s clusters and services, managing access within K8s workflows. The primary recommended approach uses the Twingate Kubernetes Operator to define and manage Twingate components directly in Kubernetes deployments.

## Key Information
- Kubernetes Operator is the recommended deployment method for Twingate on K8s
- Supports privileged access with identity propagation and session recording
- `twingate kube config sync` syncs kubeconfig for direct `kubectl` access without cloud provider CLIs
- Operator allows co-locating Twingate config with cluster config

## Core Components
| Component | Purpose |
|-----------|---------|
| Kubernetes Operator | Deploy/manage Twingate on K8s, define access authorizations |
| Kubernetes Access Gateway | Open-source gateway enabling privileged access (session recording, identity propagation) |
| Kubeconfig Sync | CLI command to sync kubeconfig for kubectl access |

## Available Guides
- Kubernetes Operator Quick Start Guide
- Securely manage Kubernetes using kubectl
- Route traffic from K8s cluster using Twingate Client
- Securely access private resources in a K8s cluster
- Securely access publicly exposed resources in a K8s cluster
- Helm Chart deployment

## CLI Commands
```bash
twingate kube config sync   # Sync kubeconfig for kubectl access
```

## Privileged Access Features
- Identity propagation for K8s interactions
- Session recording
- CI/CD pipeline support via kubeconfig sync

## Related Docs
- Twingate Kubernetes Operator (GitHub repo)
- Kubernetes Access Gateway (GitHub, open source)
- Kubernetes Kubeconfig Sync (includes CI/CD examples)
- Kubernetes access guide (Privileged Access setup)
- Helm Chart docs

## Gotchas
- Privileged Access requires the Kubernetes Access Gateway setup before using kubeconfig sync
- Operator configuration lives in K8s manifests — changes to access policy should go through K8s deployment workflow, not Twingate admin console alone