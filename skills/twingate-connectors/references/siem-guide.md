## SIEM Integration for Connector Logs

Options for centralizing Twingate Connector logs into a SIEM. Connectors log all events in real time via `journald` (systemd). Four integration paths are supported.

**Option 1 — AWS S3 (recommended):**
- Configure Twingate's native S3 sync to deliver audit logs, network events, and DNS filtering logs every 5 minutes
- Feed from S3 into your SIEM downstream
- See /docs/syncing-data-to-s3 for setup

**Option 2 — Syslog:**
1. Enable real-time connection logs on Connectors (`TWINGATE_LOG_ANALYTICS=v2`)
2. Edit `/etc/systemd/journald.conf`: uncomment `#ForwardToSyslog=yes`
3. Configure syslog (`/etc/syslog.conf`) to forward to your central syslog server
4. Restart the Connector

**Option 3 — Vector (open-source log pipeline):**
- Supports sources (journald), transforms, and sinks including: AWS CloudWatch, AWS S3, Datadog, Elasticsearch, GCP Cloud Monitoring, Honeycomb, New Relic, Prometheus, Splunk, and many more
1. Enable real-time connection logs on Connectors
2. Install Vector on the Connector host
3. Create `vector.toml` with source (journald), transforms, and sink config for your SIEM
- See Vector docs and Twingate documentation for config details

**Option 4 — Datadog Agent:**
- Datadog agent reads from journald and feeds the Twingate analytics dashboard in Datadog
- Requires real-time connection logs enabled; follow Datadog's official agent documentation

**Related Docs:**
- /docs/syncing-data-to-s3 -- Native S3 sync setup
- /docs/connector-real-time-logs -- Enabling real-time connection logs
- /docs/advanced-connector-management -- Advanced Connector env var reference
