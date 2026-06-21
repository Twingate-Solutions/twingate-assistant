# Twingate Connectors Overview

## Summary
Connectors are Twingate components deployed behind your firewall to provide access to private Resources. They run as containers or Linux systemd services and are managed via the Twingate Admin console.

## Key Information
- Connectors run as either a **container** or **Linux systemd service**
- Admin console provides ready-made deployment scripts for all supported environments
- Connector names are randomly generated at creation but can be edited (must be unique across account)
- Admins receive email notifications when Connectors go offline/come back online

## Supported Deployment Environments
- Docker
- Kubernetes (via Helm Chart)
- Azure (via ContainerInstance)
- Linux (generic systemd deployment script)
- AWS ECS Fargate
- AWS AMI

## Gotchas
- **Windows + Docker**: Not recommended due to a known Docker issue. Use a Linux VM via Hyper-V instead
- **Connector naming**: Renaming a Connector in the Admin console does **not** update the name in your deployment environment. Rename before deployment if custom names are needed
- Connector names must be unique across all Connectors in your account

## Configuration Notes
- Status availability emails are enabled by default; must be explicitly disabled per Connector in settings
- Rename Connectors in Admin console **before** deploying if you want the deployment environment name to match

## Prerequisites
- Access to Twingate Admin console
- Appropriate infrastructure for chosen deployment method (Docker, K8s, AWS, Azure, or Linux)

## Related Docs
- First-time configuration guide (Connector deployment in Admin console)
- Connector Management section (detailed deployment and management)
- How Twingate Works (architecture overview)