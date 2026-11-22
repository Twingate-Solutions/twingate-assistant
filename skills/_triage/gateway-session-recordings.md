---
source: https://www.twingate.com/docs/gateway-session-recordings
type: docs
fetched: 2026-11-22
source_version: 1e9a7f7572d2275542cdabb8ce4682cf2bda78f69972eee2ac24e223f761cdcd
trust: official
---

<!-- triage: unassigned -->

# Session Recordings (Twingate Gateway)

## Summary
The Twingate Gateway records interactive sessions (`kubectl exec`, SSH shells) in asciicast v2 format and emits them as structured JSON log entries. Recordings stay in your environment and are never uploaded to Twingate. Any log pipeline can route them to storage, and the page includes a Vector-to-GCS example.

## Key Information
- Replay with the Twingate session player (https://www.twingate.com/sessionplayer) or `asciinema play`.
- Default output is JSON log lines on `stderr`. Set `log.sessionRecording.output` to `stdout` or a file (optional rotation) to separate recordings from other logs.
- Log entry fields:
  - `logger`: always `session_recording`
  - `asciicast`: recording content
  - `asciicast_sequence_num`: segment number, increasing per flush
  - `conn_id`: shared by all segments of a session
  - `user`: the Twingate user
  - `ts`: log timestamp
- To rebuild a session, collect all entries with the same `conn_id` and order them by `asciicast_sequence_num`.
- Compatible log shippers: Vector, Fluentd, Fluent Bit.

## Prerequisites (for the Vector → GCS example)
- A Google Cloud Storage bucket.
- A GCP service account with write access to the bucket (Vector authenticates via Workload Identity).
- The label `vector.dev/twingate-gateway=true` on Gateway pods, set via the Gateway's `podLabels` Helm value.
- Recordings must go to `stderr` or `stdout`, since the example reads container logs.

## Step-by-Step (Vector → GCS)
1. Create a Vector `values.yaml`, replacing `<SERVICE_ACCOUNT_EMAIL>` and `<YOUR_GCS_BUCKET_NAME>`. Key parts:
   - `role: Agent`
   - Service account annotation `iam.gke.io/gcp-service-account`
   - Source `kubernetes_logs` with `extra_label_selector: vector.dev/twingate-gateway=true`
   - Transform `gateway_json_logs`: parse the JSON message and keep only `logger == "session_recording"`
   - Transform `session_logging`: drop entries without `.asciicast`, then build the filename parts (`filename_ts_part`, sanitized `user_id`, `conn_id`, `asciicast_sequence_num`)
   - Sink `gcp_cloud_storage` with `filename_extension: cast`, `filename_append_uuid: false`, `compression: none`, `codec: text`, and batch `max_events: 1`, `timeout_secs: 1`
2. Add the Helm repo: `helm repo add vector https://helm.vector.dev`, then `helm repo update`.
3. Install: `helm install vector vector/vector -n vector --create-namespace -f values.yaml`.

Result: each segment is written as `sessionrecordings/<user>_<timestamp>_<sequence>.cast`.

## Configuration Values
```yaml
log:
  sessionRecording:
    output: stderr   # or stdout / file
    segment:
      maxDuration: 5m
      maxSize: "64KiB"
```
- `maxSize` defaults to `64KiB` (65,536 bytes), with a maximum of `256KiB` (262,144 bytes).
- Accepted units: bytes (no unit or `B`), decimal (`KB`/`K`, ×1,000), binary (`KiB`/`Ki`, ×1,024).
- A segment is flushed when it reaches `maxDuration` or `maxSize`.

## Gotchas
- Gateway 2.0 renamed the logger from `gateway.audit` to `session_recording`. Update any existing log filters.
- Kubernetes recording requires the WebSocket streaming protocol. Sessions that fall back to SPDY are not recorded.
- SSH: only interactive shell sessions are recorded. Remote commands (`ssh host <command>`), file transfer, and port forwarding are not.
- Long sessions are split into multiple segments, so don't treat a single log entry as a full session.

## Related Docs
- Gateway (https://www.twingate.com/docs/gateway)
- Kubernetes known issues (https://www.twingate.com/docs/kubernetes-troubleshooting#known-issues)
- Vector Helm chart (https://vector.dev/docs/setup/installation/package-managers/helm/)
- asciicast v2 format (https://docs.asciinema.org/manual/asciicast/v2/)