# Upgrading Containerized Twingate Connectors (Docker/AWS ECS/Azure)

## Summary
Instructions for upgrading Twingate Connectors running in Docker, AWS ECS, or Azure Container Instances. Each platform requires a different upgrade approach. Manual Docker upgrades require reprovisioning the Connector in the Admin Console.

## Key Information
- Image tag `1` or `latest` ensures you pull the most recent version
- Avoid manual Docker upgrade path if possible (loses auth tokens, requires reprovisioning)
- Watchtower is not recommended for production systems
- Azure Container Instances can no longer be restarted to upgrade — must destroy and recreate

## Prerequisites
- Running Twingate Connector as a container
- AWS CLI (for ECS CLI method), Azure CLI (for Azure method)
- Docker Hub account with credentials (Azure only, due to rate limiting)
- Access to Twingate Admin Console (for manual Docker reprovisioning)

## Step-by-Step by Platform

### AWS ECS (Console)
1. Select Connector service in ECS cluster → **Update**
2. Check **Force new deployment** → **Skip to review**
3. Click **Update Service**

### AWS ECS (CLI)
```bash
aws ecs update-service --region <REGION> --cluster <CLUSTER_NAME> --service <SERVICE_NAME> --force-new-deployment
```

### Azure Container Instance
Destroy old container, recreate with `az container create`:
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
Preserves environment variables, pulls latest image automatically.

### Docker (Manual — requires reprovisioning)
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

**Watchtower label:** `com.centurylinklabs.watchtower.enable=true`

## Check Current Version
```bash
docker exec twingate-connector ./connectord --version
```

## Gotchas
- Azure: SSO Docker Hub logins (Google/GitHub) require a Personal Access Token instead of password
- Azure: `--registry-password` value must be in double quotes
- Manual Docker upgrade **destroys auth tokens** — must reprovision Connector in Admin Console
- ECS: If task definition uses a pinned tag (not `1` or `latest`), force-deploy won't pull latest
- Watchtower (original project) is archived; use fork `nicholas-fedor/watchtower`

## Related Docs
- [Linux Docker Deployment](https://www.twingate.com/docs/docker-deployment)
- [Upgrading Connectors Best Practices](https://www.twingate.com/docs/upgrading-connectors)
- [Connector Release Notes](https://www.twingate.com/docs/connector-release-notes)