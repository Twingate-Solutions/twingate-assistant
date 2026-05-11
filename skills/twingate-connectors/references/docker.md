# Upgrading Containerized Twingate Connectors

## Summary
Instructions for upgrading Twingate Connectors running in Docker, AWS ECS, or Azure Container Instances. Each platform requires a different upgrade approach. Avoid downtime by following best practices from the Upgrading Connectors guide.

## Key Information
- Image tag `1` or `latest` ensures you always pull the most recent version
- Check running connector version: `docker exec twingate-connector ./connectord --version`
- Watchtower is not recommended for critical production systems

## Prerequisites
- Running Twingate Connector container(s)
- Platform-specific CLI tools (AWS CLI, Azure CLI, Docker CLI)
- Azure: Free Docker Hub account with username/password or PAT (required due to rate limiting)

## Step-by-Step by Platform

### AWS ECS (Console)
1. Select running Connector service in ECS cluster → **Update**
2. Check **Force new deployment** → **Skip to review**
3. Click **Update Service** (auto-pulls latest image)

### AWS ECS (CLI)
```bash
aws ecs update-service --region <REGION> --cluster <CLUSTER_NAME> --service <SERVICE_NAME> --force-new-deployment
```

### Azure Container Instance
Must destroy and recreate (restart no longer works):
```bash
az container create --name twingate-connector-name --image twingate/connector:1 \
  --resource-group RSG-here --vnet VNet-here --subnet Subnet-here \
  --cpu 1 --memory 2 --os-type Linux \
  --environment-variables TWINGATE_NETWORK="your-network" TWINGATE_ACCESS_TOKEN= \
    TWINGATE_REFRESH_TOKEN= TWINGATE_TIMESTAMP_FORMAT=2 TWINGATE_LABEL_DEPLOYED_BY=azure \
  --registry-username DockerHubUsername --registry-password "password" \
  --registry-login-server index.docker.io
```

### Docker (Automated Script)
```bash
curl -s https://binaries.twingate.com/connector/docker-upgrade.sh | sudo nohup sudo bash
```
Handles: pull latest image → compare → stop outdated → restart with same env vars.

### Docker (Manual)
```bash
docker ps
docker container rm -f [container ID or name]
docker image rm -f twingate/connector
# Reprovision in Admin Console, then:
docker run ...
```
⚠️ Manual method requires reprovisioning — does not preserve auth tokens.

### Watchtower (Auto-updates)
```bash
# Watch all containers
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock nicholas-fedor/watchtower:latest --cleanup

# Watch only labeled containers
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock nicholas-fedor/watchtower:latest --label-enable=true
```
Add label to connector: `--label com.centurylinklabs.watchtower.enable=true`

## Configuration Values

| Variable | Description |
|----------|-------------|
| `TWINGATE_NETWORK` | Your Twingate network name |
| `TWINGATE_ACCESS_TOKEN` | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token |
| `TWINGATE_TIMESTAMP_FORMAT` | Timestamp format (Azure: `2`) |
| `TWINGATE_LABEL_DEPLOYED_BY` | Deployment label |

## Gotchas
- **Azure**: Cannot restart containers to upgrade — must destroy and recreate; Docker Hub credentials required
- **Azure**: SSO Docker Hub users must use a PAT, not password; `--registry-password` must be in double quotes
- **ECS**: Non-`latest`/`1` image tags may not pull the actual latest image
- **Manual Docker**: Tokens are lost; connector must be reprovisioned in Admin Console
- **Watchtower**: Archived project; use fork `nicholas-fedor/watchtower`

## Related Docs
- [Linux Docker Deployment](https://www.twingate.com/docs/docker-deploy)
- [