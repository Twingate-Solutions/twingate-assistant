# Manage Kubernetes Using kubectl via Twingate

## Summary
Secure access to a Kubernetes cluster API endpoint using Twingate, eliminating the need to expose the API server to the public Internet. Traffic is proxied through a Twingate Connector deployed outside the target cluster.

## Key Information
- Connector must be deployed **outside** the target K8s cluster
- Connector needs network access to the K8s API endpoint
- Neither Connector nor API endpoint should be publicly accessible
- No separate K8s proxy required when using Twingate

## Prerequisites
- Twingate Connector deployed with network access to the K8s API endpoint
- Twingate Resource configured for the cluster's API endpoint IP
- `kubectl` installed on local machine
- User authorized to access the K8s API endpoint Resource in Twingate

## Step-by-Step

1. **Deploy Connector** outside the target K8s cluster with network access to the API endpoint
2. **Create a Twingate Resource** using the cluster's private API endpoint address (e.g., `10.1.1.15`)
3. **Update local kubectl config** to point to the private API endpoint address:
   ```bash
   kubectl config set-cluster example-cluster --server=https://10.1.1.15
   ```
4. **Connect to Twingate** — traffic to the API endpoint is automatically proxied through the Connector

## Configuration Values

| Parameter | Example Value | Notes |
|-----------|--------------|-------|
| `--server` | `https://10.1.1.15` | Private K8s API endpoint IP defined as Twingate Resource |

## Gotchas
- Connector placement is critical: must be **outside** the target cluster but with internal network access to the API endpoint
- Access only works while actively connected to Twingate and authorized for the Resource
- The private IP used in kubectl config must exactly match the address configured as the Twingate Resource

## Related Docs
- Twingate Connector deployment
- Creating Twingate Resources
- Kubernetes Operator / in-cluster Connector deployment (separate use case)