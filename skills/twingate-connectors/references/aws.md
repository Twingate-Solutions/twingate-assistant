# Deploy a Connector on AWS

## Summary
Twingate supports multiple AWS deployment methods for Connectors: CloudFormation, EC2 (Linux/Docker), AMI, ECS Fargate, and EKS. All deployments require outbound internet access from the subnet. Tokens are generated per-Connector and must not be reused across instances.

## Key Information
- Subnet must have outbound internet access (for container image download and Twingate connectivity)
- Peer-to-peer connections recommended to stay within Fair Use Policy
- Tokens are Connector-specific — create separate task definitions per Connector instance
- AMIs use Ubuntu x86 base with `systemd` pre-installed
- ECS Fargate containers have Connector service pre-installed
- AWS SSM Agent pre-installed on AMIs for remote shell access

## Prerequisites
- Twingate Admin Console access
- Existing Remote Network configured in Twingate
- AWS account with appropriate permissions (EC2, ECS, CloudFormation, or EKS depending on method)
- SSH key pair and Subnet ID (CloudFormation)
- AWS CLI configured (AMI, ECS deployments)

## Deployment Methods

### CloudFormation (Easiest)
1. Admin Console → Remote Networks → Select network → Add Connector
2. Open new Connector → Choose **AWS Quick Start** deployment
3. Select AWS region → Click **Open AWS**
4. Select SSH key and Subnet ID → Click **Create stack**
5. Connector live within a few minutes

### AMI Deployment
1. Admin Console → Remote Networks → Add Connector → Select **AMI** option
2. Generate tokens (requires re-authentication)
3. Fill out AWS environment configuration
4. Select CLI environment, copy and run the generated command

### ECS Fargate Deployment
1. Admin Console → Remote Networks → Add Connector → Select **ECS** option
2. Generate tokens (requires re-authentication)
3. Fill in AWS environment details and optional features
4. Run AWS CLI command to create task definition
5. Run AWS CLI command to launch the Connector

### EC2 Deployment
- Follow standard Linux Connector deployment instructions
- Docker: any 64-bit Linux distro Docker supports
- `systemd` service: Ubuntu, Fedora, Debian, CentOS only

### EKS Deployment
- Use official Twingate Helm chart
- Reference Kubernetes Best Practices Guide

## Configuration Values

### ECS Ping Support (systemControls)
```json
"systemControls": [
  {
    "namespace": "net.ipv4.ping_group_range",
    "value": "0 2147483647"
  }
]
```
Add to `containerDefinitions` section of task definition to enable ICMP ping to Resources.

## Gotchas
- **Do not reuse Connector tokens** — each running instance needs its own tokens and task definition
- Subnet must have outbound internet access or deployment will fail
- Ping to Resources in ECS Fargate requires manual `systemControls` addition to task definition
- Stagger updates across multiple Connectors to avoid downtime

## Update Methods
| Deployment | Update Method |
|------------|---------------|
| EC2 / AMI (`systemd`) | Linux package manager or scheduled task |
| ECS Fargate | AWS management console or CLI |

## Related Docs
- Connector Best Practices (hardware recommendations for EC2)
- Systemd Connector Update Guide
- ECS Connector Update Guide
- Twingate Helm Chart (EKS)
- Terraform / Pulumi / API (Infrastructure as Code)
- AWS Systems Manager User Guide (SSM remote access)