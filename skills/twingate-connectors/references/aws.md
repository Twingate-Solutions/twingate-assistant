---
source: https://www.twingate.com/docs/aws
type: docs
fetched: 2026-08-14
source_version: 3eb182ba17f40eee2e3a75ba99ad37b201e08387c8f01066dc73c5ec10fa58b8
---

# Deploy a Connector on AWS

## Summary
Twingate supports multiple AWS deployment methods for Connectors: CloudFormation, EC2 (Linux/AMI), ECS Fargate, and EKS. Each method requires the subnet to have outbound internet access for container image downloads and Twingate connectivity.

## Key Information
- Subnet must have outbound internet access
- Peer-to-peer connections recommended to improve UX and comply with Fair Use Policy
- Connector tokens are instance-specific — never reuse across multiple instances
- AMI comes pre-installed with AWS SSM Agent for remote management

## Deployment Methods

### CloudFormation (Easiest)
1. Admin Console → Remote Networks → select network → Add Connector
2. Click new Connector → choose **AWS Quick Start** deployment
3. Select region → click **Open AWS**
4. Select SSH key and Subnet ID → **Create stack**
5. Live within ~5 minutes

### EC2 (Linux)
- Follow standard [Linux Connector deployment](https://www.twingate.com/docs/linux)
- Docker: any 64-bit Linux Docker supports
- systemd: Ubuntu, Fedora, Debian, CentOS only

### AMI Deployment
1. Admin Console → Remote Networks → Add Connector → select **AMI** option
2. Generate tokens (requires re-authentication)
3. Fill in AWS environment details and optional features
4. Select CLI environment, copy and run generated command

### ECS Fargate
1. Admin Console → Remote Networks → Add Connector → select **ECS** option
2. Generate tokens
3. Fill in AWS environment configuration
4. Run AWS CLI command to create task definition
5. Run AWS CLI command to launch Connector

**Ping support:** Add `systemControls` to `containerDefinitions`:
```json
"systemControls": [
  {
    "namespace": "net.ipv4.ping_group_range",
    "value": "0 2147483647"
  }
]
```

### EKS
- Use official [Twingate Helm chart](https://www.twingate.com/docs/helm)

### Infrastructure as Code
- Terraform, Pulumi, or Twingate API

## Configuration Values
| Variable | Description |
|---|---|
| `TWINGATE_ACCESS_TOKEN` | Embedded in EC2 user-data by AMI deploy script |
| `TWINGATE_REFRESH_TOKEN` | Embedded in EC2 user-data by AMI deploy script |

## Gotchas
- **Security:** AMI deploy script embeds tokens in EC2 user-data — readable by any AWS user with EC2 viewer permissions. Use **AWS Secrets Manager** in production instead
- **Token reuse:** Do not reuse tokens across Connector instances; create separate task definitions per Connector
- **Region selection:** Deploy Connector in same region as Resources when possible

## Updates
- **systemd (EC2/AMI):** Manual via Linux package manager or scheduled task; stagger updates across Connectors to avoid downtime
- **ECS Fargate:** Via AWS console or CLI

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Linux Deployment](https://www.twingate.com/docs/linux)
- [Twingate Helm Chart](https://www.twingate.com/docs/helm)
- [Kubernetes Best Practices](https://www.twingate.com/docs/kubernetes-best-practices)
- [Systemd Connector Update Guide](https://www.twingate.com/docs/systemd-update)
- [ECS Connector Update Guide](https://www.twingate.com/docs/ecs-update)
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)