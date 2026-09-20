---
source: https://www.twingate.com/docs/pulumi-aws
type: docs
fetched: 2026-09-20
source_version: da532dd13baa8daba7484157db78e9887d4103d7fafa2c3cb82147631e952ae0
---

# Pulumi with AWS and Twingate

## Summary
Step-by-step guide for automating Twingate deployments on AWS using Pulumi with TypeScript. Creates a VPC with a demo server (no public IP) and a Twingate Connector EC2 instance, wiring them together via Twingate resources and groups.

## Key Information
- Uses TypeScript/Node.js Pulumi program
- Deploys two EC2 instances: a private demo server and a public-facing Twingate Connector
- Connector configured via userdata script writing to `/etc/twingate/connector.conf`
- Twingate AMI used for both instances (owner ID: `617935088040`)
- Instance type: `t2.micro`
- Additional examples available at Twingate's GitHub repository

## Prerequisites
- AWS account with permissions to create/delete resources
- Pulumi CLI installed and configured
- Node.js installed (`node -v` to verify)
- Twingate API key and tenant name
- Bash-compatible OS
- Existing Pulumi account/stack prerequisites met

## Step-by-Step

1. `mkdir twingate_pulumi_aws_demo && cd twingate_pulumi_aws_demo`
2. `pulumi new typescript` — initialize project
3. Set AWS credentials as env vars
4. `pulumi config set twingate:apiToken YOUR_TOKEN --secret`
5. `pulumi config set twingate:network <tenant-name>`
6. Generate SSH keypair: `ssh-keygen` → save to `~/.ssh/aws_id_rsa`
7. `cat ~/.ssh/aws_id_rsa.pub | pulumi config set publicKey`
8. `npm install @pulumi/aws @twingate/pulumi-twingate`
9. Write `index.ts` with full configuration (see below)
10. `pulumi preview` → `pulumi up`
11. Assign Twingate user to the created group in Twingate admin
12. Test: `ssh -i ~/.ssh/aws_id_rsa ubuntu@<private-ip>`
13. Cleanup: `pulumi down`

## Configuration Values

| Config Key | Command | Notes |
|---|---|---|
| `twingate:apiToken` | `pulumi config set twingate:apiToken TOKEN --secret` | Mark as secret |
| `twingate:network` | `pulumi config set twingate:network TENANT` | Tenant prefix only |
| `publicKey` | `cat key.pub \| pulumi config set publicKey` | SSH public key |

**AWS env vars:**
```
AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION
```

**Connector env vars (written to `/etc/twingate/connector.conf`):**
```
TWINGATE_URL, TWINGATE_ACCESS_TOKEN, TWINGATE_REFRESH_TOKEN,
TWINGATE_LOG_ANALYTICS=v3, TWINGATE_LABEL_HOSTNAME,
TWINGATE_LABEL_EGRESSIP, TWINGATE_LABEL_DEPLOYEDBY=tg-pulumi-aws-ec2
```

**Resource protocol config:** TCP ports `22`, `80` (RESTRICTED); UDP `ALLOW_ALL`; ICMP enabled.

**Twingate AMI filter:** `twingate/images/hvm-ssd/twingate-amd64-*`, owner `617935088040`

## Gotchas
- Demo server has `associatePublicIpAddress: false`; Connector has `true` — don't swap these
- Pulumi stores encrypted secrets in `Pulumi.<stack>.yaml` — exclude from source control
- Must manually assign Twingate users to the created group after `pulumi up`
- AMI owner ID `617935088040` is listed as "Amazon" in docs — verify it's current
- Guide-only; not hardened for production use

## Related Docs
- Twingate API key generation
- Twingate Pulumi provider (`@twingate/pulumi-twingate`)
- Twingate GitHub repository (additional Pulumi/AWS examples)
- General Pulumi prerequisites guide