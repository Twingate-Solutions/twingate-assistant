---
source: https://www.twingate.com/docs/connectors
type: docs
fetched: 2026-09-27
source_version: fa630cbd94f04052359d048bbcc90c5618a74c052ffe164cb45cc3d79de9599f
---

# Twingate Connectors Overview

## Summary
Connectors are Twingate components deployed behind your firewall to provide access to private Resources. They run as containers or Linux systemd services and are managed through the Twingate admin console.

## Key Information
- Connectors run as either a **container** or **Linux systemd service**
- Admin console provides ready-made deployment scripts for supported environments
- Connector names are randomly generated at creation but are editable
- Names must be **unique across all Connectors** in your account
- Admins receive email notifications when Connectors go offline/online

## Supported Deployment Environments
- Docker
- Kubernetes (via Helm Chart)
- Azure (via ContainerInstance)
- Linux (generic systemd deployment script)
- AWS ECS Fargate
- AWS AMI

## Prerequisites
- Access to Twingate Admin Console
- Target deployment environment (Docker, K8s, AWS, Azure, or Linux)
- For Windows: Hyper-V with a Linux VM (Docker on Windows not recommended)

## Configuration Values
- Connector names: configurable in Admin Console (must be unique per account)
- Status availability emails: configurable per Connector in Admin Console

## Gotchas
- **Do not deploy Connectors via Docker on Microsoft Windows** — known Docker issue makes this unreliable
- **Windows alternative**: Deploy inside a Linux VM using Hyper-V
- Renaming a Connector in the Admin Console **does not rename it in your deployment environment** — rename before deployment if a custom name is needed
- Connector names must be unique across the entire account

## Step-by-Step
1. Create a Connector in the Admin Console (name is auto-generated)
2. Optionally rename the Connector **before** deployment
3. Use the admin console deployment script for your target environment
4. Deploy using the generated script/config
5. Configure status email notifications per Connector as needed

## Related Docs
- First-time configuration guide (Connector deployment in Admin Console)
- Connector Management section (detailed deployment and management)
- How Twingate Works (architecture deep-dive)
- General Architecture section