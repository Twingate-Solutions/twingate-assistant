# How to Upgrade Containerized Twingate Connectors

## Summary
Covers upgrading Twingate Connectors running in Docker, AWS ECS, and Azure Container Instances. Methods range from automated scripts to manual container replacement. Avoid downtime by following best practices from the Upgrading Connectors guide.

## Key Information
- Image tag `1` or `latest` ensures you always pull the newest version
- Docker upgrade script automates pull, comparison, stop, delete, and restart while preserving env vars
- Azure Container Instances cannot be restarted to upgrade — must destroy and recreate
- Watchtower is **not recommended for production systems**

## Prerequisites
- Running Twingate Connector container(s)
- For Azure: Free Docker Hub account (username + password or PAT)
- For manual Docker: Access to Twingate Admin Console to reprovision

---

## Step-by-Step by Environment

### AWS ECS (Console)
1. Select running Connector service in ECS cluster → **Update**
2. Check **Force new deployment** → **Skip to review**
3. Click **Update Service** — pulls latest image automatically

### AWS ECS (CLI)
```bash
aws ecs update-service --region <REGION> --cluster <CLUSTER_NAME> --service <SERVICE_NAME> --force-new-deployment
```

### Azure Container Instance
Must destroy old container and recreate:
```bash
az container create --name twingate-connector-name --image twingate/connector:1 \
  --resource-group RSG-here --vnet VNet-here --subnet Subnet-here \
  --cpu 1 --memory 2 --os-type Linux \
  --environment-variables TWINGATE_NETWORK="your-network" \
    TWINGATE_ACCESS_TOKEN= TWINGATE_REFRESH_TOKEN= \
    TWINGATE_TIMESTAMP_FORMAT=2 TWINGATE_LABEL_DEPLOYED_BY=azure \
  --registry-username DockerHubUsername \
  --registry-password "dockerhub-password-or-PAT" \
  --registry-login-server index.docker.io
```

### Docker (Automated Script)
```bash
curl -s https://binaries.twingate.com/connector/docker-upgrade.sh | sudo nohup sudo bash
```

### Docker (Manual — tokens NOT preserved, reprovision required)
```bash
docker ps
docker container rm -f [container ID or name]
docker image rm -f twingate/connector
# Get new run command from Admin Console after reprovisioning
docker run ...
```

### Check Current Version
```bash
docker exec twingate-connector ./connectord --version
```

---

## Configuration Values

| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Your Twingate network name |
| `TWINGATE_ACCESS_TOKEN` | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token |
| `TWINGATE_TIMESTAMP_FORMAT` | Set to `2` for Azure |
| `TWINGATE_LABEL_DEPLOYED_BY` | Deployment label (e.g., `azure`) |

**Watchtower label:** `com.centurylinklabs.watchtower.enable=true`

---

## Gotchas
- Azure: `--registry-password` value **must be in double quotes**; SSO Docker Hub logins (Google/GitHub) require a PAT instead of password
- ECS: If task definition image tag is not `1` or `latest`, upgrade may not pull newest image
- Manual Docker upgrade: **destroys auth tokens** — must reprovision in Admin Console
- Watchtower: Original project archived; use fork `nicholas-fedor/watchtower`

---

## Related Docs
- Upgrading Connectors (best practices)
- Linux Docker Deployment
- Connector Release Notes
- Twingate KB: Azure deployment with Docker Hub credentials