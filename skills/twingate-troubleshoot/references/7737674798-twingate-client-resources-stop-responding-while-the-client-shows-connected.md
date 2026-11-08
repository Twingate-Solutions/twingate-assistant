---
source: https://help.twingate.com/articles/7737674798-twingate-client-resources-stop-responding-while-the-client-shows-connected
type: help
fetched: 2026-11-08
source_version: 14839e5971162c24595ec6d6e659239e64b3f0dc7801805f350d6425ea698be7
trust: official
---

# [Twingate Client] Resources Stop Responding While Client Shows Connected

## Summary
Twingate Resources become unresponsive while the Client displays a Connected status, with no error messages shown. The issue affects connections routed through Twingate Relays and is currently under active investigation. Access is immediately restored by disconnecting and reconnecting the Client.

## Key Information
- **Components affected:** Client and Connector
- **Platform:** Reported on macOS
- **Status:** Under active investigation; article will be updated
- **Connections involved:** Affected connections pass through a Twingate Relay

## Symptoms
- Resources fail to load, hang, or time out with no Client error
- Affects web apps, git operations, and internal services
- Client continues to show **Connected** throughout
- Non-Twingate traffic (regular internet) works normally
- Issue does **not** self-resolve; persists until Client reconnect or device restart
- Intermittent; typically affects individual users, not all users simultaneously

## Workaround (Step-by-Step)
1. Click the Twingate Client and **Disconnect** (full application quit is not required)
2. **Reconnect** the Client
3. Verify Resources are accessible again

> ⚠️ The issue can recur after reconnecting.

## Gotchas
- No error is displayed in the Client UI — the Connected status is misleading during the failure state
- The fix is temporary; the issue may recur and requires another disconnect/reconnect cycle
- If disconnecting and reconnecting does **not** restore access, this issue is likely not the cause

## Escalation / Support
If the issue occurs frequently or affects multiple users:
- Contact Twingate Support
- Include a **Client log upload**
- Include the **approximate time** the issue started

## Related Docs
- Client log upload (referenced in Twingate Help Center)