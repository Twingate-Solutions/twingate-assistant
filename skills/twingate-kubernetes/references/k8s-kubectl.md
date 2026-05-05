## Manage Kubernetes Using kubectl

How to give kubectl users private access to a cluster's API endpoint via Twingate -- without exposing the API server to the public internet.

**Use Case:**
- Cluster API server is on a private IP only
- Admins still need to run `kubectl get pods`, `apply`, etc. from their laptops
- Don't want a public LoadBalancer or jump host with SSH tunneling

**Architecture:**
1. Deploy a Connector **outside the target cluster**, on a network that can reach the cluster's API endpoint (e.g., a Connector pod in a management cluster, a VM in the same VPC, or a Connector running on the cluster's bastion subnet)
2. Define the API endpoint IP (e.g., `10.1.1.15`) as a Twingate Resource in the Remote Network served by that Connector
3. On the admin laptop, `kubectl` is configured to talk to the **private IP** -- Twingate Client transparently proxies the traffic

**kubectl Configuration:**
```
kubectl config set-cluster example-cluster --server=https://10.1.1.15
```

The `--server` value is the **private IP** of the K8s API endpoint (the same IP defined as the Twingate Resource).

**Authorization Requirements:**
- The user must be a member of a Group that has access to the API endpoint Resource
- The user must be connected to Twingate (Client running, online)
- Standard K8s RBAC still applies on top -- Twingate gates network reachability, RBAC gates permissions

**Why This Works:**
- Twingate Client intercepts traffic to the private IP and tunnels it through the Connector
- No `kubectl proxy`, no SSH port-forward, no public LoadBalancer needed
- TLS is end-to-end -- the Connector forwards encrypted bytes; Twingate cannot see API traffic

**Decision Notes:**
- Connector placement: closer to the API endpoint = lower latency. Putting the Connector inside a management cluster or as a sidecar to the cluster's bastion is typical
- For **identity-aware kubectl audit** (logs show the actual Twingate user, not a shared kubeconfig identity) and **session recording**, use the Twingate Kubernetes Access Gateway -- see /docs/kubernetes-access
- For **routing pod traffic outbound** through Twingate to other Resources, use the headless Client router pattern -- see /docs/k8s-cluster-access (different problem)

**Gotchas:**
- TLS cert: the K8s API endpoint cert must include the private IP in its SAN (most managed clusters do this; self-managed may need cert regeneration)
- DNS: if the kubeconfig uses a hostname rather than an IP, define a Twingate Resource with that FQDN -- Twingate intercepts DNS and routes the FQDN to the Connector
- Multi-cluster admins: each cluster's API endpoint is a separate Twingate Resource; group them by environment for cleaner access policies

**Related Docs:**
- /docs/k8s -- K8s overview, Operator vs Helm vs Gateway
- /docs/kubernetes-access -- Identity-aware kubectl with session recording
- /docs/k8s-cluster-access -- Egress traffic from cluster to Twingate Resources
