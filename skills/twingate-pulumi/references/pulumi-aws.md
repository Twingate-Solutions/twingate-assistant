# Pulumi with AWS and Twingate

## Summary
Step-by-step guide for automating Twingate deployments on AWS using Pulumi with TypeScript. Creates a VPC with a private demo server and a Twingate Connector EC2 instance, then exposes the private server as a Twingate Resource.

## Key Information
- Uses TypeScript/Node.js for Pulumi configuration
- Deploys two EC2 instances: one private demo server, one public-facing Twingate Connector
- Connector configured via cloud-init user_data script
- Twingate AMI owner ID: `617935088040`; AMI filter: `twingate/images/hvm-ssd/twingate-amd64-*`
- Instance type: `t2.micro`
- Network CIDR: `10.0.0.0/16`, Subnet: `10.0.1.0/24`

## Prerequisites
- AWS account with permissions to create/delete EC2, VPC, Subnet, IGW, RouteTable resources
- Pulumi CLI installed and configured
- Node.js installed (`node -v` to verify)
- Twingate API key and tenant name
- Bash-compatible OS

## Step-by-Step

```bash
# 1. Create project
mkdir twingate_pulumi_aws_demo && cd twingate_pulumi_aws_demo
pulumi new typescript

# 2. Set AWS credentials
export AWS_ACCESS_KEY_ID=<key>
export AWS_SECRET_ACCESS_KEY=<secret>
export AWS_REGION=<region>

# 3. Configure Twingate
pulumi config set twingate:apiToken YOUR_TOKEN --secret
pulumi config set twingate:network <tenant-name>

# 4. Generate SSH key pair
ssh-keygen  # save to ~/.ssh/aws_id_rsa
cat ~/.ssh/aws_id_rsa.pub | pulumi config set publicKey

# 5. Install modules
npm install @pulumi/aws @twingate/pulumi-twingate

# 6. Write index.ts (see Configuration Values)

# 7. Deploy
pulumi preview
pulumi up

# 8. Teardown
pulumi down
```

## Configuration Values

| Config Key | Method | Notes |
|---|---|---|
| `AWS_ACCESS_KEY_ID` | env var | AWS auth |
| `AWS_SECRET_ACCESS_KEY` | env var | AWS auth |
| `AWS_REGION` | env var | AWS region |
| `twingate:apiToken` | `pulumi config set --secret` | Encrypted in Pulumi.stack.yaml |
| `twingate:network` | `pulumi config set` | Tenant prefix only (e.g., `mycorp`) |
| `publicKey` | `pulumi config set` | SSH public key content |

**Connector `/etc/twingate/connector.conf` variables:**
- `TWINGATE_URL`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`
- `TWINGATE_LOG_ANALYTICS=v1`
- `TWINGATE_LABEL_HOSTNAME`, `TWINGATE_LABEL_EGRESSIP`, `TWINGATE_LABEL_DEPLOYEDBY=tg-pulumi-aws-ec2`

## Gotchas
- **Pulumi.demo.yaml** contains encrypted secrets — exclude from source control
- Demo server has `associatePublicIpAddress: false`; Connector has `true` — required for outbound connectivity
- After `pulumi up`, manually assign the Twingate user to the created group (`aws demo group`)
- SSH test uses private IP (`ubuntu@<private-ip>`), requires active Twingate client connection
- AMI owner ID comment says "Amazon" but it's the Twingate AMI owner

## Related Docs
- [Twingate Pulumi GitHub examples](https://github.com/Twingate)
- [Twingate API key generation](https://www.twingate.com/docs/api-overview)
- [Pulumi AWS provider docs](https://www.pulumi.com/registry/packages/aws/)
- [Twingate Pulumi provider](https://