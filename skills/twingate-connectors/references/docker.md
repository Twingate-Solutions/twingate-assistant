# Upgrading Containerized Twingate Connectors

## Summary
Instructions for upgrading Twingate Connectors running as containers in Docker, AWS ECS, and Azure Container Instances. Each platform requires a different upgrade approach. Manual Docker upgrades require reprovisioning the connector in the Admin Console.

## Key Information
- Always use image tag `1` or `latest` to ensure upgrades pull the newest image
- Two Docker upgrade paths: automated script (preserves tokens) or manual (requires reprovisioning)
- Azure Container Instances cannot be restarted to upgrade — must destroy and recreate
- Watchtower not recommended for production systems

## Prerequisites
- Running Twingate Connector container
- Platform-specific CLI tools (AWS CLI, Azure CLI, Docker CLI)
- Azure upgrades require Docker Hub account (username + password or PAT)

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
Destroy old container and recreate:
```bash
az container create --name twingate-connector-name --image twingate/connector:1 \
  --resource-group RSG-here --vnet VNet-here --subnet Subnet-here \
  --cpu 1 --memory 2 --os-type Linux \
  --environment-variables TWINGATE_NETWORK="your-network" TWINGATE_ACCESS_TOKEN= TWINGATE_REFRESH_TOKEN= \
  TWINGATE_TIMESTAMP_FORMAT=2 TWINGATE_LABEL_DEPLOYED_BY=azure \
  --registry-username DockerHubUsername --registry-password "dockerhub-password" \
  --registry-login-server index.docker.io
```

### Docker (Automated Script — preserves tokens)
```bash
curl -s https://binaries.twingate.com/connector/docker-upgrade.sh | sudo nohup sudo bash
```

### Docker (Manual — requires reprovisioning)
```bash
docker ps
docker container rm -f [container ID or name]
docker image rm -f twingate/connector
# Reprovision in Admin Console, then run new docker run command
```

### Check Current Version
```bash
docker exec twingate-connector ./connectord --version
```

## Configuration Values

| Parameter | Notes |
|-----------|-------|
| `twingate/connector:1` | Recommended image tag |
| `--registry-password` | Must be in double quotes for Azure CLI |
| `com.centurylinklabs.watchtower.enable=true` | Label required for selective Watchtower updates |

## Watchtower (Auto-updates)
```bash
# Update all containers
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock nicholas-fedor/watchtower:latest --cleanup

# Update only labeled containers
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock nicholas-fedor/watchtower:latest --label-enable=true
```
Add `--label com.centurylinklabs.watchtower.enable=true` to connector's `docker run` command.

## Gotchas
- ECS task definitions with hardcoded non-`latest`/`1` tags won't pull newest image on force deploy
- Azure CLI `container restart` no longer works for upgrades due to Docker Hub rate limiting
- Azure SSO users (Google/GitHub login) must use a PAT instead of password
- Manual Docker upgrade **does not** preserve auth tokens — must reprovision connector
- Original Watchtower project is archived; use `nicholas-fedor/watchtower` fork

## Related Docs
- [Upgrading Connectors best practices](#)
- [Linux Docker deployment](#)
- [Connector Release Notes](#)
- [Reprovision a Connector](#)