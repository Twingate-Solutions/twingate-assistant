---
source: https://help.twingate.com/articles/5872386799-using-sse-kms-s3-realtime-connector-logs-sync-results-in-your-s3-sync-is-experiencing-issues
type: help
fetched: 2026-09-06
source_version: 7b643bd0a565224ea1150f127a77a063809182edaba2e6505727c51aa30557a1
---

# Using SSE-KMS S3 Realtime Connector Logs Sync Issues

## Page Title
Using SSE-KMS S3 Realtime Connector logs sync results in "Your S3 sync is experiencing issues"

## Summary
When configuring Twingate real-time connection logs to sync to AWS S3 using SSE-KMS encryption, the sync fails with empty files and repeated "Your S3 sync is experiencing issues" errors. The root cause is missing KMS permissions required by AWS for encrypted S3 object operations.

## Key Information
- Affects: AWS S3 real-time connection logs connector using SSE-KMS encryption
- Symptom: Empty files written to S3 bucket + repeated sync error notifications
- Root cause: Missing `kms:GenerateDataKey` and `kms:Decrypt` IAM permissions on the KMS key

## Prerequisites
- Twingate Connector configured for AWS S3 real-time connection logs
- Terraform used for infrastructure configuration
- SSE-KMS encryption enabled on the target S3 bucket

## Configuration Values

### Required KMS Permissions (when using SSE-KMS)
| Permission | Required For |
|---|---|
| `kms:GenerateDataKey` | `PutObject` requests / multipart uploads |
| `kms:Decrypt` | Downloading encrypted objects / multipart uploads |

## Step-by-Step Fix

**Option 1 (Simplest): Switch to SSE-S3**
- Change bucket encryption from SSE-KMS to SSE-S3 to avoid KMS permission requirements entirely.

**Option 2: Add required KMS permissions**
Add the following Terraform IAM policy statement to grant the connector the necessary KMS key permissions:

```hcl
# apply kms:GenerateDataKey and kms:Decrypt
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
- Both `kms:GenerateDataKey` AND `kms:Decrypt` are required — missing either one causes failure
- Multipart uploads require both permissions simultaneously
- Errors appear as empty files rather than explicit permission denied messages, making diagnosis non-obvious
- The `resources` field must point to the specific KMS key ARN used for bucket encryption

## Related Docs
- [AWS SSE-KMS Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html)
- Twingate: AWS S3 real-time connection logs connector setup
- Twingate: Terraform provider configuration for connectors