# Twingate Connectors Overview

## Summary
Connectors are Twingate components deployed behind your firewall to enable access to private Resources. They run as containers or Linux systemd services and can be deployed across multiple environments via admin console deployment scripts.

## Key Information
- Connectors run as either a **container** or **Linux systemd service**
- Admin console provides ready-made deployment scripts for supported environments
- Connector names are randomly generated at creation but editable
- Admins receive email notifications when Connectors go offline/online

## Supported Deployment Environments
- Docker
- Kubernetes (via Helm Chart)
- Azure (via ContainerInstance)
- Linux (generic systemd)
- AWS ECS Fargate
- AWS AMI

## Prerequisites
- Access to Twingate Admin console
- Target deployment environment provisioned
- Network access behind firewall where Resources reside

## Connector Names
- Auto-generated on creation
- Must be **unique across all Connectors** in the account
- Renaming in Admin console does **not** rename in deployment environment
- Recommended: rename before deployment if custom names are needed

## Gotchas
- **Do not use Docker on Microsoft Windows** — known Docker issue makes this unsupported
- Windows deployment: use Linux VM via Hyper-V instead
- Admin console name changes are cosmetic only; deployment environment name is independent
- Status notification emails are on by default; must be manually disabled per Connector if unwanted

## Configuration Values
- No direct env vars or CLI flags documented on this page (see Connector Management docs for deployment-specific config)

## Related Docs
- First-time configuration guide (Admin console deployment)
- Connector Management section (detailed deployment/management)
- How Twingate Works (architecture deep-dive)
- Architecture section (general overview)