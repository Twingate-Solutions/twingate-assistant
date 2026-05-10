# Private Resources in Kubernetes

## Page Title
Private Resources in Kubernetes - Access Private Services Within a K8s Cluster

## Summary
Deploy Twingate Connectors inside a Kubernetes cluster via Helm Chart to enable authorized users to access internal K8s services without public internet exposure. Users access services using internal IPs or K8s cluster DNS names through Twingate Resources.

## Key Information
- Connectors must be deployed **inside** the K8s cluster (not external)
- Resources can be defined using internal service IPs or K8s cluster-internal DNS addresses
- No public internet exposure required for the target services
- Access control managed via Twingate Resource permissions

## Prerequisites
- Kubernetes cluster running
- Helm installed
- Twingate account with admin access
- Twingate Helm Chart (available on GitHub)

## Step-by-Step

1. **Deploy Connector(s)** inside the K8s cluster using the Twingate Helm Chart
   - Reference the Helm Chart deployment guide in the Twingate GitHub repository

2. **Create a Twingate Resource** using either:
   - Internal service IP address
   - K8s cluster-internal DNS address (e.g., `service-name.namespace.svc.cluster.local`)

3. **Grant user access** to the defined Resource — users can then reach the service via its internal IP or DNS name

## Configuration Values
- **Resource address**: Internal K8s service IP or cluster DNS name
  - DNS format example: `<service>.<namespace>.svc.cluster.local`

## Gotchas
- Connector must be deployed **inside** the cluster so it can reach cluster-internal DNS and IPs
- K8s cluster-internal DNS names are not resolvable outside the cluster — Connector placement inside the cluster is what makes this work
- Multiple Connectors can be deployed for redundancy (recommended)

## Related Docs
- [Twingate Helm Chart deployment guide (GitHub)](https://github.com/Twingate/helm-charts)
- Twingate Resource creation documentation
- Connector deployment documentation