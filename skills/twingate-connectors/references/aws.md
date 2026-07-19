# Deploy a Connector on AWS

## Summary
Twingate Connectors can be deployed on AWS using multiple methods: CloudFormation, EC2 (Linux/AMI), ECS Fargate, or EKS. Each method is initiated from the Admin Console's Remote Network Connector deployment page. Subnets must have outbound internet access for image downloads and Twingate connectivity.

## Key Information
- Four primary deployment methods: CloudFormation, EC2/AMI, ECS Fargate, EKS (Helm)
- IaC options: Terraform, Pulumi, Twingate API
- Subnet requires outbound internet access
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits
- Do **not** reuse Connector tokens across instances; each Connector needs unique tokens

## Prerequisites
- Access to Twingate Admin Console
- Remote Network already created
- AWS account with permissions to deploy chosen resource type
- SSH key pair and Subnet ID (CloudFormation)
- AWS CLI configured (AMI/ECS deployments)

## Step-by-Step by Method

### CloudFormation
1. Admin Console → Remote Networks → Select network → Add Connector
2. Select new Connector → Choose **AWS Quick Start** deployment
3. Select region → Click **Open AWS**
4. Select SSH key and Subnet ID → **Create stack**
5. Live within a few minutes

### AMI Deployment
1. Admin Console → Remote Networks → Add Connector → Select **AMI** option
2. Generate tokens (requires re-authentication)
3. Fill in AWS environment details and optional features
4. Select CLI environment, copy and run generated command

### ECS Fargate
1. Admin Console → Remote Networks → Add Connector → Select **ECS** option
2. Generate tokens
3. Fill in AWS environment configuration
4. Run task definition creation command in AWS CLI
5. Run Connector launch command in AWS CLI

### EKS
- Use official Twingate Helm chart; see Kubernetes Best Practices Guide

## Configuration Values

| Parameter | Notes |
|-----------|-------|
| `TWINGATE_ACCESS_TOKEN` | Embedded in user-data by default (insecure for prod) |
| `TWINGATE_REFRESH_TOKEN` | Embedded in user-data by default (insecure for prod) |
| `net.ipv4.ping_group_range` | ECS sysctl required for ICMP/ping support |

**ECS ping support** — add to `containerDefinitions`:
```json
"systemControls": [
  {
    "namespace": "net.ipv4.ping_group_range",
    "value": "0 2147483647"
  }
]
```

## Gotchas
- **Security**: AMI/ECS scripts embed tokens in EC2 user-data — readable by any AWS user with EC2 viewer permissions. Use **AWS Secrets Manager** in production.
- EC2 systemd service only supported on Ubuntu, Fedora, Debian, CentOS
- AMI is x86 Ubuntu only
- Stagger updates across multiple Connectors to avoid downtime

## Updating Connectors
- **systemd (EC2/AMI)**: Manual via Linux package manager or scheduled task; see Systemd Connector Update Guide
- **ECS Fargate**: Via AWS management console or CLI; see ECS Connector Update Guide

## Related Docs
- Connector Best Practices (hardware sizing, recommendations)
- Systemd Connector Update Guide
- ECS Connector Update Guide
- Kubernetes Best Practices Guide
- Twingate Helm chart
- Peer-to-peer connections guide
- Terraform / Pulumi / API deployment docs