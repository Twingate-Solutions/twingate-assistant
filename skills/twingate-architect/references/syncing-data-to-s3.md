# Syncing Data to AWS S3

## Page Title
Syncing Data to AWS S3 (Twingate → AWS S3)

## Summary
Twingate (Business/Enterprise) can sync audit logs, network events, DNS filtering logs, and DLP events to an AWS S3 bucket in JSON format every 5 minutes. Two auth methods are supported: OIDC IAM Role (recommended) and static IAM User credentials. Setup is available via Admin Console UI or Terraform.

## Key Information
- **Plans**: Business & Enterprise only
- **Sync interval**: Every 5 minutes; up to 10 minutes for first appearance
- **File format**: JSON, filename format `2025-07-25T18:20:00+00:00.json`
- **Event types**: `network_access`, `dns_filtering`, `audit_log`, `data_loss_prevention`
- No file written if no events occurred in interval

## Prerequisites
- Business or Enterprise Twingate plan
- AWS S3 bucket (existing or new)
- IAM permissions to create roles/policies/users in AWS

## Step-by-Step

### Option 1: OIDC (Recommended)
1. In Twingate Admin Console → Settings → Reports → Sync to S3 Bucket → OIDC Role → copy IAM Identity Provider URL
2. In AWS: IAM → Identity Providers → Add Provider → OpenID Connect
   - Provider URL: copied from Twingate
   - Audience: `<your-network-slug>` (e.g., `acme`)
3. Create IAM Policy granting `s3:PutObject` on bucket
4. Create IAM Role: Trusted entity = Web Identity; add condition:
   - Key: `<network>.twingate.com/oidc:sub` = `events_sync`
   - Audience: network slug
5. In Twingate Console: enter bucket name + IAM Role ARN

### Option 2: IAM User Credentials
1. Create IAM User in AWS
2. Create policy granting `s3:PutObject` and attach to user
3. Generate Access Key + Secret Access Key
4. In Twingate Console: enter bucket name, Access Key, Secret Key

## Configuration Values

| Field | OIDC | IAM User |
|-------|------|----------|
| Bucket name | Required (no `arn:aws:s3:::` prefix) | Required |
| IAM Role ARN | Required | — |
| Access Key | — | Required |
| Secret Access Key | — | Required |

**Required IAM permissions (s3:PutObject):**
```json
{"Action": "s3:PutObject", "Resource": "arn:aws:s3:::<bucket>/*"}
```
**Additional for SSE-KMS:** `kms:GenerateDataKey*`, `kms:Decrypt`

**Terraform versions tested:** Terraform `v1.12.2`, AWS Provider `~> 6.0.0`

## Gotchas
- **Do NOT include** `arn:aws:s3:::` prefix when entering bucket name in UI
- **AWS opt-in regions** (Jakarta `ap-southeast-3`, Hong Kong `ap-east-1`, Bahrain `me-south-1`) require STS V2 tokens — change Global endpoint to V2 in IAM Account Settings
- Static IAM credentials require manual rotation; not recommended for production
- First sync can take up to 10 minutes after configuration

## Related Docs
- [Network Events Schema](https://www.twingate.com/docs/network-events-schema)
- [DNS Filtering Logs Schema](https://www.twingate.com/docs/dns-filtering-logs-schema)
- [Audit Logs Schema](https://www.twingate.com/docs/audit-logs-schema)
- [Terraform Examples](https://www.twingate.com/docs/terraform)
- [AWS S3 User Guide](https://docs.aws.amazon.com/s3/)