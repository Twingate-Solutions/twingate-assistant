---
source: https://help.twingate.com/articles/1364033881-repeating-token-is-expired-error-in-connector-logs
type: help
fetched: 2026-11-08
source_version: d2d2c729e6f1aed4935526930cd281e1749a972a0d599e07b24e66943089f42d
trust: official
---

# Repeating 'Token is expired' Error in Connector Logs

## Summary
Twingate connectors periodically log a `Token is expired` 403 error from the Access Manager service. This is expected behavior — the connector automatically renews its token and resumes normal operation without any manual intervention.

## Key Information
- Error originates from PubNub subscription token expiration (HTTP 403 from Access Manager)
- Connector self-heals by automatically requesting a new token
- No service disruption occurs during token renewal
- Error is especially visible when detailed logging is disabled, making it appear more significant than it is

## Sample Log Output
```
connector_hostname twingate-connector[6479]: Response was: {"error":true,"status":403,"service":"Access Manager","message":"Token is expired."}
connector_hostname twingate-connector[6479]: pbcc_parse_subscribe_v2_response - AccessDenied: response from server
```

## Resolution
**No action required.** The connector handles token renewal automatically.

## Gotchas
- With minimal/non-detailed logging enabled, this 403 error may be one of the only log messages visible, creating a false impression of a persistent failure
- The error references `pubnub_netcore.c` — this is Twingate's internal use of PubNub for real-time communication, not a customer-facing configuration item
- If the error appears continuously without recovery (connector stays offline), that would indicate a separate underlying issue beyond normal token expiration

## Related Docs
- Twingate Connector troubleshooting (Twingate Help Center)
- Connector logging configuration