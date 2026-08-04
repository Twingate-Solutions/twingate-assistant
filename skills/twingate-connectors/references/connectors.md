# Twingate Connectors Overview

## Summary
Connectors are Twingate components deployed behind your firewall to enable access to private Resources. They run as containers or Linux systemd services and can be deployed across multiple environments using admin console deployment scripts.

## Key Information
- Connectors run as either a **container** or **Linux systemd service**
- Admin console provides ready-made deployment scripts for all supported environments
- Connector names are randomly generated on creation but are editable
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
- Access to Twingate Admin console
- Target deployment environment provisioned
- For Windows: Linux VM via Hyper-V (Docker on Windows not supported)

## Gotchas
- **Do not deploy via Docker on Microsoft Windows** — known Docker issue makes this unsupported
- Windows recommended path: deploy inside a Linux VM using Hyper-V
- Renaming a Connector in the Admin console **does NOT rename it in your deployment environment** — rename before deployment if custom naming is needed
- Connector names must be globally unique within your account

## Configuration Notes
- Status availability emails are enabled by default; can be disabled per-Connector in settings
- Rename Connectors **before** deployment if you want the deployment environment name to match

## Related Docs
- First-time configuration guide (Admin console deployment)
- Connector Management section (detailed deployment and management)
- How Twingate Works (architecture deep-dive)
- Twingate Architecture section