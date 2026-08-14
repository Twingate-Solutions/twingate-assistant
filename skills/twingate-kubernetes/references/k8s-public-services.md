---
source: https://www.twingate.com/docs/k8s-public-services
type: docs
fetched: 2026-08-14
source_version: 8a05d9b388196346b35cb766ab7a0b2b79e437ac5a68b0ebc11253c97ecfe16e
---

# Publicly Exposed Resources in Kubernetes

## Summary
Provides external access to a Kubernetes service using Twingate without exposing it to the public internet. Access is controlled via Twingate Resources and Group assignments. The Connector is deployed outside the target cluster to proxy access to the service.

## Key Information
- Connector must be deployed **outside** the target K8s cluster
- The K8s service needs an external IP (private, not public internet-facing)
- Access control is managed through Twingate Resource and Group assignments
- Private DNS can be used instead of private IP for the service address

## Prerequisites
- A running K8s cluster with a service to expose
- Network path exists between the external Connector and the K8s service endpoint
- Neither the Connector nor the API endpoint should be publicly accessible

## Step-by-Step

1. **Deploy Connector(s) outside the target K8s cluster**
   - Connector must have network access to the K8s service endpoint
   - Connector and endpoint must not be reachable from public internet

2. **Configure an external IP for the K8s service**
   - IP must be private (not public)
   - Must be reachable from the deployed Connector
   - Optionally configure private DNS for the service address

3. **Create a Twingate Resource**
   - Use the service's private IP or private DNS name as the resource address
   - Assign appropriate Groups to control user access

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Resource address | Private IP or private DNS of the K8s service |
| Connector placement | Outside K8s cluster, same private network reachability as service |

## Gotchas
- Connector must be **external** to the cluster — do not deploy it inside the cluster for this use case
- The external IP configured for the K8s service is external to the cluster but must remain private (not internet-routable)
- No direct mention of LoadBalancer vs NodePort — ensure the service type exposes an IP reachable from the Connector's network

## Related Docs
- [Private DNS configuration](https://www.twingate.com/docs) — for DNS-based resource access instead of IP
- [Twingate Resource creation](https://www.twingate.com/docs)
- [Connector deployment](https://www.twingate.com/docs)