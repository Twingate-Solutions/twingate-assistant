# Twingate Connectors Overview

## Summary
Connectors are Twingate components deployed behind your firewall to enable access to private Resources. They run as containers or Linux systemd services and can be deployed across multiple environments via admin console deployment scripts.

## Key Information
- Connectors run as either a **container** or **Linux systemd service**
- Admin console provides ready-made deployment scripts for all supported environments
- Connector names are randomly generated at creation but can be edited (must be unique across all Connectors in account)
- Admins receive email notifications when Connectors go offline/come back online (can be disabled per Connector)

## Supported Deployment Environments
- Docker
- Kubernetes (via Helm Chart)
- Azure (via ContainerInstance)
- Linux (generic systemd deployment script)
- AWS ECS Fargate
- AWS AMI

## Prerequisites
- Access to Twingate Admin Console
- Appropriate infrastructure for chosen deployment environment
- For Windows: Linux VM via Hyper-V (Docker on Windows not supported)

## Gotchas
- **Windows + Docker**: Deploying Connectors via Docker on Microsoft Windows is unsupported due to a known Docker issue. Use a Linux VM with Hyper-V instead
- **Connector renaming**: Changing a Connector name in the Admin Console does **not** update the name in your deployment environment — rename before deployment if custom names are needed
- Connector names must be unique across the entire account

## Configuration Notes
- Status availability emails are enabled by default; must be disabled per-Connector individually
- Deployment scripts are generated from the Admin Console (not manually crafted)

## Related Docs
- First-time configuration guide (Connector deployment in Admin Console)
- Connector Management section (detailed deployment and management)
- How Twingate Works (architectural deep dive)
- Architecture section (general overview)