# How to Upgrade Containerized Connectors (AWS/Azure/Docker)

## Summary
Covers upgrading Twingate Connectors running in Docker, AWS ECS, and Azure Container Instances. Each platform has different upgrade mechanisms. Manual Docker upgrades require reprovisioning the Connector in the Admin Console.

## Key Information
- Image tag `1` or `latest` ensures latest image is pulled on restart
- Check running connector version: `docker exec twingate-connector ./connectord --version`
- Release notes available in Connector Release Notes page
- Watchtower is **not recommended for production systems**

## Prerequisites
- Running Twingate Connector container
- Platform-specific CLI tools (AWS CLI, Azure `az` CLI, Docker CLI)
- Azure upgrades require a free Docker Hub account (username + password or PAT)

## Step-by-Step by Platform

### AWS ECS (Console)
1. Select running Connector service in ECS cluster → **Update**
2. Select **Force new deployment** → **Skip to review**
3. Click **Update Service**

### AWS ECS (CLI)
```bash
aws ecs update-service --region <REGION> --cluster <CLUSTER_NAME> --service <SERVICE_NAME> --force-new-deployment
```

### Azure Container Instance
Must destroy and recreate (restart no longer works due to Docker Hub rate limiting):
```bash
az container create --name twingate-connector-name --image twingate/connector:1 \
  --resource-group RSG-here --vnet VNet-here --subnet Subnet-here \
  --cpu 1 --memory 2 --os-type Linux \
  --environment-variables TWINGATE_NETWORK="your-twingate-network" \
    TWINGATE_ACCESS_TOKEN= TWINGATE_REFRESH_TOKEN= \
    TWINGATE_TIMESTAMP_FORMAT=2 TWINGATE_LABEL_DEPLOYED_BY=azure \
  --registry-username DockerHubUsername \
  --registry-password "dockerhub-password" \
  --registry-login-server index.docker.io
```

### Docker (Automated Script)
```bash
curl -s https://binaries.twingate.com/connector/docker-upgrade.sh | sudo nohup sudo bash
```
Automatically pulls latest image, compares running containers, replaces outdated ones preserving env vars.

### Docker (Manual — requires reprovisioning)
```bash
docker ps
docker container rm -f [container ID or name]
docker image rm -f twingate/connector
# Get new run command from Admin Console after reprovisioning
docker run ...
```

### Docker (Watchtower)
```bash
# Watch all containers
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock nicholas-fedor/watchtower:latest --cleanup

# Watch only labeled containers
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock nicholas-fedor/watchtower:latest --label-enable=true
```
Add label to connector: `--label com.centurylinklabs.watchtower.enable=true`

## Configuration Values
| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Your Twingate network name |
| `TWINGATE_ACCESS_TOKEN` | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token |
| `TWINGATE_TIMESTAMP_FORMAT` | Log timestamp format |
| `TWINGATE_LABEL_DEPLOYED_BY` | Deployment label |

## Gotchas
- **Azure**: `--registry-password` must be in double quotes; SSO Docker Hub logins require a PAT
- **Manual Docker upgrade**: Auth tokens are NOT preserved — must reprovision connector in Admin Console
- **ECS**: If task definition uses a pinned tag (not `1`/`latest`), force-new-deployment won't pull latest
- **Watchtower**: Original project archived; use `nicholas-fedor/watchtower` fork

## Related Docs
- Upgrading Connectors (best practices)
- Linux Docker deployment
- Connector Release Notes
- Twingate KB article for Azure deployment