# Deploy a Connector on AWS

## Summary
Twingate Connectors can be deployed on AWS via CloudFormation, EC2 (Linux/AMI), ECS Fargate, or EKS. Each method is configured through the Admin Console's Connector deployment page. Subnet must have outbound internet access for image download and Twingate connectivity.

## Key Information
- Four primary deployment methods: CloudFormation, EC2 (Linux), AMI, ECS Fargate
- EKS deployment available via official Twingate Helm chart
- IaC options: Terraform, Pulumi, Twingate API
- Each Connector instance requires unique tokens — do not reuse tokens across instances
- AWS SSM Agent pre-installed on AMI images for remote shell access

## Prerequisites
- Subnet with outbound internet access
- Twingate Admin Console access
- Remote Network configured with a Connector added
- AWS credentials/CLI configured (for AMI/ECS methods)
- SSH key and Subnet ID (CloudFormation)

## Step-by-Step by Method

**CloudFormation (easiest):**
1. Admin Console → Remote Networks → Select Network → Add Connector
2. Select new Connector → Choose AWS Quick Start deployment
3. Select region → Click Open AWS
4. Select SSH key and Subnet ID → Create stack (live in ~minutes)

**AMI:**
1. Admin Console → Add Connector → Select AMI option
2. Generate tokens (re-authentication required)
3. Fill AWS environment configuration
4. Select CLI environment, copy and run generated command

**ECS Fargate:**
1. Admin Console → Add Connector → Select ECS option
2. Generate tokens
3. Fill AWS environment configuration
4. Run task definition creation command via AWS CLI
5. Run Connector launch command via AWS CLI

## Configuration Values

| Parameter | Notes |
|-----------|-------|
| `TWINGATE_ACCESS_TOKEN` | Embedded in user-data by default (AMI) |
| `TWINGATE_REFRESH_TOKEN` | Embedded in user-data by default (AMI) |
| `net.ipv4.ping_group_range` | ECS sysctl: `0 2147483647` (required for ping) |

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
- **Security**: AMI user-data embeds tokens in plaintext — any AWS user with EC2 viewer permissions can read them. Use **AWS Secrets Manager** for production.
- EC2 systemd service supported only on Ubuntu, Fedora, Debian, CentOS (not all distros)
- Stagger updates across multiple Connectors to avoid downtime
- ECS: create separate task definitions per Connector instance

## Updates
- **systemd (EC2/AMI)**: Manual via Linux package manager or scheduled task; see Systemd Connector Update Guide
- **ECS Fargate**: Via AWS management console or CLI; see ECS Connector Update Guide

## Related Docs
- Connector Best Practices (hardware recommendations, peer-to-peer)
- Linux Connector deployment
- Twingate Helm chart (EKS)
- Kubernetes Best Practices Guide
- Systemd/ECS Connector Update Guides
- Terraform/Pulumi/API deployment guides