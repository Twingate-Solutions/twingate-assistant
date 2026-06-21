# Syncing Data to AWS S3

## Page Title
Syncing Data to AWS S3 (Twingate → AWS S3)

## Summary
Twingate can push audit logs, network events, DNS filtering logs, and DLP events to an AWS S3 bucket as JSON files every 5 minutes. Supports two auth methods: OIDC IAM Role (recommended) or static IAM User credentials. Business and Enterprise plans only.

## Key Information
- **Sync frequency**: Every 5 minutes; up to 10 minutes for first sync or recent events
- **File format**: JSON; filename format `2025-07-25T18:20:00+00:00.json`
- **Event types**: `network_access`, `dns_filtering`, `audit_log`, `data_loss_prevention`
- **No events = no file**: Twingate skips upload if nothing to sync
- **Config location**: Admin Console → Settings → Reports → Sync to S3 Bucket

## Prerequisites
- Business or Enterprise Twingate plan
- AWS S3 bucket created
- IAM permissions configured (role or user)
- For OIDC: IAM Identity Provider created in AWS

## Step-by-Step

### Option 1: OIDC (Recommended)
1. Admin Console → Settings → Reports → Sync to S3 Bucket → OIDC Role → copy IAM Identity Provider URL
2. AWS IAM → Identity Providers → Add Provider → OpenID Connect
   - Provider URL: copied from Twingate
   - Audience: your network slug (e.g., `acme`)
3. Create IAM Policy with `s3:PutObject` on bucket
4. Create IAM Role → Trusted entity: Web Identity
   - Add condition: `<slug>.twingate.com/oidc:sub` = `events_sync`
   - Attach policy
5. Enter bucket name + Role ARN in Admin Console

### Option 2: IAM User Credentials
1. Create IAM User → attach policy with `s3:PutObject`
2. Generate Access Key + Secret Access Key
3. Enter bucket name, Access Key, Secret in Admin Console

## Configuration Values

| Field | OIDC | IAM User |
|-------|------|----------|
| Bucket name | Required (no `arn:aws:s3:::` prefix) | Required |
| IAM Role ARN | Required | — |
| Access Key | — | Required |
| Secret Access Key | — | Required |

**Required IAM action**: `s3:PutObject` on `arn:aws:s3:::<bucket>/*`

**SSE-KMS additional actions**: `kms:GenerateDataKey*`, `kms:Decrypt`

**Terraform versions tested**: Terraform `v1.12.2`, AWS Provider `~> 6.0.0`

## Gotchas
- **Do not** include `arn:aws:s3:::` prefix when entering bucket name in UI
- **Opt-in AWS regions** (Jakarta `ap-southeast-3`, Hong Kong `ap-east-1`, Bahrain `me-south-1`) require STS V2 tokens → change in IAM Console → Account Settings → STS Global endpoint → V2
- Static IAM credentials require manual rotation; not recommended for production
- OIDC condition key must be `<slug>.twingate.com/oidc:sub` = `events_sync` exactly

## Related Docs
- Network Events Schema
- DNS Filtering Logs Schema
- Audit Logs Schema
- Twingate Terraform Examples
- AWS S3 User Guide