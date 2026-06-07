# Resource Tags

## Summary
Tags are key-value metadata pairs attached to Twingate Resources for organization and filtering. They enable categorizing Resources by ownership, environment, application, or any custom attribute. Tags can be managed via Admin Console or API.

## Key Information
- Each tag is a **key-value pair** (e.g., `environment: production`)
- Tags appear on Resources in the Admin Console under Network → Resources
- Filterable via the **Tags filter** in the Resource table (include/exclude by key+value)
- API-managed tags supported now; Terraform/Pulumi/K8s operator support coming soon

## Prerequisites
- Admin Console access or Twingate API credentials
- Resources already created in the Network

## Tag Requirements
| Constraint | Detail |
|---|---|
| Max tags per Resource | 64 |
| Unique keys per Resource | One tag per key |
| Case sensitivity | Keys and values are case sensitive |
| Key length | 1–128 characters |
| Value length | 1–256 characters |
| Forbidden key prefix | Cannot start with `tg` (e.g., `tg_remote_network` prohibited) |
| Whitespace | Cannot start/end with whitespace (auto-trimmed) |
| Character set | Any valid UTF-8 |

## Common Tag Keys
- `owner` — team or person (e.g., `devops`, `alex@company.com`)
- `managed_by` — management system (e.g., `terraform`, `admin_console`)
- `application` — software running (e.g., `prometheus`, `kafka`)
- `environment` — deployment tier (e.g., `development`, `staging`, `production`)
- `location` — physical/virtual location (e.g., `sf-office`, `us-west-2`)
- `region` — cloud provider region (e.g., `eu-central-1`)

## Step-by-Step: Adding Tags via Admin Console
1. Navigate to a Resource (create or edit)
2. Click **Add Tag**
3. Enter key (autocomplete suggests existing keys in Network)
4. Enter value (autocomplete suggests existing values for that key)
5. Repeat for additional tags
6. Save the Resource — tags save with Resource

## Step-by-Step: Filtering Resources by Tags
1. Go to **Network → Resources**
2. Click **Tags** filter
3. Select **Select Key**, search for desired key
4. Choose filter mode: **in** (include) or **not in** (exclude)
5. Search and select tag values to filter by

## Gotchas
- Tag keys starting with `tg` are **reserved and prohibited**
- A Resource cannot have two tags with the same key — adding a duplicate key overwrites or is rejected
- Tags are **case sensitive** — `Owner` and `owner` are different keys
- Tag key/value cannot be edited after creation — must remove and re-add
- Terraform/Pulumi/K8s operator support is not yet available (API only for programmatic management)

## Related Docs
- [Twingate API](https://www.twingate.com/docs/api) — manage tags programmatically
- [Resources documentation](https://www.twingate.com/docs/resources)
- Terraform, Pulumi, Kubernetes operator (tag support forthcoming)