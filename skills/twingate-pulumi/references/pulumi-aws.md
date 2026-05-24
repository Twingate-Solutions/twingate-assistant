# Pulumi with AWS and Twingate

## Summary
Step-by-step guide for deploying Twingate infrastructure on AWS using Pulumi with TypeScript. Creates a VPC with a demo server (no public IP) and a Twingate Connector EC2 instance, then configures Twingate resources to enable private access.

## Key Information
- Uses TypeScript/Node.js for Pulumi configuration
- Deploys two EC2 instances: a private demo server and a public-facing Twingate Connector
- Twingate Connector configured via EC2 user_data startup script
- AMI filter targets Twingate-specific images from owner `617935088040`
- Instance size: `t2.micro`

## Prerequisites
- AWS account with resource creation/deletion permissions
- Pulumi CLI installed with general Pulumi prerequisites met
- Node.js installed
- Bash-compatible OS
- Twingate API key and tenant name

## Step-by-Step

1. Create project directory and initialize: `pulumi new typescript`
2. Set AWS credentials as environment variables
3. Configure Twingate secrets: `pulumi config set twingate:apiToken YOUR_TOKEN --secret` and `pulumi config set twingate:network TENANT`
4. Generate SSH keypair and store public key: `cat ~/.ssh/aws_id_rsa.pub | pulumi config set publicKey`
5. Install modules: `npm install @pulumi/aws @twingate/pulumi-twingate`
6. Write `index.ts` with full configuration (see below)
7. Preview: `pulumi preview`, then deploy: `pulumi up`
8. Assign Twingate user to the created group in Twingate admin
9. Teardown: `pulumi down`

## Configuration Values

| Parameter | Command/Value |
|-----------|--------------|
| `AWS_ACCESS_KEY_ID` | `export AWS_ACCESS_KEY_ID=<value>` |
| `AWS_SECRET_ACCESS_KEY` | `export AWS_SECRET_ACCESS_KEY=<value>` |
| `AWS_REGION` | `export AWS_REGION=<value>` |
| `twingate:apiToken` | `pulumi config set --secret` |
| `twingate:network` | Tenant name prefix (e.g., `mycorp`) |
| `publicKey` | SSH public key for EC2 access |

**Connector env vars written to `/etc/twingate/connector.conf`:**
- `TWINGATE_URL`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`
- `TWINGATE_LOG_ANALYTICS=v1`
- `TWINGATE_LABEL_HOSTNAME`, `TWINGATE_LABEL_EGRESSIP`, `TWINGATE_LABEL_DEPLOYEDBY=tg-pulumi-aws-ec2`

## Gotchas
- Demo server has `associatePublicIpAddress: false`; Connector VM has `true` — do not swap these
- Must manually assign Twingate users to the created group after deployment
- `Pulumi.demo.yaml` stores encrypted secrets — exclude from source control
- AMI owner ID `617935088040` is used in the filter; verify this is current
- Code imports `Connector` from `@pulumi/aws/mskconnect` but doesn't use it — safe to remove

## Related Docs
- [Twingate Pulumi GitHub repository](https://github.com/Twingate) — additional AWS examples
- Twingate API key generation guide
- General Pulumi prerequisites guide