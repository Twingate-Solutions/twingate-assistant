---
source: https://www.twingate.com/docs/docker
type: docs
fetched: 2026-08-14
source_version: 8a05b738f98686df03fb45672ae7a29e6244f8ef3355e6232e4a8f7fe5c10949
---

# How to Upgrade Containerized Connectors (AWS/Azure/Docker)

## Summary
Covers upgrading Twingate Connectors running in Docker, AWS ECS, or Azure Container Instances. Each platform requires a different upgrade approach. Manual Docker upgrades require reprovisioning the Connector in the Admin Console.

## Key Information
- Always use image tag `1` or `latest` to ensure upgrades pull the actual latest image
- Check current connector version: `docker exec twingate-connector ./connectord --version`
- Release notes available at Connector Release Notes page
- Watchtower is **not recommended for production systems**

## Prerequisites
- Running Twingate Connector container(s)
- For Azure: Free Docker Hub account with username/password or PAT (required due to Docker Hub rate limiting)
- For AWS CLI: ECS service name, cluster name, and AWS region

## Step-by-Step

### AWS ECS (Console)
1. Select running Connector service in ECS cluster → **Update**
2. Select **Force new deployment** → **Skip to review**
3. Click **Update Service**

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
Pulls latest image, compares running containers, stops/deletes/restarts outdated ones preserving env vars.

### Docker (Manual — requires reprovisioning)
```bash
docker ps
docker container rm -f [container ID or name]
docker image rm -f twingate/connector
# Get new run command from Admin Console after reprovisioning
docker run ...
```

### Watchtower (Auto-updates)
```bash
# Update all containers
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock nicholas-fedor/watchtower:latest --cleanup

# Update only labeled containers
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock nicholas-fedor/watchtower:latest --label-enable=true
```
Add label to Connector: `--label com.centurylinklabs.watchtower.enable=true`

## Configuration Values
| Parameter | Notes |
|---|---|
| `TWINGATE_NETWORK` | Your Twingate network name |
| `TWINGATE_ACCESS_TOKEN` | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token |
| `TWINGATE_TIMESTAMP_FORMAT` | Set to `2` for Azure |
| `TWINGATE_LABEL_DEPLOYED_BY` | e.g., `azure` |
| `--registry-password` | Must be in double quotes for Azure |

## Gotchas
- **Azure**: `az container restart` no longer works for upgrades; must destroy and recreate
- **Azure SSO users**: Must use a Docker Hub PAT instead of password
- **Manual Docker upgrade**: Destroys auth tokens — must reprovision Connector in Admin Console
- **ECS**: Non-`latest`/`1` image tags won't pull the newest image on force redeploy
- **Watchtower**: Archived original project; use `nicholas-fedor/watchtower` fork