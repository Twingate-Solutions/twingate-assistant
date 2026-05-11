# Resource Tags

## Summary
Tags are key-value metadata pairs attachable to Twingate Resources for organization and filtering. They enable categorization by attributes like ownership, environment, and application. Tags can be managed via Admin Console or API.

## Key Information
- Each tag is a **key-value pair** (e.g., `environment: production`)
- Tags enable filtering in the Resources table for quick lookup
- Manageable via Admin Console, Twingate API (Terraform/Pulumi/K8s operator support coming)

## Prerequisites
- Admin Console access or API credentials
- Resources must already exist to attach tags

## Tag Requirements / Constraints
| Property | Constraint |
|---|---|
| Max tags per Resource | 64 |
| Keys per Resource | Unique (one per key name) |
| Case sensitivity | Keys and values are case sensitive |
| Key length | 1–128 characters |
| Value length | 1–256 characters |
| Prohibited key prefix | `tg` (e.g., `tg_remote_network` is invalid) |
| Whitespace | Cannot start/end with whitespace (auto-stripped) |
| Character set | Any valid UTF-8 |

## Common Tag Patterns
```
owner: devops | it-team | user@example.com
managed_by: terraform | pulumi | admin_console | k8s_operator
application: prometheus | kafka | proxmox
environment: development | staging | production
location: sf-office | us-west-2
region: us-west-2 | eu-central-1
```

## Step-by-Step: Adding Tags (Admin Console)
1. Navigate to **Network → Resources**
2. Open or create a Resource
3. Click **Add Tag**
4. Set key (autocomplete suggests existing keys)
5. Set value (autocomplete suggests existing values)
6. Repeat as needed; click remove icon (✕) to delete a tag
7. Save the Resource

## Step-by-Step: Filtering by Tags
1. Navigate to **Network → Resources**
2. Click the **Tags** filter
3. Select **Select Key**, search for desired key
4. Choose **in** (include) or **not in** (exclude)
5. Search and select tag values to filter on

## Configuration Values
- No environment variables or CLI flags documented on this page
- API management available via [Twingate API](https://www.twingate.com/docs/)

## Gotchas
- Tag keys are **unique per Resource** — adding a duplicate key overwrites or errors
- Keys starting with `tg` are **reserved** and prohibited
- Tags are **case sensitive** — `Owner` and `owner` are different keys
- Tag key/value **cannot be edited after creation** — must delete and re-add
- Terraform/Pulumi/K8s operator tag support is **not yet available** (coming soon)

## Best Practices
- Standardize key names across all Resources (avoid mixing `owner` and `owner-team`)
- Tag all Resources for maximum utility
- Import cloud provider tags (AWS/GCP) via API/Terraform to mirror existing metadata in Twingate

## Related Docs
- [Twingate API](https://www.twingate.com/docs/)
- Resources management documentation
- Terraform / Pulumi / Kubernetes operator integration pages