# Manage Kubernetes Using kubectl via Twingate

## Summary
Securely manage a Kubernetes cluster's API endpoint using `kubectl` through Twingate without exposing the API server to the public internet. Traffic is proxied through a Twingate Connector deployed outside the target cluster.

## Key Information
- Connector must be deployed **outside** the target K8s cluster
- Connector needs network access to the K8s API endpoint
- Neither the Connector nor the API endpoint should be publicly accessible
- No separate K8s proxy required when using Twingate

## Prerequisites
- Twingate account with ability to create Resources
- Twingate Connector deployed with network access to the K8s API endpoint
- `kubectl` installed on local machine
- User authorized to access the K8s API endpoint Resource in Twingate

## Step-by-Step

1. **Deploy Connector** outside the target K8s cluster (must have network access to API endpoint)
2. **Create a Twingate Resource** using the cluster's private API endpoint address (e.g., `10.1.1.15`)
3. **Configure `kubectl`** on local machine to point to the private API endpoint address:
   ```bash
   kubectl config set-cluster example-cluster --server=https://10.1.1.15
   ```
4. **Connect to Twingate** — traffic to the API endpoint is automatically proxied through the Connector

## Configuration Values

| Parameter | Example | Description |
|-----------|---------|-------------|
| `--server` | `https://10.1.1.15` | Private K8s API endpoint defined as Twingate Resource |

## Gotchas
- Connector placement is critical: must be **outside** the target cluster but with internal network access to the API endpoint
- Local machine cannot directly reach the private API endpoint — Twingate must be connected for `kubectl` to work
- Access requires both Twingate connection **and** authorization to the specific Resource

## Related Docs
- Twingate Connector deployment
- Creating Twingate Resources
- Kubernetes Operator documentation