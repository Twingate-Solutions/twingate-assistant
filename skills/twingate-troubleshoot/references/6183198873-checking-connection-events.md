---
source: https://help.twingate.com/articles/6183198873-checking-connection-events
type: help
fetched: 2026-10-04
source_version: e559b687fc7c944d906a05ade82569d73c1ea8e1513827c8f015776e18374f6b
trust: official
---

# Checking Connection Events

## Page Title
Checking Connection Events (Twingate Troubleshooting)

## Summary
Twingate logs all connection attempts through Connectors, viewable via traffic activity reports in the Admin Console. This guide covers how to use connection events to diagnose why an end user cannot reach a Resource they have access to.

## Key Information
- All connection attempts transit through Connectors and are logged
- Events are only created when traffic **reaches the Connector** — no event means the Client never got traffic out
- DNS resolution for hostnames/FQDNs is performed by the **Connector**, not the client device
- Activity reports are per-Resource, found under **Network → [Resource] → Activity**

## Prerequisites
- Admin Console access
- Ability to SSH (or equivalent) into Connector host machines
- `dig` or `nslookup` available on Connector host

## Step-by-Step

### Setup
1. Identify the Remote Network the problematic Resource belongs to
2. Shut down all but **one Connector** in that Remote Network (isolates variables)

### Gathering Events
1. Reproduce the failure from the end user's device
2. In Admin Console: **Network** tab → locate Resource → click it → view **Activity** section
3. Hover over records to reveal **Show details** button for each event

## Diagnosing by Event Outcome

| Scenario | Likely Cause | Action |
|---|---|---|
| **No events logged** | Client not intercepting traffic, or traffic not leaving Twingate network interface | Investigate Client-side connectivity |
| **DNS lookup errors** | Connector cannot resolve the hostname/FQDN | SSH into Connector host; run `dig <hostname>` or `nslookup <hostname>` to verify resolution |
| **Successful events, no errors** | Problem between Connector and the Resource/service | Check firewalls between Connector and app; verify DNS/FQDN config on that path |

## Gotchas
- **Only run one Connector during troubleshooting** — Connectors in the same Remote Network may not be identically configured, making DNS issues hard to isolate across multiple Connectors
- No Admin Console event ≠ connection was blocked by Twingate — it means traffic never reached the Connector at all
- DNS errors are Connector-side, not client-side; fix must be applied to the Connector host's DNS configuration

## Configuration Values
None specific (no env vars or API params referenced)

## Related Docs
- [Twingate Traffic Activity Reports](https://help.twingate.com)
- [Client-side connectivity troubleshooting](https://help.twingate.com)
- Twingate Troubleshooting Guide (linked as "Back to troubleshooting guide" on source page)