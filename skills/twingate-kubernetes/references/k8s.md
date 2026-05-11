# Kubernetes Overview - Twingate

## Summary
Twingate integrates with Kubernetes to secure cluster access and manage resource permissions within K8s workflows. The recommended approach uses the Twingate Kubernetes Operator to define and manage Twingate components directly in Kubernetes manifests. Privileged Access features add identity propagation and session recording for sensitive infrastructure.

## Key Information
- **Kubernetes Operator** is the recommended deployment method for Twingate on K8s
- Operator allows managing Twingate components and access authorizations from within K8s deployments
- **Privileged Access for Kubernetes** enables identity propagation and session recording
- Kubernetes Access Gateway is open source (available on GitHub)
- Helm Chart available for deployment

## Prerequisites
- Existing Kubernetes cluster
- Twingate account with appropriate admin permissions
- kubectl access to the cluster

## Available Guides
1. Twingate Kubernetes Operator Quick Start Guide
2. How to Securely Manage Kubernetes using kubectl
3. How to Route Traffic from a Kubernetes Cluster Using the Twingate Client
4. How to Securely Access Private Resources in a Kubernetes Cluster
5. How to Securely Access Publicly Exposed Resources in a Kubernetes Cluster

## Deployment Options

| Method | Use Case |
|--------|----------|
| Kubernetes Operator | Full lifecycle management of Twingate within K8s |
| Helm Chart | Standard K8s package-based deployment |

## Key Features
- **Operator**: Manages Connectors and access policies as K8s custom resources
- **Privileged Access**: Session recording + identity propagation for audit trails
- **Kubernetes Access Gateway**: Open source component enabling privileged access flows

## Gotchas
- Operator configuration lives in K8s manifests — ensure your GitOps pipeline handles Twingate CRDs appropriately
- Privileged Access (session recording/identity propagation) requires the separate Kubernetes Access Gateway component
- Operator docs are hosted on GitHub, not the Twingate docs site — check the repo for up-to-date CRD specs

## Related Docs
- [Twingate Kubernetes Operator GitHub](https://github.com/Twingate/kubernetes-operator)
- [Kubernetes Access Gateway GitHub](https://github.com/Twingate/kubernetes-access-gateway)
- Kubernetes Access Guide (Privileged Access)
- Twingate Helm Chart docs