# How to Deploy a Connector on AWS

## Summary
Covers multiple AWS deployment methods for Twingate Connectors: CloudFormation, EC2, AMI, ECS Fargate, and EKS. Each method integrates with the Admin Console to generate tokens and deployment commands. Subnet must have outbound internet access.

## Key Information
- **Deployment options**: CloudFormation (easiest), EC2/Linux, AMI, ECS Fargate, EKS (Helm chart)
- Subnet requires outbound internet access for container image download and Twingate connectivity
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits
- AMI is pre-installed with Connector systemd service on Ubuntu x86; includes AWS SSM Agent for remote shell access
- Infrastructure-as-Code available via Terraform, Pulumi, or Twingate API

## Prerequisites
- Access to Twingate Admin Console
- Existing Remote Network configured
- AWS account with permissions to create EC2/ECS/CloudFormation resources
- Subnet with outbound internet access
- SSH key pair (CloudFormation method)

## Step-by-Step (Common Flow)
1. Admin Console → Remote Networks → select network → **Add Connector**
2. Click newly created Connector → choose deployment type (AWS Quick Start / AMI / ECS)
3. Generate tokens (re-authentication required)
4. Fill in AWS environment parameters (region, subnet, SSH key, etc.)
5. Copy and run generated CLI command or open AWS CloudFormation stack

## Configuration Values

| Token/Variable | Notes |
|---|---|
| `TWINGATE_ACCESS_TOKEN` | Generated per-connector; embedded in user-data by default |
| `TWINGATE_REFRESH_TOKEN` | Generated per-connector; embedded in user-data by default |

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
- **Security**: AMI/ECS user-data embeds tokens in plaintext — any user with EC2 viewer permissions can read them. Use **AWS Secrets Manager** in production.
- **Token reuse**: Tokens are instance-specific; create separate task definitions per Connector instance.
- **EC2 systemd**: Only supported on Ubuntu, Fedora, Debian, CentOS (not all Linux distros).
- **Updates**: Stagger updates across multiple Connectors to avoid downtime. systemd uses package manager or scheduled task; ECS uses AWS console/CLI.

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)
- [Twingate Helm Chart (EKS)](https://www.twingate.com/docs/helm)
- [Kubernetes Best Practices](https://www.twingate.com/docs/kubernetes-best-practices)
- [Systemd Connector Update Guide](https://www.twingate.com/docs/systemd-update)
- [ECS Connector Update Guide](https://www.twingate.com/docs/ecs-update)
- [Terraform/Pulumi/API Deployment](https://www.twingate.com/docs/automation)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)