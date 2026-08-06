---
source: https://help.twingate.com/articles/2906603735-twingate-connector-logs
type: help
fetched: 2026-08-06
source_version: 6f87b96b2498c48a0a86349f03bb19dbf1b2dd5cd008e772952ab3e572057284
---

# Twingate Connector Logs

## Summary
Covers enabling debug-level logging on Twingate Connectors for troubleshooting. Default log level is error; debug level (7) must be explicitly enabled. Process varies by deployment type: systemd vs. containerized.

## Key Information
- Default log level: **error**
- Debug log level value: **7**
- Debug logging should be disabled after troubleshooting to avoid excessive disk usage
- Applies to: Linux, Docker, ECS, ACI, Kubernetes

## Configuration Values
| Variable | Value | Purpose |
|----------|-------|---------|
| `TWINGATE_LOG_LEVEL` | `7` | Enable debug logging |
| `TWINGATE_LOG_LEVEL` | *(absent)* | Restore default error logging |

---

## Step-by-Step

### Systemd (Linux / AWS AMI)
**Enable:**
```bash
echo "TWINGATE_LOG_LEVEL=7" | sudo tee -a /etc/twingate/connector.conf
sudo systemctl restart twingate-connector
```
**Export logs:**
```bash
ts=$(date -d "today" +"%Y%m%d%H%M") && sudo journalctl --utc -u twingate-connector | tee /tmp/$(hostname -s)_$ts.log && sudo gzip /tmp/$(hostname -s)_$ts.log
```
**Disable:**
```bash
sudo sed -i '/TWINGATE_LOG_LEVEL=7/d' /etc/twingate/connector.conf && sudo systemctl restart twingate-connector
```

### Docker (Linux / macOS)
**Enable:**
```bash
curl -s https://binaries.twingate.com/connector/docker-change-log-level.sh | sudo bash -s 7
```
**Export logs** (replace `<container>` with ID or name):
```bash
cont=<container> && ts=$(date -d "today" +"%Y%m%d%H%M") && sudo docker logs -t $cont 2>&1 | sudo tee $cont_$ts.log && sudo gzip $cont_$ts.log
```
**Disable:**
```bash
curl -s https://binaries.twingate.com/connector/docker-change-log-level.sh | sudo bash
```

### Other Containers (ECS, ACI, Kubernetes)
**Enable:** Add `TWINGATE_LOG_LEVEL=7` to deployment YAML, then redeploy.  
**Disable:** Remove `TWINGATE_LOG_LEVEL=7` from YAML, then redeploy.  
**Export:** Use platform-native log tooling; include both `stdout`/`stderr` and timestamps.

---

## Gotchas
- Docker export command requires `2>&1` to capture full output (stderr + stdout)
- Debug logging left enabled long-term causes unnecessary disk utilization
- Container redeployment required for YAML-based deployments to pick up env var changes
- Config file for systemd is `/etc/twingate/connector.conf`

## Related Docs
- ECS logs: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/logs.html
- ACI logs: https://docs.microsoft.com/en-us/azure/container-instances/container-instances-get-logs
- Kubernetes logs: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs