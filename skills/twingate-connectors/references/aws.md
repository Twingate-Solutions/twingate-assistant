# Deploy a Connector on AWS

## Summary
Twingate supports multiple AWS deployment methods for Connectors: CloudFormation, EC2 (Linux), AMI, ECS Fargate, and EKS. Each method is configured through the Admin Console under Remote Networks → Add Connector. Subnets must have outbound internet access.

## Key Information
- Subnet requires outbound internet access to download container image and connect to Twingate
- Peer-to-peer connections recommended to improve performance and stay within Fair Use Policy
- Connector tokens are instance-specific — never reuse tokens across Connector instances
- Remote shell access for AMI instances available via pre-installed AWS SSM Agent

## Prerequisites
- Access to Twingate Admin Console
- AWS account with appropriate IAM permissions
- Remote Network already created in Twingate
- Subnet with outbound internet access

## Deployment Methods

### CloudFormation (Easiest)
1. Admin Console → Remote Networks → Select network → Add Connector
2. Click new Connector → Choose **AWS Quick Start** deployment
3. Select AWS region → Click **Open AWS**
4. Select SSH key and Subnet ID → Click **Create stack**
5. Connector live within ~few minutes

### EC2
- Follow standard Linux Connector deployment instructions
- Docker: any 64-bit Linux with Docker support
- systemd service: Ubuntu, Fedora, Debian, CentOS only

### AMI (Ubuntu x86, systemd pre-installed)
1. Add Connector → Select **AMI** option
2. Generate tokens (requires re-authentication)
3. Fill in AWS environment details and optional features
4. Select CLI environment, copy and run generated command
- Remote access via AWS SSM Agent (requires IAM role assignment)

### ECS Fargate
1. Add Connector → Select **ECS** option
2. Generate tokens
3. Fill in AWS environment configuration
4. Run task definition creation command via AWS CLI
5. Run Connector launch command via AWS CLI

**Ping support** — Add to `containerDefinitions` in task definition:
```json
"systemControls": [{
  "namespace": "net.ipv4.ping_group_range",
  "value": "0 2147483647"
}]
```

### EKS
- Use official Twingate Helm chart
- See Kubernetes Best Practices Guide

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| `net.ipv4.ping_group_range` | `0 2147483647` — required for ICMP ping in ECS |
| SSH Key | Required for CloudFormation |
| Subnet ID | Required for CloudFormation; must have outbound internet |

## Updating Connectors
- **systemd (EC2/AMI):** Manual via Linux package manager or scheduled update task; stagger updates across instances
- **ECS Fargate:** Via AWS management console or CLI
- See separate update guides for each method

## Gotchas
- Do not reuse Connector tokens — create separate task definitions per Connector instance
- Subnet must have outbound internet access or deployment will fail
- systemd service only supported on Ubuntu, Fedora, Debian, CentOS (not all Linux distros)
- ECS ping requires explicit `systemControls` sysctl configuration

## Related Docs
- Connector Best Practices (hardware sizing, general recommendations)
- Linux Connector Deployment
- Kubernetes Best Practices Guide
- Terraform / Pulumi / Twingate API (IaC deployment)
- Systemd Connector Update Guide
- ECS Connector Update Guide
- AWS Systems Manager User Guide (SSM/IAM setup)