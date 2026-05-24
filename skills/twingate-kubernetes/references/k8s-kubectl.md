# Manage Kubernetes Using kubectl via Twingate

## Summary
Secure kubectl access to a Kubernetes cluster API endpoint without exposing it to the public Internet. Twingate proxies traffic to the private API endpoint via a Connector deployed with network access to the cluster.

## Key Information
- Connector must be deployed **outside** the target K8s cluster but with network access to the API endpoint
- Neither the Connector nor the API endpoint should be publicly accessible
- No separate K8s proxy required
- Access is controlled via Twingate Resource authorization

## Prerequisites
- Twingate Connector deployed with network access to the K8s API endpoint
- K8s API endpoint on a private address (e.g., `10.1.1.15`)
- Twingate client running on local machine
- Authorization to access the K8s API endpoint Resource in Twingate

## Step-by-Step

1. **Deploy Connector** outside the target K8s cluster, ensuring it has network access to the cluster API endpoint
2. **Create a Twingate Resource** using the cluster's private API endpoint address (e.g., `10.1.1.15`)
3. **Update local kubectl config** to point to the private API endpoint address:
   ```bash
   kubectl config set-cluster example-cluster --server=https://10.1.1.15
   ```
4. **Connect Twingate** on local machine — traffic is automatically proxied through the Connector

## Configuration Values

| Parameter | Example Value | Description |
|-----------|---------------|-------------|
| `--server` | `https://10.1.1.15` | Private K8s API endpoint defined as Twingate Resource |

## Gotchas
- Connector placement is critical: must be **outside** the target cluster but on a network that can reach the API endpoint
- If not connected to Twingate or not authorized to the Resource, kubectl commands will fail silently or timeout
- The private IP used in kubectl config must exactly match the address configured as the Twingate Resource

## Related Docs
- Twingate Connector deployment
- Creating Twingate Resources
- Kubernetes Connector deployment (for in-cluster use cases)