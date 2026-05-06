# How to Upgrade Containerized Connectors (AWS/Azure/Docker)

## Summary
Covers upgrading Twingate Connectors running as containers in Docker, AWS ECS, and Azure Container Instances. Each platform has a distinct upgrade path. Manual Docker upgrades require reprovisioning the Connector in the Admin Console.

## Key Information
- Always use image tag `1` or `latest` to ensure upgrades pull the newest image
- AWS ECS: Force new deployment (preserves config)
- Azure: Must destroy and recreate container (no restart support due to Docker Hub rate limiting)
- Docker: Automated script, Watchtower, or manual steps available
- Manual Docker removal requires reprovisioning (tokens not preserved)

## Prerequisites
- Azure upgrades: Free Docker Hub account with username + password or PAT
- Azure SSO Docker Hub users (Google/GitHub): Must use PAT instead of password
- Watchtower: Not recommended for critical production systems

## Step-by-Step

### AWS ECS (Console)
1. Select running Connector service in ECS cluster → **Update**
2. Check **Force new deployment** → **Skip to review**
3. Click **Update Service**

### AWS ECS (CLI)
```bash
aws ecs update-service --region <REGION> --cluster <CLUSTER_NAME> --service <SERVICE_NAME> --force-new-deployment
```

### Azure Container Instance
Destroy old container, then recreate:
```bash
az container create --name twingate-connector-name --image twingate/connector:1 \
  --resource-group RSG-here --vnet VNet-here --subnet Subnet-here \
  --cpu 1 --memory 2 --os-type Linux \
  --environment-variables TWINGATE_NETWORK="your-network" TWINGATE_ACCESS_TOKEN= TWINGATE_REFRESH_TOKEN= \
  TWINGATE_TIMESTAMP_FORMAT=2 TWINGATE_LABEL_DEPLOYED_BY=azure \
  --registry-username DockerHubUsername --registry-password "password" \
  --registry-login-server index.docker.io
```

### Docker (Automated Script)
```bash
curl -s https://binaries.twingate.com/connector/docker-upgrade.sh | sudo nohup sudo bash
```
Handles: pull latest → compare → stop/delete outdated → restart with same env vars.

### Docker (Manual - requires reprovisioning)
```bash
docker ps
docker container rm -f [container ID or name]
docker image rm -f twingate/connector
# Get new run command from Admin Console
docker run ...
```

## Configuration Values

| Parameter | Notes |
|---|---|
| `twingate/connector:1` | Recommended image tag |
| `TWINGATE_NETWORK` | Network name (Azure env var) |
| `TWINGATE_ACCESS_TOKEN` | Auth token |
| `TWINGATE_REFRESH_TOKEN` | Refresh token |
| `TWINGATE_TIMESTAMP_FORMAT=2` | Azure deployment |
| `TWINGATE_LABEL_DEPLOYED_BY` | Deployment label |
| `com.centurylinklabs.watchtower.enable=true` | Watchtower label-enable filter |

## Gotchas
- Azure: `--registry-password` value **must** be in double quotes; `--registry-username` does not require quotes
- ECS: If task definition uses a pinned tag (not `1`/`latest`), force deployment won't pull newest image
- Manual Docker removal destroys auth tokens — must reprovision in Admin Console
- Watchtower: Original project archived; use `nicholas-fedor/watchtower` fork

## Related Docs
- [Linux Docker Deployment](https://www.twingate.com/docs/linux-docker)
- [Upgrading Connectors (best practices)](https://www.twingate.com/docs/upgrading-connectors)
- [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes)
- [Docker Hub PAT documentation](https://docs.docker.com/security/for-developers/access-tokens/)