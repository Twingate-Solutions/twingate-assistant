---
source: https://help.twingate.com/articles/4693640683-terraform-error-an-argument-named-group-ids-is-not-expected-here
type: help
fetched: 2026-08-06
source_version: d9abb85d98d6feeb2efacbd04b856072e7e8af34be1399a7103ee95b9511061f
---

# Terraform Error: "An argument named group_ids is not expected here"

## Summary
Breaking change introduced in Twingate Terraform provider v1.0.0 removed top-level `group_ids` argument from `twingate_resource`. The argument must now be nested inside an `access` block.

## Key Information
- Affects all `twingate_resource` configurations using top-level `group_ids`
- `group_ids` was deprecated in pre-v1.0.0 releases before being removed
- Functionality is identical — only the schema location changed
- Multiple resource blocks in a configuration may need updating

## Prerequisites
- Twingate Terraform provider v1.0.0+
- Existing configs using `group_ids` at top level of `twingate_resource`

## Migration Change

**Before (invalid in v1.0.0+):**
```hcl
resource "twingate_resource" "resource" {
  name              = "network"
  address           = "internal.int"
  remote_network_id = twingate_remote_network.aws_network.id
  group_ids         = [twingate_group.aws.id]
}
```

**After (correct):**
```hcl
resource "twingate_resource" "resource" {
  name              = "network"
  address           = "internal.int"
  remote_network_id = twingate_remote_network.aws_network.id

  access {
    group_ids = [twingate_group.aws.id]
  }
}
```

## Configuration Values
| Old Argument | New Location | Notes |
|---|---|---|
| `group_ids` (top-level) | `access.group_ids` (block) | Value/references unchanged |

## Gotchas
- Search entire codebase for `group_ids` — error only surfaces at `terraform validate` or apply time, so multiple files may be affected
- Variable references (e.g., `var.demo_resource_group_ids`) remain valid; only the nesting location changes
- The `access` block is expected to evolve with additional arguments in future releases

## Related Docs
- [Twingate Terraform Provider v1.0.0 upgrade guide](https://help.twingate.com)
- [`twingate_resource` resource documentation](https://registry.terraform.io/providers/Twingate/twingate/latest/docs/resources/resource)