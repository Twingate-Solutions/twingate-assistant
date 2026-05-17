# Publicly Exposed Resources in Kubernetes

## Page Title
Publicly Exposed Resources in Kubernetes - Access an Exposed Service on a K8s Cluster

## Summary
This pattern enables external access to Kubernetes services using Twingate without exposing them to the public internet. A Connector deployed outside the cluster proxies access to services that have private (non-public) external IPs. Access is controlled via Twingate Resources and Group assignments.

## Key Information
- Connector must be deployed **outside** the target K8s cluster
- The K8s service gets an external IP that is **private** (not public internet-facing)
- Access is controlled through Twingate Resource and Group configuration
- Private DNS can substitute for IP-based access

## Prerequisites
- Twingate account with ability to create Resources and Groups
- A K8s cluster with at least one service to expose
- Network infrastructure that supports private (non-public) external IPs for K8s services
- Twingate Connector deployable on a host with network access to the K8s API/service endpoint

## Step-by-Step

1. **Deploy Connector(s) outside the target cluster**
   - Connector must have network access to the cluster's service endpoint
   - Neither the Connector nor the endpoint should be publicly internet-accessible

2. **Configure a private external IP for the K8s service**
   - Assign an external IP address that is reachable from the Connector
   - IP must be private (external to K8s cluster, but not public internet)
   - Optionally configure private DNS instead of using raw IP address

3. **Create a Twingate Resource**
   - Use the service's private IP or private DNS address as the Resource address
   - Assign appropriate Groups to control which users can access the Resource

## Configuration Values
| Parameter | Value/Notes |
|---|---|
| Connector placement | Outside the target K8s cluster |
| Service external IP | Private IP reachable by Connector (not public) |
| Resource address | Private IP or private DNS of the K8s service |

## Gotchas
- The Connector must **not** be deployed inside the same cluster it's providing access to in this pattern
- The external IP must be reachable from the Connector — verify routing between Connector host and K8s service external IP
- Public internet exposure of either the Connector or the service endpoint invalidates the security model
- If using DNS, ensure private DNS resolution is configured correctly before creating the Resource

## Related Docs
- Twingate Resource creation
- Private DNS configuration for Resources
- Connector deployment documentation
- Group assignment for access control