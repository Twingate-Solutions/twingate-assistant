# Policy on Resource Migration

## Page Title
Migration to Policy on Resource

## Summary
Twingate is migrating Security Policies from Group-level associations to Resource-level associations. Resources will have a directly assigned Policy, while individual Group-Resource pairs can still override with their own Policy. Migration is automatic with no customer action required.

## Key Information
- **Old model**: Security Policies attached to Groups
- **New model**: Security Policies attached directly to Resources (Resource Policy); Groups can have per-Resource Policy overrides
- Rollout is phased; no customer action needed
- API and Terraform backwards compatibility is maintained

## Migration Logic

| Scenario | Result |
|----------|--------|
| All Groups accessing a Resource share the same Policy | That Policy becomes the Resource Policy |
| Groups accessing a Resource have different Policies | Default Policy becomes the Resource Policy; individual Group-Resource Policies are preserved |

**Example:**
- Resource A + Group 1 (Company Policy) + Group 2 (Company Policy) → Resource Policy = Company Policy; both Groups inherit it
- Resource A + Group 1 (Company Policy) + Group 2 (Contractor Policy) → Resource Policy = Default Policy; Group-level Policies remain intact

## Prerequisites
- No prerequisites; migration is automatic for all Twingate customers

## Configuration Values
- None required; existing API calls and Terraform configurations are automatically mapped to the new model

## Verification Steps
1. Navigate to a Resource in the Twingate admin UI
2. Confirm a **Resource Policy** field appears in the left-hand column
3. Check updated views:
   - **Resources table**: optional column for Resource Policy
   - **Group detail page**: Policy listed next to each Resource
   - **Policy page**: Resources using that Policy as Resource Policy are listed

## Gotchas
- If Groups previously had **different** Policies on a Resource, the Resource Policy defaults to **Default Policy** — verify this is acceptable for your security posture
- Groups with conflicting Policies will have their individual overrides preserved, but the baseline Resource Policy changes to Default Policy
- Migration is phased; check your admin UI to confirm if your account has been updated yet

## Related Docs
- [Updated Policy on Resource model](https://www.twingate.com/docs/policy-on-resource) (referenced inline)
- Terraform provider documentation (implied by backwards compatibility note)