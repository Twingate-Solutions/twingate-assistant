---
source: https://help.twingate.com/articles/5872386799-using-sse-kms-s3-realtime-connector-logs-sync-results-in-your-s3-sync-is-experiencing-issues
type: help
fetched: 2026-11-08
source_version: 6a0f75a0ffd9289e9a3bec82dd8fa4921d793113d156c03c32bc77afb1683577
trust: official
---

# Using SSE-KMS S3 Real-Time Connector Logs Sync Issues

## Page Title
Using SSE-KMS S3 Realtime Connector logs sync results in "Your S3 sync is experiencing issues"

## Summary
When configuring Twingate real-time connection logs to sync to AWS S3 buckets using SSE-KMS encryption, users encounter empty files and repeated "Your S3 sync is experiencing issues" errors. This is caused by missing KMS permissions required for S3 `PutObject` and multipart upload operations.

## Key Information
- Affects: AWS S3 real-time connection logs connector with SSE-KMS encryption
- Symptom: Empty log files in S3 and repeated sync error notifications
- Root cause: Missing `kms:GenerateDataKey` and `kms:Decrypt` permissions on the KMS key

## Prerequisites
- Twingate Connector configured for AWS S3 real-time connection logs
- S3 bucket using SSE-KMS encryption
- IAM/KMS policy management access

## Workarounds

### Option 1: Switch to SSE-S3
Use SSE-S3 instead of SSE-KMS to avoid KMS permission requirements entirely.

### Option 2: Add Required KMS Permissions
Grant `kms:GenerateDataKey` and `kms:Decrypt` on the KMS key used by the S3 bucket.

## Configuration Values

**Required KMS actions:**
- `kms:GenerateDataKey` — needed for `PutObject` and multipart uploads
- `kms:Decrypt` — needed for downloading/reading encrypted objects

**Terraform example:**
```hcl
statement {
  actions = [
    "kms:GenerateDataKey",
    "kms:Decrypt"
  ]
  resources = [
    aws_kms_key_this.arn
  ]
}
```

## Gotchas
- Both permissions are required even if the connector is only writing logs (multipart uploads require both `GenerateDataKey` and `Decrypt`)
- Missing either permission causes silent failures — files are created but remain empty
- Error message ("Your S3 sync is experiencing issues") is generic and does not indicate KMS as the root cause

## Related Docs
- [AWS: Using server-side encryption with AWS KMS (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html)
- Twingate: AWS S3 real-time connection logs connector configuration