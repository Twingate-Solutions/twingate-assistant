---
source: https://github.com/Twingate/helm-charts
type: github
fetched: 2026-08-06
source_version: afc9ffacb45dd18f8ef3e3c90a1bf993824dd446
---

<!-- triage: unassigned -->

# Twingate Helm Charts

## Summary
Official Helm charts repository for deploying Twingate components on Kubernetes. Charts are hosted via GitHub Pages and served from the `stable` folder.

## Key Information
- Charts live in the `stable/` directory
- Hosted at `https://twingate.github.io/helm-charts`
- Standard Helm chart repository structure

## Prerequisites
- Helm 3.x installed
- Kubernetes cluster access (`kubectl` configured)
- Twingate account with valid credentials/tokens

## Usage / Step-by-Step

**Add the repository:**
```shell
helm repo add twingate https://twingate.github.io/helm-charts
```

**Update repo index:**
```shell
helm repo update
```

**List available charts:**
```shell
helm search repo twingate
```

**Install a chart:**
```shell
helm install <release-name> twingate/<chart-name> --values values.yaml
```

**Contributing a chart:**
1. Place chart directory into the `stable/` folder
2. Submit changes via pull request

## Configuration Values
Refer to each chart's individual `values.yaml` for specific parameters. Common Twingate-related values typically include:

| Parameter | Description |
|-----------|-------------|
| `network` | Twingate network name (e.g., `yourorg.twingate.com`) |
| `serviceKey` | Twingate service account key or token |
| `replicaCount` | Number of connector replicas |
| `image.repository` | Container image repository |
| `image.tag` | Container image tag |

## Gotchas
- The `stable/` directory is the only supported chart location; charts placed elsewhere will not be indexed
- GitHub Pages serves the chart index, so there may be a delay between merging changes and chart availability
- Always run `helm repo update` before installing or upgrading to ensure you have the latest chart index
- Twingate service keys/tokens are sensitive — use Kubernetes Secrets or a secrets manager rather than plain `values.yaml`

## Related Docs
- [Twingate Documentation](https://docs.twingate.com)
- [Twingate Connector Deployment](https://docs.twingate.com/docs/connector)
- [Helm Docs](https://helm.sh/docs/)
- [Artifact Hub listing](https://artifacthub.io/) (search "Twingate")