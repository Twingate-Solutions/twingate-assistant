---
source: https://help.twingate.com/articles/5872386799-using-sse-kms-s3-realtime-connector-logs-sync-results-in-your-s3-sync-is-experiencing-issues
type: help
fetched: 2026-08-06
source_version: 90c1c71d6ba418c4a649c2a821c9e8042e084f54755f7c290fa4cdb0863f1e25
---

# Using SSE-KMS S3 Realtime Connector Logs Sync Issues

## Page Title
Using SSE-KMS S3 Realtime Connector logs sync results in "Your S3 sync is experiencing issues"

## Summary
When configuring Twingate real-time connection logs to AWS S3 with SSE-KMS encryption, logs fail to write and users receive repeated "Your S3 sync is experiencing issues" errors with empty files. This is caused by missing KMS permissions required for S3 PutObject and multipart upload operations.

## Key Information
- **Affected feature**: AWS S3 real-time connection logs connector
- **Symptom**: Empty log files + repeated "Your S3 sync is experiencing issues" alerts
- **Root cause**: SSE-KMS requires explicit `kms:GenerateDataKey` and `kms:Decrypt` permissions on the KMS key
- **Affected operations**: `PutObject` and multipart uploads to S3

## Prerequisites
- Twingate Connector configured for AWS S3 real-time logs
- Terraform (if using IaC approach)

## Workaround Options

### Option 1: Switch to SSE-S3
Use SSE-S3 encryption instead of SSE-KMS — no additional KMS permissions required.

### Option 2: Add Required KMS Permissions
Grant the connector's IAM role `kms:GenerateDataKey` and `kms:Decrypt` on the KMS key used by the S3 bucket.

## Configuration Values

**Required KMS permissions when using SSE-KMS:**
- `kms:GenerateDataKey` — needed for PutObject and multipart upload initiation
- `kms:Decrypt` — needed for downloading objects and multipart uploads

**Terraform example:**
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

## Gotchas
- Files will be created but **empty** — no error at the file level, making diagnosis non-obvious
- Both `kms:GenerateDataKey` AND `kms:Decrypt` are required; granting only one will still cause failures
- Multipart uploads (large log files) require both permissions, not just `GenerateDataKey`

## Related Docs
- [AWS SSE-KMS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html)
- Twingate: AWS S3 real-time connection logs configuration