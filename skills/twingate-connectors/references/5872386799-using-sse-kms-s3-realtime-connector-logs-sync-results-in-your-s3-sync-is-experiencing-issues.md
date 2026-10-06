---
source: https://help.twingate.com/articles/5872386799-using-sse-kms-s3-realtime-connector-logs-sync-results-in-your-s3-sync-is-experiencing-issues
type: help
fetched: 2026-10-04
source_version: 92f80fa4d87e63587bb0df38cd481f51448a27a8e58d10d4cabffede5ece209b
trust: official
---

# Using SSE-KMS with S3 Real-Time Connector Logs

## Page Title
Using SSE-KMS S3 Realtime Connector logs sync results in "Your S3 sync is experiencing issues"

## Summary
When configuring Twingate real-time connection logs to sync to an SSE-KMS-encrypted S3 bucket, users see empty log files and repeated sync error alerts. The root cause is missing KMS IAM permissions required for S3 PutObject and multipart upload operations.

## Key Information
- Affects: AWS S3 real-time connection logs connector (configured via Terraform)
- Symptom: Empty files in S3 bucket + repeated "Your S3 sync is experiencing issues" notifications
- Root cause: The connector role lacks `kms:GenerateDataKey` and `kms:Decrypt` permissions on the KMS key used for SSE-KMS

## Prerequisites
- Twingate real-time connection logs configured for AWS S3
- SSE-KMS encryption enabled on target S3 bucket
- IAM policy control over the KMS key

## Workaround Options

### Option 1 (Simplest)
Switch bucket encryption from **SSE-KMS** to **SSE-S3** — no KMS permissions required.

### Option 2: Grant Required KMS Permissions
Add the following IAM policy statement granting `kms:GenerateDataKey` and `kms:Decrypt` to the role used by the connector:

```hcl
statement {
  actions = [
    "kms:GenerateDataKey",
    "kms:Decrypt"
  ]
  resources = [
    aws_kms_key.this.arn
  ]
}
```

## Configuration Values

| Permission | Required For |
|---|---|
| `kms:GenerateDataKey` | `PutObject` and multipart upload to KMS-encrypted S3 |
| `kms:Decrypt` | Downloading/reading objects encrypted with KMS key |

## Gotchas
- Both permissions are required — `GenerateDataKey` alone is insufficient if multipart uploads or reads are involved
- Empty files (not missing files) are the symptom; the bucket write succeeds but encryption fails silently
- This is an AWS-enforced requirement, not a Twingate bug

## Related Docs
- [AWS SSE-KMS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html)
- Twingate: AWS S3 real-time connection logs setup (Terraform)