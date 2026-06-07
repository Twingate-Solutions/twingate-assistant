# Upgrading Containerized Twingate Connectors (Docker/AWS ECS/Azure)

## Summary
Instructions for upgrading Twingate Connector containers across Docker, AWS ECS, and Azure Container Instances. Methods range from automated scripts to manual image replacement. Avoid downtime by following best practices from the Upgrading Connectors guide.

## Key Information
- Default image tag: `twingate/connector:1` (always pulls latest in `1.x` line)
- Avoid pinning to specific version tags if you want automatic latest pulls
- Azure Container Instances require full destroy/recreate due to Docker Hub rate limiting
- Manual Docker upgrade does **not** preserve auth tokens — reprovisioning required

## Check Current Version
```bash
docker exec twingate-connector ./connectord --version
```

## Step-by-Step by Platform

### AWS ECS — Console
1. Select Connector service in ECS cluster → **Update**
2. Enable **Force new deployment** → Skip to review
3. Click **Update Service**

### AWS ECS — CLI
```bash
aws ecs update-service --region <REGION> --cluster <CLUSTER_NAME> --service <SERVICE_NAME> --force-new-deployment
```

### Azure Container Instances
Must destroy and recreate (no restart supported):
```bash
az container create \
  --name twingate-connector-name \
  --image twingate/connector:1 \
  --resource-group RSG-here \
  --vnet VNet-here --subnet Subnet-here \
  --cpu 1 --memory 2 --os-type Linux \
  --environment-variables TWINGATE_NETWORK="your-network" TWINGATE_ACCESS_TOKEN= TWINGATE_REFRESH_TOKEN= TWINGATE_TIMESTAMP_FORMAT=2 TWINGATE_LABEL_DEPLOYED_BY=azure \
  --registry-username DockerHubUsername \
  --registry-password "dockerhub-password-or-PAT" \
  --registry-login-server index.docker.io
```

### Docker — Automated Script
```bash
curl -s https://binaries.twingate.com/connector/docker-upgrade.sh | sudo nohup sudo bash
```
Handles: pull latest → compare → stop outdated → restart with same env vars.

### Docker — Watchtower (Auto-update)
```bash
# All containers
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock nicholas-fedor/watchtower:latest --cleanup

# Connector only (add label to connector run command first)
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock nicholas-fedor/watchtower:latest --label-enable=true
```
Add to connector: `--label com.centurylinklabs.watchtower.enable=true`

### Docker — Manual (tokens NOT preserved)
```bash
docker ps
docker container rm -f [container ID or name]
docker image rm -f twingate/connector
# Reprovision in Admin Console, then run new docker run command
```

## Configuration Values
| Variable | Purpose |
|---|---|
| `TWINGATE_NETWORK` | Network name |
| `TWINGATE_ACCESS_TOKEN` | Auth token |
| `TWINGATE_REFRESH_TOKEN` | Refresh token |
| `TWINGATE_TIMESTAMP_FORMAT` | Log timestamp format |
| `TWINGATE_LABEL_DEPLOYED_BY` | Deployment label |

## Gotchas
- **Azure**: SSO Docker Hub accounts (Google/GitHub) must use a PAT, not password
- **Azure**: `--registry-password` value must be in double quotes
- **ECS**: Non-`1`/`latest` image tags won't pull the actual latest
- **Manual Docker**: Loses auth tokens; must reprovision connector in Admin Console
- **Watchtower**: Not recommended for production; original project archived, use `nicholas-fedor/watchtower` fork

## Related Docs
- Upgrading Connectors (best practices)
- Linux Docker Deployment
- Connector Release Notes
- Azure KB article for Docker Hub credentials