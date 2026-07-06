# Resource Tags

## Summary
Tags are key-value metadata pairs attachable to Twingate Resources for organization and filtering. They enable categorization by attributes like ownership, environment, and application. Tags can be managed via Admin Console or API.

## Key Information
- Each tag is a key-value pair (e.g., `environment: production`)
- Used for: adding context, filtering/searching Resources in Admin Console
- Manageable via Admin Console, Twingate API; Terraform/Pulumi/K8s operator support coming soon
- Filter UI located at: **Network → Resources → Tags filter** (supports `in` / `not in` operators)

## Prerequisites
- Admin Console access
- Resources already created in Network
- API credentials if managing programmatically

## Tag Requirements / Constraints
| Property | Constraint |
|---|---|
| Max tags per Resource | 64 |
| Key uniqueness | One tag per key per Resource |
| Case sensitivity | Keys and values are case-sensitive |
| Character set | Any valid UTF-8 |
| Leading/trailing whitespace | Auto-stripped |
| Prohibited key prefix | Cannot start with `tg` (e.g., `tg_remote_network` is invalid) |
| Key length | 1–128 characters |
| Value length | 1–256 characters |

## Common Tag Keys
- `owner` — e.g., `devops`, `alex@company.com`
- `managed_by` — e.g., `terraform`, `admin_console`, `pulumi`
- `application` — e.g., `prometheus`, `kafka`
- `environment` — e.g., `development`, `staging`, `production`
- `location` — e.g., `sf-office`, `us-west-2`
- `region` — e.g., `us-west-2`, `eu-central-1`

## Adding Tags (Admin Console)
1. Navigate to a Resource (create or edit)
2. Click **Add Tag**
3. Enter key (autocomplete suggests existing keys)
4. Enter value (autocomplete suggests existing values)
5. Repeat as needed; click remove icon (✕) to delete a tag
6. Save the Resource to persist tags

> **Note:** Tags can only be edited during creation. To change a tag, remove it and add a new one.

## Filtering by Tags (Admin Console)
1. Go to **Network → Resources**
2. Click **Tags** filter
3. Select **Select Key**, search for desired key
4. Choose `in` (include) or `not in` (exclude)
5. Search and select tag values

## Gotchas
- Tag keys starting with `tg` are reserved and prohibited
- Keys are unique per Resource — adding a duplicate key overwrites or errors
- Tags are case-sensitive: `Production` ≠ `production`
- Terraform/Pulumi/K8s operator support not yet available (API only for programmatic management)
- Cloud provider tag import (AWS, GCP) possible via API/Terraform integration when available

## Best Practices
- Standardize key names across all Resources (avoid mixing `owner` and `owner-team`)
- Tag all Resources for consistent organization
- Use tags for multiple contexts: technical, ownership, security

## Related Docs
- Twingate API (for programmatic tag management)
- Resources documentation
- Terraform / Pulumi / Kubernetes operator (future tag support)