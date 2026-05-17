# Kubernetes Overview - Twingate

## Summary
Twingate provides Kubernetes integration to secure K8s clusters and services while managing access within existing K8s workflows. The recommended approach uses the Twingate Kubernetes Operator to define and manage Twingate components directly from Kubernetes deployments.

## Key Information
- Twingate Kubernetes Operator is the recommended deployment method
- Operator manages Twingate components and access authorizations within K8s
- Supports Privileged Access for K8s: identity propagation + session recording
- Helm Chart available for deployment
- Open source Kubernetes Access Gateway available on GitHub

## Available Guides
- Quick Start Guide (Kubernetes Operator)
- Securely manage Kubernetes using `kubectl`
- Route traffic from a K8s cluster using Twingate Client
- Securely access private resources in a K8s cluster
- Securely access publicly exposed resources in a K8s cluster

## Privileged Access Features
- Identity propagation for Kubernetes interactions
- Session recording for auditable access
- Targets sensitive infrastructure use cases
- Requires Kubernetes Operator + Kubernetes Access Gateway

## Deployment Options
| Method | Use Case |
|--------|----------|
| Kubernetes Operator | Recommended; full lifecycle management |
| Helm Chart | Alternative deployment method |

## External Resources
- Operator config: [GitHub repo](https://github.com/Twingate/kubernetes-operator)
- Access Gateway: [GitHub (open source)](https://github.com/Twingate/kubernetes-access-gateway)

## Gotchas
- Operator documentation lives in GitHub, not solely in Twingate docs
- Privileged Access (session recording/identity propagation) requires both the Operator and the separate Kubernetes Access Gateway component

## Related Docs
- Twingate Kubernetes Operator (GitHub)
- Kubernetes Access Guide (Privileged Access)
- Helm Chart documentation
- Quick Start Guide