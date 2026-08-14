---
source: https://www.twingate.com/docs/pulumi-aws
type: docs
fetched: 2026-08-14
source_version: 4570a8c7c7a96669e33fe512181940c6a574bfbf569e49980d59da7d147d2174
---

# How to Use Pulumi with AWS and Twingate

## Summary
Step-by-step guide for deploying Twingate infrastructure on AWS using Pulumi with TypeScript. Creates a VPC with a demo server (private IP) and a Twingate Connector EC2 instance, wired together as a Twingate Resource accessible via group membership.

## Key Information
- Language: TypeScript/Node.js
- Instance type: `t2.micro` for both VMs
- Connector VM gets a public IP; demo server is private-only
- Twingate AMI owner ID: `617935088040`, filter: `twingate/images/hvm-ssd/twingate-amd64-*`
- Connector config written to `/etc/twingate/connector.conf` via user_data script
- Additional examples: [Twingate GitHub repo](https://github.com/Twingate)

## Prerequisites
- AWS account with permissions to create/delete EC2, VPC, subnet, gateway, route table resources
- Pulumi CLI installed and configured
- Node.js installed (`node -v` to verify)
- Twingate account with API key
- Bash-compatible OS

## Step-by-Step

1. **Create project directory and initialize**
   ```bash
   mkdir twingate_pulumi_aws_demo && cd twingate_pulumi_aws_demo
   pulumi new typescript
   ```

2. **Set AWS credentials**
   ```bash
   export AWS_ACCESS_KEY_ID=<key>
   export AWS_SECRET_ACCESS_KEY=<secret>
   export AWS_REGION=<region>
   ```

3. **Set Twingate config**
   ```bash
   pulumi config set twingate:apiToken YOUR_TOKEN --secret
   pulumi config set twingate:network <tenant-prefix>
   ```

4. **Generate SSH key and store public key**
   ```bash
   ssh-keygen  # save to ~/.ssh/aws_id_rsa
   cat ~/.ssh/aws_id_rsa.pub | pulumi config set publicKey
   ```

5. **Install npm packages**
   ```bash
   npm install @pulumi/aws @twingate/pulumi-twingate
   ```

6. **Write `index.ts`** (see Configuration Values for resources created)

7. **Deploy**
   ```bash
   pulumi preview  # dry run
   pulumi up       # apply
   ```

8. **Assign Twingate user to the created group** (manual step in Twingate admin)

9. **Teardown**
   ```bash
   pulumi down
   ```

## Configuration Values

| Config Key | Set Via | Notes |
|---|---|---|
| `twingate:apiToken` | `pulumi config set --secret` | Mark as secret |
| `twingate:network` | `pulumi config set` | Tenant prefix only |
| `publicKey` | `pulumi config set` | SSH public key content |

**Connector env vars** (written to `/etc/twingate/connector.conf`):
- `TWINGATE_URL`
- `TWINGATE_ACCESS_TOKEN`
- `TWINGATE_REFRESH_TOKEN`
- `TWINGATE_LOG_ANALYTICS=v1`
- `TWINGATE_LABEL_HOSTNAME`, `TWINGATE_LABEL_EGRESSIP`, `TWINGATE_LABEL_DEPLOYEDBY`

**Resource protocol config**: TCP restricted to ports 22, 80; UDP allow all; ICMP enabled.

## Gotchas
- `Pulumi.demo.yaml` stores encrypted secrets — exclude from source control
- After `pulumi up`, users must be manually added to the created Twingate group to gain access
- AMI image versions may be outdated in examples; verify latest via AWS AMI lookup
- Connector VM needs `associatePublicIpAddress: true`; demo server should be `false`

## Related Docs
- Twingate API key generation guide
- Pulumi Twingate provider docs
- [Additional AWS + Twingate Pulumi examples (GitHub)](https://github.com/Twingate)