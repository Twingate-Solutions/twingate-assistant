# Publicly Exposed Resources in Kubernetes

## Summary
Provides controlled external access to Kubernetes cluster services using Twingate without public internet exposure. A Connector deployed outside the cluster proxies access to internally-exposed services via Twingate Resource assignments.

## Key Information
- Use case: Access K8s services externally while controlling access via Twingate Resources and Group assignments
- Connector is deployed **outside** the target K8s cluster
- Service gets an external IP (private, not public internet)
- Access is controlled without exposing the service to the public internet

## Prerequisites
- A Kubernetes cluster with a service to expose
- Ability to deploy a Twingate Connector on a host with network access to the K8s API/service endpoint
- Twingate admin access to create Resources and configure Group assignments
- (Optional) Private DNS infrastructure

## Step-by-Step

1. **Deploy Connector outside the K8s cluster**
   - Connector must have network access to the K8s service endpoint
   - Neither the Connector nor the service endpoint should be publicly accessible

2. **Configure an external IP for the K8s service**
   - Assign an IP address external to the cluster but on a private network
   - IP must be reachable from the deployed Connector
   - Optionally configure private DNS instead of using a raw IP address

3. **Create a Twingate Resource**
   - Use the service's private IP or private DNS address as the Resource address
   - Assign appropriate Groups to control which users can access the Resource

## Configuration Values
| Parameter | Value/Notes |
|-----------|-------------|
| Connector location | Outside target K8s cluster |
| Service IP type | Private (not public internet) |
| Resource address | Private IP or private DNS of the K8s service |

## Gotchas
- Connector must NOT be deployed inside the same cluster as the target service in this pattern
- The external IP must be reachable from the Connector's network — verify routing/firewall rules
- The service endpoint should not be accessible from the public internet; Twingate is the sole access path
- Using private DNS is recommended over raw IPs for maintainability

## Related Docs
- [Deploy Twingate Connectors](https://www.twingate.com/docs/connectors)
- [Private DNS configuration](https://www.twingate.com/docs/private-dns)
- [Create a Twingate Resource](https://www.twingate.com/docs/resources)
- [Kubernetes Connector deployment](https://www.twingate.com/docs/kubernetes)