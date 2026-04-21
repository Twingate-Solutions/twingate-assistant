## Migration to Policy on Resource

Documents the phased migration of Twingate's Security Policy model from Group-based to Resource-based Policy association. No admin action is required; existing configurations are automatically migrated.

**Key Information:**
- Resource Policies are migrating from Group-level association to direct Resource-level association
- A per-Group-per-Resource Policy override remains available when Groups need different Policies on the same Resource
- No action required from admins; rollout is phased for all customers
- Existing API and Terraform configurations are automatically mapped to the new model (backwards compatible)

**Migration Logic:**
- All Groups on a Resource used the same Policy → that Policy becomes the Resource Policy
- Groups used different Policies → Default Policy becomes the Resource Policy; per-Group Policy overrides are preserved

**Verification:**
- Navigate to a Resource in Admin Console; if "Resource Policy" appears in the left-hand column, migration is active for your account

**UI Changes After Migration:**
- Resources table: optional Resource Policy column
- Group detail page: Policy displayed next to each Resource
- Policy page: lists Resources using that Policy

**Gotchas:**
- Resources where Groups had conflicting Policies default to Default Policy at the Resource level -- review Group overrides to confirm intent
- Verify Terraform policy assignments after migration even though backwards compatibility is maintained

**Related Docs:**
- /docs/resource-policies -- Resource Policy configuration (updated model)
- /docs/security-policies -- Security policy overview
- /docs/groups -- Group configuration
