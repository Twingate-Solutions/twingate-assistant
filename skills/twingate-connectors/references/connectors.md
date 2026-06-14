# Twingate Connectors Overview

## Summary
Connectors are Twingate components deployed behind your firewall to enable access to private Resources. They run as containers or Linux systemd services and can be deployed across multiple environments via admin console scripts.

## Key Information
- Connectors run as a **container** or **Linux systemd service**
- Admin console provides ready-made deployment scripts for all supported environments
- Connector names are randomly generated at creation but are editable
- Names must be **unique across all Connectors** in your account
- Admins receive email notifications when a Connector goes offline/comes back online

## Supported Deployment Environments
- Docker
- Kubernetes (via Helm Chart)
- Azure (via ContainerInstance)
- Linux (generic systemd)
- AWS ECS Fargate
- AWS AMI

## Prerequisites
- Access to Twingate Admin Console
- Target deployment environment provisioned
- Admin role to receive status emails and manage Connectors

## Gotchas
- **Do not use Docker on Microsoft Windows** — known Docker issue makes this unsupported
  - Recommended alternative: deploy inside a Linux VM using Hyper-V on Windows
- Renaming a Connector in the Admin Console **does not rename it in the deployment environment** — rename before deployment if custom naming is needed
- Connector names must be unique account-wide; duplicate names will cause conflicts

## Configuration Notes
- No specific env vars or CLI flags documented on this page
- Deployment scripts are generated via the Admin Console (see first-time configuration guide)
- Status availability emails can be disabled per-Connector in settings

## Related Docs
- [First-time Configuration Guide] — Connector deployment in Admin Console
- [Connector Management Section] — detailed deployment and management
- [How Twingate Works] — architectural deep dive
- [Architecture Section] — general system architecture