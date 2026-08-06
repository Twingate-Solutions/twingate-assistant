---
source: https://github.com/Twingate-Labs/tg-aws-tag-sync
type: github
fetched: 2026-08-06
source_version: e4d4a550049d02de55b157252bdcb662642967e5
---

<!-- triage: unassigned -->

# tg-aws-tag-sync

## Summary
AWS Lambda function that monitors AWS resource tag changes via CloudWatch Events and automatically creates/removes Twingate resources and manages group memberships. Triggered by tagging EC2 instances, ECS tasks/services/clusters, and RDS instances with specific `tg_*` tags.

## Key Information
- Deployed as an AWS Serverless Application (SAR) or manually via CloudFormation
- Uses EventBridge/CloudWatch rules to detect tag change events
- Supports EC2 instances, ECS clusters/services/tasks/container instances, and RDS instances
- Auto-fills resource name and address for EC2, ECS Task, and RDS Instance types
- Can be deployed across multiple AWS regions independently

## Prerequisites
- AWS user with permissions to create IAM roles, Lambda functions, and EventBridge rules
- Twingate Network Address (e.g., `acme.twingate.com`)
- Twingate API Key with **Read, Write, and Provision** permissions (generated in Admin Console → Settings)
- Target remote networks must already exist in Twingate before tagging

## Usage / Step-by-Step

**Deploy via AWS Serverless Application Repository:**
1. Navigate to the [SAR listing](https://serverlessrepo.aws.amazon.com/applications/eu-west-2/284996965266/tg-aws-tag-sync)
2. Select Deploy → choose AWS region
3. Input `TwingateNetworkAddress` and `TwingateApiKey`
4. Acknowledge custom IAM role creation
5. Deploy and monitor CloudFormation stack events until complete

**Trigger via AWS tags:**

| Tag Key | Value Format | Effect |
|---|---|---|
| `tg_resource` | `RemoteNetworkNameOrId++ResourceName++ResourceAddress` | Creates Twingate resource; writes `tg_resource_id` back to AWS resource |
| `tg_groups` | `Group1++Group2++Group3` | Adds groups to the Twingate resource |
| `tg_resource_id` (remove) | — | Deletes Twingate resource; removes `tg_resource` and `tg_groups` tags |

## Configuration Values

| Parameter | Description |
|---|---|
| `TwingateNetworkAddress` | Your Twingate network hostname (e.g., `acme.twingate.com`) |
| `TwingateApiKey` | API key with Read/Write/Provision scope |

See [`docs/CONFIGURATION_SUMMARY.md`](./docs/CONFIGURATION_SUMMARY.md) for additional options.

## Gotchas
- **`tg_resource` must be added before `tg_groups`** — adding groups without an existing `tg_resource` tag on the resource has no effect
- **Modifying `tg_resource`** creates a new Twingate resource but does **not** delete the old one — manual cleanup required
- **Removing `tg_resource` or `tg_groups` tags directly** has no effect on Twingate — use `tg_resource_id` removal to delete resources
- **Modifying `tg_groups`** only adds groups; existing groups are never removed from the Twingate resource
- **Modifying `tg_resource_id`** deletes the RDS resource from Twingate (no effect on EC2/ECS)
- Adding `tg_resource_id` manually has no effect and may cause unexpected behavior later
- Remote networks referenced in `tg_resource` must already exist in Twingate

## Related Docs
- [Manual Installation Steps](./docs/MANUAL_INSTALL.md)
- [Configuration Summary](./docs/CONFIGURATION_SUMMARY.md)
- [AWS Serverless Application Repository listing](https://serverlessrepo.aws.amazon.com/applications/eu-west-2/284996965266/tg-aws-tag-sync)