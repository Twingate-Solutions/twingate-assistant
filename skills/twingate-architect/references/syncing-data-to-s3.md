# Syncing Data to AWS S3

## Page Title
Syncing Data to AWS S3 (Twingate → S3)

## Summary
Twingate can sync audit logs, network events, DNS filtering logs, and DLP events to an AWS S3 bucket in JSON format every 5 minutes. Supports two auth methods: OIDC IAM Role (recommended) or static IAM User credentials. Available on Business and Enterprise plans only.

## Key Information
- Files written every ~5 minutes; filename format: `2025-07-25T18:20:00+00:00.json`
- Event types: `network_access`, `dns_filtering`, `audit_log`, `data_loss_prevention`
- Initial sync delay up to 10 minutes after configuration
- No file written if no events occurred in the interval
- Configurable via Admin Console UI or Terraform

## Prerequisites
- Business or Enterprise Twingate plan
- AWS S3 bucket
- IAM permissions to create roles/policies/users in AWS

## Step-by-Step

### Option 1: OIDC (Recommended)
1. Admin Console → Settings → Reports → Sync to S3 Bucket → OIDC Role → copy IAM Identity Provider URL
2. AWS IAM → Identity Providers → Add Provider → OpenID Connect
   - Provider URL: copied URL from step 1
   - Audience: `<your-network-slug>` (e.g., `acme`)
3. Create IAM Policy granting `s3:PutObject` on bucket ARN
4. Create IAM Role → Web Identity → select OIDC provider
   - Condition: `<network>.twingate.com/oidc:sub` = `events_sync`
   - Attach policy from step 3
5. Admin Console → enter bucket name + IAM Role ARN

### Option 2: IAM User Credentials
1. AWS IAM → Create User
2. Create policy granting `s3:PutObject` → attach to user
3. Create Access Key + Secret Access Key for user
4. Admin Console → enter bucket name, Access Key, Secret Key

## Configuration Values

| Field | OIDC | IAM User |
|-------|------|----------|
| Bucket name | Required (no `arn:aws:s3:::` prefix) | Required |
| IAM Role ARN | Required | — |
| Access Key | — | Required |
| Secret Access Key | — | Required |

**Required IAM policy (both methods):**
```json
{"Action": "s3:PutObject", "Resource": "arn:aws:s3:::<bucket>/*"}
```
**SSE-KMS additional permissions:** `kms:GenerateDataKey*`, `kms:Decrypt`

## Gotchas
- **Do NOT include `arn:aws:s3:::` prefix** when entering bucket name in Admin Console
- **Opt-in AWS regions** (Jakarta, Hong Kong, Bahrain) require STS V2 tokens — change in IAM Console → Account Settings → STS Global Endpoint → V2
- Static IAM credentials require manual rotation; not recommended for production
- OIDC `sub` condition value must be exactly `events_sync`
- Terraform tested with: Terraform `v1.12.2`, AWS Provider `~> 6.0.0`

## Related Docs
- Network Events Schema
- DNS Filtering Logs Schema
- Audit Logs Schema
- Twingate Terraform Examples
- AWS S3 User Guide