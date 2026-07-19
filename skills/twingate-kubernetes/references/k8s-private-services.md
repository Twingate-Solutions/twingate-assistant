# Private Resources in Kubernetes

## Page Title
Private Resources in Kubernetes: Access Private Services Within a K8s Cluster

## Summary
Deploy a Twingate Connector inside a Kubernetes cluster via Helm Chart, then define a Twingate Resource using the service's internal IP or cluster DNS name. Authorized users can then access the private K8s service without public internet exposure.

## Key Information
- Connector must be deployed **inside** the K8s cluster (not externally) to reach cluster-internal services
- Resources can be defined using either internal service IPs or K8s cluster-internal DNS addresses (e.g., `service.namespace.svc.cluster.local`)
- No public exposure of the service is required

## Prerequisites
- Twingate account with ability to create Resources
- Kubernetes cluster
- Helm installed
- Access to Twingate Helm Chart (hosted on GitHub)

## Step-by-Step
1. Deploy Twingate Connector(s) inside the K8s cluster using the Helm Chart (see [Helm Chart deployment docs on GitHub](https://github.com/Twingate/helm-charts))
2. Create a new Twingate Resource specifying the target service's internal IP or K8s cluster-internal DNS name
3. Grant users access to the Resource — they can then reach the service via its internal address through Twingate

## Configuration Values
| Parameter | Value/Format |
|---|---|
| Resource address | Internal service IP or K8s DNS (e.g., `my-service.my-namespace.svc.cluster.local`) |
| Connector deployment method | Helm Chart |

## Gotchas
- Connector must run **within the cluster** — an externally deployed Connector cannot resolve cluster-internal DNS names or reach ClusterIP services
- K8s DNS names are only resolvable from within the cluster; ensure the Connector pod has standard cluster DNS configured
- Multiple Connectors can be deployed for redundancy (recommended)

## Related Docs
- [Twingate Helm Chart on GitHub](https://github.com/Twingate/helm-charts)
- Twingate Resource creation documentation
- Connector deployment documentation