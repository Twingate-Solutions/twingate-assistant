## Private Resources in Kubernetes

How to provide Twingate access to ClusterIP / internal services running inside a Kubernetes cluster -- without exposing them on the public internet or via a LoadBalancer.

**Architecture:**
1. Deploy Connector(s) **inside the cluster** via the Twingate Helm chart (or the Twingate Kubernetes Operator)
2. Define a Twingate **Resource** for each internal service using:
   - the service's ClusterIP, or
   - the cluster-internal DNS name (e.g., `myservice.namespace.svc.cluster.local`)
3. Grant access to the Resource via Group membership

**Why It Works:**
- The Connector pod runs in the same network namespace as other cluster pods, so it can reach ClusterIP services and resolve cluster DNS
- Twingate Client on the user's machine intercepts traffic to the configured Resource address and tunnels it through the in-cluster Connector
- No NodePort, LoadBalancer, or Ingress required

**Resource Address Choices:**

| Address Type | Example | When to Use |
|---|---|---|
| ClusterIP | `10.96.0.42` | Stable IP, but changes if Service is recreated |
| Cluster DNS FQDN | `db.production.svc.cluster.local` | Recommended -- survives Service recreation |
| Custom DNS (FQDN as Resource) | `db.example.internal` | When you map private DNS to ClusterIP via CoreDNS or external-dns |

**Connector Placement:**
- One Connector per cluster is functional; two+ for HA
- For multi-namespace clusters, the Connector pod can usually reach all namespaces' Services unless NetworkPolicies restrict it -- review NetworkPolicies if Resources are unreachable
- Connector pod needs outbound internet access to Twingate Controller (egress on standard HTTPS + UDP for P2P)

**Gotchas:**
- ClusterIP changes if you delete and recreate the Service -- prefer DNS FQDNs in the Twingate Resource
- NetworkPolicies that block egress from the Connector pod will block all Twingate access to that namespace
- For multi-cluster setups, deploy a Connector per cluster and a Remote Network per cluster

**Related Docs:**
- /docs/k8s-helm-chart -- Connector deployment via Helm
- /docs/k8s-public-services -- Sibling pattern for already-exposed services
- /docs/k8s -- K8s deployment overview (Operator vs Helm)
- /docs/private-dns-best-practices -- Using FQDNs as Resource addresses
