---
source: https://help.twingate.com/articles/6965244612-azure-container-docker-hub-rate-limits-block-connector-deployment-or-restart
type: help
fetched: 2026-10-04
source_version: 14c5227e03b22e346a35a69037caf3d0d8405cb4944b975be654638785e43684
trust: official
---

# Azure Container: Docker Hub Rate Limits Block Connector Deployment

## Summary
Docker Hub rate limiting causes failures when deploying or restarting Twingate Connectors via Azure Container Instances. Authenticated Docker Hub requests receive higher rate limit thresholds, resolving the issue.

## Key Information
- Error occurs during Connector deployment or update/restart via Azure Container Services
- Root cause: Docker Hub rate limiting on unauthenticated pulls from `index.docker.io`
- Fix: Add Docker Hub credentials to the `az container` deployment command

## Error Messages
- Deployment: `(RegistryErrorResponse) An error response is received from the docker registry 'index.docker.io'. Please retry later.`
- Restart: `Failed to restart the container group ''. Error: An error response is received from the docker registry 'index.docker.io'.`

## Prerequisites
- Docker Hub account (paid account provides highest rate limit thresholds)
- Azure CLI with `az container` access
- Existing Twingate Connector deployment on Azure Container Instances

## Resolution

Add Docker Hub authentication parameters to the `az container` deployment command:

```
--registry-username [dockerhub username] \
--registry-password [dockerhub password] \
--registry-login-server index.docker.io
```

**Example (appended to existing deploy command):**
```bash
az container create \
  ... [existing parameters] ... \
  --registry-login-server index.docker.io \
  --registry-username YOUR_DOCKERHUB_USERNAME \
  --registry-password YOUR_DOCKERHUB_PASSWORD
```

## Configuration Values

| Parameter | Value |
|---|---|
| `--registry-login-server` | `index.docker.io` |
| `--registry-username` | Your Docker Hub username |
| `--registry-password` | Your Docker Hub password or access token |

## Gotchas
- Free Docker Hub accounts still have rate limits; a paid account provides the highest thresholds
- Retry without credentials will continue to fail if rate limit is hit — credentials must be added to the command
- Use a Docker Hub access token instead of password where possible for better security

## Related Docs
- [Docker Hub Rate Limiting Documentation](https://docs.docker.com/docker-hub/download-rate-limit/)
- [Azure `az container` CLI Reference](https://learn.microsoft.com/en-us/cli/azure/container)