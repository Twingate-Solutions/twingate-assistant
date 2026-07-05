# Private Resources in Kubernetes

## Page Title
Private Resources in Kubernetes - Access private services within a K8s cluster

## Summary
Deploy Twingate Connectors inside a Kubernetes cluster via Helm Chart to enable authorized users to access internal K8s services without exposing them to the public internet. Users access services using internal IPs or K8s cluster DNS names through defined Twingate Resources.

## Key Information
- Connectors must be deployed **inside** the K8s cluster (not external)
- Resources can be defined using either internal service IPs or K8s cluster-internal DNS addresses
- No public internet exposure required for the target services
- Access is scoped per-user based on Twingate Resource permissions

## Prerequisites
- A Twingate account with a configured network
- Kubernetes cluster with Helm installed
- Twingate Helm Chart (available on GitHub)
- Internal service IP or DNS name of the target K8s service

## Step-by-Step

1. **Deploy Connector(s)** inside the K8s cluster using the Twingate Helm Chart
   - Follow deployment steps in the Twingate Helm Chart GitHub repository
2. **Create a Twingate Resource** using either:
   - Internal service IP address, or
   - K8s cluster-internal DNS address (e.g., `service-name.namespace.svc.cluster.local`)
3. **Grant user access** to the defined Resource
4. **Users connect** via Twingate Client using the internal IP or DNS name directly

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Resource address | Internal service IP or K8s DNS (e.g., `svc.cluster.local`) |
| Deployment method | Helm Chart |

## Gotchas
- Connector must run **inside** the cluster — it needs to reach cluster-internal DNS/IPs
- K8s internal DNS names are only resolvable from within the cluster; Twingate proxies this resolution through the Connector
- Multiple Connectors recommended for high availability

## Related Docs
- [Twingate Helm Chart on GitHub](https://github.com/Twingate/helm-charts)
- Twingate Resource configuration docs
- Connector deployment documentation