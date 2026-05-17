# Private Resources in Kubernetes

## Page Title
Private Resources in Kubernetes: Access Private Services Within a K8s Cluster

## Summary
Deploy Twingate Connectors inside a Kubernetes cluster via Helm Chart to enable access to internal K8s services. Users access services through their internal IPs or cluster DNS names without public internet exposure.

## Key Information
- Connectors must be deployed **inside** the K8s cluster to reach internal services
- Resources can be defined using either internal service IP or K8s cluster-internal DNS addresses
- Access is scoped to authorized Twingate users only

## Prerequisites
- A Twingate account with a configured network
- Helm installed and configured for your K8s cluster
- Access to the Twingate Helm Chart repository (GitHub)

## Step-by-Step

1. **Deploy Connector(s)** inside the K8s cluster using the Twingate Helm Chart (see linked GitHub repo for deployment steps)
2. **Create a Twingate Resource** using either:
   - Internal service IP address
   - K8s cluster-internal DNS address (e.g., `service-name.namespace.svc.cluster.local`)
3. **Grant user access** to the Resource — authorized users can then reach the service via its internal IP or DNS name

## Configuration Values
- **Resource address formats:**
  - Internal IP: `10.x.x.x`
  - K8s DNS: `<service>.<namespace>.svc.cluster.local`

## Gotchas
- Connector must be deployed **within** the cluster — external Connectors cannot resolve cluster-internal DNS names or reach internal service IPs
- No specific port/protocol restrictions mentioned; configure Resource definitions accordingly in the Twingate admin console

## Related Docs
- [Twingate Helm Chart (GitHub)](https://github.com/Twingate/helm-charts) — Connector deployment steps
- Twingate Resource configuration docs
- Helm Chart deployment guide