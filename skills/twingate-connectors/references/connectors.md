---
source: https://www.twingate.com/docs/connectors
type: docs
fetched: 2026-08-14
source_version: a6659b294fc234210ad13ad820ae739d5c5d1c5e9b8d4ea01a4ff18b6f885e67
---

# Twingate Connectors Overview

## Summary
Connectors are Twingate components deployed behind your firewall to enable access to private Resources. They run as containers or Linux systemd services and can be deployed across multiple environments via admin console scripts.

## Key Information
- Connectors run as either a **container** or **Linux systemd service**
- Admin console provides ready-made deployment scripts for all supported environments
- Admins receive email notifications when a Connector goes offline/comes back online
- Connector names are randomly generated on creation but can be edited

## Supported Deployment Environments
- Docker
- Kubernetes (via Helm Chart)
- Azure (Container Instance)
- Linux (generic systemd script)
- AWS ECS Fargate
- AWS AMI

## Prerequisites
- Access to Twingate Admin Console
- Appropriate infrastructure for target deployment environment
- For Windows: Linux VM via Hyper-V (Docker on Windows not supported)

## Configuration Values
- **Connector names**: Must be unique across all Connectors in the account
- **Status emails**: Configurable per-Connector in Admin Console

## Gotchas
- **Docker on Windows is not recommended** due to a known Docker issue — use a Linux VM via Hyper-V instead
- Renaming a Connector in the Admin Console **does not rename it in your deployment environment** — rename before deployment if custom naming is needed
- Connector names must be **globally unique** within your account

## Step-by-Step (High Level)
1. Navigate to Admin Console
2. Select target deployment environment
3. Copy/run the generated deployment script
4. (Optional) Rename Connector before deployment if custom name is needed
5. Configure status email notifications per Connector as needed

## Related Docs
- First-time configuration guide (Connector deployment in Admin Console)
- Connector Management section (detailed deployment and management)
- "How Twingate Works" architecture article