# Twingate Connectors Overview

## Summary
Connectors are Twingate components deployed behind your firewall to provide access to private Resources. They run as containers or Linux systemd services and are managed through the Twingate admin console.

## Key Information
- Connectors bridge internal network resources to Twingate's access control layer
- Run as container or Linux `systemd` service
- Admin console provides ready-made deployment scripts for supported environments
- Admins receive email notifications when Connectors go offline/online

## Supported Deployment Environments
- Docker
- Kubernetes (via Helm Chart)
- Azure (via ContainerInstance)
- Linux (generic `systemd` deployment script)
- AWS ECS Fargate
- AWS AMI

## Connector Names
- Auto-generated randomly on creation
- Editable at any time; must be **unique** across all Connectors in the account
- Renaming in Admin console does **not** rename in deployment environment
- Recommended: rename Connectors in Admin console **before** deployment if custom names are needed

## Gotchas
- **Do not deploy Connectors via Docker on Microsoft Windows** — known Docker issue causes problems
- Windows recommendation: deploy inside a Linux VM using Hyper-V instead
- Name changes in Admin console are decoupled from deployment environment names — manual sync required

## Notifications
- Status availability emails sent to admins on Connector offline/online events
- Can be disabled per-Connector in settings

## Related Docs
- [First-time configuration guide] — Connector deployment in Admin console
- [Connector Management section] — detailed deployment and management
- [How Twingate Works] — architectural details
- [Architecture section] — general system design