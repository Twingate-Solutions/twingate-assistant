# Kubernetes Overview - Twingate

## Summary
Twingate provides Kubernetes integration for securing cluster access and managing resource permissions within K8s workflows. The primary deployment method is the Twingate Kubernetes Operator, which co-locates access configuration with cluster configuration. Privileged Access features add identity propagation and session recording for sensitive infrastructure.

## Key Information
- Twingate Kubernetes Operator is the recommended deployment method
- Operator manages Twingate components and access authorizations directly from K8s manifests
- Privileged Access for Kubernetes enables identity propagation and session recording
- `twingate kube config sync` syncs kubeconfig for direct `kubectl` access without cloud provider CLIs
- Helm Chart available for deployment

## Prerequisites
- Kubernetes cluster
- Twingate account with appropriate plan for desired features
- Kubernetes Operator installed (via GitHub repo or Helm Chart)

## Core Components

### Kubernetes Operator
- Manages Twingate deployment and access rules declaratively
- Configuration lives alongside K8s manifests
- Source: [GitHub repo](https://github.com/Twingate/kubernetes-operator)

### Privileged Access for Kubernetes
- Requires Kubernetes Operator setup
- Uses open-source [Kubernetes Access Gateway](https://github.com/Twingate/kubernetes-access-gateway)
- Enables session recording and identity propagation

### Kubeconfig Sync
- CLI command: `twingate kube config sync`
- Enables direct `kubectl` access after Privileged Access setup
- Supports CI/CD workflows

## Configuration Values

| Item | Value |
|------|-------|
| CLI command | `twingate kube config sync` |
| Deployment method | Kubernetes Operator or Helm Chart |

## Step-by-Step (High Level)
1. Deploy Twingate Kubernetes Operator via GitHub repo or Helm Chart
2. Define Twingate resources and access policies in K8s manifests
3. (Optional) Configure Privileged Access using Kubernetes Access Gateway
4. Run `twingate kube config sync` to enable `kubectl` access

## Gotchas
- Privileged Access must be fully configured before `twingate kube config sync` is useful
- Cloud provider CLIs (e.g., `aws`, `gcloud`) are not required after kubeconfig sync, but Privileged Access setup is a prerequisite

## Related Docs
- [Twingate Kubernetes Operator (GitHub)](https://github.com/Twingate/kubernetes-operator)
- [Kubernetes Access Gateway (GitHub)](https://github.com/Twingate/kubernetes-access-gateway)
- Kubernetes Access Guide
- Kubernetes Kubeconfig Sync
- Quick Start Guide
- How to Securely Manage Kubernetes using kubectl
- How to Route Traffic from a Kubernetes Cluster Using the Twingate Client
- How to Securely Access Private Resources in a Kubernetes Cluster
- How to Securely Access Publicly Exposed Resources in a Kubernetes Cluster
- Helm Chart