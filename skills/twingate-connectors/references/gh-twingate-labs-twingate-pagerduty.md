---
source: https://github.com/Twingate-Labs/twingate-pagerduty
type: github
fetched: 2026-08-06
source_version: eaa08cd4b6cd5e8c6d746041cf066e824879dbc7
---

<!-- triage: unassigned -->

# Twingate-PagerDuty Integration

## Summary
A bash script integration that monitors a Twingate connector via `journalctl` and forwards connection errors and state changes to PagerDuty. It triggers incidents when the connector goes offline or encounters errors, and auto-resolves them when the connector returns online.

## Key Information
- Runs as a systemd service on the Twingate connector host
- Tails connector logs using `journalctl -f`, filtering for `error_message` and `State:` entries
- Uses PagerDuty's `dedup_key` for incident deduplication
- Sends raw analytics JSON payloads for connection errors; constructs custom JSON for state change events
- Connector states that trigger an incident: `Offline`, `Error`, `Unrecoverable error`
- Connector state `Online` sends a recovery event to auto-resolve the incident

## Prerequisites
- Active Twingate account and a deployed Twingate connector
- PagerDuty account with Admin base role
- A configured PagerDuty service with an **Events API v2** integration (Integration Key required)
- `curl`, `journalctl`, and `systemd` available on the connector host

## Usage / Step-by-Step

**PagerDuty side:**
1. Add a new integration to a PagerDuty service (or create a new service)
2. Select **Twingate** as the integration type
3. Save and copy the generated **Integration Key** / Integration URL

**Connector host:**
1. Enable analytics logging:
   ```
   echo 'TWINGATE_LOG_ANALYTICS=v1' >> /etc/twingate/connector.conf
   sudo service twingate-connector restart
   ```
2. Create the config file with your values:
   ```
   sudo echo 'PAGERDUTY_INTEGRATION_URL=<url>' > /etc/twingate/twingate-pagerduty.conf
   sudo echo 'CONNECTOR_NAME=<name>' >> /etc/twingate/twingate-pagerduty.conf
   ```
3. Create `/usr/bin/twingate-pagerduty.sh` and `/etc/systemd/system/twingate-pagerduty.service` using the commands in the README
4. Reload systemd and start the service:
   ```
   sudo systemctl daemon-reload
   sudo service twingate-pagerduty start
   ```

## Configuration Values

| Variable | Location | Description |
|---|---|---|
| `PAGERDUTY_INTEGRATION_URL` | `/etc/twingate/twingate-pagerduty.conf` | Full PagerDuty Events API endpoint URL |
| `CONNECTOR_NAME` | `/etc/twingate/twingate-pagerduty.conf` | Unique identifier for the connector; falls back to `hostname` if unset |
| `TWINGATE_LOG_ANALYTICS` | `/etc/twingate/connector.conf` | Must be set to `v1` to enable analytics log output |

## Gotchas
- The script uses `grep` exit codes for flow control; any changes to log format in future connector versions may silently break filtering
- `CONNECTOR_NAME` is arbitrary but should be unique per connector to avoid dedup key collisions across connectors
- The service file's `EnvironmentFile` points to `/etc/twingate/twingate-pagerduty.conf`; file must exist before starting the service
- No log rotation or error handling for failed `curl` calls—failed PODs are silently dropped

## Related Docs
- [PagerDuty Services and Integrations](https://support.pagerduty.com/docs/services-and-integrations)
- [PagerDuty Event Deduplication](https://support.pagerduty.com/docs/event-management#deduplicate-incidents)
- [PagerDuty User Roles](https://support.pagerduty.com/docs/user-roles)
- [Issues / Support](https://github.com/Twingate-Labs/twingate-pagerduty/issues)