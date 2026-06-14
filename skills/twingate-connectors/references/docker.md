# How to Upgrade Containerized Connectors (AWS/Azure/Docker)

## Summary
Covers upgrading Twingate Connectors running in Docker, AWS ECS, and Azure Container Instances. Methods range from automated scripts to manual container recreation. Azure requires full destroy/recreate due to Docker Hub rate limiting changes.

## Key Information
- Image tag `1` or `latest` ensures you always pull the most recent Connector version
- Check running version: `docker exec twingate-connector ./connectord --version`
- Watchtower is **not recommended for production** systems
- Manual Docker upgrade requires reprovisioning (tokens not preserved)
- Release notes available in Connector Release Notes page

## Prerequisites
- AWS CLI upgrades: ECS service name, cluster name, AWS region
- Azure upgrades: Free Docker Hub account (username + password or PAT)
- Azure SSO users (Google/GitHub login): must use PAT instead of password

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
  --environment-variables TWINGATE_NETWORK="your-network" \
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
Pulls latest image, compares running containers, replaces outdated ones preserving env vars.

### Docker (Manual — tokens NOT preserved)
```bash
docker ps
docker container rm -f [container-id-or-name]
docker image rm -f twingate/connector
# Reprovision connector in Admin Console, then run new docker run command
```

## Configuration Values

| Parameter | Notes |
|-----------|-------|
| `twingate/connector:1` | Recommended image tag |
| `--registry-password` | Must be in double quotes for Azure |
| `com.centurylinklabs.watchtower.enable=true` | Label to enable Watchtower selective updates |

## Gotchas
- **Azure**: `az container restart` no longer works for upgrades due to Docker Hub rate limiting — must recreate
- **Azure**: `--registry-username` no quotes needed; `--registry-password` requires double quotes
- **ECS**: Non-`1`/`latest` image tags may not pull the newest version
- **Manual Docker**: Reprovisioning required — existing auth tokens are not preserved
- **Watchtower**: Original project archived; use `nicholas-fedor/watchtower` fork

## Related Docs
- Linux Docker deployment
- Upgrading Connectors (best practices)
- Connector Release Notes
- Twingate KB article for Azure deployment with Docker Hub credentials