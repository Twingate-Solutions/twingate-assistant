# Resource Tags

## Summary
Tags are key-value metadata pairs attachable to Twingate Resources for organization and filtering. Each Resource supports up to 64 tags, manageable via Admin Console or API. Tags enable filtering in the Resource table to quickly locate specific Resource sets.

## Key Information
- Tags are key-value pairs (e.g., `owner: devops`, `environment: production`)
- Used for: adding context, filtering/searching Resources
- Managed via Admin Console (UI) or Twingate API
- Terraform, Pulumi, and Kubernetes operator support coming soon

## Prerequisites
- Admin Console access
- Resources already created in the Network

## Tag Requirements / Constraints
| Property | Constraint |
|----------|-----------|
| Max tags per Resource | 64 |
| Unique keys per Resource | 1 per key (no duplicate keys) |
| Case sensitivity | Keys and values are case sensitive |
| Key length | 1–128 characters |
| Value length | 1–256 characters |
| Prohibited key prefix | Cannot start with `tg` (e.g., `tg_remote_network` is invalid) |
| Whitespace | Cannot start/end with whitespace (auto-stripped) |
| Character set | Any valid UTF-8 |

## Step-by-Step: Adding Tags via Admin Console
1. Navigate to **Network → Resources**
2. Open a Resource (create or edit)
3. Click **Add Tag**
4. Enter key (autocomplete suggests existing keys from Network)
5. Enter value (autocomplete suggests existing values)
6. Repeat as needed
7. Remove tags with the **✕** icon
8. Save the Resource

## Step-by-Step: Filtering Resources by Tags
1. Navigate to **Network → Resources**
2. Click the **Tags** filter in the Resource table
3. Select **Select Key**, search for desired key
4. Choose **in** (include) or **not in** (exclude)
5. Search and select tag values for the filter

## Common Tag Patterns
| Key | Example Values | Purpose |
|-----|---------------|---------|
| `owner` | `devops`, `it-team`, `alex@example.com` | Ownership |
| `managed_by` | `terraform`, `pulumi`, `k8s_operator` | Management source |
| `application` | `prometheus`, `kafka` | Running application |
| `environment` | `development`, `staging`, `production` | Environment tier |
| `location` | `sf-office`, `us-west-2` | Physical/virtual location |
| `region` | `us-west-2`, `eu-central-1` | Cloud provider region |

## Gotchas
- Keys starting with `tg` are **reserved and prohibited**
- Each Resource can only have **one tag per key** — adding a duplicate key overwrites or is blocked
- Tag key/value **cannot be edited after creation** — must delete and re-add
- Trailing/leading whitespace is silently stripped on input

## API / Integration
- Full tag management available via [Twingate API](https://www.twingate.com/docs/api)
- Terraform/Pulumi/K8s operator support not yet available (coming soon)
- API enables bulk tag management and importing tags from AWS/GCP

## Related Docs
- Twingate API documentation
- Resources documentation
- Terraform integration
- Pulumi integration
- Kubernetes operator