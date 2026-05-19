# Manage Kubernetes Using kubectl via Twingate

## Summary
Securely access a Kubernetes cluster API endpoint using kubectl without exposing it to the public Internet. Twingate proxies kubectl traffic through a Connector deployed outside the target cluster, eliminating the need for a separate K8s proxy.

## Key Information
- Connector must be deployed **outside** the target K8s cluster
- Connector needs network access to the K8s API endpoint
- Neither Connector nor API endpoint should be publicly accessible
- No separate K8s proxy setup required
- Access is controlled via Twingate Resource authorization

## Prerequisites
- Twingate account with ability to create Resources and deploy Connectors
- Connector deployed with network reach to the K8s API endpoint
- kubectl installed on local machine
- User authorized to access the K8s API endpoint Resource in Twingate

## Step-by-Step

1. **Deploy Connector** outside the target K8s cluster (must have network access to cluster API endpoint)
2. **Create Twingate Resource** pointing to the cluster's API endpoint (e.g., `10.1.1.15`)
3. **Configure kubectl** on local machine to use the private API endpoint address:
   ```bash
   kubectl config set-cluster example-cluster --server=https://10.1.1.15
   ```
4. **Connect Twingate client** on local machine — traffic automatically proxies through the Connector

## Configuration Values

| Parameter | Example Value | Description |
|-----------|--------------|-------------|
| `--server` | `https://10.1.1.15` | Private K8s API endpoint defined as Twingate Resource |

## Gotchas
- Connector placement is critical: must be **outside** the target cluster but with internal network access to its API endpoint
- Local machine cannot directly reach the API endpoint IP — this is intentional; Twingate handles routing
- kubectl will fail if Twingate client is disconnected or user lacks Resource authorization

## Related Docs
- Twingate Connector deployment
- Creating Twingate Resources
- Kubernetes Connector deployment (for in-cluster scenarios)