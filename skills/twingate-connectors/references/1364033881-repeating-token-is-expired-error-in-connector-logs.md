---
source: https://help.twingate.com/articles/1364033881-repeating-token-is-expired-error-in-connector-logs
type: help
fetched: 2026-11-01
source_version: 6fe28b9167faab4141c19b94109ff2482d53e240afb35990e45743dc589ac610
trust: official
---

# Repeating 'Token is expired' Error in Connector Logs

## Summary
Twingate connectors periodically log a `Token is expired` 403 error from PubNub's Access Manager. This is expected behavior — the connector automatically renews the token and resumes normal operation without any manual intervention.

## Key Information
- Error appears in connector logs when the PubNub subscription token naturally expires
- Connector self-heals: it requests a new token automatically after expiration
- The error is cosmetic/informational, not indicative of a real failure
- The message may appear prominent when detailed logging is disabled, as it may be one of the few visible log entries in that mode

## Sample Log Output
```
twingate-connector[6479]: Response was: {"error":true,"status":403,"service":"Access Manager","message":"Token is expired."}
twingate-connector[6479]: pbcc_parse_subscribe_v2_response ... AccessDenied: response from server
```

## Resolution
**No action required.** The connector automatically obtains a new token and continues normal operation.

## Gotchas
- If detailed logging is disabled, this 403 error may be one of the only log messages visible, making it appear more serious than it is
- The error originates from PubNub's Access Manager (not Twingate's core auth), which can cause confusion
- Do not treat this as a credential failure or connector misconfiguration

## Related Docs
- Twingate Connector documentation (general)
- Connector logging configuration (enable detailed logging to see full context around this message)