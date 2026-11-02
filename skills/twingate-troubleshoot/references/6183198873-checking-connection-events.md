---
source: https://help.twingate.com/articles/6183198873-checking-connection-events
type: help
fetched: 2026-11-01
source_version: 532beac9e25c8c719b8511fdd3dd928f505bc0b049cf0df14f0b1584d1a26783
trust: official
---

# Checking Connection Events

## Page Title
Checking Connection Events

## Summary
Guide for troubleshooting failed Resource connections by reviewing connection events in the Twingate Admin Console. Covers isolating Connectors for diagnosis and interpreting three distinct failure scenarios from activity logs.

## Key Information
- All connection attempts through Connectors are logged in the Admin Console
- Activity reports are accessible via **Network** tab → select Resource → **Activity** section
- Each activity record has a **Show details** option on hover
- DNS resolution for Resources is performed by the Connector, not the client device

## Prerequisites
- Admin Console access
- At least one Connector running in the relevant Remote Network
- Ability to SSH into Connector host machine for DNS debugging

## Step-by-Step

### Isolate the Connector
1. Identify which Remote Network the problematic Resource belongs to
2. Shut down all but one Connector in that Remote Network

### Check Connection Events
1. Reproduce the failure from the end user's device
2. In Admin Console → **Network** tab → locate Resource → view **Activity**
3. Hover over records to access **Show details**

## Failure Scenarios & Actions

| Symptom | Cause | Action |
|---|---|---|
| No events logged | Traffic not reaching Connector (client interception or network interface issue) | Investigate connectivity from the client side |
| DNS lookup errors | Connector cannot resolve the hostname/FQDN | SSH into Connector host; run `dig` (Linux/macOS) or `nslookup` (Windows) against the Resource hostname |
| Successful events, no errors | Issue between Connector and the Resource itself | Check firewalls between Connector and app; verify DNS/FQDN resolution from Connector host |

## Gotchas
- Events are only logged when traffic **reaches** a Connector — absence of events does not confirm the Connector is at fault
- All Connectors in a Remote Network must be able to resolve all Resources in that network; configurations may differ between Connectors, making single-Connector isolation critical for DNS debugging
- DNS resolution happens at the **Connector**, not at the client — DNS errors in logs point to Connector-side resolution failure

## Related Docs
- Twingate Traffic Activity Reports
- Twingate Troubleshooting Guide (linked as "Back to troubleshooting guide")
- Client-side connectivity investigation (referenced but not linked)