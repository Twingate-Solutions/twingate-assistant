# Manage Kubernetes Using kubectl via Twingate

## Summary
Secure `kubectl` access to a Kubernetes cluster API endpoint without exposing it to the public Internet. Twingate acts as the proxy layer, routing `kubectl` traffic through a Connector deployed with network access to the cluster API.

## Key Information
- Connector is deployed **outside** the target K8s cluster but must have network access to the API endpoint
- Neither the Connector nor the API endpoint should be publicly accessible
- No separate K8s proxy needed when using Twingate

## Prerequisites
- Twingate Connector deployed with network reachability to the K8s API endpoint
- Twingate Resource created for the cluster API endpoint (private IP/hostname)
- `kubectl` installed on local machine
- User authorized to access the Twingate Resource
- Twingate client connected on local machine

## Step-by-Step

1. **Deploy Connector** outside the target K8s cluster, ensuring it has network access to the cluster API endpoint (not publicly accessible)

2. **Create Twingate Resource** using the cluster's private API endpoint address (e.g., `10.1.1.15`)

3. **Configure kubectl** on local machine to point to the private API endpoint:
   ```bash
   kubectl config set-cluster example-cluster --server=https://10.1.1.15
   ```

4. **Connect Twingate client** — traffic to the API endpoint will be proxied through the Connector automatically

## Configuration Values

| Parameter | Example Value | Notes |
|-----------|---------------|-------|
| Twingate Resource address | `10.1.1.15` | Private K8s API endpoint IP |
| kubectl server flag | `https://10.1.1.15` | Must match Twingate Resource address |

## Gotchas
- Connector must be deployed **outside** the target cluster (separate host/VM with network access to the API)
- Both the Connector host and API endpoint must be off the public Internet
- Local machine must be actively connected to Twingate for `kubectl` commands to reach the endpoint
- User must be authorized on the specific Twingate Resource — network access alone is insufficient

## Related Docs
- Twingate Connector deployment
- Creating Twingate Resources
- Twingate K8s documentation (other cluster management patterns)