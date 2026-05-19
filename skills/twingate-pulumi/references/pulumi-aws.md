# Pulumi with AWS and Twingate

## Summary
Step-by-step guide for deploying Twingate Connectors on AWS EC2 using Pulumi with TypeScript. Creates a VPC with a private demo server and a public-facing Connector VM, then configures Twingate resources to enable private access.

## Key Information
- Uses TypeScript/Node.js for Pulumi configuration
- Deploys two EC2 instances: one private demo server, one public Twingate Connector
- Connector VM uses Twingate AMI (`twingate/images/hvm-ssd/twingate-amd64-*`, owner `617935088040`)
- SSH key pair used for VM authentication; public key stored in Pulumi config

## Prerequisites
- AWS account with resource create/delete permissions
- Pulumi CLI installed (with general Pulumi prerequisites met)
- Node.js installed (`node -v` to verify)
- Twingate account with API key
- Bash-compatible OS

## Step-by-Step

1. `mkdir twingate_pulumi_aws_demo && cd twingate_pulumi_aws_demo`
2. `pulumi new typescript`
3. Set AWS credentials as env vars
4. `pulumi config set twingate:apiToken YOUR_TOKEN --secret`
5. `pulumi config set twingate:network <tenant-name>`
6. Generate SSH key: `ssh-keygen` → save to `~/.ssh/aws_id_rsa`
7. `cat ~/.ssh/aws_id_rsa.pub | pulumi config set publicKey`
8. `npm install @pulumi/aws @twingate/pulumi-twingate`
9. Write `index.ts` with full configuration
10. `pulumi preview` then `pulumi up`
11. Assign Twingate user to the created group in Twingate admin
12. Teardown: `pulumi down`

## Configuration Values

| Config Key | Method | Notes |
|---|---|---|
| `AWS_ACCESS_KEY_ID` | env var | AWS auth |
| `AWS_SECRET_ACCESS_KEY` | env var | AWS auth |
| `AWS_REGION` | env var | AWS region |
| `twingate:apiToken` | `pulumi config set --secret` | Twingate API key |
| `twingate:network` | `pulumi config set` | Tenant prefix (e.g., `mycorp`) |
| `publicKey` | `pulumi config set` | SSH public key content |

**Connector startup env vars written to `/etc/twingate/connector.conf`:**
- `TWINGATE_URL`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`
- `TWINGATE_LOG_ANALYTICS=v1`
- `TWINGATE_LABEL_HOSTNAME`, `TWINGATE_LABEL_EGRESSIP`, `TWINGATE_LABEL_DEPLOYEDBY=tg-pulumi-aws-ec2`

**Network layout:** VPC `10.0.0.0/16`, Subnet `10.0.1.0/24`, instance size `t2.micro`

**Resource protocol config:** TCP ports 22/80 (RESTRICTED), UDP ALLOW_ALL, ICMP enabled

## Gotchas
- Demo server has `associatePublicIpAddress: false`; Connector VM has it `true` — do not swap these
- `Pulumi.demo.yaml` contains encrypted secrets — exclude from source control
- User must manually be added to the Twingate group after `pulumi up` completes
- AMI owner ID `617935088040` is listed as Amazon in comments but is the Twingate AMI publisher

## Related Docs
- [Twingate Pulumi GitHub examples](https://github.com/Twingate)
- Twingate API key generation docs
- Pulumi general prerequisites guide