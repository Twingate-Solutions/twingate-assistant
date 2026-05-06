# Resource Tags

## Summary
Tags are key-value metadata pairs attachable to Twingate Resources for organization and filtering. Each Resource supports up to 64 tags, manageable via Admin Console or API. Tags enable structured categorization by ownership, environment, application, and other attributes.

## Key Information
- Tags are key-value pairs (e.g., `environment: production`)
- Used for: adding context to Resources, filtering/searching Resources efficiently
- Manageable via Admin Console or Twingate API; Terraform/Pulumi/K8s operator support coming soon
- Tag suggestions auto-populate from existing Network tags as you type

## Prerequisites
- Admin Console access or API credentials
- Resources already created in Twingate Network

## Tag Requirements / Constraints
| Constraint | Detail |
|---|---|
| Max tags per Resource | 64 |
| Unique keys per Resource | One tag per key |
| Case sensitivity | Both keys and values are case-sensitive |
| Key length | 1–128 characters |
| Value length | 1–256 characters |
| Whitespace | Leading/trailing whitespace auto-stripped; cannot start/end with whitespace |
| Prohibited key prefix | Keys cannot start with `tg` (e.g., `tg_remote_network` is invalid) |
| Character set | Any valid UTF-8 characters |

## Adding Tags (Admin Console)
1. Navigate to **Network → Resources**
2. Create or edit a Resource
3. Click **Add Tag**
4. Set key, then set value (autocomplete suggests existing Network tags)
5. Repeat for additional tags
6. Save the Resource
- To remove a tag: click the **✕** icon next to the tag (only removable, not editable after creation—must delete and re-add)

## Filtering Resources by Tags
1. Navigate to **Network → Resources**
2. Use the **Tags** filter in the Resource table
3. Select **Select Key** → search for desired key
4. Choose filter mode: **in** (include) or **not in** (exclude)
5. Search and select tag values to filter

## Common Tag Patterns
```
owner: devops | it-team | user@example.com
managed_by: terraform | pulumi | admin_console | k8s_operator
application: prometheus | kafka | proxmox
environment: development | staging | production
location: sf-office | us-west-2
region: us-west-2 | eu-central-1
```

## Configuration Values (API)
- Tags manageable via [Twingate API](https://www.twingate.com/docs/api)
- Terraform/Pulumi/K8s operator: not yet supported (upcoming)
- API enables bulk tag management and importing tags from cloud providers (AWS, GCP)

## Gotchas
- Tag keys **cannot start with `tg`**—this prefix is reserved
- Keys are **immutable after creation**—must delete and recreate to change a key
- Duplicate keys on the same Resource are not allowed
- Tags are most useful when applied **consistently across all Resources**; partial tagging reduces filter effectiveness
- Avoid mixing similar key names (e.g., `owner` vs `owner-team`) without a standard

## Related Docs
- [Twingate API](https://www.twingate.com/docs/api)
- Resources management
- Terraform/Pulumi/Kubernetes operator integration (forthcoming tag support)