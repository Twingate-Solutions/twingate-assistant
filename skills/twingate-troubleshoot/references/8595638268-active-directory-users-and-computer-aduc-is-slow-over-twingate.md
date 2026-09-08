---
source: https://help.twingate.com/articles/8595638268-active-directory-users-and-computer-aduc-is-slow-over-twingate
type: help
fetched: 2026-09-06
source_version: d8bd39c04e10105d11ebf3c412a8b8b8e733df4e0fcaf4ac8585e947b6a1921f
---

# Active Directory Users and Computers (ADUC) Slow Over Twingate

## Summary
ADUC performance degrades when accessed through the Twingate client on Windows. Root cause is under investigation. Two workarounds are available depending on environment configuration.

## Key Information
- Affects: Twingate Client on Windows
- Issue: ADUC slow performance when routed through Twingate
- Status: Under active investigation by Twingate

## Prerequisites
- Twingate Client installed on Windows
- Access to Domain Controller IP address
- (Alternative) Jumpbox/admin host on same network as managed domain

## Workarounds (in order of preference)

### Option 1: Bypass DNS, Connect via IP
Run ADUC directly against the Domain Controller IP to bypass DNS resolution overhead:

```cmd
dsa.msc /server="<domain controller IP>"
```

Replace `<domain controller IP>` with the actual IP of your DC.

### Option 2: Use a Jumpbox/Administrative Host
If Option 1 doesn't resolve the issue, connect to a jumpbox or administrative host that resides on the **same network** as the managed domain. Perform all AD tasks from that host locally.

## Configuration Values
| Parameter | Value | Notes |
|-----------|-------|-------|
| `/server` flag | Domain Controller IP | Use IP, not hostname, to bypass DNS |

## Gotchas
- Option 1 works for many but not all environments — results vary by customer setup
- DNS resolution through Twingate appears to be a likely contributor; using IP sidesteps this
- Option 2 (jumpbox) is the fallback and aligns with Microsoft's secure administrative host best practices

## Related Docs
- [Microsoft: Securing Privileged Access / Secure Administrative Hosts](https://learn.microsoft.com/en-us/security/privileged-access-workstations/privileged-access-devices)