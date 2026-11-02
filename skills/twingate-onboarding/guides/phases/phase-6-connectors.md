<!-- manual-reference: do-not-overwrite -->
# Phase 6 — Connectors

**Goal:** at least two healthy connectors per Remote Network, placed with line of sight to their
resources.

**Load:** twingate-connectors (platform methods, egress requirements, HA, tokens, health states).
twingate-troubleshoot for anything not coming up ALIVE. twingate-kubernetes for cluster hosting.

## Steps

1. Per network: platform, host(s)/VLAN/subnet, DHCP or static, egress path. Record in
   `connector_hosts`.
2. Get egress requirements from twingate-connectors' references (grep "outbound", "egress") and
   raise the firewall change early — it is usually the slowest task. Never quote ports from memory.
3. Run the connector-host preflight (`intake-discovery.md`) on each candidate host.
4. Deploy: cloud networks → delegate to the matching deployer agent; on-prem → load
   twingate-connectors and grep for the platform (docker, systemd, hyper-v, vmware…) — reference
   implementations exist for many platforms. Connector tokens are generated and used by the
   admin on the host; never in chat or the state file.
5. Read connector states via the API (twingate-api recipes) or a screenshot; record
   `{name, id, state}` per connector.

## Exit gate

Every remote network has `connector_count` (≥2) connectors in state ALIVE.

## Notes

- Not ALIVE → load twingate-troubleshoot, grep the exact state string, and follow its diagnosis;
  TLS inspection and blocked egress are the usual causes.
- Different hosts (and hypervisors/AZs where possible) for the two connectors.
