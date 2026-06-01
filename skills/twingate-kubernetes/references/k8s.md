# Kubernetes Overview – Twingate

## Summary
Twingate integrates with Kubernetes to secure cluster access and manage resource permissions within K8s workflows. The recommended approach uses the Twingate Kubernetes Operator to co-locate Twingate configuration with cluster configuration. Privileged Access features add identity propagation and session recording for sensitive infrastructure.

## Key Information
- Twingate Kubernetes Operator is the **recommended deployment method**
- Operator allows defining Twingate components and access authorizations directly in K8s manifests
- Privileged Access for Kubernetes provides identity propagation + session recording
- Kubernetes Access Gateway is open source (available on GitHub)
- Helm Chart available for deployment

## Prerequisites
- Kubernetes cluster
- Twingate account
- kubectl access to cluster

## Available Guides
1. Kubernetes Operator Quick Start Guide
2. Securely manage Kubernetes using kubectl
3. Route traffic from a K8s cluster using Twingate Client
4. Securely access **private** resources in a K8s cluster
5. Securely access **publicly exposed** resources in a K8s cluster
6. Helm Chart deployment

## Deployment Options
| Method | Use Case |
|--------|----------|
| Kubernetes Operator | Recommended; manages Twingate config alongside K8s config |
| Helm Chart | Alternative chart-based deployment |

## Privileged Access Features
- **Identity propagation**: Passes user identity through to K8s interactions
- **Session recording**: Auditable logs of K8s sessions
- Requires Kubernetes Access Gateway (open source, GitHub)

## Gotchas
- Operator configuration and access rules live in the same K8s deployment — changes to either affect the other
- Privileged Access requires the separate Kubernetes Access Gateway component
- Instructions for the Operator are maintained in the GitHub repo, not solely in Twingate docs

## Related Docs
- [Twingate Kubernetes Operator GitHub](https://github.com/Twingate/kubernetes-operator)
- [Kubernetes Access Gateway GitHub](https://github.com/Twingate/kubernetes-access-gateway)
- Kubernetes Access Guide (Twingate docs)
- Helm Chart page