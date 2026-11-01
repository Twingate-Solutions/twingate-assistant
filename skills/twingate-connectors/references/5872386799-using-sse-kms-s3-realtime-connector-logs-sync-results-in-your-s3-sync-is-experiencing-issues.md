---
source: https://help.twingate.com/articles/5872386799-using-sse-kms-s3-realtime-connector-logs-sync-results-in-your-s3-sync-is-experiencing-issues
type: help
fetched: 2026-11-01
source_version: 77b1ec2e153e24d8e845931153322ec7806ebacd811b9ea1aaaa7657efc94fd9
trust: official
---

# Using SSE-KMS with S3 Real-Time Connector Logs

## Page Title
Using SSE-KMS S3 Realtime Connector Logs Sync Results in "Your S3 sync is experiencing issues"

## Summary
When configuring Twingate real-time connection logs to sync to AWS S3 buckets using SSE-KMS encryption, users encounter empty files and repeated sync error alerts. The root cause is missing KMS permissions required by AWS for PutObject and multipart upload operations.

## Key Information
- Affects: AWS S3 real-time connection logs connector using SSE-KMS encryption
- Symptom: Empty log files in S3 bucket + repeated "Your S3 sync is experiencing issues" alert
- Root cause: Twingate connector lacks `kms:GenerateDataKey` and `kms:Decrypt` permissions on the KMS key

## Prerequisites
- Twingate AWS S3 real-time connection logs configured
- SSE-KMS encryption enabled on target S3 bucket
- Access to IAM/KMS policy configuration (Terraform or AWS Console)

## Configuration Values

### Required KMS Permissions
| Permission | Required For |
|---|---|
| `kms:GenerateDataKey` | PutObject and multipart upload |
| `kms:Decrypt` | Downloading/reading encrypted objects; multipart upload |

## Step-by-Step (Terraform Workaround)

Add the following IAM policy statement to grant the Twingate connector role the necessary KMS permissions:

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
- **Both permissions are required** — `kms:GenerateDataKey` alone is insufficient; multipart uploads also require `kms:Decrypt`
- **SSE-S3 avoids this entirely** — if KMS is not a hard requirement, switching to SSE-S3 encryption is the simpler workaround
- Error message ("Your S3 sync is experiencing issues") is generic and does not directly indicate a KMS permissions issue — empty files are the distinguishing symptom

## Workarounds (Summary)
1. **Switch to SSE-S3** — no additional KMS configuration needed
2. **Keep SSE-KMS** — add `kms:GenerateDataKey` and `kms:Decrypt` permissions to the IAM policy for the connector's role on the KMS key ARN

## Related Docs
- [AWS SSE-KMS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html)
- Twingate: AWS S3 real-time connection logs connector setup