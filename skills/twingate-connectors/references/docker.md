# How to Upgrade Containerized Twingate Connectors

## Summary
Covers upgrading Twingate Connectors running in Docker, AWS ECS, and Azure Container Instances. Methods range from automated scripts to manual container replacement. Some platforms (Azure) require full destroy-and-recreate workflows due to external constraints.

## Key Information
- Always use image tag `1` or `latest` to ensure upgrades pull current images
- Two Connectors per Resource are recommended to avoid downtime during upgrades
- Check running version: `docker exec twingate-connector ./connectord --version`
- Release notes available in Connector Release Notes page

## Prerequisites
- AWS CLI configured with appropriate permissions (for ECS CLI method)
- Docker Hub account with username/password or PAT (for Azure)
- Twingate Admin Console access (for manual Docker reprovisioning)

## Step-by-Step by Platform

### AWS ECS — Console
1. Select running Connector service in ECS cluster → **Update**
2. Check **Force new deployment** → **Skip to review**
3. Click **Update Service** — pulls latest image automatically

### AWS ECS — CLI
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
  --registry-password "dockerhub-password-or-PAT" \
  --registry-login-server index.docker.io
```

### Docker — Automated Script (Recommended)
```bash
curl -s https://binaries.twingate.com/connector/docker-upgrade.sh | sudo nohup sudo bash
```
Pulls latest image, compares running containers, stops/removes/restarts outdated ones with same env vars.

### Docker — Watchtower (Auto-updates)
```bash
# Run Watchtower (all containers)
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock nicholas-fedor/watchtower:latest --cleanup

# Run Watchtower (label-scoped only)
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock nicholas-fedor/watchtower:latest --label-enable=true
```
Add `--label com.centurylinklabs.watchtower.enable=true` to Connector `docker run` command for label-scoped mode.

### Docker — Manual (Requires Reprovisioning)
```bash
docker ps
docker container rm -f [container ID or name]
docker image rm -f twingate/connector
# Get new run command from Admin Console after reprovisioning
```

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| `twingate/connector:1` | Recommended image tag |
| `TWINGATE_NETWORK` | Network name env var |
| `TWINGATE_ACCESS_TOKEN` | Auth token (lost on manual upgrade) |
| `TWINGATE_REFRESH_TOKEN` | Auth token (lost on manual upgrade) |
| `--registry-login-server` | Use `index.docker.io` for Docker Hub |

## Gotchas
- **Azure**: `az container restart` no longer works for upgrades — must recreate
- **Azure**: `--registry-password` must be in double quotes; SSO Docker Hub users must use PAT
- **ECS**: Non-`latest`/`1` image tags won't auto-pull newest version
- **Manual Docker**: Destroys auth tokens — must reprovision in Admin Console
- **Watchtower