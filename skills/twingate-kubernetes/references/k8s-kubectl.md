---
source: https://www.twingate.com/docs/k8s-kubectl
type: docs
fetched: 2026-08-14
source_version: 154e31b9bd9987d59eb4dd29576e0c24d988462b44d7c122aa65264ebb6fae45
---

# Manage Kubernetes Using kubectl via Twingate

## Summary
Secure `kubectl` access to a Kubernetes cluster API endpoint without exposing it to the public internet. Twingate proxies traffic through a Connector deployed outside the target cluster, eliminating the need for a separate K8s proxy.

## Key Information
- Connector must be deployed **outside** the target K8s cluster
- Connector only needs network access to the cluster API endpoint
- Neither the Connector nor the API endpoint should be publicly accessible
- No separate K8s proxy required when using Twingate

## Prerequisites
- Twingate Connector deployed with network access to the K8s API endpoint
- Twingate Resource configured for the cluster API endpoint IP/hostname
- `kubectl` installed on local machine
- User authorized to access the K8s API endpoint Resource in Twingate
- Active Twingate connection on local machine

## Step-by-Step

1. **Deploy Connector** outside the target K8s cluster, ensuring it has network access to the API endpoint
2. **Create Twingate Resource** with the cluster's API endpoint address (e.g., `10.1.1.15`)
3. **Configure kubectl** on your local machine to point to the private API endpoint address:
   ```bash
   kubectl config set-cluster example-cluster --server=https://10.1.1.15
   ```
4. **Connect to Twingate** — traffic to the API endpoint will be automatically proxied via the Connector

## Configuration Values

| Parameter | Example | Notes |
|-----------|---------|-------|
| `--server` | `https://10.1.1.15` | Private K8s API endpoint defined as Twingate Resource |

## Gotchas
- Connector placement is critical: must be **outside** the target cluster but still able to reach its API endpoint
- Local machine cannot reach the API endpoint directly — Twingate must be connected for `kubectl` to function
- Both conditions must be met simultaneously: active Twingate connection **and** authorized Resource access

## Related Docs
- [Deploy a Connector](https://www.twingate.com/docs/connectors)
- [Create a Resource](https://www.twingate.com/docs/resources)
- Kubernetes Connector deployment (for in-cluster Connector use cases)