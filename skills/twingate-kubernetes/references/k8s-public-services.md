# Publicly Exposed Resources in Kubernetes

## Summary
Provides controlled external access to Kubernetes cluster services using Twingate without public internet exposure. A Connector deployed outside the cluster proxies access to internally-exposed services through Twingate Resource/Group assignments.

## Key Information
- Use case: Grant external users access to K8s services while keeping them off the public internet
- Connector must be deployed **outside** the target K8s cluster
- Service gets an external (but private/non-public) IP address
- Access control managed via Twingate Resources and Group assignments

## Prerequisites
- Twingate account with admin access
- A K8s cluster with a service to expose
- Network infrastructure supporting private IP assignment to K8s services
- Connector host with network access to the K8s API/service endpoint

## Step-by-Step

1. **Deploy Connector outside the K8s cluster**
   - Connector must have network access to the cluster's service endpoint
   - Neither the Connector nor the service endpoint should be publicly accessible

2. **Configure external IP for the K8s service**
   - Assign an IP external to the cluster but not public (e.g., via LoadBalancer with internal annotation)
   - Alternatively, configure private DNS for the service address

3. **Create a Twingate Resource**
   - Use the service's private IP address or private DNS name as the Resource address
   - Assign appropriate Groups to control who can access it

## Configuration Values
- **Resource address**: Private IP or private DNS hostname of the exposed K8s service
- **Connector placement**: External to cluster, same private network reachability as service

## Gotchas
- Connector placement is critical — it must be **outside** the cluster, not deployed as a pod inside it
- The external IP must be reachable from the Connector but must not be publicly routable
- No direct mention of cloud-specific LoadBalancer annotations (e.g., `cloud.google.com/load-balancer-type: Internal`), but these would be required in practice for private LoadBalancer IPs
- Private DNS is recommended over raw IPs for maintainability

## Related Docs
- [Private DNS with Twingate](https://www.twingate.com/docs/use-private-dns)
- [Deploying Connectors](https://www.twingate.com/docs/connectors)
- [Creating Resources](https://www.twingate.com/docs/resources)
- [Kubernetes Connector deployment](https://www.twingate.com/docs/k8s) (for in-cluster Connector scenarios)