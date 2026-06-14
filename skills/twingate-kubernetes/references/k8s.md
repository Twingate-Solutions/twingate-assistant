# Kubernetes Overview – Twingate

## Summary
Twingate integrates with Kubernetes to secure cluster access and manage resource permissions within existing K8s workflows. The recommended deployment method is the Twingate Kubernetes Operator, which centralizes Twingate configuration alongside cluster configuration. Privileged Access features add identity propagation and session recording for sensitive infrastructure.

## Key Information
- Twingate Kubernetes Operator is the **recommended** deployment method
- Operator enables managing Twingate components and access authorizations directly from K8s manifests
- Privileged Access for Kubernetes provides identity propagation + session recording
- Kubernetes Access Gateway is open source (available on GitHub)
- Helm Chart available for deployment

## Available Guides
- Kubernetes Operator Quick Start Guide
- Securely manage Kubernetes using `kubectl`
- Route traffic from a K8s cluster using the Twingate Client
- Securely access **private** resources in a K8s cluster
- Securely access **publicly exposed** resources in a K8s cluster
- Helm Chart deployment

## Deployment Options
| Method | Use Case |
|--------|----------|
| Kubernetes Operator | Recommended; manages Twingate config within K8s |
| Helm Chart | Alternative chart-based deployment |
| Twingate Client | Routing traffic from within a cluster |

## Privileged Access Features
- **Identity propagation** – passes user identity through to K8s API interactions
- **Session recording** – auditable logs of K8s sessions
- Requires: Kubernetes Operator + Kubernetes Access Gateway

## External Resources
- Operator repo: GitHub (Twingate Kubernetes Operator)
- Access Gateway repo: GitHub (open source)

## Gotchas
- Operator and Access Gateway are managed separately; both needed for Privileged Access
- Configuration lives in K8s manifests when using the Operator — changes outside K8s may conflict

## Related Docs
- Twingate Kubernetes Operator (GitHub)
- Kubernetes Access Gateway (GitHub)
- Kubernetes Privileged Access guide
- Helm Chart reference