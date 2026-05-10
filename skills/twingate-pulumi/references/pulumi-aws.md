# Pulumi with AWS and Twingate

## Summary
Step-by-step guide for deploying Twingate Connectors on AWS EC2 using Pulumi with TypeScript. Creates a VPC, subnet, demo server, and Twingate Connector VM with automated connector configuration via user data script.

## Key Information
- Uses TypeScript/Node.js for Pulumi configuration
- Deploys two EC2 instances: a private demo server and a public-facing Twingate Connector
- Connector auto-configures via bash user data script on startup
- Uses Twingate AMI from owner `617935088040` with filter `twingate/images/hvm-ssd/twingate-amd64-*`
- Instance size: `t2.micro`

## Prerequisites
- AWS account with resource creation/deletion permissions
- Pulumi CLI installed with general Pulumi prerequisites met
- Node.js installed (`node -v` to verify)
- Bash-compatible OS
- Twingate API key and tenant name

## Step-by-Step
1. `mkdir twingate_pulumi_aws_demo && cd twingate_pulumi_aws_demo`
2. `pulumi new typescript` (follow prompts)
3. Set AWS credentials as env vars
4. `pulumi config set twingate:apiToken YOUR_TOKEN --secret`
5. `pulumi config set twingate:network <tenant-name>`
6. Generate SSH keypair: `ssh-keygen` → save to `~/.ssh/aws_id_rsa`
7. `cat ~/.ssh/aws_id_rsa.pub | pulumi config set publicKey`
8. `npm install @pulumi/aws @twingate/pulumi-twingate`
9. Write `index.ts` with full configuration (see below)
10. `pulumi preview` → `pulumi up`
11. Assign Twingate user to created group manually in Twingate admin

## Configuration Values

| Config Key | Command | Notes |
|---|---|---|
| `twingate:apiToken` | `pulumi config set twingate:apiToken TOKEN --secret` | Mark as secret |
| `twingate:network` | `pulumi config set twingate:network TENANT` | Tenant prefix only |
| `publicKey` | `cat key.pub \| pulumi config set publicKey` | SSH public key |

**Environment Variables (AWS auth):**
```bash
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_REGION=...
```

**Connector config written to `/etc/twingate/connector.conf`:**
- `TWINGATE_URL`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`
- `TWINGATE_LOG_ANALYTICS=v1`
- `TWINGATE_LABEL_DEPLOYEDBY=tg-pulumi-aws-ec2`

## Twingate Resources Created
- `TwingateRemoteNetwork` → `TwingateConnector` → `TwingateConnectorTokens`
- `TwingateGroup` (name: "aws demo group")
- `TwingateResource` (TCP ports 22/80 restricted; UDP allow all; ICMP allowed)

## Gotchas
- Demo server has `associatePublicIpAddress: false`; Connector VM has `true` — don't swap these
- After `pulumi up`, manually assign Twingate users to the created group — not automated
- `Pulumi.demo.yaml` stores encrypted secrets — exclude from source control
- AMI owner ID `617935088040` is hardcoded; verify this is current
- Connector tokens are sensitive — passed via `pulumi.all()` to avoid plaintext exposure

## Teardown
```bash
pulumi down
```

## Related Docs
- [Twingate Pulumi GitHub Examples](https://github.com/Twingate)
- [Twingate API Key Generation](https://www.twingate.com/docs/api-overview)
- [Pulumi General Twingate Guide](https://www.twingate.com/docs/pulumi)