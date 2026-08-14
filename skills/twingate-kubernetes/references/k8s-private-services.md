---
source: https://www.twingate.com/docs/k8s-private-services
type: docs
fetched: 2026-08-14
source_version: 51e10f96e4d2ea23da2406b8303af0a509e45bfc138aa00cf9fe5f4a7b9e84a7
---

# Private Resources in Kubernetes

## Page Title
Private Resources in Kubernetes: Access Private Services Within a K8s Cluster

## Summary
Deploy Twingate Connectors inside a Kubernetes cluster via Helm Chart to expose internal K8s services as Twingate Resources. Authorized users can access these services using internal IPs or cluster DNS names without exposing them publicly.

## Key Information
- Connectors must be deployed **inside** the K8s cluster to reach internal services
- Resources can be defined using internal service IPs or K8s cluster-internal DNS addresses (e.g., `service.namespace.svc.cluster.local`)
- No public internet exposure required for the target services
- Access is controlled via standard Twingate Resource permissions

## Prerequisites
- Twingate account with a configured Network
- Helm installed and configured for your K8s cluster
- Twingate Helm Chart (available on GitHub)
- Connector tokens/credentials for deployment

## Step-by-Step
1. **Deploy Connector(s)** inside the K8s cluster using the Twingate Helm Chart
2. **Create a Twingate Resource** specifying either:
   - Internal service IP address, or
   - K8s cluster-internal DNS name (e.g., `my-service.my-namespace.svc.cluster.local`)
3. **Grant user/group access** to the Resource in Twingate admin
4. Users connect via Twingate Client and access the service via its internal address

## Configuration Values
- Resource address: internal cluster IP or DNS (e.g., `<service>.<namespace>.svc.cluster.local`)
- Deployment method: Helm Chart (refer to Twingate GitHub repository for chart values)

## Gotchas
- Connector must be deployed **within** the cluster — an external Connector cannot reach cluster-internal DNS or private ClusterIP services
- K8s DNS names are only resolvable from within the cluster; ensure the Connector pod has standard cluster DNS configured
- Multiple Connectors can be deployed for redundancy (recommended for production)

## Related Docs
- [Twingate Helm Chart (GitHub)](https://github.com/Twingate/helm-charts)
- Twingate Resource configuration docs
- Connector deployment guide