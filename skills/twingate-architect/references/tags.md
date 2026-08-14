---
source: https://www.twingate.com/docs/tags
type: docs
fetched: 2026-08-14
source_version: b511ea2ca7c891044de0263716812a3596e1b8a12352c62419f32816329da7a1
---

# Resource Tags

## Summary
Tags are key-value metadata pairs attachable to Twingate Resources for organization and filtering. Each Resource supports up to 64 tags, manageable via Admin Console or API. Tags enable categorization by ownership, environment, application, and other custom attributes.

## Key Information
- Tags are key-value pairs (e.g., `owner=devops`, `environment=production`)
- Maximum 64 tags per Resource
- One tag per unique key per Resource
- Keys and values are case-sensitive
- Leading/trailing whitespace is auto-stripped
- Manageable via Admin Console, API, and (soon) Terraform/Pulumi/K8s operator

## Prerequisites
- Admin Console access
- Resources already created in Twingate Network

## Configuration Values

| Property | Constraint |
|----------|-----------|
| Key length | 1–128 characters |
| Value length | 1–256 characters |
| Tags per Resource | Max 64 |
| Prohibited key prefix | `tg` (e.g., `tg_remote_network` disallowed) |
| Character set | Any valid UTF-8 |

## Common Tag Keys

**Ownership:**
- `owner` — e.g., `devops`, `it-team`, `alex@company.com`
- `managed_by` — e.g., `terraform`, `admin_console`, `k8s_operator`

**Technical:**
- `application` — e.g., `prometheus`, `kafka`
- `environment` — e.g., `development`, `staging`, `production`
- `location` — e.g., `sf-office`, `us-west-2`
- `region` — e.g., `us-west-2`, `eu-central-1`

## Step-by-Step

**Adding tags (Admin Console):**
1. Open Resource (create or edit)
2. Click **Add Tag**
3. Enter key (autocomplete suggests existing keys)
4. Enter value (autocomplete suggests existing values)
5. Repeat as needed; click ✕ to remove
6. Save Resource

**Filtering by tags:**
1. Navigate to **Network → Resources**
2. Click **Tags** filter
3. Select **Select Key**, search for key
4. Choose `in` (include) or `not in` (exclude)
5. Select tag values to filter on

## Gotchas
- Keys cannot start with `tg` — reserved prefix
- Cannot edit a tag's key or value after creation; must delete and re-add
- Duplicate keys on same Resource not allowed
- Terraform/Pulumi/K8s operator support listed as "coming soon" — use API for programmatic management currently
- Tags are most useful only when applied consistently across **all** Resources

## Related Docs
- Twingate API (for programmatic tag management)
- Terraform provider (pending tag support)
- Pulumi integration (pending tag support)
- Kubernetes operator (pending tag support)