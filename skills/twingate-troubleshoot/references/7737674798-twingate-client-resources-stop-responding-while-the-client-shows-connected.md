---
source: https://help.twingate.com/articles/7737674798-twingate-client-resources-stop-responding-while-the-client-shows-connected
type: help
fetched: 2026-11-15
source_version: bc69570d49acad8c1e37416fe62f7a0ad0c34848156cef0470b3427da78605dd
trust: official
---

# Page Title
[Twingate Client] Resources Stop Responding While the Client Shows Connected

## Summary
Twingate Resources can stop responding while the Client still shows Connected, with no error displayed. Reconnecting the Client restores access immediately. Twingate is investigating; the issue has been reported on macOS and the root cause is not yet known.

## Key Information
- **Applies to:** Twingate Client and Connector; reported on macOS.
- **Symptoms:**
  - Resources hang, time out, or fail to load (web apps, git operations, internal services) with no Client error.
  - Client displays Connected throughout.
  - Non-Twingate traffic (public websites and apps) works normally.
  - Does not self-resolve; persists until the Client is reconnected or the device is restarted.
  - Intermittent, typically affects individual users rather than everyone at once.
- **Diagnostic hint:** If disconnecting and reconnecting immediately restores access, this issue is the most likely cause.
- **Cause:** Under investigation. In reported cases, affected connections pass through a Twingate Relay.
- The article is being updated as more information becomes available.

## Prerequisites
- None specific. Access to the Twingate Client on the affected device. A Client log upload is needed if contacting Support.

## Step-by-Step (Workaround)
1. Disconnect the Twingate Client.
2. Connect it again. A full quit of the application is not required.
3. Verify Resource access is restored.
4. If the issue recurs frequently or affects many users, contact Twingate Support with:
   - A Client log upload
   - The approximate time the issue started

## Configuration Values
- None. No env vars, CLI flags, or API parameters are documented for this issue.

## Gotchas
- The Client status gives no indication of failure, so "Connected" does not confirm the tunnel is working.
- The problem can recur after reconnecting; reconnecting is a workaround, not a fix.
- The issue won't clear on its own, so waiting is not effective.
- Only macOS reports are documented so far, but the component scope is listed as Client and Connector.
- The Relay involvement is an observation from reported cases, not a confirmed cause.

## Related Docs
- Twingate Support: submit a ticket with logs for frequent or widespread occurrences.
- Twingate documentation on uploading Client logs (linked from the original article as "Client log upload").
- Original article: https://help.twingate.com/articles/7737674798-twingate-client-resources-stop-responding-while-the-client-shows-connected