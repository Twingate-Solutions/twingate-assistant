---
source: https://help.twingate.com/articles/7737674798-twingate-client-resources-stop-responding-while-the-client-shows-connected
type: help
fetched: 2026-11-19
source_version: 8dd37b669c3bae5ce3ffa0821438889c8060858473fc7b2659a757ef6c200fe2
trust: official
---

# Page Title
[Twingate Client] Resources Stop Responding While the Client Shows Connected

## Summary
Twingate Resources can stop responding while the Client still shows Connected, with no error displayed. Reconnecting the Client restores access immediately. Twingate is investigating and has not identified a root cause. The page will be updated as more information becomes available.

## Key Information
- **Applies to:** Twingate Client and Connector. Reported on macOS.
- **Symptoms:**
  - Resources hang, stop loading, or time out. This affects web apps, git operations, and internal services.
  - The Client shows Connected throughout.
  - Non-Twingate sites and apps keep working normally.
  - The issue does not clear on its own. It persists until the Client is reconnected or the device is restarted.
  - It is intermittent and usually affects individual users, not everyone at once.
- **Diagnostic hint:** If disconnecting and reconnecting the Client fixes the problem, this issue is the most likely cause.
- **Cause:** Under investigation. In the reported cases, the affected connections pass through a Twingate Relay.

## Prerequisites
None stated.

## Step-by-Step (Workaround)
1. Disconnect the Twingate Client.
2. Connect it again. A full quit of the application is not required.
3. Access to Resources is restored once the Client reconnects.

If the issue recurs frequently or affects many users, contact Twingate Support and include:
- A Client log upload
- The approximate time the issue started

## Configuration Values
None. There are no env vars, CLI flags, or API parameters in this article.

## Gotchas
- The Client UI gives no error and shows Connected, so the status indicator cannot be used to detect the problem.
- The issue can recur after reconnecting.
- It will not self-resolve. A reconnect or device restart is required.
- Because it is intermittent and per-user, it can be mistaken for an app-level or network problem.
- Reports so far involve macOS, but the article lists Client and Connector as the affected components.

## Related Docs
- Twingate Support, for escalation.
- Client log upload instructions. The article links to these but gives no URL.