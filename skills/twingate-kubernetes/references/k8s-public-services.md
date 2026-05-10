# Publicly Exposed Resources in Kubernetes

## Page Title
Publicly Exposed Resources in Kubernetes - Access an Exposed Service on a K8s Cluster

## Summary
This guide covers how to provide controlled external access to a Kubernetes service using Twingate without exposing the service to the public internet. Access is managed through Twingate Resources and Group assignments, with a Connector deployed outside the target cluster acting as the secure access point.

## Key Information
- Connector must be deployed **outside** the target K8s cluster
- The K8s service gets an external (but private/non-public) IP address
- Access is controlled via Twingate Resource + Group assignments
- Private DNS can substitute for private IP addressing

## Prerequisites
- A Twingate account with admin access
- A K8s cluster with a service to expose
- Network infrastructure supporting private (non-public) IP assignment to K8s services
- A separate host/node outside the cluster to deploy the Twingate Connector

## Step-by-Step

1. **Deploy Connector outside the target K8s cluster**
   - Connector must have network access to the cluster's API/service endpoint
   - Neither the Connector nor the endpoint should be publicly accessible

2. **Configure an external (private) IP for the K8s service**
   - IP must be reachable from the Connector deployed in step 1
   - Optionally configure private DNS to use a hostname instead of IP

3. **Create a Twingate Resource**
   - Use the service's private IP address or private DNS name
   - Assign appropriate Groups to control which users can access the Resource

## Configuration Values
| Parameter | Value/Notes |
|---|---|
| Resource address | Private IP or private DNS hostname of the K8s service |
| Connector placement | External to target K8s cluster |
| Network access requirement | Connector → K8s service endpoint (private network) |

## Gotchas
- Connector must **not** be deployed inside the same K8s cluster as the target service for this pattern
- The service's external IP must be private (not public internet-routable)
- If the Connector or service endpoint is internet-accessible, the security model is compromised
- Private DNS setup is optional but recommended over raw IP addresses for maintainability

## Related Docs
- [Private DNS configuration](https://www.twingate.com/docs) (use private DNS for service access)
- [Twingate Resource creation](https://www.twingate.com/docs)
- [Connector deployment](https://www.twingate.com/docs)