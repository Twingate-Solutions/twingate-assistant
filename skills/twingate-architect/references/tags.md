# Resource Tags

## Summary
Tags are key-value metadata pairs attached to Twingate Resources for organization and filtering. They enable categorization by ownership, environment, application, and other attributes. Tags can be managed via Admin Console or API.

## Key Information
- Each tag is a key-value pair (e.g., `environment: production`)
- Tags appear on Resources and are filterable in the Admin Console under **Network → Resources**
- API support available; Terraform/Pulumi/K8s operator support coming soon
- Suggested completions appear when typing keys/values based on existing Network tags

## Prerequisites
- Admin Console access or API credentials
- Resources already created in Twingate

## Tag Requirements / Constraints
| Property | Constraint |
|----------|-----------|
| Max tags per Resource | 64 |
| Keys per Resource | Unique (one per key name) |
| Case sensitivity | Both keys and values are case sensitive |
| Key length | 1–128 characters |
| Value length | 1–256 characters |
| Prohibited key prefix | Cannot start with `tg` (e.g., `tg_remote_network` is invalid) |
| Whitespace | Cannot start/end with whitespace (auto-trimmed) |
| Character set | Any valid UTF-8 |

## Common Tag Patterns
- `owner` → `devops`, `it-team`, `alex@company.com`
- `managed_by` → `terraform`, `pulumi`, `admin_console`, `k8s_operator`
- `environment` → `development`, `staging`, `production`
- `application` → `prometheus`, `kafka`, `proxmox`
- `location` → `sf-office`, `us-west-2`
- `region` → `us-west-2`, `eu-central-1`

## Step-by-Step: Adding Tags (Admin Console)
1. Navigate to **Network → Resources**
2. Create or edit a Resource
3. Click **Add Tag**
4. Set key, then set value (autocomplete suggests existing keys/values)
5. Repeat for additional tags
6. Click save — tags persist with the Resource
7. To remove a tag: click the **✕** icon before saving

## Step-by-Step: Filtering by Tags
1. Navigate to **Network → Resources**
2. Open the **Tags** filter
3. Select **Select Key**, search for desired key
4. Choose **in** (include) or **not in** (exclude)
5. Search and select tag values to filter

## Configuration Values (API)
- Tags manageable via [Twingate API](https://www.twingate.com/docs/api)
- Terraform/Pulumi: future support — will enable importing tags from AWS/GCP

## Gotchas
- Editing a tag key or value is **not possible after creation** — must delete and re-add
- Keys starting with `tg` are **reserved** and prohibited
- Duplicate keys on the same Resource are not allowed
- Tags are most useful only when applied **consistently across all Resources**
- Key/value comparison is **case sensitive** — `Owner` ≠ `owner`

## Related Docs
- [Twingate API](https://www.twingate.com/docs/api)
- Resources documentation
- Terraform / Pulumi / Kubernetes operator (tag support pending)