# Resource Tags

## Summary
Tags are key-value metadata pairs attachable to Twingate Resources for organization and filtering. They enable categorization by ownership, environment, application, or any custom attribute. Tags can be managed via Admin Console or API.

## Key Information
- Each tag is a key-value pair (e.g., `environment: production`)
- Max **64 tags per Resource**
- Tags are used for filtering in the Admin Console under **Network → Resources**
- Manageable via Admin Console, Twingate API; Terraform/Pulumi/K8s operator support coming soon
- Tags suggested from existing network tags as you type

## Prerequisites
- Admin Console access or API credentials
- Resources already created in Twingate network

## Tag Requirements / Constraints
- Max 1 tag per unique key per Resource
- Keys and values are **case sensitive**
- Keys: 1–128 characters; Values: 1–256 characters
- Keys **cannot start with `tg`** (e.g., `tg_remote_network` is prohibited)
- Leading/trailing whitespace automatically stripped
- Valid UTF-8 characters allowed

## Step-by-Step: Adding Tags via Admin Console
1. Navigate to **Network → Resources**
2. Open a Resource (create or edit)
3. Click **Add Tag**
4. Enter key, then value (autocomplete suggests existing keys/values)
5. Add additional tags as needed
6. Click save to persist tags
7. To remove a tag, click the **✕** icon before saving

## Step-by-Step: Filtering by Tags
1. Navigate to **Network → Resources**
2. Use the **Tags** filter in the Resource table
3. Select **Select Key**, search for desired key
4. Choose filter mode: **in** (include) or **not in** (exclude)
5. Search and select tag values

## Common Tag Patterns

| Key | Example Values | Purpose |
|-----|---------------|---------|
| `owner` | `devops`, `alex@company.com` | Ownership |
| `managed_by` | `terraform`, `admin_console` | Management system |
| `application` | `prometheus`, `kafka` | Running app |
| `environment` | `development`, `staging`, `production` | Env classification |
| `location` | `sf-office`, `us-west-2` | Physical/virtual location |
| `region` | `us-west-2`, `eu-central-1` | Cloud region |

## Gotchas
- A Resource **cannot have two tags with the same key** — adding a duplicate key requires removing the existing one
- Keys starting with `tg` are reserved and will be rejected
- Tag key/value cannot be empty strings (minimum 1 character)
- Tags cannot be edited after creation — must delete and re-add to change key or value

## Related Docs
- [Twingate API](https://www.twingate.com/docs/api) — manage tags programmatically at scale
- Terraform/Pulumi/Kubernetes operator — tag support forthcoming
- Resources documentation