# Resource Tags

## Summary
Tags are key-value metadata pairs attachable to Twingate Resources for organization and filtering. They enable categorization by owner, environment, purpose, or other attributes. Tags can be managed via Admin Console or API.

## Key Information
- Each tag is a **key-value pair** (e.g., `environment: production`)
- Tags appear on Resources in the Admin Console under Network → Resources
- Filterable via the **Tags** filter in the Resource table (include/exclude by key+value)
- API support available; Terraform/Pulumi/K8s operator support coming soon

## Prerequisites
- Admin Console access
- Resources already created in your Network

## Tag Requirements / Constraints
- Max **64 tags** per Resource
- Keys must be **unique per Resource** (no duplicate keys)
- Keys and values are **case sensitive**
- Valid UTF-8 characters allowed
- No leading/trailing whitespace (auto-stripped)
- Keys **cannot start with `tg`** (e.g., `tg_remote_network` is prohibited)
- Key length: 1–128 characters
- Value length: 1–256 characters

## Configuration Values

### Common Tag Keys
| Key | Purpose | Example Values |
|-----|---------|----------------|
| `owner` | Resource owner | `devops`, `alex@company.com` |
| `managed_by` | Management system | `terraform`, `admin_console`, `k8s_operator` |
| `application` | Running application | `prometheus`, `kafka` |
| `environment` | Deployment environment | `development`, `staging`, `production` |
| `location` | Physical/virtual location | `sf-office`, `us-west-2` |
| `region` | Cloud provider region | `us-west-2`, `eu-central-1` |

## Step-by-Step: Adding Tags
1. Navigate to Admin Console → Network → Resources
2. Create or edit a Resource
3. Click **Add Tag**
4. Enter key (autocomplete suggests existing keys)
5. Enter value (autocomplete suggests existing values)
6. Repeat as needed; click ✕ to remove a tag
7. Save the Resource

## Step-by-Step: Filtering by Tags
1. Navigate to Admin Console → Network → Resources
2. Click the **Tags** filter
3. Select **Select Key**, search for desired key
4. Choose **in** (include) or **not in** (exclude)
5. Search and select target values

## Gotchas
- Tag keys starting with `tg` are **reserved and prohibited**
- Keys are unique per Resource — adding a second tag with the same key is not allowed
- Tag key/value can only be edited **during creation**; to change, remove and re-add
- Terraform/Pulumi/K8s operator support is **not yet available** (API only for automation)
- Cloud provider tag import (AWS/GCP → Twingate) requires API/Terraform integration

## Related Docs
- Twingate API (for programmatic tag management)
- Terraform Provider
- Pulumi Provider
- Kubernetes Operator