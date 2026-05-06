# Syncing Data to AWS S3

## Page Title
Syncing Data to AWS S3 (Twingate)

## Summary
Twingate (Business/Enterprise) can sync audit logs, network events, DNS filtering logs, and DLP events to an AWS S3 bucket in JSON format every 5 minutes. Two authentication methods are supported: OIDC IAM Role (recommended) and static IAM User credentials. Configuration is done via the Admin Console or Terraform.

## Key Information
- **Sync frequency**: Every 5 minutes; initial sync may take up to 10 minutes
- **File format**: JSON; filename format: `2025-07-25T18:20:00+00:00.json`
- **Event types**: `network_access`, `dns_filtering`, `audit_log`, `data_loss_prevention`
- No file is written if there are no events to sync
- Plan restriction: Business & Enterprise only

## Prerequisites
- AWS S3 bucket created
- IAM policy granting `s3:PutObject` on bucket
- If SSE-KMS encryption: also need `kms:GenerateDataKey*` and `kms:Decrypt`
- Twingate Admin Console access

## Step-by-Step

### Option 1: OIDC Role (Recommended)
1. Admin Console → Settings → Reports → Sync to S3 Bucket → OIDC Role → copy IAM Identity Provider URL
2. AWS IAM → Identity Providers → Add provider → OpenID Connect
   - Provider URL: copied URL from step 1
   - Audience: `<network-slug>` (e.g., `acme`)
3. Create IAM Policy with `s3:PutObject` on bucket
4. Create IAM Role:
   - Trusted entity: Web identity
   - Provider: OIDC provider from step 2
   - Condition: `<network>.twingate.com/oidc:sub` = `events_sync`
   - Attach policy from step 3
5. Admin Console → Settings → Reports → Sync to S3 Bucket → enter bucket name + IAM Role ARN

### Option 2: IAM User Credentials
1. Create IAM User in AWS
2. Create and attach IAM policy with `s3:PutObject`
3. Generate Access Key + Secret Access Key
4. Admin Console → Settings → Reports → Sync to S3 Bucket → enter bucket name, Access Key, Secret

## Configuration Values

| Field | OIDC | IAM User |
|-------|------|----------|
| Bucket name | Required (no `arn:aws:s3:::` prefix) | Required |
| IAM Role ARN | Required | — |
| Access Key | — | Required |
| Secret Access Key | — | Required |

**OIDC condition key**: `<tenant>.twingate.com/oidc:sub` = `events_sync`  
**OIDC audience**: network slug (e.g., `acme`)  
**Terraform versions**: Terraform ≥ 1.12.2, AWS Provider ~> 6.0.0

## Gotchas
- Do **not** include `arn:aws:s3:::` prefix when entering bucket name in Admin Console
- Static IAM credentials require manual rotation — not recommended for production
- SSE-KMS encryption requires additional KMS permissions beyond `s3:PutObject`
- AWS Admin performing setup needs broad IAM permissions (CreateRole, CreateOpenIDConnectProvider, CreateUser, CreateAccessKey, etc.)
- No file written to S3 if zero events occurred in the 5-minute window

## Related Docs
- [Network Events Schema](https://www.twingate.com/docs/network-events)
- [DNS Filtering Logs Schema](https://www.twingate.com/docs/dns-filtering-logs)
- [Audit Logs Schema](https://www.twingate.com/docs/audit-logs)
- [Terraform Examples](https://www.twingate.com/docs/terraform)
- [AWS S3 User Guide](https://docs.aws.amazon.com/s3/)