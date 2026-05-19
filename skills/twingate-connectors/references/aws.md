# Deploy a Connector on AWS

## Summary
Twingate supports multiple AWS deployment methods for Connectors: CloudFormation, EC2 (Linux), AMI, ECS Fargate, and EKS. Each method is configured via the Admin Console's Connector deployment page. Subnets must have outbound internet access for image downloads and Twingate connectivity.

## Key Information
- Subnet requires outbound internet access for Connector to function
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits
- Do **not** reuse Connector tokens across multiple instances — each Connector needs unique tokens
- CloudFormation is the fastest/easiest deployment path
- AMIs come pre-installed with AWS SSM Agent for remote shell access

## Deployment Options

### CloudFormation (Quickest)
1. Admin Console → Remote Networks → Select network → Add Connector
2. Open new Connector → Choose **AWS Quick Start** deployment
3. Select region → Click **Open AWS**
4. In AWS: select SSH key + Subnet ID → **Create stack**
5. Live within ~5 minutes

### EC2
- Follow standard Linux Connector deployment instructions
- Docker: any 64-bit Linux with Docker support
- systemd service: Ubuntu, Fedora, Debian, CentOS only

### AMI (Ubuntu x86, systemd pre-installed)
1. Admin Console → Add Connector → Select **AMI** option
2. Generate tokens (requires re-authentication)
3. Fill in AWS environment details + optional features
4. Select CLI environment, copy and run generated command

### ECS Fargate
1. Admin Console → Add Connector → Select **ECS** option
2. Generate tokens
3. Fill in AWS environment config
4. Run task definition creation command via AWS CLI
5. Run Connector launch command via AWS CLI

### EKS
- Use official Twingate Helm chart
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
Required only if Resources need to be pingable.

## Updating Connectors
| Deployment | Update Method |
|---|---|
| EC2 / AMI (systemd) | Linux package manager (manual) or scheduled task (auto) |
| ECS Fargate | AWS management console or CLI |

- Stagger updates across multiple Connectors to avoid downtime

## Gotchas
- Each Connector instance needs its own tokens — never reuse tokens
- Subnet must have outbound internet; private-only subnets will fail
- Ping support on ECS Fargate requires explicit `systemControls` sysctl config
- CloudFormation region should match the region where your Resources reside

## Related Docs
- Connector Best Practices (hardware sizing, general recommendations)
- Linux Connector Deployment
- Systemd Connector Update Guide
- ECS Connector Update Guide
- Twingate Helm Chart (EKS)
- Kubernetes Best Practices Guide
- Terraform / Pulumi / API deployment