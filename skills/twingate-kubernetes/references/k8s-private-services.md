---
source: https://www.twingate.com/docs/k8s-private-services
type: docs
fetched: 2026-10-04
source_version: 50b022ee07aad4a6e5e87d76a471e025459043d2ca773e75c92f8ccd0ed17db9
trust: official
---

# Private Resources in Kubernetes

## Page Title
Access Private Services Within a K8s Cluster

## Summary
Deploy Twingate Connectors inside a Kubernetes cluster to provide authorized users access to internal K8s services without public internet exposure. Users access services via internal IPs or K8s cluster DNS names through the Twingate Resource definition.

## Key Information
- Connectors must be deployed **inside** the K8s cluster (not externally) to reach cluster-internal services
- Access is scoped to specific services via Twingate Resources, not the entire cluster network
- Users connect using internal K8s DNS names (e.g., `my-service.namespace.svc.cluster.local`) or internal IPs
- No public exposure of internal services required

## Prerequisites
- A Twingate account with admin access
- A running Kubernetes cluster
- Helm installed and configured for the cluster
- Twingate Connector deployment via Helm Chart (see [Twingate Helm Chart repo](https://github.com/Twingate/helm-charts))

## Step-by-Step

1. **Deploy Connector(s) inside the K8s cluster** using the Twingate Helm Chart
   - Follow deployment steps in the Helm Chart GitHub repository
   - Connector must run as a pod within the cluster to resolve internal DNS and reach cluster services

2. **Create a Twingate Resource** pointing to the internal service address:
   - Use the service's cluster-internal IP, or
   - Use the K8s DNS name (e.g., `my-service.default.svc.cluster.local`)

3. **Grant user/group access** to the Twingate Resource via the Twingate Admin Console

4. **Users connect** to the service using its internal IP or K8s DNS name via the Twingate Client

## Configuration Values
| Parameter | Description |
|-----------|-------------|
| Resource Address | Internal service IP or K8s DNS FQDN |
| K8s DNS format | `<service>.<namespace>.svc.cluster.local` |

## Gotchas
- Connector must be deployed **inside** the cluster — an external Connector cannot resolve `*.svc.cluster.local` DNS names
- Multiple Connectors recommended for high availability; deploy at least 2 replicas
- Ensure the Connector pod's service account has appropriate permissions if accessing secured internal services
- K8s DNS names only resolve within the cluster network; Connector placement is critical

## Related Docs
- [Twingate Helm Chart (GitHub)](https://github.com/Twingate/helm-charts)
- Twingate Resource configuration (Admin Console)
- Connector deployment documentation