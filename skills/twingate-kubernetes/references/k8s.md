# Kubernetes Overview - Twingate

## Summary
Twingate provides Kubernetes integration for securing K8s clusters and services, managing access within existing K8s workflows. The recommended approach uses the Twingate Kubernetes Operator to define and manage Twingate components directly from Kubernetes deployments.

## Key Information
- Kubernetes Operator is the recommended deployment method for Twingate on K8s
- Supports Privileged Access with identity propagation and session recording
- Configuration and cluster access managed from a single location
- Helm Chart available for deployment
- Open source Kubernetes Access Gateway available on GitHub

## Prerequisites
- Existing Kubernetes cluster
- Access to Twingate account
- kubectl configured for your cluster

## Available Deployment Options
- **Kubernetes Operator** – Manage Twingate components and access authorizations via K8s manifests
- **Helm Chart** – Standard Helm-based deployment
- **Privileged Access / Access Gateway** – Enhanced access with session recording (open source)

## Use Cases Covered
| Guide | Purpose |
|-------|---------|
| Quick Start | Initial Operator setup |
| kubectl access | Secure cluster management |
| Traffic routing | Route traffic from K8s cluster via Twingate Client |
| Private resources | Access private K8s services |
| Public resources | Access publicly exposed K8s services |
| Privileged Access | Identity propagation + session recording |

## Related Docs
- [Twingate Kubernetes Operator GitHub](https://github.com/Twingate/kubernetes-operator)
- [Kubernetes Access Gateway GitHub](https://github.com/Twingate/kubernetes-access-gateway)
- Kubernetes Operator Quick Start Guide
- Helm Chart documentation
- Kubernetes Privileged Access guide

## Gotchas
- Operator configuration lives in K8s manifests — changes to access policy must go through K8s deployment workflow
- Privileged Access (session recording/identity propagation) requires the separate Kubernetes Access Gateway component, not just the base Operator