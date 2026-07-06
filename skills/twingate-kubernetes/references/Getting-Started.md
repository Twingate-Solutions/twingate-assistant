# Twingate Kubernetes Operator - Getting Started

## Summary
The Twingate Kubernetes Operator automates exposing Kubernetes services via Twingate by introducing CRDs that sync with the Twingate API. It manages connectors, resources, and access control declaratively. Install via Helm, then define `TwingateConnector`, `TwingateResource`, and `TwingateResourceAccess` objects.

## Prerequisites
- Kubernetes cluster v1.16+ with admin permissions
- `kubectl` configured for cluster access
- Helm v3
- Twingate account with admin access
- Remote Network created in Twingate Admin console
- API key with **Read, Write, & Provision** permissions

## Installation Steps

1. **Create Remote Network** in Twingate Admin: Network tab → Remote Networks → "+Remote Network"
2. **Note Remote Network ID** from URL: `https://<network-name>.twingate.com/networks/<remote-network-id>`
3. **Create API key**: Settings → API with "Read, Write, & Provision" permissions
4. **Create `values.yaml`**:
```yaml
twingateOperator:
  apiKey: "<api-key>"
  network: "<network-slug>"
  remoteNetworkId: "<remote-network-id>"
```
5. **Install with Helm**:
```bash
helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator --install --wait -f ./values.yaml
```
Add `-n [namespace]` for a specific namespace.

## CRD Definitions

### TwingateConnector
```yaml
apiVersion: twingate.com/v1beta
kind: TwingateConnector
metadata:
  name: my-connector
spec:
  imagePolicy:
    provider: dockerhub
    schedule: "0 0 * * *"  # Daily updates at midnight UTC
```

### TwingateResource
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

### TwingateResourceAccess
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
    name: "DevOps Engineers"
```

## Configuration Values
| Field | Description |
|-------|-------------|
| `twingateOperator.apiKey` | Twingate API key |
| `twingateOperator.network` | Network slug (subdomain) |
| `twingateOperator.remoteNetworkId` | Remote Network ID from admin URL |
| `imagePolicy.provider` | Image registry (`dockerhub`) |
| `imagePolicy.schedule` | Cron schedule for image updates |

## Principal Reference Options
- `principalId` — direct ID of a Group or ServiceAccount
- `principalExternalRef` — reference by `type` (`group`/service account) and `name`

## Gotchas
- API key is shown only once — save it immediately after creation
- Remote Network ID is extracted from the admin console URL, not a named field
- Alternative to `TwingateResource`: annotate the Kubernetes Service directly and let the operator create the resource automatically

## Related Docs
- [API Reference](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference)
- [imagePolicy documentation](https://github.com/Twingate/kubernetes-operator/wiki)
- [Service annotation approach](https://github.com/Twingate/kubernetes-operator/wiki)
- [Full values.yaml reference](https://github.com/Twingate/kubernetes-operator/wiki)