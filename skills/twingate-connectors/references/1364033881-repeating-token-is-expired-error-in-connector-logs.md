---
source: https://help.twingate.com/articles/1364033881-repeating-token-is-expired-error-in-connector-logs
type: help
fetched: 2026-08-06
source_version: d10d49ebbd3bd5202caf463f44128beddd485ca0284b13fe0625f4ea78ea6ee1
---

# Repeating 'Token is expired' Error in Connector Logs

## Summary
Twingate connectors log a `Token is expired` 403 error when their authentication token naturally expires. This is expected behavior — the connector automatically requests a new token and resumes normal operation without manual intervention.

## Key Information
- Error originates from PubNub Access Manager (403 response)
- Token expiration and renewal is part of normal connector lifecycle
- Connector auto-renews tokens with no downtime or manual action required
- Message appears more alarming when detailed logging is disabled, as it may be one of the few visible log entries

## Error Signature
```
{"error":true,"status":403,"service":"Access Manager","message":"Token is expired."}
```
Logged by: `twingate-connector` process via `pubnub_netcore.c`

## Resolution
**No action required.** The connector handles token renewal automatically.

## Gotchas
- If verbose/detailed logging is disabled, this error may appear isolated without surrounding context logs, making it look like a persistent failure when it is not
- The error does **not** indicate connector misconfiguration, network issues, or authentication problems requiring intervention
- Seeing this error repeatedly in logs is normal — each recurrence is a natural token refresh cycle

## Related Docs
- Twingate Connector deployment and configuration
- Connector log monitoring