---
source: https://help.twingate.com/articles/9539322912-twingate-linux-client-fails-to-start-logs-show-dns-errors
type: help
fetched: 2026-08-06
source_version: bbaa4de9b58e4803239355179fa4e6a35a575843d4546beedd7eaf0fdd349ea8
---

# Twingate Linux Client Fails to Start - DNS Errors

## Page Title
Twingate Linux Client fails to start - logs show DNS errors

## Summary
A compatibility issue between Twingate Linux client v1.0.78 or earlier and Network Manager v1.42+ causes the client to set an invalid upstream DNS server address, preventing authentication and connection. The symptom is a log error indicating all nameservers have failed.

## Key Information
- **Affected component:** Twingate Linux Client
- **Affected platform:** Linux only
- **Affected versions:** Twingate client v1.0.78 or earlier
- **Conflicting component:** Network Manager v1.42 or later
- **Root cause:** Network Manager v1.42 changed nameserver reporting behavior; Twingate misinterprets this and sets an invalid upstream DNS server

## Prerequisites
- Access to terminal with ability to run `NetworkManager -V`
- Ability to either upgrade Twingate client or downgrade Network Manager

## Diagnosis

Check Network Manager version:
```bash
NetworkManager -V
```
If output shows v1.42 or later, this issue applies.

**Log error indicator:**
```
[msg] All nameservers have failed
```

## Solutions

Two options (either/or):

1. **Upgrade Twingate client** to a version greater than v1.0.78
   - Preferred long-term fix
   - Note: at time of documentation, this version was not yet released

2. **Downgrade Network Manager** to v1.40 or lower
   - Temporary workaround if updated Twingate client is unavailable

## Gotchas
- This issue only manifests after updating Network Manager to v1.42+; existing installations may break after a system package update
- The "not yet released" note on the Twingate fix may be outdated — check current client version availability before downgrading Network Manager
- Downgrading Network Manager may affect other system networking functionality; prefer upgrading Twingate client when possible

## Related Docs
- Twingate Linux client installation documentation
- Network Manager release notes for v1.42