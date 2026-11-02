<!-- manual-reference: do-not-overwrite -->
# Phase 9 — Rollout & harden

**Goal:** everyone migrated in waves, controls tightened, legacy access retired, and the state
handed over.

**Load:** twingate-identity (device trust, policies), twingate-connectors (monitoring, upgrades),
twingate-architect (VPN replacement guidance).

## Steps

1. Rollout waves by team; run Twingate in parallel with the existing VPN — never a day-one hard
   cutover.
2. Enable device trust / tighten policies per tier once the pilot is stable.
3. Tighten each zone's firewall to accept resource traffic only from the connectors.
4. Connector operations: health alerting and an upgrade approach (twingate-connectors).
5. Plan VPN decommission once usage drops (VPN logs/hit counts help).
6. Revoke temporary API tokens used during the build.
7. Write `twingate-context.md` (schema in the plugin's `docs/twingate-context-template.md`) from
   the final state so future sessions and the `twingate-se` agent start from current topology.
8. Get admin sign-off; log a phase-9 decision.

## Exit gate

A phase-9 decision (admin sign-off).
