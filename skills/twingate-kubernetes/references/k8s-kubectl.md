# Manage Kubernetes Using kubectl via Twingate

## Summary
Secure kubectl access to a Kubernetes cluster API endpoint without exposing it to the public internet. Twingate proxies kubectl traffic through a Connector deployed with network access to the cluster API, eliminating the need for a separate K8s proxy.

## Key Information
- Connector must be deployed **outside** the target K8s cluster
- Connector requires network access to the cluster API endpoint
- Neither the Connector nor the API endpoint should be internet-accessible
- No separate K8s proxy setup required
- Access control enforced via Twingate Resource authorization

## Prerequisites
- Twingate Connector deployed with network access to the K8s API endpoint
- Twingate Resource created for the cluster API endpoint IP/address
- Twingate client connected on local machine
- User authorized to access the K8s API endpoint Resource in Twingate
- `kubectl` installed locally

## Step-by-Step

1. **Deploy Connector** outside the target K8s cluster with network access to the API endpoint (no public internet exposure)

2. **Create Twingate Resource** using the cluster's private API endpoint address (e.g., `10.1.1.15`)

3. **Update kubectl config** on local machine to point to the private API endpoint:
```bash
kubectl config set-cluster example-cluster --server=https://10.1.1.15
```

4. **Connect Twingate client** — traffic to the API endpoint is automatically proxied through the Connector

## Configuration Values

| Parameter | Example Value | Notes |
|-----------|--------------|-------|
| Resource address | `10.1.1.15` | Private K8s API endpoint IP |
| kubectl server flag | `https://10.1.1.15` | Must match Resource address |

## Gotchas
- Connector placement is critical: must be **outside** the cluster but with internal network access to the API endpoint
- Local machine cannot directly reach the API endpoint IP — this is expected; Twingate handles routing
- kubectl will fail if Twingate client is disconnected or user lacks Resource authorization
- Ensure the API endpoint is not publicly routable before relying on this setup for security

## Related Docs
- Twingate Connector deployment
- Creating Twingate Resources
- Kubernetes Connector deployment (in-cluster variant)