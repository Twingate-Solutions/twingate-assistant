# Publicly Exposed Resources in Kubernetes

## Summary
Provides external access to a Kubernetes service using Twingate without exposing it to the public internet. Access is controlled via Twingate Resources and Group assignments, with a Connector deployed outside the target cluster.

## Key Information
- Connector must be deployed **outside** the target K8s cluster
- The K8s service needs an external (but non-public) IP address
- Access is controlled via Twingate Resource + Group assignments
- Neither the Connector nor the API endpoint should be publicly accessible

## Prerequisites
- A running K8s cluster with a service to expose
- Network path between the external Connector and the K8s service's external IP
- Twingate account with ability to create Resources and Groups

## Step-by-Step

1. **Deploy Connector(s) outside the target K8s cluster**
   - Connector must have network access to the cluster's API endpoint
   - Neither the Connector nor the endpoint should be internet-accessible

2. **Configure an external IP for the K8s service**
   - Must be an IP external to the cluster but not public
   - Must be reachable from the Connector deployed in step 1
   - Optionally use private DNS instead of a raw IP address

3. **Create a Twingate Resource**
   - Use the service's private IP or private DNS address
   - Assign appropriate Groups to control user access

## Configuration Values
- **Resource address**: Private IP or private DNS name of the exposed K8s service
- **Connector placement**: External to K8s cluster, internal to private network

## Gotchas
- Connector placement is critical — it must be **outside** the K8s cluster, not deployed as a pod inside it
- The external IP must be reachable from the Connector's network location — verify routing before creating the Resource
- Private DNS is recommended over raw IPs for maintainability

## Related Docs
- [Private DNS configuration](https://www.twingate.com/docs) (use private DNS for service access)
- Twingate Resource creation
- Connector deployment guides