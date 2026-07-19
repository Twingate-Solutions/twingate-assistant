# Publicly Exposed Resources in Kubernetes

## Summary
Provides external access to a Kubernetes service using Twingate without exposing it to the public internet. Access is controlled through Twingate Resources and Group assignments. The Connector is deployed outside the target cluster to proxy access to the service.

## Key Information
- Connector must be deployed **outside** the target K8s cluster
- The K8s service gets an external IP that is private (not public internet-facing)
- Access control enforced via Twingate Resource and Group assignments
- Private DNS can substitute for IP address in Resource configuration

## Prerequisites
- Twingate account with ability to create Resources and Groups
- A K8s cluster with a service to expose
- Network path from Connector host to K8s service external IP
- Connector host must NOT be publicly internet-accessible

## Step-by-Step

1. **Deploy Connector** outside the target K8s cluster
   - Connector must have network access to the K8s service endpoint
   - Neither Connector nor endpoint should be publicly accessible

2. **Configure external IP** for the K8s service
   - Must be a private (non-public) IP address
   - Must be reachable from the deployed Connector
   - Optionally configure private DNS for the service address

3. **Create Twingate Resource** using the service's private IP or DNS address
   - Assign appropriate Groups to control access
   - Authorized users access the service through Twingate without public exposure

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Connector location | External to target K8s cluster |
| Service IP type | Private/internal (not public) |
| Resource address | Private IP or private DNS name |

## Gotchas
- Connector placement is critical — must be **outside** the cluster, not inside as a pod
- The "external" IP is external to the K8s cluster but still private/non-public
- No direct network path should exist between the public internet and either the Connector or the K8s service endpoint

## Related Docs
- [Deploy a Connector](https://www.twingate.com/docs/connectors)
- [Private DNS configuration](https://www.twingate.com/docs/private-dns)
- [Create a Twingate Resource](https://www.twingate.com/docs/resources)
- Contrast with internal K8s services (Connector deployed inside cluster)