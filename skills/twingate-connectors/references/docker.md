# How to Upgrade Containerized Twingate Connectors

## Summary
Covers upgrading Twingate Connectors running in Docker, AWS ECS, and Azure Container Instances. Methods range from automated scripts to manual container replacement. Azure requires full container destruction and recreation due to Docker Hub rate limiting.

## Key Information
- Image tag `1` or `latest` ensures you always pull the most recent version
- Check running connector version: `docker exec twingate-connector ./connectord --version`
- Release notes available in Connector Release Notes documentation
- Watchtower is **not recommended for production systems**

## Prerequisites
- Running Twingate Connector container(s)
- For Azure: Free Docker Hub account (username + password or PAT)
- AWS CLI configured with appropriate permissions (for ECS CLI method)

---

## Step-by-Step by Environment

### AWS ECS — Console
1. Select running Connector service in ECS cluster → **Update**
2. Check **Force new deployment** → **Skip to review**
3. Click **Update Service** (auto-pulls latest image)

### AWS ECS — CLI
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
  --registry-username DockerHubUsername \
  --registry-password "dockerhub-password-or-PAT" \
  --registry-login-server index.docker.io
```

### Docker — Automated Script
```bash
curl -s https://binaries.twingate.com/connector/docker-upgrade.sh | sudo nohup sudo bash
```
Automatically: pulls latest image, compares running containers, stops/deletes outdated ones, restarts with same env vars.

### Docker — Watchtower (Auto-update)
```bash
# Update all containers
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock \
  nicholas-fedor/watchtower:latest --cleanup

# Update only labeled containers
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock \
  nicholas-fedor/watchtower:latest --label-enable=true
```
Add label to connector: `--label com.centurylinklabs.watchtower.enable=true`

### Docker — Manual (requires reprovisioning)
```bash
docker ps
docker container rm -f [container ID or name]
docker image rm -f twingate/connector
# Get new run command from Admin Console after reprovisioning
```

---

## Configuration Values
| Parameter | Notes |
|---|---|
| `twingate/connector:1` | Recommended image tag |
| `TWINGATE_NETWORK` | Network name (quoted) |
| `TWINGATE_ACCESS_TOKEN` | Auth token |
| `TWINGATE_REFRESH_TOKEN` | Refresh token |
| `--registry-password` | Must use double quotes in Azure CLI |

## Gotchas
- **Azure**: `az container restart` no longer works for upgrades — must recreate
- **Azure SSO users**: Must use PAT instead of password for Docker Hub auth
- **Manual Docker upgrade**: Destroys auth tokens — must reprovision connector in Admin Console
- **ECS**: Non-`latest`/`1` image tags won't auto-pull newest version
- **Watchtower**: Original project archived; use `nicholas-fedor/watchtower` fork

## Related Docs
- Linux Docker Deployment
- Upgrading Connectors (best practices for avoiding downtime)
- Connector Release Notes
- Twingate KB article for Azure deployment with Docker