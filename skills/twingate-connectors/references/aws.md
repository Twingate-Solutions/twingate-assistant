# Deploy a Connector on AWS

## Summary
Twingate supports multiple AWS deployment methods for Connectors: CloudFormation, EC2 (Linux), AMI, ECS Fargate, and EKS. All deployments require a subnet with outbound internet access to download container images and connect to Twingate.

## Key Information
- Subnet must have outbound internet access for image download and Twingate connectivity
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits
- Each Connector instance requires its own unique tokens — never reuse tokens across instances
- AMIs come pre-installed with AWS SSM Agent for remote management

## Prerequisites
- Twingate Admin Console access
- Remote Network already created in Admin Console
- AWS account with appropriate IAM permissions
- Subnet with outbound internet access

## Deployment Methods

### CloudFormation (Easiest)
1. Admin Console → Remote Networks → Select Network → Add Connector
2. Click new Connector → Choose **AWS Quick Start** deployment
3. Select target region → Click **Open AWS**
4. Select SSH key and Subnet ID → Click **Create Stack**
5. Connector live within a few minutes

### EC2
- Follow standard Linux Connector deployment instructions
- Docker: any 64-bit Linux distro Docker supports
- systemd service: Ubuntu, Fedora, Debian, CentOS only

### AMI (Ubuntu x86, systemd pre-installed)
1. Admin Console → Add Connector → Select **AMI** option
2. Generate tokens (requires re-authentication)
3. Fill in AWS environment details and optional features
4. Select CLI environment, copy and run the generated command

### ECS Fargate
1. Admin Console → Add Connector → Select **ECS** option
2. Generate tokens (requires re-authentication)
3. Fill in AWS environment details
4. Run task definition creation command via AWS CLI
5. Run Connector launch command via AWS CLI

### EKS
- Use the official Twingate Helm chart
- See Kubernetes Best Practices Guide

### Infrastructure as Code
- Terraform, Pulumi, or Twingate API

## Configuration Values

### ECS Fargate — Ping Support
Add to `containerDefinitions` in task definition:
```json
"systemControls": [
  {
    "namespace": "net.ipv4.ping_group_range",
    "value": "0 2147483647"
  }
]
```

## Gotchas
- **Do not reuse Connector tokens** — create separate task definitions per Connector instance
- Subnet must have outbound internet access or deployment will fail silently
- systemd-based updates (EC2/AMI): stagger updates across Connectors to avoid downtime
- ECS Fargate ping to Resources requires explicit `systemControls` sysctl config

## Updates
| Deployment Type | Update Method |
|---|---|
| EC2 / AMI (systemd) | Manual via package manager or scheduled task — see Systemd Update Guide |
| ECS Fargate | AWS management console or CLI — see ECS Update Guide |

## Related Docs
- Connector Best Practices Guide
- Peer-to-peer connections setup
- Kubernetes Best Practices Guide
- Systemd Connector Update Guide
- ECS Connector Update Guide
- Terraform / Pulumi / Twingate API docs
- AWS Systems Manager User Guide