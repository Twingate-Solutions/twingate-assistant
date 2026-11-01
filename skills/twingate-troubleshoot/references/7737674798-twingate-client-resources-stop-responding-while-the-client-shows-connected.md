---
source: https://help.twingate.com/articles/7737674798-twingate-client-resources-stop-responding-while-the-client-shows-connected
type: help
fetched: 2026-11-01
source_version: f584c548c9db0a82351b3b9490412fabc3e63923830ea44e9aa67cd21383817d
trust: official
---

# [Twingate Client] Resources Stop Responding While Client Shows Connected

## Summary
A known bug causes Twingate Resources to become unresponsive while the Client displays "Connected," with no error shown. The issue occurs after brief network interruptions (sleep/Wi-Fi switching) that leave the Client-Connector connection in a degraded state. Only Relay-based connections are affected; peer-to-peer connections are not.

## Key Information
- **Status:** Known issue; fix in progress
- **Affected component:** Twingate Client with Connector version **1.93.0 or later**
- **Reported platform:** macOS
- **Connection type affected:** Relay-based only (not peer-to-peer)
- **Trigger:** Brief network loss (device sleep, Wi-Fi network switch)
- **Scope:** Intermittent; typically affects individual users, not all users simultaneously

## Symptoms
- Resources hang, time out, or fail to load with no Client error
- Client displays "Connected" throughout the incident
- Non-Twingate traffic (regular internet) continues working normally
- Issue does not self-resolve; persists until Client reconnect or device restart
- Immediate resolution upon disconnect/reconnect confirms this bug as cause

## Workaround (Step-by-Step)
1. Click the Twingate Client and select **Disconnect**
2. Select **Connect** to reconnect — a full application quit is not required
3. Verify Resources are accessible again

> **Note:** The issue can recur after subsequent network interruptions.

## Prerequisites / Conditions to Confirm This Issue
- Connector version ≥ 1.93.0
- Connection routes through a Twingate Relay (not peer-to-peer)
- Disconnect/reconnect restores access immediately

## Gotchas
- The Client shows no error, making this easy to misdiagnose as a Resource-side problem
- Full application quit is **not** required — a simple disconnect/reconnect suffices
- Peer-to-peer connections are **not** affected by this bug
- Restarting the device also resolves the issue but is unnecessary

## Escalation
If the issue recurs frequently or affects multiple users, contact **Twingate Support** with:
- A **Client log upload**
- The **approximate time** the issue started

## Related Docs
- [Client log upload instructions](https://help.twingate.com) *(refer to Twingate Support documentation)*