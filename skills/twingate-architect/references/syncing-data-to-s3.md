# Syncing Data to AWS S3

## Page Title
Syncing Data to AWS S3 (Twingate → AWS S3)

## Summary
Twingate can sync audit logs, network events, DNS filtering logs, and DLP events to an AWS S3 bucket in JSON format every 5 minutes. Supports two auth methods: OIDC IAM Role (recommended) or static IAM User credentials. Available on Business and Enterprise plans only.

## Key Information
- Files written as JSON, filename format: `2025-07-25T18:20:00+00:00.json`
- Sync interval: every 5 minutes; up to 10 minutes for first appearance
- No files written if no events to sync
- Four event types: `network_access`, `dns_filtering`, `audit_log`, `data_loss_prevention`
- Config location: Admin Console → Settings → Reports → Sync to S3 Bucket

## Prerequisites
- Business or Enterprise Twingate plan
- Existing AWS S3 bucket
- IAM permissions to create roles/policies/providers in AWS

## Authentication Options

### Option 1: OIDC IAM Role (Recommended)
Uses short-lived credentials; no long-lived access keys.

**Steps:**
1. In Twingate Admin Console: Settings → Reports → Sync to S3 Bucket → OIDC Role → copy IAM Identity Provider URL
2. In AWS: IAM → Identity Providers → Add Provider → OpenID Connect
   - Provider URL: copied from Twingate console
   - Audience: `<network-slug>` (e.g., `acme` from `acme.twingate.com`)
3. Create IAM Policy with `s3:PutObject` on bucket
4. Create IAM Role:
   - Trusted entity: Web identity
   - Add condition: `<network>.twingate.com/oidc:sub` = `StringEquals` = `events_sync`
5. In Twingate console: enter bucket name + IAM Role ARN

### Option 2: IAM User Credentials
Static credentials; manual rotation required.

**Steps:**
1. Create IAM User in AWS
2. Create and attach policy with `s3:PutObject`
3. Generate Access Key + Secret Access Key
4. In Twingate console: enter bucket name + Access Key + Secret

## Configuration Values

| Field | OIDC | IAM User |
|-------|------|----------|
| Bucket name | ✓ (no `arn:aws:s3:::` prefix) | ✓ |
| IAM Role ARN | ✓ | — |
| Access Key | — | ✓ |
| Secret Access Key | — | ✓ |

**Required IAM Actions (sync role/user):**
- `s3:PutObject` on `arn:aws:s3:::<bucket>/*`
- If SSE-KMS: also `kms:GenerateDataKey*`, `kms:Decrypt`

**Terraform versions tested:** Terraform `v1.12.2`, AWS Provider `~> 6.0.0`

## Gotchas
- Do **not** include `arn:aws:s3:::` prefix when entering bucket name in Twingate console
- OIDC condition key must be `events_sync` for the `sub` claim
- SSE-KMS encrypted buckets require additional KMS permissions
- Static IAM credentials require manual rotation and are not recommended for production
- Admin AWS user needs explicit IAM management permissions (CreateRole, CreateOpenIDConnectProvider, CreateUser, CreateAccessKey, etc.) to set up via Console/Terraform

## Related Docs
- [Network Events Schema](https://www.twingate.com/docs/network-events-schema)
- [DNS Filtering Logs Schema](https://www.twingate.com/docs/dns-filtering-logs-schema)
- [Audit Logs Schema](https://www.twingate.com/docs/audit-logs-schema)
- [Terraform Examples](https://www.twingate.com/docs/terraform)
- [Twingate Pricing](https://www.twingate.com/pricing)