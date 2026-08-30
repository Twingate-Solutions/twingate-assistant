---
source: https://github.com/Twingate/kubernetes-operator/wiki
type: github
fetched: 2026-08-30
source_version: 9703051c8d00007e758dec09dc1f5635dedb535d
---

# Twingate Kubernetes Operator

## Summary
A Kubernetes operator (OSS) that manages Twingate network resources as Kubernetes custom resources. It syncs CRD definitions to the Twingate control plane, handling connectors, resources, access policies, gateways, and identity firewall configuration. Deployed via Helm and built on the `kopf` Python framework.

## Key Information
- API group: `twingate.com/v1beta`
- Custom resource types: `TwingateConnector`, `TwingateResource`, `TwingateResourceAccess`, `TwingateGroup`, `TwingateGateway`, `TwingateCertificateAuthority`
- Resource types supported: `Network`, `Kubernetes`, `WebApp`
- Identity Firewall support via `TwingateGateway` (Layer 7 reverse proxy for Kubernetes impersonation and WebApp header injection)
- Image auto-update via `imagePolicy` with DockerHub or Google Container Registry providers and cron schedule
- Kubernetes labels on `TwingateResource` sync to Twingate as tags by default (`syncLabels: true`)

## Prerequisites
- Kubernetes v1.16+ with admin permissions
- `kubectl` configured
- Helm v3
- Twingate account with admin access
- Twingate API key with "Read, Write, & Provision" permissions
- A Twingate Remote Network created before installation

## Usage / Step-by-Step
1. Create a Remote Network in the Twingate Admin Console; note the ID from the URL
2. Generate an API key at `Settings > API`
3. Create `values.yaml`:
   ```yaml
   twingateOperator:
     apiKey: "<api-key>"
     network: "<network-slug>"
     remoteNetworkId: "<remote-network-id>"
   ```
4. Install via Helm:
   ```bash
   helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator --install --wait -f ./values.yaml
   ```
5. Deploy a connector, then define `TwingateResource` and `TwingateResourceAccess` objects

## Configuration Values

| Field | Description |
|-------|-------------|
| `twingateOperator.apiKey` | Twingate API key |
| `twingateOperator.network` | Twingate network slug |
| `twingateOperator.remoteNetworkId` | Default Remote Network ID (overridable per resource) |
| `TwingateConnector.spec.imagePolicy.schedule` | Cron schedule for image updates |
| `TwingateConnector.spec.logLevel` | `-1` to `7`, default `3` |
| `TwingateResource.spec.type` | `Network` (default), `Kubernetes`, `WebApp` |
| `TwingateResourceAccess.spec.accessPolicy.mode` | `MANUAL`, `AUTO_LOCK`, `ACCESS_REQUEST` |
| `TwingateResourceAccess.spec.approvalMode` | `MANUAL` or `AUTOMATIC` |

## Gotchas
- `id`, `remoteNetworkId`, `resourceRef`, `groupRef`, `principalId`, `principalExternalRef`, and resource `type` are **immutable once set**
- `image` and `imagePolicy` are mutually exclusive on `TwingateConnector`
- `accessPolicy`, `approvalMode`, and `expiresAt` must be `null` when the principal is a `ServiceAccount`
- `isBrowserShortcutEnabled` only works on `Network`-type resources and cannot be used with wildcard addresses
- `requestHeaderRewrites` only applies to `WebApp` resources
- `TwingateGateway` and `TwingateResource` of type `Kubernetes`/`WebApp` require `gatewayRef`; `Network` resources do not allow it
- `TwingateGateway.spec.remoteNetworkId` is immutable once set (overrides operator-wide default)
- For HA, run multiple connectors with staggered `imagePolicy` schedules and pod anti-affinity rules
- `principalExternalRef` name uniqueness is not enforced; if multiple