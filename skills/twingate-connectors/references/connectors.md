# Twingate Connectors Overview

## Summary
Connectors are Twingate components deployed behind your firewall to enable access to private Resources. They run as containers or Linux systemd services and can be deployed across multiple environments via admin console deployment scripts.

## Key Information
- Connectors operate as either a **container** or **Linux systemd service**
- Admin console provides ready-made deployment scripts for all supported environments
- Connector names are randomly generated at creation but can be edited (must be unique across account)
- Admins receive email notifications when Connectors go offline/come back online (configurable)

## Supported Deployment Environments
- Docker
- Kubernetes (Helm Chart)
- Azure Container Instance
- Linux (generic systemd)
- AWS ECS Fargate
- AWS AMI

## Prerequisites
- Access to Twingate Admin console
- Target deployment environment provisioned
- Network access behind the firewall where Resources reside

## Gotchas
- **Do not deploy via Docker on Microsoft Windows** — known Docker issue makes this unreliable
  - Recommended Windows alternative: Linux VM using Hyper-V
- Renaming a Connector in the Admin console **does not** rename it in the deployment environment — rename before deployment if custom naming is needed
- Connector names must be **unique across all Connectors** in the account

## Configuration Notes
- Status availability emails are enabled by default; disable per-Connector in settings
- No environment variables or CLI flags documented on this page — see Connector Management section for details

## Related Docs
- [First-time Configuration Guide](https://www.twingate.com/docs) — Admin console deployment walkthrough
- [Connector Management](https://www.twingate.com/docs/connector-management) — Detailed deployment and management
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works) — Architecture deep dive