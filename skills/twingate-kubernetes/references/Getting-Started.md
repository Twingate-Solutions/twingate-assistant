# Twingate Kubernetes Operator - Getting Started

## Summary
The Twingate Kubernetes Operator exposes Kubernetes services via Twingate by introducing custom CRDs that sync with the Twingate control plane. It manages Connectors, Resources, and Access policies as Kubernetes objects. Installation is via Helm; configuration is declarative YAML.

## Prerequisites
- Kubernetes cluster v1.16+ with admin permissions
- `kubectl` configured for cluster access
- Helm v3
- Twingate account with admin access
- Remote Network created in Twingate Admin console
- API key with **Read, Write, & Provision** permissions

## Key Information
- Three primary CRDs: `TwingateConnector`, `TwingateResource`, `TwingateResourceAccess`
- Helm chart hosted at `oci://ghcr.io/twingate/helmcharts/twingate-operator`
- Remote Network ID found in URL: `https://<network>.twingate.com/networks/<remote-network-id>`
- Services can be auto-managed via annotations instead of manual `TwingateResource` objects

## Step-by-Step Installation

**1. Gather Twingate values:**
- Network slug (subdomain of `twingate.com`)
- Remote Network ID (from Admin console URL)
- API key (Settings > API)

**2. Create `values.yaml`:**
```yaml
twingateOperator:
  apiKey: "<api-key>"
  network: "<network-slug>"
  remoteNetworkId: "<remote-network-id>"
```

**3. Install via Helm:**
```bash
helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator \
  --install --wait -f ./values.yaml [-n <namespace>]
```

## Configuration: Core CRD Specs

**TwingateConnector:**
```yaml
spec:
  imagePolicy:
    provider: dockerhub
    schedule: "0 0 * * *"  # cron for update checks
```

**TwingateResource:**
```yaml
spec:
  name: Foo
  address: foo.default.svc.cluster.local  # internal DNS
  alias: foo.local                         # user-facing hostname
```

**TwingateResourceAccess:**
```yaml
spec:
  resourceRef:
    name: foo
  principalExternalRef:
    type: group        # group or serviceaccount
    name: "DevOps Engineers"
  # OR use principalId: "<id>" for direct ID reference
```

## Gotchas
- API key is shown **only once** — save it immediately after creation
- `principalExternalRef` references by name; `principalId` references by Twingate internal ID — use accordingly
- Connector must be deployed before Resources can be accessed
- Namespace must be specified with `-n` flag if not installing to `default`
- Internal DNS format for services: `<service>.<namespace>.svc.cluster.local`

## Related Docs
- [API Reference](https://github.com/Twingate/kubernetes-operator/wiki/API-Reference)
- [imagePolicy documentation](https://github.com/Twingate/kubernetes-operator/wiki/Connector)
- [Service annotations](https://github.com/Twingate/kubernetes-operator/wiki/Kubernetes-resources)
- [Full values.yaml reference](https://github.com/Twingate/kubernetes-operator/wiki)
- [Migration: v1 to v2](https://github.com/Twingate/kubernetes-operator/wiki/Migration:-v1-to-v2)