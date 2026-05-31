# Deploy a Connector on AWS

## Summary
Twingate supports multiple AWS deployment methods for Connectors: CloudFormation, EC2 (Linux), AMI, ECS Fargate, and EKS. Each method requires the deployment subnet to have outbound internet access. Tokens are generated per-Connector and must not be reused across instances.

## Key Information
- Subnet must have outbound internet access (for container image download and Twingate connectivity)
- Peer-to-peer connections recommended to improve performance and stay within Fair Use Policy
- Tokens (`TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`) are unique per Connector instance
- AMI is based on Ubuntu x86 with systemd pre-installed
- ECS Fargate requires extra config to support ICMP ping

## Prerequisites
- Access to Twingate Admin Console
- Remote Network already created
- AWS account with permissions to create EC2/ECS/CloudFormation resources
- SSH key pair and Subnet ID (for CloudFormation)
- AWS CLI configured (for AMI/ECS deployments)

## Deployment Methods

### CloudFormation (Easiest)
1. Admin Console → Remote Networks → Select network → Add Connector
2. Click new Connector → Choose **AWS Quick Start** deployment
3. Select AWS region → Click **Open AWS**
4. Select SSH key and Subnet ID → Click **Create stack**
5. Connector live within ~5 minutes

### AMI Deployment
1. Admin Console → Add Connector → Select **AMI** option
2. Generate tokens (requires re-authentication)
3. Fill in AWS environment details and optional features
4. Select CLI environment → Copy and run generated command

### ECS Fargate Deployment
1. Admin Console → Add Connector → Select **ECS** option
2. Generate tokens
3. Fill in AWS environment configuration
4. Run command to create task definition (AWS CLI)
5. Run command to launch Connector (AWS CLI)

### EKS
- Use the [official Twingate Helm chart](https://www.twingate.com/docs/kubernetes)

### EC2 (Manual)
- Follow standard [Linux Connector deployment](https://www.twingate.com/docs/linux) instructions
- Supports Docker (any 64-bit Linux) or systemd (Ubuntu, Fedora, Debian, CentOS)

## Configuration Values
| Variable | Description |
|---|---|
| `TWINGATE_ACCESS_TOKEN` | Connector access token (generated in Admin Console) |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token (generated in Admin Console) |

### ECS Ping Support (containerDefinitions)
```json
"systemControls": [
  {
    "namespace": "net.ipv4.ping_group_range",
    "value": "0 2147483647"
  }
]
```

## Gotchas
- **Security**: AMI/ECS deployment scripts embed tokens in EC2 user-data (readable by any AWS user with EC2 viewer permissions) — use **AWS Secrets Manager** for production
- **Token reuse**: Never reuse tokens across Connector instances; create separate task definitions per instance
- **Updates**: Stagger updates across multiple Connectors to avoid downtime
- AMI uses SSM Agent for remote shell access (requires IAM role assignment)

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)
- [ECS Connector Update Guide](https://www.twingate.com/docs/ecs-update)
- [Systemd Connector Update Guide](https://www.twingate.com/docs/systemd-update)
- [Kubernetes Best Practices](https://www.twingate.com/docs/kubernetes-best-practices)
- [Terraform/Pulumi/API Deployment](https://www.twingate.com/docs/deployment-automation)