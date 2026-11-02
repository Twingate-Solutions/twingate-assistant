<!-- manual-reference: do-not-overwrite -->
# Phase 8 — Pilot

**Goal:** prove the success criteria with real users before rollout.

**Load:** twingate-architect (Client platforms, MDM deployment), twingate-troubleshoot (any
failure), twingate-dns-security if DNS filtering or another DNS product is in play.

## Steps

1. Pick 2–5 pilot users covering different roles and OSes.
2. Client deployment method (MDM push or self-install) — get platform steps from the references.
3. Check for conflicting software on pilot machines (other VPNs, SSE agents, DNS filters, AV web
   protection) — grep twingate-troubleshoot for the product name before predicting conflicts.
4. Give the admin a test checklist: per pilot user × resource, connect and use the actual port.
5. Mark each success criterion `met`, or `deferred` with a note. Failures → twingate-troubleshoot,
   grepping the user's literal error text first.

## Exit gate

Every success criterion `met` or `deferred` with a note.
