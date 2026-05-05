## Connector Health Checks

How to check whether the Twingate Connector service is running correctly. Health checks verify the service process only — not network connectivity to Twingate infrastructure.

**Health Check Responses:**
- Returns `OK` with exit code `0` = healthy
- Any other response or nonzero exit code = unhealthy

**How to Run:**
- **systemd:** `twingate-connectorctl health`
- **Docker:** health check is built into the container image; visible in `docker ps` under Status
  - More detail: `docker inspect --format "{{json .State.Health }}" <container-name>`
- **Non-Docker containers (e.g., ECS):** run `connectorctl health` inside the container; ECS natively supports Docker image health check definitions (no additional config needed)

**Automated Actions:**
- Override the Dockerfile `HEALTHCHECK` directive to trigger custom actions on health check failure
- Or use your orchestration service's equivalent health check mechanism

**Related Docs:**
- /docs/connector-details -- Runtime metadata and status info
- /docs/advanced-connector-management -- Advanced Connector features index
