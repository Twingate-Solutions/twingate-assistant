---
source: https://help.twingate.com/articles/6965244612-azure-container-docker-hub-rate-limits-block-connector-deployment-or-restart
type: help
fetched: 2026-11-01
source_version: 84096097ea0d46b11e97d6618f49295f7f5318ccd462ba534abfc6d9528a7676
trust: official
---

# Azure Container: Docker Hub Rate Limits Block Connector Deployment

## Summary
Docker Hub rate limiting causes failures when deploying or restarting Twingate Connectors via Azure Container Instances. Authenticated Docker Hub requests receive higher rate limit thresholds, resolving the issue.

## Key Information
- Affects Connector deployments and restarts on Azure Container Instances (ACI)
- Error originates from `index.docker.io` (Docker Hub)
- Authenticated and paid Docker Hub users receive higher pull rate limits

## Error Signatures
```
(RegistryErrorResponse) An error response is received from the docker registry 'index.docker.io'. Please retry later.
```
```
Failed to restart the container group ''. Error: An error response is received from the docker registry 'index.docker.io'. Please retry later.
```

## Resolution: Add Docker Hub Credentials to Deployment Command

Append the following flags to your `az container` deployment command:

```
--registry-username [dockerhub username] \
--registry-password [dockerhub password] \
--registry-login-server index.docker.io
```

## Configuration Values

| CLI Flag | Value |
|---|---|
| `--registry-username` | Your Docker Hub username |
| `--registry-password` | Your Docker Hub password |
| `--registry-login-server` | `index.docker.io` (literal) |

## Prerequisites
- An authenticated Docker Hub account (free tier gets higher limits than unauthenticated; paid tier gets highest)
- Azure CLI with `az container` command access

## Gotchas
- Unauthenticated pulls share rate limits by source IP — shared Azure egress IPs exhaust limits quickly
- This affects both initial deployments and container group restarts/updates
- Free Docker Hub accounts still benefit over unauthenticated pulls

## Related Docs
- [Docker Hub Rate Limiting Documentation](https://docs.docker.com/docker-hub/download-rate-limit/)
- [Azure `az container` CLI Reference](https://learn.microsoft.com/en-us/cli/azure/container)