# Policy on Resource Migration

## Page Title
Migration to Policy on Resource

## Summary
Twingate is migrating Security Policies from Group-associations to Resource-associations. Resources will now have a directly assigned Policy, with the option for Group-specific Policy overrides per Resource. Rollout is automatic and phased; no customer action required.

## Key Information
- **New model**: Policies attach directly to Resources (Resource Policy), not Groups
- **Override capability**: A specific Group accessing a specific Resource can have its own Policy separate from the Resource Policy
- **Migration is automatic**: No action needed from customers
- **Backwards compatible**: Existing APIs and Terraform code will be mapped to the updated model

## Migration Logic

| Scenario | Result |
|----------|--------|
| All Groups accessing a Resource use the **same** Policy | That Policy becomes the Resource Policy; Groups inherit it |
| Groups accessing a Resource use **different** Policies | Default Policy becomes the Resource Policy; individual Group↔Resource Policies are preserved |

**Example:**
- Resource A + Group 1 (Company Policy) + Group 2 (Company Policy) → Resource Policy = Company Policy
- Resource A + Group 1 (Company Policy) + Group 2 (Contractor Policy) → Resource Policy = Default Policy; each Group retains its specific Policy

## Prerequisites
- None; migration is handled automatically by Twingate

## Configuration Values
- No new env vars, CLI flags, or API params introduced
- Existing API/Terraform configurations are mapped automatically

## Verifying Migration Status
1. Navigate to a Resource in the Twingate admin console
2. Check the left-hand column for a **Resource Policy** field
3. If present, the updated model is active for your account

## UI Changes Post-Migration
- **Resources table**: Optional column to display Resource Policy
- **Group detail page**: Policy shown next to each Resource in the Group
- **Policy page**: Lists all Resources using that Policy as their Resource Policy

## Gotchas
- Resources with mixed Group Policies will fall back to **Default Policy** as the Resource Policy — review these cases to ensure Default Policy meets your security requirements
- Groups with access to the same Resource may now rely on Group-level Policy overrides; verify contractor/restricted Groups still have correct Policies applied post-migration
- API/Terraform backwards compatibility is maintained, but new features (Resource Policy field) may require schema updates to manage explicitly

## Related Docs
- [Updated Policy on Resource model](https://www.twingate.com/docs/) (referenced inline, URL not provided)
- Twingate Security Policies documentation
- Terraform provider documentation for Resources and Groups