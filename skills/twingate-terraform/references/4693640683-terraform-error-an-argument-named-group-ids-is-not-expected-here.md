---
source: https://help.twingate.com/articles/4693640683-terraform-error-an-argument-named-group-ids-is-not-expected-here
type: help
fetched: 2026-09-06
source_version: 11340d66d89ecffe51e11cf42486079197a8ada3088186596c9a803fcc67856d
---

# Terraform Error: "An argument named 'group_ids' is not expected here"

## Summary
In Twingate Terraform provider v1.0.0, `group_ids` was removed as a top-level argument on `twingate_resource`. It must now be nested inside an `access` block. Configurations using the old syntax will fail validation.

## Key Information
- Breaking change introduced in provider **v1.0.0**
- `group_ids` was deprecated in prior releases before full removal
- Affects all `twingate_resource` blocks using top-level `group_ids`
- The `access` block is the replacement and will continue to be extended

## Prerequisites
- Twingate Terraform provider >= v1.0.0
- Existing configs using `group_ids` at the `twingate_resource` top level

## Migration: Before vs After

**Before (invalid in v1.0.0+):**
```hcl
resource "twingate_resource" "resource" {
  name              = "network"
  address           = "internal.int"
  remote_network_id = twingate_remote_network.aws_network.id
  group_ids         = [twingate_group.aws.id]  # ❌ No longer valid
}
```

**After (correct syntax):**
```hcl
resource "twingate_resource" "resource" {
  name              = "network"
  address           = "internal.int"
  remote_network_id = twingate_remote_network.aws_network.id

  access {
    group_ids = [twingate_group.aws.id]  # ✅ Nested in access block
  }
}
```

## Configuration Values
| Old Argument | New Location | Type |
|---|---|---|
| `group_ids` (top-level) | `access.group_ids` (block) | `list(string)` |

## Gotchas
- The error may appear in **multiple files/resources** across a large codebase — audit all `twingate_resource` blocks
- Using variables (e.g., `group_ids = var.demo_resource_group_ids`) still works but must be inside the `access` block
- Run `terraform validate` after migration to confirm all instances are fixed

## Related Docs
- [Twingate Terraform Provider v1.0.0 upgrade guide](https://help.twingate.com/articles/update-to-v1.0.0)
- [`twingate_resource` resource reference](https://registry.terraform.io/providers/Twingate/twingate/latest/docs/resources/resource)