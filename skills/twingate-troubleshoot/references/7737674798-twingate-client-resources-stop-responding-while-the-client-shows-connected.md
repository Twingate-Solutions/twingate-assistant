---
source: https://help.twingate.com/articles/7737674798-twingate-client-resources-stop-responding-while-the-client-shows-connected
type: help
fetched: 2026-11-22
source_version: d6f60e4b0645aa15b66fd9224c15323741805c93cd5259e96ff4bd28e311b76e
trust: official
---

# Page Title
[Twingate Client] Resources Stop Responding While the Client Shows Connected

## Summary
Twingate Resources can stop responding while the Client still shows Connected, with no error displayed. Reconnecting the Client restores access immediately. Twingate is investigating; the cause is not yet determined. Reported on macOS.

## Key Information
- **Applies to:** Twingate Client and Connector; reported on macOS.
- **Symptoms:**
  - Resources hang, time out, or fail to load, with no Client error. This affects web apps, git operations, and internal services.
  - The Client shows Connected the whole time.
  - Non-Twingate sites and apps keep working.
  - The issue does not clear on its own. It persists until the Client reconnects or the device restarts.
  - It is intermittent and usually affects individual users, not everyone at once.
- **Diagnostic hint:** If disconnecting and reconnecting the Client restores access, this issue is the most likely cause.
- **Cause:** Under investigation. In reported cases, the affected connections pass through a Twingate Relay.

## Prerequisites
- None stated.

## Step-by-Step (Workaround)
1. Disconnect the Twingate Client.
2. Connect it again. A full quit of the application is not needed.
3. Confirm Resource access is restored.

If the issue recurs often or affects many users, contact Twingate Support and include:
- A Client log upload
- The approximate time the issue started

## Configuration Values
- None. No env vars, CLI flags, or API parameters are given.

## Gotchas
- The Client UI gives no indication of the failure, so "Connected" does not confirm a working tunnel.
- The issue can recur after a reconnect.
- It does not self-resolve.
- The page says it will be updated as the investigation progresses, so check it for a root cause or fix.

## Related Docs
- Client logs article: [Twingate Client logs](https://help.twingate.com/articles/8458642629-twingate-client-logs)
- Twingate Support (no URL in source)