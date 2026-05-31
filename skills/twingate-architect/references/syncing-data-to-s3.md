# Syncing Data to AWS S3

## Page Title
Syncing Data to AWS S3 (Twingate → AWS S3)

## Summary
Twingate can sync audit logs, network events, DNS filtering logs, and DLP events to an AWS S3 bucket as JSON files every 5 minutes. Two auth methods are supported: OIDC IAM Role (recommended) and static IAM User credentials. Available on Business and Enterprise plans only.

## Key Information
- Files written every ~5 minutes; filename format: `2025-07-25T18:20:00+00:00.json`
- Event types: `network_access`, `dns_filtering`, `audit_log`, `data_loss_prevention`
- Up to 10 minutes delay before first events appear
- No files sent to S3 if no events occurred in interval
- Configure via Admin Console (Settings → Reports → Sync to S3 Bucket) or Terraform

## Prerequisites
- Business or Enterprise Twingate plan
- AWS S3 bucket
- IAM permissions to create roles/policies/users in AWS
- Twingate Admin access

## Step-by-Step

### Option 1: OIDC (Recommended)
1. In Twingate Admin Console: Settings → Reports → Sync to S3 Bucket → OIDC Role → copy IAM Identity Provider URL
2. In AWS IAM: Create OpenID Connect provider with that URL; Audience = `<network-slug>`
3. Create IAM policy granting `s3:PutObject` on bucket ARN
4. Create IAM Role (Web Identity), attach OIDC provider, set condition `<slug>.twingate.com/oidc:sub = events_sync`
5. In Twingate Admin Console: enter bucket name + IAM Role ARN

### Option 2: IAM User Credentials
1. Create IAM user in AWS
2. Create and attach policy granting `s3:PutObject`
3. Generate Access Key + Secret Access Key
4. In Twingate Admin Console: enter bucket name, Access Key, Secret Access Key

## Configuration Values

| Field | Option 1 (OIDC) | Option 2 (IAM User) |
|-------|-----------------|---------------------|
| Bucket name | Required (no `arn:aws:s3:::` prefix) | Required (no `arn:aws:s3:::` prefix) |
| IAM Role ARN | Required | — |
| Access Key | — | Required |
| Secret Access Key | — | Required |

**OIDC Condition Key:** `<slug>.twingate.com/oidc:sub` = `events_sync`  
**OIDC Audience:** `<network-slug>` (e.g., `acme` from `acme.twingate.com`)

## Required IAM Permissions (Twingate sync role/user)
```json
"Action": "s3:PutObject", "Resource": "arn:aws:s3:::<bucket>/*"
```
Add for SSE-KMS: `kms:GenerateDataKey*`, `kms:Decrypt`

## Gotchas
- **Do not** include `arn:aws:s3:::` prefix when entering bucket name in Admin Console
- AWS opt-in regions (Jakarta `ap-southeast-3`, Hong Kong `ap-east-1`, Bahrain `me-south-1`) require STS V2 tokens — change AWS account Global STS endpoint to V2 in IAM Console → Account Settings
- Terraform tested with: Terraform `v1.12.2`, AWS Provider `~> 6.0.0`
- Static IAM credentials require manual rotation; not recommended for production

## Related Docs
- [Network Events Schema](https://www.twingate.com/docs/network-events-schema)
- [DNS Filtering Logs Schema](https://www.twingate.com/docs/dns-filtering-logs-schema)
- [Audit Logs Schema](https://www.twingate.com/docs/audit-logs-schema)
- [Terraform Examples](https://www.twingate.com/docs/terraform)
- [AWS S3 User Guide](https://docs.aws.amazon.com/s3/)