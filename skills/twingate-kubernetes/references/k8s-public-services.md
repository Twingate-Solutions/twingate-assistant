## Publicly Exposed Resources in Kubernetes

How to gate access to a service that is *exposed* outside the cluster (e.g., via a LoadBalancer, Ingress, or NodePort) using Twingate -- without leaving it open on the public internet.

**Architecture:**
1. Deploy Connector(s) **outside the target cluster**, on a network that can reach the service's external (but not public) IP/hostname
2. Configure the K8s service with an external IP/DNS that is **routable from the Connector** but **not reachable from the public internet** (e.g., internal LoadBalancer, private Ingress, RFC1918 IP)
3. Define a Twingate **Resource** with that internal IP or private DNS name
4. Grant access via Group membership

**Vs. Private Services Pattern:**

| Pattern | Connector Location | Service Type | Use Case |
|---|---|---|---|
| /docs/k8s-private-services | Inside cluster | ClusterIP / internal | Reach ClusterIP services |
| **This guide** | Outside cluster | Internal LoadBalancer, private Ingress | Multi-cluster, shared service mesh, services already exposed for non-Twingate clients |

**Why External-but-Private Exposure:**
- Many production clusters use **internal LoadBalancers** (cloud-specific: AWS NLB internal, GCP internal LB, Azure internal LB) for shared services consumed by multiple clusters or VPCs
- The Connector lives in a "shared services" VPC/subnet that has reachability to those internal LBs
- Twingate provides identity-based access to the LB endpoint without making it public

**Configuration Tips:**
- **Use private DNS** for the Resource address rather than IPs -- LB IPs can change on recreation, FQDNs are stable
- Twingate intercepts DNS queries for FQDNs defined as Resources, so the user's resolver doesn't need to know about the private DNS zone
- See /docs/private-dns-best-practices for FQDN-as-Resource patterns

**Gotchas:**
- The Connector must have network reachability to the LB/Ingress -- verify with `curl` or `kubectl run --rm -it` from a pod in the Connector's network
- If the LB cert SAN doesn't include the FQDN you use as the Twingate Resource, TLS verification fails -- either fix the cert or use `--insecure` in the client (not recommended)
- This pattern is **not** for ClusterIP-only services -- those need the in-cluster Connector pattern (private-services)

**Related Docs:**
- /docs/k8s-private-services -- Sibling pattern with in-cluster Connector
- /docs/k8s -- K8s deployment overview
- /docs/private-dns-best-practices -- FQDN-as-Resource patterns
