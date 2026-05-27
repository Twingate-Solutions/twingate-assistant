# Publicly Exposed Resources in Kubernetes

## Page Title
Publicly Exposed Resources in Kubernetes - Access an Exposed Service on a K8s Cluster

## Summary
This guide covers how to provide controlled external access to a Kubernetes service using Twingate, without exposing the service to the public internet. Access is managed through Twingate Resources and Group assignments, with a Connector deployed outside the target cluster.

## Key Information
- Connector must be deployed **outside** the target K8s cluster
- The K8s service needs an external IP that is private (not public internet-facing)
- Access control is enforced via Twingate Resource and Group assignments
- Private DNS can be used instead of a private IP address for the service

## Prerequisites
- A K8s cluster with a service to expose
- Ability to deploy a Twingate Connector on a host with network access to the cluster's API endpoint
- Neither the Connector nor the API endpoint should be publicly accessible

## Step-by-Step

1. **Deploy Connector(s) outside the target K8s cluster**
   - Connector must have network access to the cluster's API endpoint
   - Connector and API endpoint must not be accessible from the public internet

2. **Configure an external IP for the K8s service**
   - IP must be external to the K8s cluster but **not** public
   - Must be reachable from the Connector deployed in step 1
   - Optionally use private DNS instead of a private IP address

3. **Create a new Twingate Resource**
   - Use the service's private IP or private DNS address
   - Assign appropriate Groups to control which users can access the resource

## Configuration Values
- **Resource address**: Private IP or private DNS name of the exposed K8s service
- **Connector placement**: External to K8s cluster, internal to private network

## Gotchas
- The Connector must be outside the target cluster — do not deploy it inside the cluster you're trying to secure
- The external IP must be reachable from the Connector but must **not** be a public internet address
- No Connector should be publicly internet-accessible

## Related Docs
- [Deploy a Twingate Connector](#)
- [Create a Twingate Resource](#)
- [Private DNS configuration](#)