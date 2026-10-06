---
source: https://www.twingate.com/docs/pulumi-aws
type: docs
fetched: 2026-10-04
source_version: b44cce13d9a4101f54215d3e049e9325194bb124c8e474e5243a6bd52507fe2b
trust: official
---

# Pulumi with AWS and Twingate

## Page Title
How to Use Pulumi with AWS and Twingate

## Summary
Automates Twingate deployment on AWS using Pulumi (TypeScript). Creates a VPC, subnets, two EC2 instances (one demo server, one Twingate Connector), and the corresponding Twingate Remote Network, Connector, Group, and Resource objects.

## Key Information
- Language: TypeScript/Node.js
- NPM packages: `@pulumi/aws`, `@twingate/pulumi-twingate`
- Connector VM uses a Twingate-published AMI (owner ID `617935088040`, pattern `twingate/images/hvm-ssd/twingate-amd64-*`)
- Connector configured via `/etc/twingate/connector.conf` written by user-data script
- Demo server has no public IP; Connector VM has a public IP
- Instance size: `t2.micro`
- VPC CIDR: `10.0.0.0/16`, Subnet: `10.0.1.0/24`

## Prerequisites
- AWS account with permissions to create EC2, VPC, Subnet, IGW, RouteTable resources
- Pulumi CLI installed and authenticated
- Node.js installed (`node -v` to verify)
- Twingate API key and tenant name
- SSH key pair generated locally

## Step-by-Step

```bash
# 1. Project setup
mkdir twingate_pulumi_aws_demo && cd twingate_pulumi_aws_demo
pulumi new typescript

# 2. AWS auth (env vars)
export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
export AWS_REGION=<YOUR_AWS_REGION>

# 3. Twingate config
pulumi config set twingate:apiToken YOUR_TOKEN --secret
pulumi config set twingate:network <tenant-name>

# 4. SSH key
ssh-keygen -f ~/.ssh/aws_id_rsa
cat ~/.ssh/aws_id_rsa.pub | pulumi config set publicKey

# 5. Install packages
npm install @pulumi/aws @twingate/pulumi-twingate

# 6. Write index.ts (see Configuration Values / full example in source)

# 7. Preview and deploy
pulumi preview
pulumi up

# 8. Tear down
pulumi down
```

## Configuration Values

| Config Key | Set Via | Notes |
|---|---|---|
| `twingate:apiToken` | `pulumi config set --secret` | Encrypted in `Pulumi.<stack>.yaml` |
| `twingate:network` | `pulumi config set` | Tenant prefix only (e.g., `mycorp`) |
| `publicKey` | `pulumi config set` | SSH public key content |
| `AWS_ACCESS_KEY_ID` | env var | |
| `AWS_SECRET_ACCESS_KEY` | env var | |
| `AWS_REGION` | env var | |

### Connector `/etc/twingate/connector.conf` variables
- `TWINGATE_URL`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`, `TWINGATE_LOG_ANALYTICS=v3`, `TWINGATE_LABEL_HOSTNAME`, `TWINGATE_LABEL_EGRESSIP`, `TWINGATE_LABEL_DEPLOYEDBY=tg-pulumi-aws-ec2`

## Gotchas
- `Pulumi.<stack>.yaml` contains encrypted secrets — exclude from source control (`.gitignore`)
- Demo server has `associatePublicIpAddress: false`; Connector has `true` — don't swap these
- After `pulumi up`, manually assign the Twingate user to the created group in the Twingate admin console; without this, access tests will fail
- AMI owner ID comment in source incorrectly labels `617935088040` as "Amazon" — it is Twingate's publisher ID

## Related Docs
- [Twingate Pulumi examples (GitHub)](https://github.com/Twingate)
-