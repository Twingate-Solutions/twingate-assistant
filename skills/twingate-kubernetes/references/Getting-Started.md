# Twingate Kubernetes Operator - Getting Started

## Summary
The Twingate Kubernetes Operator exposes Kubernetes services via Twingate by introducing CRDs that sync Twingate configuration. Deploy the operator via Helm, then define `TwingateConnector`, `TwingateResource`, and `TwingateResourceAccess` objects to manage access.

## Key Information
- Introduces three primary CRDs: `TwingateConnector`, `TwingateResource`, `TwingateResourceAccess`
- Operator provisions connectors and manages Twingate resources declaratively
- Services can be exposed via CRDs directly or by annotating existing Kubernetes services

## Prerequisites
- Kubernetes cluster v1.16+ with admin permissions
- `kubectl` configured for cluster access
- Helm v3
- Twingate account with admin access
- API key with "Read, Write, & Provision" permissions
- Remote Network created in Twingate Admin console

## Step-by-Step

### 1. Twingate Setup
- Create Remote Network: Admin Console → Network → Remote Networks → "+Remote Network"
- Note Remote Network ID from URL: `https://<network-name>.twingate.com/networks/<remote-network-id>`
- Create API key: Settings → API → "Read, Write, & Provision" permissions

### 2. Install Operator
Create `values.yaml`:
```yaml
twingateOperator:
  apiKey: "<api-key>"
  network: "<network-slug>"
  remoteNetworkId: "<remote-network-id>"
```
```bash
helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator --install --wait -f ./values.yaml
```

### 3. Deploy Connector
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

### 4. Create Resource
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

### 5. Grant Access
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

## Configuration Values

| Field | Description |
|-------|-------------|
| `twingateOperator.apiKey` | Twingate API key |
| `twingateOperator.network` | Network slug (subdomain) |
| `twingateOperator.remoteNetworkId` | Remote Network ID from URL |
| `imagePolicy.provider` | Image registry (`dockerhub`) |
| `imagePolicy.schedule` | Cron schedule for update checks |

## Gotchas
- API key is only shown once at creation — save it immediately
- `principalExternalRef` uses `type: group` or `type: serviceaccount`; alternatively use `principalId` for direct ID reference
- Add `-n [namespace]` to Helm command to install to non-default namespace

## Related Docs
- [API Reference](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference)
- [imagePolicy documentation](https://github.com/Twingate/kubernetes-operator/wiki)
- [Service annotation method](https://github.com/Twingate/kubernetes-operator/wiki)
- [Full values.yaml reference](https://github.com/Twingate/kubernetes-operator/wiki)