---
source: https://www.twingate.com/docs/docker
type: docs
fetched: 2026-11-13
source_version: a01a6ba661bd80a6126078e2d541627d36a97fcc014018945e0c55c5bda9c9e6
trust: official
---

# How to Upgrade Containerized Connectors (AWS/Azure/Docker)

## Summary
Covers upgrading Twingate Connectors deployed as containers on AWS ECS, Azure Container Instances, and Docker hosts. Each environment has a different upgrade mechanism. Follow the best practices in "Upgrading Connectors" to avoid user downtime.

## Key Information
- **AWS ECS:** Upgrade by forcing a new deployment, which restarts the service and pulls the latest image.
- **Azure Container Instances:** Restart no longer works for upgrades because of Docker Hub rate limiting and `az` CLI restart changes. Destroy the old Connector and recreate it with `az container create`, passing Docker Hub credentials.
- **Docker:** Options are the upgrade script, Watchtower, or a manual remove and re-provision.
- Latest image tag: `twingate/connector:1`.
- Release notes are in the Connector Release Notes.

## Prerequisites
- ECS: service name, cluster name, and AWS region.
- Azure: a free Docker Hub account (username plus password or personal access token), resource group, VNet, subnet, and Connector tokens.
- Docker: access to the host and the Connector container name.

## Step-by-Step

**ECS (Console):** Select the service, then Update, then "Force new deployment", then Skip to review, then Update Service.

**ECS (CLI):**
`aws ecs update-service --region <REGION> --cluster <CLUSTER_NAME> --service <SERVICE_NAME> --force-new-deployment`

**Azure:** Delete the old container, then run `az container create` with `--image twingate/connector:1`, the Twingate environment variables, `--registry-username`, `--registry-password "<password>"`, and `--registry-login-server index.docker.io`.

**Docker, check version:** `docker exec twingate-connector ./connectord --version`

**Docker, upgrade script:** The page provides a script at `binaries.twingate.com/connector/docker-upgrade.sh`. It pulls the latest image, compares running containers, and recreates outdated ones with the same environment variables. See the source page for the exact invocation.

**Docker, Watchtower:**
- Update all containers: `docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock nicholas-fedor/watchtower:latest --cleanup`
- Limit to labeled containers: use `--label-enable=true` instead of `--cleanup`, and add `--label com.centurylinklabs.watchtower.enable=true` to the Connector's `docker run` command.

**Docker, manual:**
1. `docker ps` and copy the container ID or name.
2. `docker container rm -f <id|name>`
3. `docker image rm -f twingate/connector`
4. Reprovision the Connector in the Admin Console and run the new `docker run` command.

## Configuration Values
- Env vars: `TWINGATE_NETWORK`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`, `TWINGATE_TIMESTAMP_FORMAT=2`, `TWINGATE_LABEL_DEPLOYED_BY=azure`, `TWINGATE_LABEL_HOSTNAME`
- Docker run flags: `--sysctl net.ipv4.ping_group_range="0 2147483647"`, `--restart=unless-stopped`, `--pull=always`
- Azure flags: `--registry-username`, `--registry-password`, `--registry-login-server index.docker.io`
- Watchtower label: `com.centurylinklabs.watchtower.enable=true`

## Gotchas
- ECS: if the task definition image tag is not `1` or `latest`, the pulled image may not be the newest.
- Azure: the password must be in double quotes and the username unquoted. If you use SSO (Google or GitHub) for Docker Hub, you must use a PAT.
- Watchtower is not meant for critical production systems. The original project is archived, and the examples use the `nicholas-fedor` fork. Kubernetes or similar tooling is recommended instead.
- The manual Docker method does not preserve tokens, so you must reprovision the Connector.
- Without the label option, Watchtower updates all containers on the host.

## Related Docs
- Upgrading Connectors (best practices)
- Linux Docker deployment
- Connector Release Notes
- Twingate Knowledge Base article on Azure Connector deployment