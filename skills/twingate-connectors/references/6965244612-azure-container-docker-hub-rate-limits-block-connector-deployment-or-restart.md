---
source: https://help.twingate.com/articles/6965244612-azure-container-docker-hub-rate-limits-block-connector-deployment-or-restart
type: help
fetched: 2026-09-06
source_version: 7b7e52820063d79f72e9e3e6743ac92a62930a764b131e348a069148e311f881
---

# Azure Container: Docker Hub Rate Limits Block Connector Deployment

## Page Title
Azure Container Docker Hub Rate Limits Block Connector Deployment or Restart

## Summary
Docker Hub rate limiting can block Twingate Connector deployments or restarts on Azure Container Instances, returning a `RegistryErrorResponse` error from `index.docker.io`. The fix is to authenticate image pull requests with Docker Hub credentials.

## Key Information
- Affects: Connector deployments and restarts via Azure Container Services
- Root cause: Docker Hub rate limits unauthenticated pulls more aggressively than authenticated/paid accounts
- Error appears during initial deployment or container group restarts

## Error Messages
- Deployment: `(RegistryErrorResponse) An error response is received from the docker registry 'index.docker.io'. Please retry later.`
- Restart: `Failed to restart the container group ''. Error: An error response is received from the docker registry 'index.docker.io'. Please retry later.`

## Prerequisites
- Docker Hub account (free or paid; paid accounts have higher thresholds)
- Azure Container Instances deployment via `az container` CLI

## Resolution: CLI Parameters

Add Docker Hub authentication flags to the `az container` deployment command:

```bash
az container create \
  ... \
  --registry-login-server index.docker.io \
  --registry-username [dockerhub_username] \
  --registry-password [dockerhub_password]
```

## Configuration Values

| Parameter | Value |
|---|---|
| `--registry-login-server` | `index.docker.io` |
| `--registry-username` | Your Docker Hub username |
| `--registry-password` | Your Docker Hub password |

## Gotchas
- Authenticated free-tier Docker Hub accounts still have rate limits, just higher than unauthenticated — paid Docker Hub accounts get the highest thresholds
- Error message says "Please retry later" which may suggest a transient issue, but repeated failures indicate rate limiting
- Applies to both new deployments and container group restarts/updates

## Related Docs
- [Docker Hub Rate Limiting Documentation](https://docs.docker.com/docker-hub/download-rate-limit/)
- [Azure `az container` CLI Reference](https://learn.microsoft.com/en-us/cli/azure/container)