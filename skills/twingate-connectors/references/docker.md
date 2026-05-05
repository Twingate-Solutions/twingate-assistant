## Upgrade Docker/ECS/Azure Connectors

Specific instructions for updating Twingate Connectors deployed as Docker containers (Linux Docker, AWS ECS, Azure Container Instances).

**AWS ECS — Force New Deployment:**
- Management Console: ECS cluster → select Connector service → Update → Force new deployment → Skip to review → Update Service
- AWS CLI: `aws ecs update-service --region <REGION> --cluster <CLUSTER_NAME> --service <SERVICE_NAME> --force-new-deployment`
- Gotcha: if task definition image tag was changed from `1` or `latest`, the pulled image may not be latest

**Azure Container Instance:**
- Container restart command no longer works for upgrades (Docker Hub rate limiting + Azure CLI changes)
- Must destroy old container and redeploy with `az container create` using Docker Hub credentials
- Include `--registry-username`, `--registry-password "..."`, `--registry-login-server index.docker.io`
- If signing into Docker Hub via SSO (Google/GitHub): use a Personal Access Token instead of a password

**Docker (Linux host):**
- Check current version: `docker exec twingate-connector ./connectord --version`
- Automated upgrade script (preserves env vars): `curl -s https://binaries.twingate.com/connector/docker-upgrade.sh | sudo nohup sudo bash`
  - Pulls latest `twingate/connector:1`, compares, stops/removes outdated containers, restarts with same env vars
- Watchtower (automated, non-production): use `nicholas-fedor/watchtower:latest` fork; add label `com.centurylinklabs.watchtower.enable=true` to enable per-container control
- Manual upgrade (requires reprovisioning tokens): `docker container rm -f <container>`, `docker image rm -f twingate/connector`, then deploy new `docker run` command from Admin Console

**Gotchas:**
- Manual Docker upgrade does NOT preserve tokens — requires reprovisioning in Admin Console
- Automated script and Watchtower DO preserve tokens

**Related Docs:**
- /docs/upgrading-connectors -- General upgrade best practices
- /docs/connectors-on-linux -- Docker deployment reference
