## Twingate Helm Chart

Official Helm chart for deploying Twingate Connectors into a Kubernetes cluster (GKE, EKS, AKS, MicroK8s, etc.). The chart bootstraps a Connector pod with the tokens you provide.

**Repository:**
- Helm repo: `https://twingate.github.io/helm-charts`
- Chart name: `twingate/connector`
- Source: github.com/Twingate/helm-charts

**Installation:**
```
helm repo add twingate https://twingate.github.io/helm-charts
helm upgrade --install twingate-connector twingate/connector \
  -n <namespace> \
  --set connector.network=<tenant-subdomain> \
  --set connector.accessToken=<accessToken> \
  --set connector.refreshToken=<refreshToken>
```

**Required Values:**
- `connector.network` -- Twingate tenant subdomain (e.g., `acme` for `acme.twingate.com`)
- `connector.accessToken` -- per-Connector access token from Admin Console / Terraform
- `connector.refreshToken` -- per-Connector refresh token

**Deployment Pattern:**
- Each Connector requires a unique token pair -- generate one Connector per Helm release (or use multiple Helm releases with different release names)
- Use Kubernetes Secrets to inject tokens via `--values` files instead of `--set` for production (avoid tokens in shell history / CI logs)
- Run multiple Connectors per Remote Network for HA (e.g., separate Helm releases or replica configurations)

**Uninstall:**
```
helm del twingate-connector -n <namespace>
```

**Updates:**
- `helm repo update` pulls the latest chart version
- Chart updates do **not** automatically update the Connector image -- restart pods to pull the latest image (chart sets `imagePullPolicy: Always` by default)
- See /docs/k8s-helm-chart-upgrades for the upgrade workflow

**Decision Notes:**
- The Helm chart is the simplest deployment for a Connector-in-cluster
- For declarative Twingate Resources/RemoteNetworks/Groups managed via CRDs, prefer the **Twingate Kubernetes Operator** (different repo, different model)
- P2P connections improve user experience and stay within the Fair Use bandwidth policy -- ensure node firewalls allow Connector P2P traffic

**Related Docs:**
- /docs/k8s-helm-chart-upgrades -- How to upgrade Connectors
- /docs/k8s -- Kubernetes overview, Operator vs Helm guidance
- /docs/peer-to-peer-communication-in-twingate -- P2P firewall requirements
