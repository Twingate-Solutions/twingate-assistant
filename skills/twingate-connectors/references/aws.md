# Deploy a Connector on AWS

## Summary
Covers multiple deployment methods for Twingate Connectors on AWS: CloudFormation, EC2 (Linux/Docker), AMI, ECS Fargate, and EKS. Each method requires outbound internet access from the subnet and connector tokens generated from the Admin Console.

## Key Information
- Subnet must have outbound internet access (for container image download and Twingate connectivity)
- Peer-to-peer connections recommended to reduce bandwidth and comply with Fair Use Policy
- Connector tokens are instance-specific — never reuse tokens across multiple Connector instances
- AMI is pre-installed with AWS SSM Agent for remote shell access

## Prerequisites
- Twingate Admin Console access
- Remote Network already created in Twingate
- AWS account with permissions to create EC2/ECS/CloudFormation resources
- SSH key pair and Subnet ID (for CloudFormation)
- AWS CLI configured (for AMI/ECS deployments)

## Deployment Methods

### CloudFormation (Easiest)
1. Admin Console → Remote Networks → select network → Add Connector
2. Select new connector → choose **AWS Quick Start** deployment
3. Select AWS region → click **Open AWS**
4. Set SSH key and Subnet ID → click **Create stack**
5. Connector live within a few minutes

### AMI Deployment
1. Admin Console → Remote Networks → Add Connector → select **AMI** option
2. Generate tokens (re-authentication required)
3. Fill in AWS environment details and optional features
4. Select CLI environment → copy and run the generated command

### ECS Fargate Deployment
1. Admin Console → Remote Networks → Add Connector → select **ECS** option
2. Generate tokens
3. Fill in AWS environment configuration
4. Run AWS CLI command to create task definition
5. Run AWS CLI command to launch the Connector

### EKS Deployment
- Use the official Twingate Helm chart
- See Kubernetes Best Practices Guide

## Configuration Values

| Variable | Description |
|---|---|
| `TWINGATE_ACCESS_TOKEN` | Connector access token (generated in Admin Console) |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token (generated in Admin Console) |

**ECS Fargate ping support** — add to `containerDefinitions`:
```json
"systemControls": [
  {
    "namespace": "net.ipv4.ping_group_range",
    "value": "0 2147483647"
  }
]
```

## Gotchas
- **Security risk**: AMI deployment embeds tokens in EC2 user-data (readable by any AWS user with EC2 viewer permissions) — use AWS Secrets Manager in production
- EC2 `systemd` service only supported on Ubuntu, Fedora, Debian, CentOS
- Docker-based EC2 deployment requires 64-bit Linux
- Do not reuse connector tokens across multiple instances
- Stagger updates across multiple Connectors to avoid downtime

## Related Docs
- Connector Best Practices (hardware recommendations)
- Linux Connector Deployment
- Systemd Connector Update Guide
- ECS Connector Update Guide
- Twingate Helm Chart (EKS)
- Terraform / Pulumi / Twingate API (IaC)
- AWS Systems Manager User Guide