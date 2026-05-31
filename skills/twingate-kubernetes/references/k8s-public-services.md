# Publicly Exposed Resources in Kubernetes

## Page Title
Publicly Exposed Resources in Kubernetes - Access an exposed service on a K8s cluster

## Summary
This guide covers how to provide controlled external access to a Kubernetes service using Twingate, without exposing the service to the public internet. A Connector deployed outside the cluster proxies access to an internally-exposed service endpoint.

## Key Information
- Connector must be deployed **outside** the target K8s cluster
- K8s service gets an external IP that is **private** (not public internet-facing)
- Access control is managed via Twingate Resources and Group assignments
- Private DNS can substitute for raw IP addresses

## Prerequisites
- Twingate account with ability to create Resources and Groups
- A K8s cluster with a service to expose
- Infrastructure to deploy a Twingate Connector outside the cluster (but with network access to the cluster)
- Network path from Connector to the K8s service's external IP

## Step-by-Step

1. **Deploy Connector(s) outside the target K8s cluster**
   - Connector must have network access to the K8s API/service endpoint
   - Neither the Connector nor the endpoint should be publicly accessible

2. **Configure an external IP for the K8s service**
   - IP must be private (internal network only, not public internet)
   - IP must be reachable from the deployed Connector
   - Optionally configure private DNS for the exposed service

3. **Create a Twingate Resource**
   - Use the service's private IP address or private DNS name
   - Assign appropriate Groups to control which users can access the Resource

## Configuration Values
- **Resource address**: Private IP or private DNS hostname of the K8s service
- **Group assignments**: Define which Twingate users/groups get access

## Gotchas
- Connector placement is critical — it must be **outside** the cluster, not inside
- The external IP for the K8s service is external to the cluster but **not** public — common point of confusion
- No public internet exposure at any point in the chain (Connector, service endpoint, or Resource)

## Related Docs
- [Private DNS usage](https://www.twingate.com/docs) — for DNS-based access instead of raw IPs
- Twingate Resource creation docs
- Twingate Connector deployment docs
- Group assignment and access control docs