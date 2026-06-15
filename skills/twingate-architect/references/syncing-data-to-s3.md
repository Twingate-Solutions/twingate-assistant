# Syncing Data to AWS S3

## Page Title
Syncing Data to AWS S3 (Twingate → AWS S3)

## Summary
Twingate can sync audit logs, network events, DNS filtering logs, and DLP events to an AWS S3 bucket in JSON format every 5 minutes. Supports two auth methods: OIDC IAM Role (recommended) or static IAM User credentials. Available on Business and Enterprise plans only.

## Key Information
- Files written every ~5 minutes; filename format: `2025-07-25T18:20:00+00:00.json`
- Event types: `network_access`, `dns_filtering`, `audit_log`, `data_loss_prevention`
- Events can take up to 10 minutes to appear after first configuration
- No files written to S3 if no events occurred in that interval
- Supports Terraform (AWS Provider ~> 6.0.0, Terraform >= 1.12.2)

## Prerequisites
- Business or Enterprise Twingate plan
- AWS S3 bucket created
- IAM permissions configured (see below)

## Step-by-Step

### Option 1: OIDC (Recommended)
1. Admin Console → Settings → Reports → Sync to S3 Bucket → OIDC Role → copy IAM Identity Provider URL
2. AWS IAM → Identity Providers → Add Provider → OpenID Connect
   - Provider URL: copied from Twingate
   - Audience: `<network-slug>` (e.g., `acme`)
3. Create IAM Policy granting `s3:PutObject` on bucket
4. Create IAM Role: Web identity → OIDC provider → add condition:
   - Key: `<network>.twingate.com/oidc:sub` | Operator: `StringEquals` | Value: `events_sync`
5. Admin Console → Settings → Reports → Sync to S3 → enter bucket name + IAM Role ARN

### Option 2: IAM User Credentials
1. Create IAM User in AWS
2. Attach policy granting `s3:PutObject`
3. Generate Access Key + Secret Access Key
4. Admin Console → Settings → Reports → Sync to S3 → enter bucket name, Access Key, Secret

## Configuration Values

| Field | OIDC | IAM User |
|-------|------|----------|
| Bucket name | Required (no `arn:aws:s3:::` prefix) | Required |
| IAM Role ARN | Required | — |
| Access Key | — | Required |
| Secret Access Key | — | Required |

**Required IAM Policy (standard):**
```json
{ "Action": "s3:PutObject", "Resource": "arn:aws:s3:::<bucket>/*" }
```
**With SSE-KMS:** also add `kms:GenerateDataKey*` and `kms:Decrypt`

## Gotchas
- **Do not** include `arn:aws:s3:::` prefix when entering bucket name in Admin Console
- **AWS opt-in regions** (Jakarta `ap-southeast-3`, Hong Kong `ap-east-1`, Bahrain `me-south-1`) require STS V2 tokens → update AWS Account Settings → STS Global endpoint → V2
- Static IAM credentials require manual rotation; not recommended for production
- OIDC condition `sub` value must be exactly `events_sync`
- Admin IAM user needs `iam:CreateRole`, `iam:CreateOpenIDConnectProvider`, `S3:PutObject`, and related permissions to set up via Console/Terraform

## Related Docs
- Network Events Schema
- DNS Filtering Logs Schema
- Audit Logs Schema
- Twingate Terraform Examples
- AWS S3 User Guide