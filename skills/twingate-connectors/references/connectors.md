# Twingate Connectors Overview

## Summary
Connectors are Twingate components deployed behind your firewall to enable access to private Resources. They run as containers or Linux systemd services and can be deployed across multiple environments via admin console deployment scripts.

## Key Information
- Connectors operate as either **containers** or **Linux systemd services**
- Admin console provides ready-made deployment scripts for supported environments
- Admins receive email notifications when Connectors go offline/online
- Connector names must be **unique across all Connectors** in your account

## Supported Deployment Environments
- Docker
- Kubernetes (via Helm Chart)
- Azure (via ContainerInstance)
- Linux (generic systemd deployment script)
- AWS ECS Fargate
- AWS AMI

## Prerequisites
- Access to Twingate Admin console
- Target deployment environment (Linux-based recommended)
- Network access to deploy behind firewall

## Gotchas
- **Docker on Windows is not recommended** — known Docker issue causes problems; deploy inside a Linux VM using Hyper-V instead
- **Renaming Connectors**: Changing the name in the Admin console does NOT update the name in your deployment environment — rename before deployment if custom naming is needed
- Connector names must be unique account-wide; randomly generated on creation

## Configuration Notes
- No specific env vars or CLI flags documented on this page
- Deployment scripts are generated via Admin console (environment-specific)
- Status availability emails can be disabled per-Connector in settings

## Related Docs
- First-time configuration guide (Admin console deployment)
- Connector Management section (detailed deployment/management)
- How Twingate Works (architecture overview)
- General Architecture section