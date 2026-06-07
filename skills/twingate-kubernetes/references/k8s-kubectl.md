# Manage Kubernetes Using kubectl via Twingate

## Summary
Secure kubectl access to a Kubernetes cluster API endpoint without exposing it to the public internet. Twingate proxies kubectl traffic through a Connector deployed outside the target cluster, eliminating the need for a separate K8s proxy.

## Key Information
- Connector must be deployed **outside** the target K8s cluster
- Connector needs network access to the cluster API endpoint
- Neither Connector nor API endpoint should be publicly accessible
- No separate K8s proxy required when using Twingate

## Prerequisites
- Twingate Connector deployed with network access to the K8s API endpoint
- Twingate Resource created for the cluster API endpoint IP/address
- kubectl installed on local machine
- User authorized to access the K8s API endpoint Resource in Twingate
- Twingate client connected on local machine

## Step-by-Step

1. **Deploy Connector** outside the target K8s cluster, ensuring it has network access to the cluster API endpoint
2. **Create Twingate Resource** using the cluster's private API endpoint address (e.g., `10.1.1.15`)
3. **Configure kubectl** on local machine to point to the private API endpoint address:
   ```bash
   kubectl config set-cluster example-cluster --server=https://10.1.1.15
   ```
4. **Connect Twingate** client — kubectl traffic will automatically proxy through the Connector

## Configuration Values

| Parameter | Example | Notes |
|-----------|---------|-------|
| Resource address | `10.1.1.15` | Private K8s API endpoint IP |
| `--server` flag | `https://10.1.1.15` | Used in `kubectl config set-cluster` |

## Gotchas
- Connector placement is critical: must be **outside** the target cluster but on the same network as the API endpoint
- If Twingate client is disconnected, kubectl will lose access to the cluster
- User must have explicit authorization to the K8s API endpoint Resource in Twingate policy
- API endpoint must not be publicly routable — private IP ranges are the intended use case

## Related Docs
- Twingate Connector deployment
- Creating Twingate Resources
- Twingate access policies/authorization