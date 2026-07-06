# Pulumi with AWS and Twingate

## Summary
Step-by-step guide for deploying Twingate Connectors on AWS EC2 using Pulumi with TypeScript. Creates a VPC with a private demo server and a Connector VM, wiring them together via Twingate resources and groups.

## Key Information
- Uses TypeScript/Node.js Pulumi program
- Deploys two EC2 instances: one demo server (private IP only) and one Twingate Connector (public IP)
- Connector configured via `user_data` startup script writing to `/etc/twingate/connector.conf`
- Twingate AMI owner ID: `617935088040`, filter: `twingate/images/hvm-ssd/twingate-amd64-*`
- Instance type: `t2.micro`
- VPC CIDR: `10.0.0.0/16`, Subnet: `10.0.1.0/24`

## Prerequisites
- AWS account with permissions to create/delete EC2, VPC, subnet, IGW, route table resources
- Pulumi CLI installed with general Pulumi prerequisites met
- Node.js installed (`node -v` to verify)
- Twingate API key and tenant name
- Bash-compatible OS

## Step-by-Step
1. `mkdir twingate_pulumi_aws_demo && cd twingate_pulumi_aws_demo`
2. `pulumi new typescript` — follow prompts for project/stack name
3. Set AWS credentials as env vars (see below)
4. `pulumi config set twingate:apiToken YOUR_TOKEN --secret`
5. `pulumi config set twingate:network YOUR_TENANT`
6. Generate SSH key: `ssh-keygen` → save to `~/.ssh/aws_id_rsa`
7. `cat ~/.ssh/aws_id_rsa.pub | pulumi config set publicKey`
8. `npm install @pulumi/aws @twingate/pulumi-twingate`
9. Write `index.ts` with full configuration (see page for complete code)
10. `pulumi preview` — validate
11. `pulumi up` — deploy
12. Assign Twingate user to the created group in Twingate admin
13. Test: `ssh -i ~/.ssh/aws_id_rsa ubuntu@<private-ip>`
14. Teardown: `pulumi down`

## Configuration Values

| Type | Key/Variable | Value/Notes |
|------|-------------|-------------|
| Env var | `AWS_ACCESS_KEY_ID` | AWS access key |
| Env var | `AWS_SECRET_ACCESS_KEY` | AWS secret key |
| Env var | `AWS_REGION` | Target AWS region |
| Pulumi config | `twingate:apiToken` | API token (set `--secret`) |
| Pulumi config | `twingate:network` | Tenant prefix (e.g., `mycorp`) |
| Pulumi config | `publicKey` | SSH public key content |
| Connector env | `TWINGATE_URL` | `https://<network>.twingate.com` |
| Connector env | `TWINGATE_ACCESS_TOKEN` | From `TwingateConnectorTokens` |
| Connector env | `TWINGATE_REFRESH_TOKEN` | From `TwingateConnectorTokens` |
| Connector env | `TWINGATE_LOG_ANALYTICS` | `v1` |
| Connector env | `TWINGATE_LABEL_DEPLOYEDBY` | `tg-pulumi-aws-ec2` |

## Gotchas
- Demo server has `associatePublicIpAddress: false`; Connector VM has it `true` — do not swap these
- Pulumi config file (`Pulumi.demo.yaml`) contains encrypted secrets — exclude from source control
- AMI owner ID comment says "Amazon" but it's the Twingate AMI owner
- Must manually grant Twingate user access to the created group after `pulumi up`
- `TwingateConnectorTokens` tokens are sensitive outputs — use `pulumi.all()` to resolve them in `user_data`

## Related Docs
- [Twingate