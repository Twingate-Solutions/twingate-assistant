# Syncing Data to AWS S3

## Summary
Twingate (Business/Enterprise) can sync audit logs, network events, DNS filtering logs, and DLP events to an AWS S3 bucket in JSON format every 5 minutes. Two authentication methods are supported: OIDC IAM Role (recommended) or static IAM User credentials. Configuration is available via the Admin Console or Terraform.

## Key Information
- **Sync frequency**: Every 5 minutes; up to 10 minutes delay for new events
- **File format**: JSON; filename format: `2025-07-25T18:20:00+00:00.json`
- **Event types**: `network_access`, `dns_filtering`, `audit_log`, `data_loss_prevention`
- **No events = no file**: Twingate skips writing if nothing to sync
- **Plan requirement**: Business & Enterprise only

## Prerequisites
- AWS S3 bucket created
- IAM permissions configured (see below)
- Twingate Admin Console access

## Authentication Options

### Option 1: OIDC IAM Role (Recommended)
- Uses short-lived, auto-rotated credentials
- Requires OIDC Identity Provider setup in AWS

### Option 2: IAM User Credentials
- Static long-lived access keys
- Simpler setup; requires manual key rotation

## Step-by-Step

### OIDC Setup
1. Admin Console → **Settings → Reports → Sync to S3 Bucket → OIDC Role** → copy IAM Identity Provider URL
2. AWS IAM → Identity Providers → Add provider → OpenID Connect
   - Provider URL: copied from Twingate
   - Audience: `<your-network-slug>` (e.g., `acme`)
3. Create IAM Policy granting `s3:PutObject` on bucket
4. Create IAM Role:
   - Trusted entity: Web identity
   - Condition key: `<network>.twingate.com/oidc:sub` = `events_sync`
5. Admin Console → enter bucket name + IAM Role ARN

### IAM User Setup
1. Create IAM User in AWS
2. Create policy granting `s3:PutObject`
3. Generate Access Key + Secret Access Key
4. Admin Console → enter bucket name, Access Key, Secret

## Configuration Values

| Field | OIDC | IAM User |
|-------|------|----------|
| Bucket name | Required (no `arn:aws:s3:::` prefix) | Required |
| IAM Role ARN | Required | — |
| Access Key | — | Required |
| Secret Access Key | — | Required |

### Required IAM Policy (minimum)
```json
{"Action": "s3:PutObject", "Resource": "arn:aws:s3:::<bucket>/*"}
```

### SSE-KMS Additional Permissions
```
kms:GenerateDataKey*
kms:Decrypt
```

### Terraform Versions Tested
- Terraform: `v1.12.2`
- AWS Provider: `~> 6.0.0`

## Gotchas
- **Opt-in AWS regions** (Jakarta, Hong Kong, Bahrain): Require STS V2 tokens. Fix: IAM Console → Account Settings → STS Global endpoint → change to V2
- **Bucket name entry**: Do NOT include `arn:aws:s3:::` prefix in Admin Console
- **OIDC condition**: `sub` must be set to `events_sync` exactly
- **Admin user permissions**: Must include `iam:CreateRole`, `iam:CreateOpenIDConnectProvider`, `iam:CreateUser`, `iam:CreateAccessKey`, `s3:PutObject`, etc.

## Related Docs
- [Network Events Schema](https://www.twingate.com/docs/network-events-schema)
- [DNS Filtering Logs Schema](https://www.twingate.com/docs/dns-filtering-logs-schema)
- [Audit Logs Schema](https://www.twingate.com/docs/audit-logs-schema)
- [Terraform Examples](https://www.twingate.com/docs/terraform)
- Twingate Pricing Page