---
source: https://help.twingate.com/articles/6965244612-azure-container-docker-hub-rate-limits-block-connector-deployment-or-restart
type: help
fetched: 2026-08-06
source_version: 71c4186c5b2aa1bbdb3563840dc25f278b24ccf3fb31aeb4dc5ba34424659a1b
---

# Azure Container: Docker Hub Rate Limits Block Connector Deployment

## Summary
When deploying or restarting Twingate Connectors via Azure Container Instances, Docker Hub rate limiting can block image pulls from `index.docker.io`. Authenticating requests with Docker Hub credentials resolves this by applying higher rate limit thresholds.

## Key Information
- Affects Connector deployments and restarts on Azure Container Instances
- Error originates from Docker Hub's unauthenticated pull rate limits
- Authenticated (and paid) Docker Hub accounts receive higher thresholds
- Fix requires adding registry auth parameters to the `az container` deployment command

## Prerequisites
- Docker Hub account (free tier may still encounter limits; paid tier preferred)
- Azure Container Instances deployment using `az container` CLI

## Error Signatures
```
(RegistryErrorResponse) An error response is received from the docker registry 'index.docker.io'. Please retry later.

Failed to restart the container group ''. Error: An error response is received from the docker registry 'index.docker.io'. Please retry later.
```

## Configuration Values

| Parameter | Value |
|---|---|
| `--registry-username` | Your Docker Hub username |
| `--registry-password` | Your Docker Hub password |
| `--registry-login-server` | `index.docker.io` |

## Step-by-Step Fix

Add the following flags to your `az container create` deployment command:

```bash
az container create \
  ... \
  --registry-username <dockerhub_username> \
  --registry-password <dockerhub_password> \
  --registry-login-server index.docker.io
```

## Gotchas
- Rate limiting applies to **unauthenticated** pulls — simply having a Docker Hub account is not enough; credentials must be explicitly passed in the deployment command
- This applies to both initial deployments **and** container group restarts/updates
- Free Docker Hub accounts still have limits even when authenticated; paid accounts have higher thresholds

## Related Docs
- [Docker Hub Rate Limiting Documentation](https://docs.docker.com/docker-hub/download-rate-limit/)
- [Azure `az container` CLI Reference](https://learn.microsoft.com/en-us/cli/azure/container)