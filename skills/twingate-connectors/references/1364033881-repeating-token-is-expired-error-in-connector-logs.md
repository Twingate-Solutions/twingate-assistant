---
source: https://help.twingate.com/articles/1364033881-repeating-token-is-expired-error-in-connector-logs
type: help
fetched: 2026-09-06
source_version: b90753245f8a0217443e99de77d886d1ab1072432fb7e00bfb5cc94ccaf6dafc
---

# Repeating 'Token is expired' Error in Connector Logs

## Summary
Twingate connectors periodically log a `Token is expired` 403 error from the Access Manager service. This is expected behavior — the connector automatically renews the token and resumes normal operation without manual intervention.

## Key Information
- Error originates from PubNub subscription token expiration
- Connector self-heals by requesting a new token automatically
- Error appears more alarming when detailed logging is disabled (may be one of few visible log messages)
- No service interruption occurs during token renewal

## Error Pattern
```
{"error":true,"status":403,"service":"Access Manager","message":"Token is expired."}
```
- HTTP status: `403`
- Service: `Access Manager`
- Source file reference: `pubnub_netcore.c` / `pbcc_parse_subscribe_v2_response`
- Error code: `AccessDenied`

## Resolution
**No action required.** The connector handles token renewal automatically.

## Gotchas
- If detailed/verbose logging is disabled, this 403 error may appear as one of the only visible log lines, making it look like a persistent failure when it is not
- The repeated appearance does not indicate the connector is stuck or broken — check connector connectivity separately if actual resource access fails

## Related Docs
- Twingate Connector documentation
- Connector logging configuration