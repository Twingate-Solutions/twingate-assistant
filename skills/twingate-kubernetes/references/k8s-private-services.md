# Private Resources in Kubernetes

## Page Title
Private Resources in Kubernetes - Access private services within a K8s cluster

## Summary
Deploy Twingate Connectors inside a Kubernetes cluster via Helm Chart, then define Resources using internal IPs or K8s cluster DNS names. Authorized users can access internal K8s services without public internet exposure.

## Key Information
- Connectors must be deployed **inside** the K8s cluster (not externally) to access internal services
- Resources can be defined using either internal service IPs or K8s cluster-internal DNS addresses
- Access is scoped per-Resource; only users explicitly granted access can reach the service

## Prerequisites
- Twingate account with a configured Network
- Helm installed and configured for the target cluster
- Kubernetes cluster with appropriate permissions to deploy via Helm

## Step-by-Step

1. **Deploy Connector(s)** inside the K8s cluster using the Twingate Helm Chart (see [Helm Chart repository](https://github.com/Twingate/helm-charts))
2. **Create a Twingate Resource** using either:
   - Internal service IP address
   - K8s cluster-internal DNS name (e.g., `my-service.my-namespace.svc.cluster.local`)
3. **Grant user/group access** to the Resource
4. Users can now connect to the service via Twingate Client using the internal address

## Configuration Values
- **Resource address**: Internal cluster IP or K8s DNS format:
  `<service>.<namespace>.svc.cluster.local`

## Gotchas
- Connector must be deployed **within** the cluster — an external Connector cannot resolve cluster-internal DNS names or reach ClusterIP services
- K8s DNS names are only resolvable from within the cluster network; the Connector acts as the in-cluster proxy
- No additional service exposure (LoadBalancer/NodePort) is needed or recommended

## Related Docs
- [Twingate Helm Chart (GitHub)](https://github.com/Twingate/helm-charts)
- Twingate Resource configuration docs
- Connector deployment documentation