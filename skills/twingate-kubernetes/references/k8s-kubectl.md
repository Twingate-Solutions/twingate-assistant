---
source: https://www.twingate.com/docs/k8s-kubectl
type: docs
fetched: 2026-11-13
source_version: d8ae8cb9bfc646d06368653c51426ce551657d667443a735831e31c53a98b7da
trust: official
---

# Page Title
Manage Kubernetes using kubectl (Twingate Docs)

## Summary
Describes how to use Twingate to run `kubectl` against a private Kubernetes cluster without exposing the API endpoint to the public internet. A Connector deployed outside the cluster reaches the API server, a Twingate Resource represents the endpoint, and the local `kubectl` config points at that address. Twingate proxies the traffic while the client is connected.

## Key Information
- Use case: manage K8s services with `kubectl` without a public API endpoint and without a separate K8s proxy.
- The Connector must be deployed **outside** the target K8s cluster.
- Neither the Connector nor the API endpoint should be reachable from the public internet.
- The Connector only needs network access to the API endpoint.
- The Twingate Resource uses the cluster API endpoint address (example: `10.1.1.15`).
- Access works only while the user is connected to Twingate and is authorized for the API endpoint Resource.
- The endpoint address is not directly reachable from the local machine. Twingate proxies traffic to it via the Connector.

## Prerequisites
- A Twingate network with a Connector that can reach the K8s API endpoint.
- The private IP or address of the K8s API endpoint.
- The Twingate client installed and connected on the machine running `kubectl`.
- Authorization (via group/policy) to the new Resource.
- `kubectl` installed locally.

## Step-by-Step
1. Deploy one or more Connectors outside the target cluster, with network access to the API endpoint.
2. Create a new Twingate Resource using the cluster API endpoint address (e.g., `10.1.1.15`).
3. Grant the relevant users or groups access to the Resource.
4. On the local machine, update the `kubectl` config to use that address as the cluster server:

```
# 10.1.1.15 is an example private K8s API endpoint defined as a Resource in Twingate
kubectl config set-cluster example-cluster --server=https://10.1.1.15
```

5. Connect to Twingate and run `kubectl` commands as usual.

## Configuration Values
- `kubectl config set-cluster <name> --server=https://<api-endpoint-address>`
  - `<name>`: example `example-cluster`
  - `--server`: the private API endpoint address defined as the Twingate Resource

## Gotchas
- Do not place the Connector inside the cluster it protects. The page specifies it must be outside.
- The `--server` address in `kubectl` must match the address defined in the Twingate Resource.
- If the Twingate client is disconnected or the user lacks Resource access, `kubectl` cannot reach the API endpoint.
- The page does not cover TLS certificate handling. If the API server certificate does not include the address you use, verification issues may arise (not addressed in the source).
- The page's example sets only the cluster server. You may still need to configure credentials and contexts in your kubeconfig (not covered in the source).

## Related Docs
- Twingate Connector deployment docs
- Twingate Resource creation and access policy docs
- Twingate Client installation docs