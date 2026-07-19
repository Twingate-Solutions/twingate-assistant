# Twingate Connectors Overview

## Summary
Connectors are Twingate components deployed behind your firewall to enable access to private Resources. They run as containers or Linux systemd services and can be deployed across multiple environments using admin console deployment scripts.

## Key Information
- Connectors run as either a **container** or **Linux systemd service**
- Admin console provides ready-made deployment scripts for supported environments
- Connector names are randomly generated at creation but can be edited (must be unique across account)
- Admins receive email notifications when Connectors go offline/come back online
- Name changes in Admin console do **not** propagate to the deployment environment

## Supported Deployment Environments
- Docker
- Kubernetes (via Helm Chart)
- Azure (via ContainerInstance)
- Linux (generic systemd script)
- AWS ECS Fargate
- AWS AMI

## Prerequisites
- Access to Twingate Admin console
- Target deployment environment provisioned
- For Windows: Linux VM via Hyper-V (Docker on Windows not supported)

## Configuration Notes
- Rename Connectors in Admin console **before** deployment if custom naming is needed
- Status availability email notifications can be disabled per-Connector in Admin console

## Gotchas
- **Docker on Windows is explicitly unsupported** due to a known Docker issue — use a Linux VM via Hyper-V instead
- Renaming a Connector in the Admin console does not update the name in the deployment environment; set names before deploying to avoid mismatch
- Connector names must be globally unique across your entire Twingate account

## Related Docs
- First-time configuration guide (Admin console deployment)
- Connector Management section (detailed deployment and management)
- How Twingate Works (architecture overview)
- Twingate Architecture section