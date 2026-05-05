## Syncing Data to S3

Continuous sync of Twingate event logs to an AWS S3 bucket. Available on Business and Enterprise plans only. Events are delivered every 5 minutes.

**Supported Event Types:**
- `network_access` -- network connection events
- `dns_filtering` -- DNS filtering events
- `audit_log` -- Admin Console audit events
- `data_loss_prevention` -- DLP events

**Authentication Methods:**
- **OIDC IAM Role** (recommended) -- no long-lived credentials; uses Twingate's OIDC provider to assume a role
- **IAM User credentials** -- access key + secret stored in Twingate Admin Console

**IAM Policy Requirements:**
- `s3:PutObject` on the target bucket/prefix (both auth methods)
- If using SSE-KMS encryption: `kms:GenerateDataKey*` and `kms:Decrypt` on the KMS key

**OIDC Trust Policy Condition:**
```
"StringEquals": { "twingate.com:sub": "events_sync" }
```

**Terraform Setup (OIDC):**
```hcl
resource "aws_iam_openid_connect_provider" "twingate" {
  url             = "https://twingate.com"
  client_id_list  = ["sts.amazonaws.com"]
  thumbprint_list = ["<thumbprint>"]
}
```

**Gotchas:**
- Business & Enterprise plans only
- Logs may take up to 10 minutes to appear in S3 after initial configuration
- Events are written every 5 minutes; not real-time
- OIDC role requires Twingate's OIDC provider to be registered in IAM before use

**Related Docs:**
- /docs/audit-logs -- Audit log overview
- /docs/detailed-network-event-schema -- JSON schema for network events
- /docs/exporting-network-traffic -- Network traffic export options
