---
source: https://www.twingate.com/docs/docker
type: docs
fetched: 2026-10-04
source_version: 0e000cccc239319f734babeea9ad23b852407a621b7022b1443f4f86e98d9a00
trust: official
---

# How to Upgrade Containerized Connectors (AWS/Azure/Docker)

## Summary
Covers upgrading Twingate Connectors running as containers in Docker, AWS ECS, and Azure Container Instances. Methods range from automated scripts to manual container replacement. Upgrade approach varies significantly by platform.

## Key Information
- Latest image tag is `twingate/connector:1`
- Check running version: `docker exec twingate-connector ./connectord --version`
- ECS task definitions should use `1` or `latest` image tags to always pull latest
- Azure Container Instances cannot be restarted to upgrade—must destroy and recreate
- Manual Docker upgrade does **not** preserve auth tokens; requires reprovisioning

## Prerequisites
- Docker, AWS CLI, or Azure CLI installed (per platform)
- Access to Twingate Admin Console (for reprovisioning if needed)
- Azure upgrades require a free Docker Hub account with username + password/PAT
- Connector Release Notes available at Twingate docs

## Step-by-Step by Platform

### AWS ECS (Console)
1. Select running Connector service in ECS cluster → **Update**
2. Check **Force new deployment** → **Skip to review**
3. Click **Update Service** (pulls latest image automatically)

### AWS ECS (CLI)
```bash
aws ecs update-service --region <REGION> --cluster <CLUSTER_NAME> --service <SERVICE_NAME> --force-new-deployment
```

### Azure Container Instances
Destroy old container, then recreate:
```bash
az container create --name twingate-connector-name --image twingate/connector:1 \
  --resource-group RSG-here --vnet VNet-here --subnet Subnet-here \
  --cpu 1 --memory 2 --os-type Linux \
  --environment-variables TWINGATE_NETWORK="your-twingate-network" \
    TWINGATE_ACCESS_TOKEN= TWINGATE_REFRESH_TOKEN= \
    TWINGATE_TIMESTAMP_FORMAT=2 TWINGATE_LABEL_DEPLOYED_BY=azure \
  --registry-username DockerHubUsername \
  --registry-password "dockerhub-password-or-PAT" \
  --registry-login-server index.docker.io
```

### Docker (Automated Script)
Downloads and runs the official upgrade script from `binaries.twingate.com` (pulls latest image, compares running containers, replaces outdated ones while preserving env vars):
```bash
curl -s https://binaries.twingate.com/connector/docker-upgrade.sh | sudo nohup sudo bash
```

### Docker (Watchtower)
Run Watchtower for selective auto-updates using label `com.centurylinklabs.watchtower.enable=true` on the Connector container. Add `--label com.centurylinklabs.watchtower.enable=true` to the `docker run` command.

### Docker (Manual)
```bash
docker ps
docker container rm -f [container ID or name]
docker image rm -f twingate/connector
# Reprovision in Admin Console, then run new docker run command
```

## Configuration Values
| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Your Twingate network name |
| `TWINGATE_ACCESS_TOKEN` | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token |
| `TWINGATE_TIMESTAMP_FORMAT` | Log timestamp format |
| `TWINGATE_LABEL_DEPLOYED_BY` | Deployment label |

## Gotchas
- Azure: `--registry-username` needs no quotes; `--registry-password` **must** be in double quotes
- Azure SSO users (Google/GitHub login) must use a PAT instead of password
- Manual Docker upgrade loses auth tokens—must reprovision connector in Admin Console
- Watchtower is **not recommended for critical production systems**
- ECS: non-`1`/`latest` image tags may not pull the actual latest version

## Related Docs
- [Linux Docker Deployment](https://www.twingate.com/docs)
- [Upgrading Connectors best practices](https://www.twingate.com/docs)
- [Connector