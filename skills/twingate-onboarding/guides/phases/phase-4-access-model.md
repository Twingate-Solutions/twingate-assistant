<!-- manual-reference: do-not-overwrite -->
# Phase 4 — Access model

**Goal:** an approved matrix of persona (→ group) × resource, with a policy tier per persona and
any special access patterns decided.

**Load:** twingate-identity (security policies, device trust, JIT/approval access, service
accounts). twingate-idfw if SSH / Kubernetes / internal web apps need per-user identity.

## Steps

1. Build the matrix: rows = resources, columns = personas (and their mapped groups). Mark
   sensitive rows. Use `persona-catalog.md` heuristics (separate admin vs app access for prod).
2. Map each `policy_tier` to concrete security-policy settings — grep twingate-identity's
   references for "security policy", "device trust", "MFA" for current options. Note which
   policies need creating. Check twingate-api's schema for what the API can do with policies
   (at the time of writing it can assign policies to groups and to individual access edges, but
   not create policies or edit their rules) — creating policies is usually an admin-console task.
3. Ask the Phase 4 questions (contractors, service accounts, admin/app split, IDFW candidates).
4. Optional: delegate a matrix draft to `network-designer`; delegate IDFW candidates to
   `idfw-deployer`.
5. Present the final matrix and get an explicit approval; log it as a phase-4 decision
   ("Approved access matrix vN").

## Exit gate

Every in-scope resource has ≥1 persona; every referenced persona exists with buildable
provenance; a phase-4 decision.

## Notes

- Warn on access via an "everyone"-style group to anything above `low` sensitivity.
- Service accounts are separate principals — record them as personas with a note, and route key
  handling to twingate-api (Provision scope stays with a human).
