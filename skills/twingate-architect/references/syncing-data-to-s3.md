# Syncing Data to AWS S3

## Page Title
Syncing Data to AWS S3

## Summary
Twingate (Business/Enterprise) can sync audit logs, network events, DNS filtering logs, and DLP events to an AWS S3 bucket in JSON format every 5 minutes. Two authentication methods are supported: OIDC IAM Role (recommended) or static IAM User credentials. Configuration is available via Admin Console UI or Terraform.

## Key Information
- **Sync frequency**: Every 5 minutes; initial sync may take up to 10 minutes
- **File format**: JSON, filename format `2025-07-25T18:20:00+00:00.json`
- **Event types**: `network_access`, `dns_filtering`, `audit_log`, `data_loss_prevention`
- **No events = no file**: Twingate skips S3 writes when there's nothing to sync
- **Plan requirement**: Business & Enterprise only

## Prerequisites
- AWS S3 bucket created
- IAM permissions configured (see below)
- Twingate Admin Console access

## Step-by-Step

### Option 1: OIDC (Recommended)
1. Admin Console → Settings → Reports → Sync to S3 Bucket → OIDC Role → copy IAM Identity Provider URL
2. AWS IAM → Identity Providers → Add Provider → OpenID Connect
   - Provider URL: copied from Twingate
   - Audience: your network slug (e.g., `acme`)
3. Create IAM Policy with `s3:PutObject` on bucket
4. Create IAM Role: Web Identity → OIDC provider → add condition:
   - Key: `<network>.twingate.com/oidc:sub` | Operator: `StringEquals` | Value: `events_sync`
5. Admin Console: enter bucket name + IAM Role ARN

### Option 2: IAM User
1. Create IAM User in AWS
2. Attach policy granting `s3:PutObject` on bucket
3. Generate Access Key + Secret Access Key
4. Admin Console: enter bucket name, Access Key, Secret

## Configuration Values

| Field | OIDC | IAM User |
|-------|------|----------|
| Bucket name | Required (no `arn:aws:s3:::` prefix) | Required |
| IAM Role ARN | Required | — |
| Access Key | — | Required |
| Secret Access Key | — | Required |

**Required IAM policy (basic):**
```json
{ "Action": "s3:PutObject", "Resource": "arn:aws:s3:::<bucket>/*" }
```

**Additional permissions for SSE-KMS:**
```
kms:GenerateDataKey*, kms:Decrypt
```

**OIDC condition sub value:** `events_sync`

**Terraform versions tested:** Terraform `v1.12.2`, AWS Provider `~> 6.0.0`

## Gotchas
- **Do not** include `arn:aws:s3:::` prefix when entering bucket name in Admin Console
- **AWS opt-in regions** (Jakarta `ap-southeast-3`, Hong Kong `ap-east-1`, Bahrain `me-south-1`) require STS V2 tokens — change Global endpoint setting in IAM → Account Settings → STS → V2
- Static IAM credentials require manual rotation; not recommended for production/regulated environments
- Admin user needs broad IAM permissions including `iam:CreateRole`, `iam:CreateOpenIDConnectProvider`, `iam:CreateUser`, etc.

## Related Docs
- [Network Events Schema](https://www.twingate.com/docs/network-events-schema)
- [DNS Filtering Logs Schema](https://www.twingate.com/docs/dns-filtering-logs-schema)
- [Audit Logs Schema](https://www.twingate.com/docs/audit-logs-schema)
- [Terraform Examples](https://www.twingate.com/docs/terraform)
- [AWS S3 User Guide](https://docs.aws.amazon.com/s3/)