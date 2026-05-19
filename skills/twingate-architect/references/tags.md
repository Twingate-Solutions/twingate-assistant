# Resource Tags

## Summary
Tags are key-value metadata pairs attached to Twingate Resources for organization and filtering. They enable categorization by ownership, environment, or technical context. Tags can be managed via Admin Console or API.

## Key Information
- Each tag is a **key-value pair** (e.g., `environment: production`)
- Tags enable filtering in the Resources table (Network → Resources → Tags filter)
- Filter supports **include** (`in`) and **exclude** (`not in`) logic
- API management available; Terraform/Pulumi/K8s operator support coming soon

## Tag Requirements / Constraints
- Max **64 tags** per Resource
- **One tag per key** per Resource (no duplicate keys)
- Keys and values are **case sensitive**
- Valid UTF-8 characters allowed; leading/trailing whitespace auto-stripped
- Keys **cannot start with `tg`** (e.g., `tg_remote_network` is prohibited)
- Key length: 1–128 characters
- Value length: 1–256 characters

## Common Tag Patterns

| Key | Example Values | Purpose |
|-----|---------------|---------|
| `owner` | `devops`, `alex@company.com` | Ownership |
| `managed_by` | `terraform`, `k8s_operator` | Management system |
| `environment` | `development`, `staging`, `production` | Environment |
| `application` | `prometheus`, `kafka` | Running service |
| `location` | `sf-office`, `us-west-2` | Physical/virtual location |
| `region` | `us-west-2`, `eu-central-1` | Cloud region |

## Step-by-Step: Adding Tags (Admin Console)
1. Navigate to Network → Resources
2. Create or edit a Resource
3. Click **Add Tag**
4. Enter key (autocomplete suggests existing keys)
5. Enter value (autocomplete suggests existing values)
6. Repeat as needed; click remove icon (✕) to delete
7. Save the Resource

## Step-by-Step: Filtering by Tags
1. Navigate to Network → Resources
2. Click **Tags** filter
3. Select **Select Key**, search for desired key
4. Choose `in` (include) or `not in` (exclude)
5. Search and select tag values

## Gotchas
- Tag key/value **cannot be edited** after creation — delete and re-add to change
- Keys starting with `tg` are reserved and prohibited
- Duplicate keys on the same Resource are not allowed
- Terraform/Pulumi/K8s operator tag support is **not yet available** (API only currently)
- Whitespace trimming is automatic but tags are otherwise case-sensitive

## Best Practices
- Standardize key names across all Resources (avoid mixing `owner` and `owner-team`)
- Tag **all** Resources for maximum utility
- Use API/Terraform to import tags from cloud providers (AWS, GCP) at scale

## Related Docs
- Twingate API (tag management)
- Terraform Provider
- Pulumi Integration
- Kubernetes Operator