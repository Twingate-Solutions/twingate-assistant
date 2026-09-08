---
source: https://help.twingate.com/articles/6183198873-checking-connection-events
type: help
fetched: 2026-09-06
source_version: 28d3f3ef5a370e5b9a0700fb341794e807a43350a4f2b7fb1c0a71c8fdd21e50
---

# Checking Connection Events

## Page Title
Checking Connection Events (Twingate Troubleshooting)

## Summary
Connection attempts through Twingate are logged when they reach a Connector, viewable via traffic activity reports in the Admin Console. This guide explains how to isolate and diagnose connection failures using those logs. Three distinct failure scenarios are covered based on what the event log shows.

## Key Information
- Only connections that **reach a Connector** are logged; no event = traffic never reached the Connector
- DNS resolution for hostnames/FQDNs is performed by the **Connector**, not the client device
- Activity logs are accessible: Admin Console → **Network** tab → Resource → **Activity** section
- Each event record has a **Show details** option on hover

## Prerequisites
- Access to Twingate Admin Console
- Ability to SSH (or equivalent) into Connector host machine for DNS debugging
- `dig` or `nslookup` available on Connector host

## Step-by-Step

1. Identify the Remote Network the problematic Resource belongs to
2. Shut down all but **one Connector** in that Remote Network
3. Reproduce the connection failure from the end user's device
4. Navigate to Admin Console → Network → Resource → **Activity**
5. Review event records; hover to access **Show details**

## Failure Scenarios & Resolution

| Symptom | Cause | Action |
|---|---|---|
| No events logged | Client not intercepting traffic OR traffic not leaving Twingate network interface | Check connectivity from Client's perspective |
| DNS lookup errors in events | Connector cannot resolve the hostname/FQDN | SSH into Connector host; run `dig` or `nslookup` to test resolution |
| Successful events, no errors | Problem between Connector and the Resource/service | Check firewalls between Connector and app; verify FQDN DNS config |

## Gotchas
- **All Connectors in a Remote Network must resolve all Resources** in that network — configs may differ between Connectors, making single-Connector isolation critical for DNS debugging
- No Admin Console events does **not** mean the connection worked — it means traffic never reached the Connector
- DNS errors point to the **Connector's** resolver, not the client's DNS

## Related Docs
- [Traffic Activity Reports](https://help.twingate.com) (referenced inline)
- Twingate Client-side connectivity troubleshooting
- Main troubleshooting guide (linked as "Back to troubleshooting guide")