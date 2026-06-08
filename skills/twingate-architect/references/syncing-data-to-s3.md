# Syncing Data to AWS S3

## Page Title
Syncing Data to AWS S3 (Twingate → AWS S3)

## Summary
Twingate can push audit logs, network events, DNS filtering logs, and DLP events to an AWS S3 bucket in JSON format every 5 minutes. Supports two auth methods: OIDC IAM Role (recommended) or static IAM User credentials. Business and Enterprise plans only.

## Key Information
- Files synced every 5 minutes; up to 10 minutes delay for new events
- Filename format: `2025-07-25T18:20:00+00:00.json`
- Event types: `network_access`, `dns_filtering`, `audit_log`, `data_loss_prevention`
- No file created if no events exist in that interval
- Sync status visible in Admin Console → Settings → Reports

## Prerequisites
- Business or Enterprise Twingate plan
- AWS S3 bucket already created
- IAM permissions on the AWS admin account (see below)
- Twingate Admin Console access

## Step-by-Step

### Option 1: OIDC (Recommended)
1. Admin Console → Settings → Reports → Sync to S3 Bucket → OIDC Role → copy IAM Identity Provider URL
2. AWS IAM → Identity Providers → Add provider → OpenID Connect
   - Provider URL: copied from Twingate
   - Audience: `<network-slug>` (e.g., `acme`)
3. Create IAM Policy granting `s3:PutObject` on bucket
4. Create IAM Role → Web identity → attach OIDC provider
   - Add condition: `<network>.twingate.com/oidc:sub` = `events_sync`
5. Admin Console → enter bucket name + IAM Role ARN

### Option 2: IAM User Credentials
1. Create IAM User
2. Attach policy granting `s3:PutObject`
3. Generate Access Key + Secret Access Key
4. Admin Console → enter bucket name, Access Key, Secret

## Configuration Values

| Field | OIDC | IAM User |
|-------|------|----------|
| Bucket name | Required (no `arn:aws:s3:::` prefix) | Required |
| IAM Role ARN | Required | — |
| Access Key | — | Required |
| Secret Access Key | — | Required |

**Minimum IAM Policy (S3 write):**
```json
{"Action": "s3:PutObject", "Resource": "arn:aws:s3:::<bucket>/*"}
```

**SSE-KMS additional permissions:** `kms:GenerateDataKey*`, `kms:Decrypt`

**OIDC condition key:** `<network>.twingate.com/oidc:sub` = `events_sync`

**Terraform versions tested:** Terraform v1.12.2, AWS Provider ~> 6.0.0

## Gotchas
- **Do not** include `arn:aws:s3:::` prefix when entering bucket name in Admin Console
- **AWS opt-in regions** (Jakarta, Hong Kong, Bahrain) require STS V2 tokens: IAM Console → Account Settings → Security Token Service → Global endpoint → change to V2
- Static IAM credentials require manual rotation; not recommended for production
- Admin AWS IAM user needs broad permissions to set up OIDC/user resources (see full policy in source)
- OIDC audience must match network slug exactly

## Related Docs
- [Network Events Schema](https://www.twingate.com/docs/network-events-schema)
- [DNS Filtering Logs Schema](https://www.twingate.com/docs/dns-filtering-logs-schema)
- [Audit Logs Schema](https://www.twingate.com/docs/audit-logs-schema)
- [Twingate Terraform Examples](https://www.twingate.com/docs/terraform)
- [Twingate Pricing](https://www.twingate.com/pricing)