# Resource Tags

## Summary
Tags are key-value metadata pairs attachable to Twingate Resources for organization and filtering. They enable categorization by ownership, environment, application, or any custom attribute. Tags can be managed via Admin Console or API.

## Key Information
- Each tag is a key-value pair (e.g., `environment: production`)
- Tags appear on Resources and are filterable in the Admin Console under Network → Resources
- API management is available; Terraform/Pulumi/K8s operator support is upcoming
- Twingate auto-suggests existing keys/values when adding new tags

## Prerequisites
- Admin Console access or API credentials
- Resources already created in Twingate

## Tag Requirements / Constraints
- Max **64 tags** per Resource
- **One tag per key** per Resource (no duplicate keys)
- Keys and values are **case sensitive**
- Valid **UTF-8 characters** allowed
- Leading/trailing whitespace is **auto-stripped**
- Keys **cannot start with `tg`** (e.g., `tg_remote_network` is prohibited)
- Key length: **1–128 characters**
- Value length: **1–256 characters**

## Configuration Values

| Field | Constraint |
|-------|-----------|
| Key prefix `tg` | Prohibited |
| Max tags/resource | 64 |
| Key max length | 128 chars |
| Value max length | 256 chars |

## Common Tag Patterns

**Ownership:**
- `owner` → `devops`, `it-team`, `alex@autoco.example`
- `managed_by` → `terraform`, `pulumi`, `admin_console`, `k8s_operator`

**Technical:**
- `application` → `prometheus`, `kafka`, `proxmox`
- `environment` → `development`, `staging`, `production`
- `location` → `sf-office`, `us-west-2`
- `region` → `us-west-2`, `eu-central-1`

## Step-by-Step: Adding Tags (Admin Console)
1. Navigate to a Resource (create or edit)
2. Click **Add Tag**
3. Enter key → enter value (autocomplete suggests existing keys/values)
4. Repeat for additional tags
5. Save the Resource
6. To remove a tag: click the **✕** icon before saving

## Step-by-Step: Filtering by Tags
1. Go to **Network → Resources**
2. Click the **Tags** filter
3. Select **Select Key** → search for key
4. Choose **in** (include) or **not in** (exclude)
5. Select tag values to filter

## Gotchas
- Tag key/value **cannot be edited after creation**; delete and recreate to change
- Duplicate keys on same Resource are not allowed — last one does not override, it's rejected
- Keys starting with `tg` are reserved and will be rejected
- Terraform/Pulumi/K8s operator support not yet available (API only for programmatic management)

## Related Docs
- Twingate API (for programmatic tag management)
- Resources documentation
- Terraform provider (upcoming tag support)