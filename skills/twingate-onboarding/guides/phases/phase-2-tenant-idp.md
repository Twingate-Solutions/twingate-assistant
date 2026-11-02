<!-- manual-reference: do-not-overwrite -->
# Phase 2 — Tenant & IdP

**Goal:** tenant exists, IdP connected with SCIM, the right groups provisioned, and every persona
mapped to real synced groups with IDs.

**Load:** twingate-identity (per-IdP setup, SCIM, groups, security policies). twingate-api for
reading groups.

## Steps

1. **Tenant.** If none exists, the admin creates it (task). Record the name.
2. **Which groups to provision** — three routes; use whichever the admin can supply:
   - Admin already knows (expert): they name the IdP groups per persona.
   - Admin shares IdP information (group export, screenshot, or a read-only IdP connector in the
     session): Claude suggests matching groups per persona from names, descriptions and member
     counts.
   - Neither: give the persona list with an `idp_search_hint` per persona, and suggest creating
     new IdP groups where nothing matches.
3. **Connect and provision.** Load twingate-identity and grep its references for the admin's IdP
   (e.g. "okta", "entra", "scim") to produce the setup steps at the admin's assist level. The admin
   assigns the chosen groups to the Twingate app in the IdP and syncs.
4. **Read groups back** via the API (twingate-api recipes; Read token in env) or a screenshot of
   the Groups page. Record each group (`sourced`, `twingate_id`, `type`, member count).
5. **Map personas → groups** and show the mapping for approval. Synced groups cannot be edited in
   Twingate: a missing group is IdP homework, not something to create. Create MANUAL groups only
   if the admin explicitly chooses to, recorded in `decisions`.
6. If the admin declines SCIM, explain the deprovisioning trade-off once and record the decision.

## Exit gate

IdP set and connected; SCIM `yes` or a recorded phase-2 decision accepting no SCIM; every persona
used by an in-scope resource maps to ≥1 group with a `twingate_id`.

## Notes

- Personas used only by out-of-scope resources don't block the gate.
- Device trust and policy tiers are configured later (Phase 4/9), but note MDM/EDR now.
