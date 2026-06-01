# Private Resources in Kubernetes

## Page Title
Private Resources in Kubernetes – Access private services within a K8s cluster

## Summary
Deploy Twingate Connectors inside a Kubernetes cluster via Helm Chart, then define Resources using internal IPs or cluster DNS names. Authorized users can access internal K8s services without public internet exposure.

## Key Information
- Connectors must be deployed **inside** the K8s cluster (not externally)
- Resources can be defined using either internal service IPs or K8s cluster-internal DNS addresses
- Access is scoped to users/groups granted permission to the specific Twingate Resource

## Prerequisites
- Twingate account with admin access
- Kubernetes cluster
- Helm installed
- Twingate Helm Chart (available on GitHub)

## Step-by-Step
1. Deploy Twingate Connector(s) inside the K8s cluster using the Helm Chart (see GitHub repo for deployment steps)
2. Create a new Twingate Resource using the internal service's IP or K8s cluster-internal DNS address (e.g., `my-service.my-namespace.svc.cluster.local`)
3. Grant users access to the Resource — they can then reach the service via its internal IP or DNS name

## Configuration Values
- **Resource address**: Internal service IP or K8s DNS name
  - Format example: `<service>.<namespace>.svc.cluster.local`
- Helm Chart deployment parameters: refer to Twingate GitHub repository

## Gotchas
- Connector must be deployed **within** the cluster to resolve cluster-internal DNS names; external Connectors cannot resolve `*.svc.cluster.local` addresses
- No specific network exposure (LoadBalancer/NodePort) required for the target service — internal ClusterIP services work

## Related Docs
- Twingate Helm Chart deployment guide (GitHub)
- Twingate Resource creation documentation
- General Connector deployment documentation