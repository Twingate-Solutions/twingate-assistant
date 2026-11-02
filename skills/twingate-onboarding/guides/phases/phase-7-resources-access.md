<!-- manual-reference: do-not-overwrite -->
# Phase 7 — Resources & group mapping

**Goal:** resources created with ports, access granted to the mapped groups with the agreed
policies, and the tenant matching the state file.

**Load:** twingate-api (schema + recipes) or twingate-terraform / twingate-pulumi;
twingate-identity for security policy assignment.

## Steps

1. Run `status.py`; require `resources_build_allowed: true`. If the admin says "just build it"
   with gates unmet, refuse for the blocked items and list exactly what needs confirming.
2. Run `deployment-reviewer`; resolve blocking findings or log the admin's acceptance.
3. Build the plan from the state file only: per resource — name, address, network ID, protocols,
   groups (IDs from `groups`), security policy. Show it; get an explicit yes; log a phase-7
   decision. Approve per batch.
4. Execute via the chosen path (`automation-paths.md`): read first and skip existing resources,
   create, then grant access. Check `ok` on every mutation.
5. Read back resources and access via the API; diff against the state file; set `twingate_id`s;
   record mismatches as open questions.

## Exit gate

Every in-scope resource has a `twingate_id`; a phase-7 decision.

## Notes

- Grant access to groups, never to individual users.
- Existing resources found at the same address: report them; change their access only if the
  admin asks.
