# Twingate Kubernetes Operator - Getting Started

## Summary
The Twingate Kubernetes Operator exposes Kubernetes services via Twingate by introducing custom CRDs that sync with the Twingate control plane. It manages connectors, resources, and access policies declaratively. Deployed via Helm from GitHub Container Registry.

## Key Information
- Introduces three primary CRDs: `TwingateConnector`, `TwingateResource`, `TwingateResourceAccess`
- Operator provisions connectors and Twingate resources automatically from Kubernetes manifests
- Services can be exposed via direct `TwingateResource` or by annotating existing Services

## Prerequisites
- Kubernetes cluster v1.16+ with admin permissions
- `kubectl` configured
- Helm v3
- Twingate account with admin access
- API key with "Read, Write, & Provision" permissions
- Remote Network created in Twingate Admin console

## Step-by-Step Installation

1. **Create Remote Network** in Twingate Admin → Network tab → Remote Networks
2. **Note Remote Network ID** from URL: `https://<network>.twingate.com/networks/<remote-network-id>`
3. **Create API key** at Settings → API with "Read, Write, & Provision" permissions
4. **Create `values.yaml`**:
   ```yaml
   twingateOperator:
     apiKey: "<api-key>"
     network: "<network-slug>"
     remoteNetworkId: "<remote-network-id>"
   ```
5. **Install via Helm**:
   ```bash
   helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator --install --wait -f ./values.yaml
   ```

## Configuration Values

| Field | Description |
|-------|-------------|
| `twingateOperator.apiKey` | Twingate API key |
| `twingateOperator.network` | Network slug (subdomain) |
| `twingateOperator.remoteNetworkId` | ID from Remote Network URL |

## CRD Examples

**TwingateConnector** (with auto-update):
```yaml
apiVersion: twingate.com/v1beta
kind: TwingateConnector
metadata:
  name: my-connector
spec:
  imagePolicy:
    provider: dockerhub
    schedule: "0 0 * * *"
```

**TwingateResource**:
```yaml
apiVersion: twingate.com/v1beta
kind: TwingateResource
metadata:
  name: foo
spec:
  name: Foo
  address: foo.default.svc.cluster.local
  alias: foo.local
```

**TwingateResourceAccess**:
```yaml
apiVersion: twingate.com/v1beta
kind: TwingateResourceAccess
metadata:
  name: foo-devops-access
spec:
  resourceRef:
    name: foo
    namespace: default
  principalExternalRef:
    type: group
    name: DevOps Engineers
```

## Gotchas
- API key is shown only once — save immediately after creation
- `principalExternalRef` references by name; `principalId` references by Twingate internal ID
- Add `-n [namespace]` to Helm install command if deploying to non-default namespace
- Helm chart release name in examples is `twop` (arbitrary, can be changed)

## Related Docs
- [API Reference](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference)
- [imagePolicy documentation](https://github.com/Twingate/kubernetes-operator/wiki)
- [Service annotation method](https://github.com/Twingate/kubernetes-operator/wiki)
- [Full values.yaml reference](https://github.com/Twingate/kubernetes-operator/wiki)