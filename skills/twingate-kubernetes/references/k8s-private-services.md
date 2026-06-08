# Private Resources in Kubernetes

## Page Title
Private Resources in Kubernetes - Access Private Services Within a K8s Cluster

## Summary
Deploy Twingate Connectors inside a Kubernetes cluster via Helm Chart to enable authorized users to access internal K8s services. Resources are defined using internal IPs or cluster DNS addresses, eliminating the need to expose services publicly.

## Key Information
- Connectors must be deployed **inside** the K8s cluster to access internal services
- Deployment method: Helm Chart (hosted on Twingate's GitHub repository)
- Resources can be defined using either internal service IPs or K8s cluster-internal DNS addresses
- Access is scoped to authorized Twingate users only

## Prerequisites
- A Twingate account with admin access
- A running Kubernetes cluster
- Helm installed and configured for the cluster
- Access to Twingate's Helm Chart repository on GitHub

## Step-by-Step

1. **Deploy Connector(s)** inside the K8s cluster using the Twingate Helm Chart (refer to the GitHub repository for Helm deployment instructions)
2. **Create a Twingate Resource** using either:
   - Internal service IP address
   - K8s cluster-internal DNS address (e.g., `service-name.namespace.svc.cluster.local`)
3. **Grant user access** to the defined Resource — users can then reach the service via its internal IP or DNS name

## Configuration Values
- **Resource address**: Internal service IP or K8s DNS name
  - DNS format example: `<service>.<namespace>.svc.cluster.local`
- Helm Chart deployment parameters: See Twingate GitHub repository

## Gotchas
- Connector must run **within the cluster** — external Connectors cannot resolve cluster-internal DNS or reach ClusterIP services
- Internal DNS names are only resolvable from within the cluster network; ensure the Connector pod has standard cluster DNS access
- Multiple Connectors can be deployed for redundancy (recommended for production)

## Related Docs
- Twingate Helm Chart deployment guide (GitHub repository)
- Twingate Resource creation documentation
- Connector deployment overview