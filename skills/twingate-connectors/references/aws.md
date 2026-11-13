---
source: https://www.twingate.com/docs/aws
type: docs
fetched: 2026-11-13
source_version: 6da1f0a7723664e6f6b9b0d4ef9dc21f38b393ba3010cca12c615e34e681df3d
trust: official
---

# How to Deploy a Connector on AWS

## Summary
Twingate Connectors can be deployed on AWS via CloudFormation, EC2 (Docker or systemd), a prebuilt Ubuntu AMI, ECS Fargate, EKS (Helm), or IaC tools. Most methods start from the Connector deployment page in the Admin Console, which generates tokens and ready-to-run commands.

## Key Information
- **CloudFormation (easiest):** Admin Console → Remote Networks → select network → Add Connector → choose **AWS Quick Start** → pick region (usually same as Resources) → **Open AWS** → select SSH key and Subnet ID → **Create stack**. Connector is live in a few minutes.
- **EC2:** Follow the general Linux Connector instructions. Docker works on any 64-bit Linux distro Docker supports. The systemd service is supported on Ubuntu, Fedora, Debian, and CentOS.
- **AMI:** Ubuntu x86 image with the Connector systemd service preinstalled. Includes AWS SSM Agent for remote shell access (requires IAM roles and Systems Manager setup).
- **ECS Fargate:** Prebuilt container with the Connector service.
- **EKS:** Use the official Twingate Helm chart (see the Kubernetes Best Practices Guide).
- **IaC:** Terraform, Pulumi, or the Twingate API.

## Prerequisites
- Twingate Admin Console access and a Remote Network
- Subnet with **outbound Internet access** (to pull the Connector image and reach Twingate)
- AWS account/CLI access (for AMI and ECS flows)
- Optional: peer-to-peer connectivity support, to improve user experience and stay within the Fair Use Policy

## Step-by-Step (AMI / ECS)
1. Admin Console → Remote Networks → select network → **Add Connector**.
2. Open the new Connector and choose the **AMI** or **ECS** tab.
3. Step 2: **Generate tokens** (re-authentication required).
4. Step 3: Enter AWS environment details and optional features.
5. AMI: Step 4, select your CLI environment, copy the generated command, and run it.
6. ECS: Step 4, copy and run the task definition command in the AWS CLI. Step 5, copy and run the launch command.

## Configuration Values
- `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`: Connector tokens, unique per Connector.
- ECS ping support: add to `containerDefinitions` in the task definition:
  ```json
  "systemControls": [
    { "namespace": "net.ipv4.ping_group_range", "value": "0 2147483647" }
  ]
  ```

## Gotchas
- **Tokens in user-data:** The AMI deployment script embeds both tokens in EC2 user-data, readable in plain text by any AWS user with EC2 viewer permissions. For production, store tokens in **AWS Secrets Manager** and retrieve them at runtime.
- **Don't reuse tokens:** Create a separate ECS task definition for each Connector instance.
- Without the `systemControls` setting, pinging Resources through an ECS Fargate Connector won't work.
- Stagger updates across multiple Connectors to avoid downtime.

## Updating
- **systemd (EC2/AMI):** Update manually via the Linux package manager, or automate with a scheduled task.
- **ECS Fargate:** Upgrade through the AWS console or CLI.

## Related Docs
- Best Practices for Connectors (including EC2 hardware recommendations)
- Linux Connector deployment
- Peer-to-peer connections
- Kubernetes Best Practices Guide
- Systemd Connector Update Guide
- ECS Connector Update Guide
- Terraform, Pulumi, and Twingate API docs
- AWS Systems Manager user guide