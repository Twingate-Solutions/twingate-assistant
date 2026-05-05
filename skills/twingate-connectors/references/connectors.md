## Connectors Overview

Landing page for Twingate Connector documentation. Covers deployment methods, Admin Console behavior, naming, and status notifications.

**Deployment Methods (from Admin Console):**
- Docker
- Kubernetes (via Helm Chart)
- Azure Container Instance
- Linux (generic systemd deployment script)
- AWS ECS Fargate
- AWS AMI
- Docker on Windows (not recommended — use Linux VM via Hyper-V instead)

**Connector Names:**
- Randomly generated on creation; editable at any time
- Names must be unique across all Connectors in the account
- Renaming in Admin Console does not rename in the deployment environment — rename before deploying for consistency

**Status Notifications:**
- Admins receive email when a Connector goes offline and when it comes back online
- Can be disabled per Connector in the Admin Console

**Related Docs:**
- /docs/understanding-connectors -- How Connectors work
- /docs/connector-deployment -- Choosing a deployment method
- /docs/connector-placement-best-practices -- Placement guidance
