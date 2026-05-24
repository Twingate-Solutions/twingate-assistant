# Policy on Resource Migration

## Summary
Twingate is migrating Security Policies from Group-level associations to Resource-level associations. Resources will now have a direct Policy, with optional per-Group-per-Resource Policy overrides. Migration is automatic and phased; no customer action required.

## Key Information
- **New model**: Policies attach directly to Resources (Resource Policy), not Groups
- **Override capability**: A specific Group accessing a specific Resource can have its own Policy distinct from the Resource Policy
- **Migration is automatic**: Twingate handles the rollout; no manual steps needed
- **API/Terraform**: Backwards compatibility maintained; existing code maps to updated model automatically

## Migration Logic

| Scenario | Result |
|----------|--------|
| All Groups on a Resource share the **same** Policy | That Policy becomes the Resource Policy; Groups inherit it |
| Groups on a Resource use **different** Policies | Default Policy becomes Resource Policy; individual Group↔Resource Policies are preserved |

**Example:**
- Resource A + Group 1 (Company Policy) + Group 2 (Company Policy) → Resource Policy = Company Policy
- Resource A + Group 1 (Company Policy) + Group 2 (Contractor Policy) → Resource Policy = Default Policy; each Group retains its specific Policy

## Verifying Migration Status
Navigate to a Resource in the admin console — if a **Resource Policy** field appears in the left-hand column, the updated configuration is active for your account.

## UI Changes After Migration
- **Resources table**: Optional column showing Resource Policy
- **Group detail page**: Policy displayed next to each associated Resource
- **Policy page**: Lists Resources using that Policy as their Resource Policy

## Gotchas
- Resources with mixed Group Policies will fall back to **Default Policy** at the Resource level — review these cases to ensure Default Policy is appropriate
- Group-specific Policy overrides are preserved but must now be managed at the Group↔Resource level, not Group level alone
- No timeline guarantee per-tenant; rollout is phased over "next few weeks"

## Prerequisites
- No prerequisites; migration is handled server-side
- Existing API integrations and Terraform configurations require no changes

## Related Docs
- [Policy on Resource model (updated)](https://www.twingate.com/docs/) — linked inline as "here" in source