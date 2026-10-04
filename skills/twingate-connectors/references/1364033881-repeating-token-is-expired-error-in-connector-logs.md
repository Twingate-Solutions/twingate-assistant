---
source: https://help.twingate.com/articles/1364033881-repeating-token-is-expired-error-in-connector-logs
type: help
fetched: 2026-10-04
source_version: 6e9cd0f51d955afa843c0be25885ca38f3ed6faa4c8396f942d1d88d918e10de
trust: official
---

# Repeating 'Token is expired' Error in Connector Logs

## Summary
Twingate connectors periodically log a `Token is expired` 403 error from the Access Manager service. This is expected behavior — the connector automatically renews its token and resumes normal operation without manual intervention.

## Key Information
- Error originates from PubNub subscription token expiration (not authentication failure)
- Connector self-heals by requesting a new token automatically
- Error is more visible when detailed logging is disabled, as it may be one of the few log entries shown
- No service disruption occurs

## Sample Log Output
```
twingate-connector[6479]: Response was: {"error":true,"status":403,"service":"Access Manager","message":"Token is expired."}
twingate-connector[6479]: pbcc_parse_subscribe_v2_response - AccessDenied: response from server
```

## Resolution
**No action required.** The connector handles token renewal automatically.

If the error repeats continuously without recovery, investigate:
- Network connectivity between connector and Twingate control plane
- Connector process health (restart if stuck)

## Gotchas
- With minimal logging enabled, this error may appear disproportionately prominent — it does not indicate the connector is broken
- A single occurrence or occasional recurrence is normal; only persistent, non-recovering errors warrant investigation

## Related Docs
- Twingate Connector documentation: https://help.twingate.com