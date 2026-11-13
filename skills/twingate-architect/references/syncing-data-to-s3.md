---
source: https://www.twingate.com/docs/syncing-data-to-s3
type: docs
fetched: 2026-11-13
source_version: 0d30389efaa0ffafbae40383bb524661cc06c0b2fde1041b9c4f27ae6d0dba12
trust: official
---

# Page Title
Syncing Data to AWS S3 (Twingate)

## Summary
Twingate can push audit logs, network events, DNS filtering logs, and DLP events to an AWS S3 bucket as JSON every ~5 minutes. Authentication is either an OIDC IAM role (recommended) or static IAM user credentials. Setup is done in the Admin Console or via Terraform. Business and Enterprise plans only.

## Key Information
- Each sync writes one JSON file named like `2025-07-25T18:20:00+00:00.json`, with separate objects per event.
- Event types: `network_access`, `dns_filtering`, `audit_log`, `data_loss_prevention`.
- Each event has `event_type` and `event` (with `version` and `time`).
- No events means no file is written.
- First logs appear within about 10 minutes. Events can lag up to 10 minutes.
- OIDC role: short-lived credentials, no long-lived keys, recommended for production.
- IAM user: static keys that must be rotated manually. Not recommended for production or regulated environments.
- Sync status is shown at Settings → Reports (upper right).

## Prerequisites
- Business or Enterprise plan.
- An S3 bucket.
- An AWS admin with IAM permissions to create roles, policies, OIDC providers, users, and access keys.
- Terraform (optional): tested with v1.12.2 and AWS provider ~> 6.0.0.

## Step-by-Step
1. Create or identify an S3 bucket.
2. Create an IAM policy granting `s3:PutObject` on `arn:aws:s3:::<S3BucketName>/*`. For SSE-KMS, also add `kms:GenerateDataKey*` and `kms:Decrypt`.
3. **OIDC path:**
   - In the Admin Console, go to Settings → Reports → Sync to S3 Bucket → OIDC Role and copy the IAM Identity Provider URL.
   - In AWS, go to IAM → Identity Providers → Add provider → OpenID Connect. Use that URL as the provider URL and your network slug as the audience.
   - Create a role with Web identity as the trusted entity, using that provider and audience. Add the condition `<network>.twingate.com/oidc:sub` StringEquals `events_sync`. Attach the policy.
4. **IAM user path:** create a user, attach the policy, generate an access key and secret, and optionally add a bucket policy restricting `PutObject` to that user.
5. In Settings → Reports → Sync to S3 Bucket, enter the bucket name plus the Role ARN (OIDC) or the access key and secret (IAM).

## Configuration Values
- OIDC provider URL: `https://<slug>.twingate.com/oidc`
- Audience / `client_id_list`: network slug (e.g. `acme`)
- Trust condition: `<slug>.twingate.com/oidc:sub` = `events_sync`, and `:aud` = slug (Terraform)
- Assume action: `sts:AssumeRoleWithWebIdentity`
- Console inputs: OIDC needs bucket name and IAM Role ARN. IAM needs bucket name, access key, and secret.
- Terraform variables: `tenant_slug`, `bucket_name`. Output: `twingate_s3_sync_role_arn`.

## Gotchas
- Do NOT include the `arn:aws:s3:::` prefix in the bucket name field.
- Opt-in regions (ap-southeast-3, ap-east-1, me-south-1) require V2 STS session tokens. Fix at IAM → Account Settings → STS Global endpoint → set Session Tokens to V2, then retry.
- An immediate failure usually means a wrong bucket name, wrong keys, or a missing `s3:PutObject`.
- SSE-KMS needs the extra KMS permissions.
- The Terraform IAM user example outputs the secret key (marked sensitive). Store it securely.

## Related Docs
- Network Events Schema
- DNS Filtering Logs Schema
- Audit Logs Schema
- Twingate Terraform Examples
- AWS S3 User Guide