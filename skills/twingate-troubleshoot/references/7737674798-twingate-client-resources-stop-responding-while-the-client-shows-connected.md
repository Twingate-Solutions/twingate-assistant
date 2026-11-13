---
source: https://help.twingate.com/articles/7737674798-twingate-client-resources-stop-responding-while-the-client-shows-connected
type: help
fetched: 2026-11-13
source_version: bdbd341b54c536194f7537c5a558166f70df58f3acfb55c030f07d7f2e11170e
trust: official
---

# Page Title
[Twingate Client] Resources Stop Responding While the Client Shows Connected

## Summary
Twingate Resources can stop responding while the Client still shows Connected, with no error displayed. Reconnecting the Client restores access immediately. Twingate is investigating the cause, and the page will be updated as more is learned.

## Key Information
- **Applies to:** Twingate Client and Connector. Reported on macOS.
- **Symptoms:**
  - Resources hang, time out, or fail to load. This affects web apps, git operations, and internal services.
  - The Client shows Connected throughout, with no error.
  - Non-Twingate traffic (sites and apps that are not Resources) works normally.
  - The issue does not clear on its own. It persists until the Client is reconnected or the device is restarted.
  - It is intermittent and typically affects individual users, not everyone at once.
- **Diagnostic hint:** If disconnecting and reconnecting immediately restores access, this issue is the most likely cause.
- **Cause:** Under investigation. In reported cases, the affected connections pass through a Twingate Relay.

## Prerequisites
- Access to the affected user's Twingate Client (to disconnect and reconnect).
- For escalation: ability to upload Client logs.

## Step-by-Step (Workaround)
1. In the Twingate Client, disconnect.
2. Connect again. A full quit of the application is not required.
3. Verify Resource access is restored.
4. If the problem recurs frequently or affects many users, contact Twingate Support with:
   - A Client log upload
   - The approximate time the issue started

## Configuration Values
None. No environment variables, CLI flags, or API parameters are documented for this issue.

## Gotchas
- The Client status gives no indication of the failure, so Connected does not mean Resources are reachable.
- Because non-Resource traffic still works, the problem can look like an application or network fault rather than a Twingate one.
- The issue can recur after reconnecting.
- No permanent fix or root cause is published yet, so check the article for updates.

## Related Docs
- Twingate guidance on uploading Client logs (linked from the original article as "Client log upload")
- Twingate Support, for frequent or widespread occurrences