## Kubernetes Overview

Index page for Twingate's Kubernetes story. Three deployment models exist; pick based on what you're trying to do.

**Deployment Models:**

| Model | Use When | Reference |
|---|---|---|
| **Twingate Kubernetes Operator** (recommended) | You want declarative Twingate config (RemoteNetworks, Connectors, Resources) as Kubernetes CRDs alongside your app manifests | github.com/Twingate/kubernetes-operator |
| **Helm Chart** | You only need to run a Connector pod and manage Twingate config via Admin Console / Terraform | /docs/k8s-helm-chart |
| **Headless Client (router VM)** | You need a cluster to *route traffic outbound* through Twingate to remote Resources | /docs/k8s-cluster-access |

**Operator Highlights:**
- Define `TwingateResource`, `TwingateRemoteNetwork`, `TwingateConnector` as CRDs
- GitOps-friendly -- Twingate config flows through your normal manifest pipeline
- Configuration and access live with your cluster manifests, not in a separate Admin Console workflow

**Privileged Access for Kubernetes:**
- Built on top of the Operator + Twingate's Kubernetes Access Gateway
- Identity propagation (kubectl audit logs include the actual Twingate user, not a shared service account)
- Session recording for sensitive operations
- Open source: github.com/Twingate/kubernetes-access-gateway
- See /docs/kubernetes-access for the full guide

**Common Use Cases:**
1. **Manage cluster via kubectl over Twingate** -- Connector outside cluster, K8s API as a Twingate Resource (/docs/k8s-kubectl)
2. **Cluster routes traffic out via Twingate** -- headless Client as router VM in same VPC (/docs/k8s-cluster-access)
3. **Access private services in the cluster** -- Connector in cluster + Resources for ClusterIP services (/docs/k8s-private-services)
4. **Access publicly exposed services** -- Connector in cluster + Resources for Ingress endpoints (/docs/k8s-public-services)
5. **Privileged kubectl with identity-aware audit** -- Kubernetes Access Gateway (/docs/kubernetes-access)

**Related Docs:**
- /docs/k8s-helm-chart -- Helm install
- /docs/k8s-cluster-access -- Egress routing pattern
- /docs/k8s-kubectl -- Securing kubectl
- /docs/k8s-private-services, /docs/k8s-public-services -- Service exposure patterns
- /docs/kubernetes-access -- Privileged Access Gateway
