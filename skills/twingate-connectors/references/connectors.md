# Twingate Connectors Overview

## Summary
Connectors are Twingate components deployed behind your firewall to provide access to private Resources. They run as containers or Linux systemd services and are managed through the Twingate admin console.

## Key Information
- Connectors act as the bridge between Twingate's network and your private resources
- Run as either a **container** or **Linux systemd service**
- Admin console provides ready-made deployment scripts for all supported environments
- Connector names are randomly generated at creation but can be edited (must be unique across account)
- Admins receive email notifications when Connectors go offline/come back online

## Supported Deployment Environments
- Docker
- Kubernetes (via Helm Chart)
- Azure (via ContainerInstance)
- Linux (generic systemd)
- AWS ECS Fargate
- AWS AMI

## Prerequisites
- Access to Twingate Admin Console
- Target deployment environment (one of the supported platforms above)
- For Windows: Linux VM via Hyper-V (Docker on Windows is not supported)

## Configuration Notes
- Rename Connectors in the admin console **before** deployment if you want custom names — renaming in the console does not update the name in the deployment environment
- Status availability emails can be toggled per-Connector in admin settings

## Gotchas
- **Do not deploy Connectors via Docker on Microsoft Windows** — known Docker issue makes this unreliable; use a Linux VM with Hyper-V instead
- Renaming a Connector in the admin console is decoupled from the deployment environment name — they are not synced
- Connector names must be unique across all Connectors in the account

## Related Docs
- First-time configuration guide (Connector deployment in Admin console)
- Connector Management section (detailed deployment and management)
- How Twingate Works (architecture deep-dive)
- General Architecture section