<!-- manual-reference: do-not-overwrite -->
# Phase 1 — Discover

**Goal:** a draft catalog — candidate Remote Networks, Resources, and personas — from whatever
the admin has.

**Load:** twingate-architect (Remote Network boundaries, FQDN vs CIDR, overlapping ranges, DNS).

## Steps

1. Ingest every artifact via the matching intake guide:
   `intake-diagrams.md` (diagrams, screenshots, exports), `intake-verbal.md` (transcripts, notes,
   spoken walkthroughs), `intake-discovery.md` (read-only commands when there's nothing else).
2. Draft remote networks (one per firewalled zone / VPC / VNet / site — confirm the current
   guidance in twingate-architect's references) and resources, all `inferred` unless transcribed.
3. Map each resource to a `service_type` and personas using `persona-catalog.md`.
4. **Guided path:** propose a persona list now — Phase 2 uses it to decide which IdP groups to
   provision. **Expert path:** record the admin's own groups/teams as personas (`stated`) and
   act as validator: flag gaps, overlaps, and over-broad access, but don't impose a model.
5. Optionally delegate a structured draft to `network-designer` for large or multi-site estates
   (see `agent-delegation.md`).
6. Show one compact table (resource, address, zone, role, ports, personas, confidence) and ask
   about the weakest rows first.

## Exit gate

≥1 remote network; every in-scope resource has an address and a known remote network; ≥1 persona.

## Notes

- Workstations and "campus users" are clients, not resources.
- Other organisations' systems are out of scope by default.
- Phase 3 (confirm resources) can run in parallel with Phase 2 while IdP admins do their part.
