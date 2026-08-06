---
source: https://help.twingate.com/articles/8595638268-active-directory-users-and-computer-aduc-is-slow-over-twingate
type: help
fetched: 2026-08-06
source_version: 09bb59c25c21e663e3012f33f514bc3865a5ce69bc04c33d4286d2268e372dee
---

# Active Directory Users and Computers (ADUC) is Slow Over Twingate

## Summary
ADUC performance degrades when used over Twingate on Windows. The root cause is under investigation. Two workarounds are available: bypassing DNS via direct IP connection or using a jumpbox.

## Key Information
- Affects ADUC (`dsa.msc`) running over Twingate on Windows clients
- Issue is DNS-related in most cases
- Not yet resolved at the Twingate client level

## Prerequisites
- Twingate Client installed on Windows
- Access to domain controller IP address

## Workarounds (in order of preference)

### Option 1: Bypass DNS with Direct IP
Launch ADUC targeting the domain controller by IP instead of hostname:
```cmd
dsa.msc /server="<domain controller IP>"
```

### Option 2: Use a Jumpbox/Administrative Host
- Deploy a jumpbox or admin host on the **same network** as the managed domain
- Perform all AD tasks from that host locally
- Aligns with Microsoft's secure administrative host guidance

## Gotchas
- Environment-specific: Option 1 (IP bypass) resolves the issue for many but not all users
- Hardcoding IP addresses for domain controllers may require updates if DCs change IPs
- Jumpbox approach adds operational overhead but is the more reliable fallback

## Related Docs
- [Microsoft Secure Administrative Hosts guidance](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/implementing-secure-administrative-hosts)