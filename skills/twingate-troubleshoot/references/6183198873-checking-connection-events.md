---
source: https://help.twingate.com/articles/6183198873-checking-connection-events
type: help
fetched: 2026-08-06
source_version: 591ed6581582a3e496c31ae2ef0e82a16f19eca1edf2b502424251da154e88e0
---

# Checking Connection Events

## Page Title
Checking Connection Events

## Summary
This page explains how to use Twingate's Admin Console traffic activity reports to troubleshoot Resource connection failures. The recommended approach isolates a single Connector per Remote Network to simplify diagnosis of DNS and routing issues.

## Key Information
- All connection attempts through Connectors are logged in the Admin Console under **Network → Resource → Activity**
- Only connections that reach the Connector are logged; missing events indicate client-side issues
- DNS resolution for hostnames/FQDNs is performed by the Connector, not the client
- Activity records show a **Show details** button on hover for granular inspection

## Prerequisites
- Access to Twingate Admin Console
- At least one Connector running in the target Remote Network
- Ability to SSH into the Connector host for DNS troubleshooting

## Step-by-Step

1. Identify the Remote Network the problematic Resource belongs to
2. Shut down all but one Connector in that Remote Network
3. Reproduce the connection failure from the end user's device
4. In Admin Console: **Network tab → Resource → Activity**
5. Hover over activity records and click **Show details**
6. Diagnose based on event results (see below)

## Diagnostic Decision Tree

| Observation | Cause | Action |
|---|---|---|
| No events logged | Client not intercepting traffic or traffic blocked at Twingate network interface | Check client-side connectivity |
| Events show DNS lookup errors | Connector cannot resolve the hostname/FQDN | SSH into Connector host; run `dig` or `nslookup` to test resolution |
| Events show success but access fails | Issue between Connector and Resource | Check firewalls; verify FQDN DNS config |

## Configuration Values
- No specific env vars or API params; diagnostics use OS-level tools:
  - `dig <hostname>` (Linux/macOS)
  - `nslookup <hostname>` (Windows or Linux)

## Gotchas
- **Single Connector rule**: Multiple Connectors in the same Remote Network may have different DNS configurations; keeping one active ensures you know exactly which Connector handled the request
- **DNS is Connector-side**: End user's local DNS config is irrelevant for Resource resolution—the Connector's DNS config is what matters
- **No events ≠ Connector issue**: Absence of logs points to a client/network problem before traffic reaches the Connector
- All Connectors in a Remote Network must be able to resolve all Resources assigned to that network

## Related Docs
- Twingate traffic activity reports
- Client-side connectivity troubleshooting
- [Twingate troubleshooting guide](https://help.twingate.com) (linked as "Back to troubleshooting guide")