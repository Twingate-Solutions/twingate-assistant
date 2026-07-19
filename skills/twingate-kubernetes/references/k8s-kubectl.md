# Manage Kubernetes Using kubectl via Twingate

## Summary
Securely manage a Kubernetes cluster via `kubectl` without exposing the cluster API endpoint to the public internet. Twingate proxies `kubectl` traffic through a Connector deployed outside the target cluster.

## Key Information
- Connector must be deployed **outside** the target K8s cluster
- Connector needs network access to the K8s API endpoint
- Neither the Connector nor the API endpoint should be publicly accessible
- No separate K8s proxy required when using Twingate

## Prerequisites
- Twingate Connector deployed with network access to the K8s API endpoint
- Twingate Resource created for the cluster's API endpoint address
- `kubectl` installed on local machine
- User must be authorized to access the K8s API endpoint Resource in Twingate

## Step-by-Step

1. **Deploy Connector** outside the target K8s cluster with network access to the API endpoint
2. **Create Twingate Resource** using the cluster's private API endpoint address (e.g., `10.1.1.15`)
3. **Configure kubectl** on local machine to point to the private API endpoint address:
   ```bash
   kubectl config set-cluster example-cluster --server=https://10.1.1.15
   ```
4. **Connect to Twingate** — traffic is automatically proxied through the Connector

## Configuration Values

| Parameter | Example | Description |
|-----------|---------|-------------|
| `--server` | `https://10.1.1.15` | Private K8s API endpoint defined as Twingate Resource |

## Gotchas
- Connector placement is critical: must be **outside** the target cluster, not inside it
- Both the Connector and API endpoint must be off the public internet
- `kubectl` will fail if Twingate client is not connected or user lacks Resource authorization

## Related Docs
- [Deploy Twingate Connectors](https://www.twingate.com/docs/connectors)
- [Create Resources](https://www.twingate.com/docs/resources)