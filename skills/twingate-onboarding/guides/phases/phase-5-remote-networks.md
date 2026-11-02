<!-- manual-reference: do-not-overwrite -->
# Phase 5 — Remote Networks

**Goal:** Remote Networks created in the tenant, IDs recorded.

**Load:** twingate-architect (naming, boundaries, location values). twingate-api or
twingate-terraform/pulumi depending on the path.

## Steps

1. Run `status.py`; require `networks_build_allowed: true`.
2. Run `deployment-reviewer` on the remote network plan; resolve blocking findings.
3. Show the plan: name, location, subnets/boundary per network. Get an explicit yes; log a
   phase-5 decision.
4. Create via the chosen path (`automation-paths.md`): console click path, Claude-run API call,
   generated script, or IaC. Location enum values come from the API schema.
5. Read back and record `twingate_id` per network (`sourced`).

## Exit gate

Every remote network has buildable provenance and a `twingate_id`; a phase-5 decision.

## Notes

- Remote Networks must exist before connectors can be created for them.
- Existing networks with the same name: reuse, don't duplicate — confirm with the admin.
