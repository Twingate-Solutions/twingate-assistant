# Deploy a Connector on AWS

## Summary
Twingate supports multiple AWS deployment methods for Connectors: CloudFormation, EC2 (Docker/systemd), AMI, ECS Fargate, and EKS. Each method requires the deployment subnet to have outbound internet access. Tokens are generated per-Connector and must not be reused across instances.

## Key Information
- Subnet requires outbound internet access for image download and Twingate connectivity
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits
- AMI is pre-installed with systemd service on Ubuntu x86 base image
- AMI instances include AWS SSM Agent for remote shell access
- ECS Fargate requires `systemControls` config to enable ICMP ping to Resources
- Connector tokens are instance-specific — never reuse across multiple Connectors

## Prerequisites
- Access to Twingate Admin Console
- Remote Network created in Admin Console
- AWS account with permissions to create EC2/ECS/CloudFormation resources
- Subnet with outbound internet access

## Deployment Methods

### CloudFormation (Easiest)
1. Admin Console → Remote Networks → Select Network → Add Connector
2. Open new Connector → Choose **AWS Quick Start** deployment
3. Select AWS region → Click **Open AWS**
4. Select SSH key and Subnet ID → Click **Create stack**
5. Connector live within ~2 minutes

### AMI Deployment
1. Admin Console → Remote Networks → Add Connector → Select **AMI** option
2. Generate tokens (requires re-authentication)
3. Fill in AWS environment details and optional features
4. Select CLI environment → Copy and run generated command

### ECS Fargate Deployment
1. Admin Console → Remote Networks → Add Connector → Select **ECS** option
2. Generate tokens
3. Fill in AWS environment configuration
4. Run task definition creation command via AWS CLI
5. Run Connector launch command via AWS CLI

### Other Methods
- **EC2**: Follow standard Linux Connector deployment docs
- **EKS**: Use official Twingate Helm chart
- **IaC**: Terraform, Pulumi, or Twingate API

## Configuration Values

| Token | Description |
|-------|-------------|
| `TWINGATE_ACCESS_TOKEN` | Embedded in EC2 user-data by default |
| `TWINGATE_REFRESH_TOKEN` | Embedded in EC2 user-data by default |

**ECS ping support (add to `containerDefinitions`):**
```json
"systemControls": [{
  "namespace": "net.ipv4.ping_group_range",
  "value": "0 2147483647"
}]
```

## Gotchas
- AMI/EC2 user-data embeds tokens in **plain text** — any AWS user with EC2 viewer permissions can read them
- **Production**: Store tokens in AWS Secrets Manager, retrieve at runtime
- systemd service supported on Ubuntu, Fedora, Debian, CentOS only
- Create separate task definitions per Connector instance (tokens are not reusable)
- Stagger updates across multiple Connectors to avoid downtime

## Updates
- **systemd (EC2/AMI)**: Manual via Linux package manager or scheduled update task
- **ECS Fargate**: Via AWS management console or CLI

## Related Docs
- Connector Best Practices (hardware recommendations)
- Linux Connector deployment
- Twingate Helm chart (EKS)
- Systemd Connector Update Guide
- ECS Connector Update Guide
- Kubernetes Best Practices Guide
- Terraform/Pulumi/API deployment docs