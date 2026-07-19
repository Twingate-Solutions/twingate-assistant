# Pulumi with AWS and Twingate

## Summary
Step-by-step guide for deploying Twingate Connectors on AWS EC2 using Pulumi with TypeScript. Creates a VPC, subnet, demo server (private IP), and Twingate Connector VM that auto-configures via userdata script. Community-maintained open source tooling.

## Key Information
- Uses TypeScript/Node.js for Pulumi configuration
- Deploys two EC2 instances: a private demo server and a public-facing Twingate Connector
- Connector self-configures via `userdata` bash script writing to `/etc/twingate/connector.conf`
- Twingate AMI owner ID: `617935088040`, filter: `twingate/images/hvm-ssd/twingate-amd64-*`
- Instance type: `t2.micro`

## Prerequisites
- AWS account with resource create/delete permissions
- Pulumi CLI installed with general Pulumi prerequisites met
- Node.js installed (`node -v` to verify)
- Twingate API key and tenant name
- Bash-compatible OS

## Step-by-Step

1. `mkdir twingate_pulumi_aws_demo && cd twingate_pulumi_aws_demo`
2. `pulumi new typescript`
3. Set AWS credentials as env vars (see Configuration Values)
4. `pulumi config set twingate:apiToken YOUR_TOKEN --secret`
5. `pulumi config set twingate:network <tenant-name>`
6. Generate SSH key: `ssh-keygen` → save to `~/.ssh/aws_id_rsa`
7. `cat ~/.ssh/aws_id_rsa.pub | pulumi config set publicKey`
8. `npm install @pulumi/aws @twingate/pulumi-twingate`
9. Write `index.ts` with full configuration
10. `pulumi preview` → `pulumi up`
11. Add Twingate user to the created group in Twingate admin console
12. Test: `ssh -i ~/.ssh/aws_id_rsa ubuntu@<private-ip>`
13. Teardown: `pulumi down`

## Configuration Values

| Variable | Description |
|---|---|
| `AWS_ACCESS_KEY_ID` | AWS access key (env var) |
| `AWS_SECRET_ACCESS_KEY` | AWS secret key (env var) |
| `AWS_REGION` | Target AWS region (env var) |
| `twingate:apiToken` | Twingate API key (Pulumi secret) |
| `twingate:network` | Twingate tenant prefix (e.g., `mycorp`) |
| `publicKey` | SSH public key (Pulumi config) |

**Connector env vars written to `/etc/twingate/connector.conf`:**
- `TWINGATE_URL`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`
- `TWINGATE_LOG_ANALYTICS=v1`
- `TWINGATE_LABEL_HOSTNAME`, `TWINGATE_LABEL_EGRESSIP`, `TWINGATE_LABEL_DEPLOYEDBY=tg-pulumi-aws-ec2`

## Gotchas
- Demo server has `associatePublicIpAddress: false`; Connector VM has `true` — do not swap these
- Must manually assign Twingate user to the created group after `pulumi up` completes
- `Pulumi.demo.yaml` contains encrypted secrets — exclude from source control
- AMI versions in guide may be outdated; always check latest available

## Related Docs
- [Twingate Pulumi GitHub examples](https://github.com/twingate) — additional AWS/Pulumi examples
- Twingate API key generation guide (linked in docs)
- Pulumi general prerequisites guide