---
source: https://www.twingate.com/docs/connectors
type: docs
fetched: 2026-11-13
source_version: 27b70328f5d4531a72797635fc2a8e8b2557f2e8db945108ef1e9f4d2b435cee
trust: official
---

# Page Title
Connectors (Twingate Docs overview)

## Summary
Connectors are Twingate components deployed behind your firewall to provide access to private Resources. They run as a container or a Linux `systemd` service. The Admin Console generates ready-made deployment scripts for several environments.

## Key Information
- Supported deployment targets with Admin Console scripts:
  - Docker
  - Kubernetes (via Helm Chart)
  - Azure (ContainerInstance)
  - Linux (generic `systemd` script)
  - AWS ECS Fargate
  - AWS AMI
- Connector names are randomly generated at creation and can be edited at any time.
- Names must be unique across all Connectors in the account.
- Renaming in the Admin Console does not change the name in the deployment environment.
- Admins receive an email when a Connector goes offline and again when it returns online. Status emails can be turned off per Connector.

## Prerequisites
- A Twingate account with Admin Console access.
- An environment behind the firewall that can reach the private Resources (for example, a Docker host, Kubernetes cluster, or Linux VM).

## Step-by-Step
Not covered on this page. Deployment is done through the Admin Console, which generates scripts per environment (see the first-time configuration guide and the "Understanding Connectors" section).

For custom names on deployed Connectors, rename the Connector in the Admin Console **before** deploying.

## Configuration Values
None listed on this page (no env vars, CLI flags, or API parameters).

## Gotchas
- Avoid deploying Connectors via Docker on Microsoft Windows because of a known Docker issue.
- Recommended on Windows: run the Connector inside a Linux VM using Hyper-V.
- Renaming a Connector in the Admin Console does not rename it in the deployment environment, so rename before deploying if you want a custom name.
- Name uniqueness is enforced across all Connectors in the account.
- Online/offline emails go to admins by default, so disable status emails per Connector if they are noisy.

## Related Docs
- First-time configuration guide (Connector deployment in the Admin Console)
- Understanding Connectors section (detailed deployment and management)
- How Twingate Works
- Architecture section