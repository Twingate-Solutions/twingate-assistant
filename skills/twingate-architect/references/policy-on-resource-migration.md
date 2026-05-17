# Migration to Policy on Resource

## Summary
Twingate is migrating Security Policies from Group-association to Resource-association. Policies are now set directly on Resources, with the option for per-Group overrides on specific Resources. Migration is automatic with no customer action required.

## Key Information
- Policies move from being Group-configured to Resource-configured
- A Group accessing a Resource can have a Policy that differs from the Resource's default Policy
- Rollout is phased across all customers
- No manual migration steps required

## Migration Logic

| Scenario | Result |
|----------|--------|
| All Groups on a Resource use the **same** Policy | That Policy becomes the Resource Policy; Groups inherit it |
| Groups on a Resource use **different** Policies | Default Policy becomes the Resource Policy; individual Group-Resource Policies are preserved |

**Example:**
- Resource A, two Groups both using "Company Policy" → Resource Policy = Company Policy (Groups inherit)
- Resource A, Group 1 = "Company Policy", Group 2 = "Contractor Policy" → Resource Policy = Default Policy; each Group retains its specific Policy

## API & Terraform Compatibility
- Existing API calls and Terraform configurations remain valid
- Twingate maps existing configurations to the new model automatically
- No code changes required

## Verifying Migration Status
Navigate to a Resource in the admin UI and check for a **Resource Policy** field in the left-hand column.

## UI Changes After Migration
- **Resources table**: Optional column to display Resource Policy
- **Group detail page**: Policy shown next to each Resource in the Group
- **Policy page**: Lists Resources using that Policy as their Resource Policy

## Gotchas
- If Groups previously had mixed Policies on a Resource, the Resource Policy defaults to **Default Policy** — verify this matches your intended security posture
- Groups with previously distinct Policies retain those Policies at the Group-Resource level; confirm these are still correct post-migration
- No rollback mechanism mentioned; review Resource Policies after migration completes

## Related Docs
- [Updated Policy on Resource model](https://www.twingate.com/docs/) (linked inline as "here" — check Twingate docs for direct URL)