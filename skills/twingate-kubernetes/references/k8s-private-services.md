# Private Resources in Kubernetes

## Page Title
Private Resources in Kubernetes: Access Private Services Within a K8s Cluster

## Summary
Deploy Twingate Connectors inside a Kubernetes cluster via Helm Chart to enable authorized users to access internal K8s services. Users access services using internal IPs or cluster DNS names without exposing them publicly.

## Key Information
- Connectors must be deployed **inside** the K8s cluster (not externally)
- Resources can be defined using either internal service IPs or K8s cluster-internal DNS addresses
- Access is scoped to authorized Twingate users only
- No public internet exposure required

## Prerequisites
- Twingate account with ability to create Resources
- Kubernetes cluster
- Helm installed
- Access to Twingate Helm Chart (hosted on GitHub)

## Step-by-Step

1. **Deploy Connector(s)** inside the K8s cluster using the Twingate Helm Chart
   - Follow deployment steps in the Twingate Helm Chart GitHub repository
2. **Create a Twingate Resource** using either:
   - Internal service IP address, or
   - K8s cluster-internal DNS address (e.g., `service-name.namespace.svc.cluster.local`)
3. **Grant user access** to the Resource
4. Users can now connect to the service via its internal IP or DNS name through Twingate

## Configuration Values
- **Resource address**: Internal pod/service IP or K8s DNS name
  - DNS format: `<service>.<namespace>.svc.cluster.local`

## Gotchas
- Connector must be deployed **within** the cluster — an external Connector cannot reach cluster-internal DNS names or private service IPs
- K8s internal DNS names are only resolvable from within the cluster; ensure the Connector has proper DNS resolution configured
- Multiple Connectors recommended for high availability (Twingate best practice)

## Related Docs
- [Twingate Helm Chart (GitHub)](https://github.com/Twingate/helm-charts)
- Twingate Resource creation documentation
- Connector deployment documentation