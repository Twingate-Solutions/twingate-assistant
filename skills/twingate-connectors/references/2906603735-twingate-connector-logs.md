---
source: https://help.twingate.com/articles/2906603735-twingate-connector-logs
type: help
fetched: 2026-11-08
source_version: 5235b5fc15cd9bf155e04a634633ae27fbd57bb8cb3a04100f2f50fad16a09bd
trust: official
---

# Twingate Connector Logs

## Summary
Covers enabling debug-level logging for Twingate Connectors across deployment types (systemd, Docker, container orchestrators). Default log level is error; debug level (`7`) is used for troubleshooting. Logs should be collected and debug mode disabled after troubleshooting.

## Key Information
- Default log level: **error**
- Debug log level value: **`7`**
- Log exports should include both `stderr` and `stdout` with timestamps
- Long-term debug logging causes unnecessary disk utilization — disable after use

## Configuration Values
| Variable | Value | Purpose |
|---|---|---|
| `TWINGATE_LOG_LEVEL` | `7` | Enable debug logging |
| `TWINGATE_LOG_LEVEL` | *(absent/removed)* | Restore error-level logging |

---

## Step-by-Step by Deployment Type

### Systemd (Linux / AWS AMI)

**Enable debug logging:**
```bash
echo "TWINGATE_LOG_LEVEL=7" | sudo tee -a /etc/twingate/connector.conf
sudo systemctl restart twingate-connector
```

**Export logs:**
```bash
ts=$(date -d "today" +"%Y%m%d%H%M") && sudo journalctl --utc -u twingate-connector | tee /tmp/$(hostname -s)_$ts.log && sudo gzip /tmp/$(hostname -s)_$ts.log
```
Output: `/tmp/<hostname>_<timestamp>.log.gz`

**Disable debug logging:**
```bash
sudo sed -i '/TWINGATE_LOG_LEVEL=7/d' /etc/twingate/connector.conf && sudo systemctl restart twingate-connector
```

---

### Docker (Linux / macOS)

**Enable debug logging** (script from official Twingate host, re-creates container with debug env var):
```bash
curl -s https://binaries.twingate.com/connector/docker-change-log-level.sh | sudo bash -s 7
```

**Export logs** (replace `<container_id>` with actual ID or name):
```bash
cont=<container_id> && ts=$(date -d "today" +"%Y%m%d%H%M") && sudo docker logs -t $cont 2>&1 | sudo tee $cont_$ts.log && sudo gzip $cont_$ts.log
```
Note: `2>&1` is required to capture full output.

**Disable debug logging:**
```bash
curl -s https://binaries.twingate.com/connector/docker-change-log-level.sh | sudo bash
```

---

### Other Containers (ECS, ACI, Kubernetes)

**Enable:** Add `TWINGATE_LOG_LEVEL=7` as an environment variable in the deployment YAML, then redeploy.

**Disable:** Remove `TWINGATE_LOG_LEVEL=7` from deployment YAML, then redeploy.

**Export logs** — platform-specific:
- **ECS:** [AWS ECS Logging Docs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/logs.html)
- **ACI:** `az container logs --resource-group <rg> --name <name>` — [Azure Docs](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-get-logs)
- **Kubernetes:** `kubectl logs` — [K8s Docs](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs)

## Gotchas
- Must include both `stderr` + `stdout` when exporting; use `2>&1` in Docker commands
- Docker log export command requires manually substituting `<container_id>`
- Debug logging left enabled long-term causes excessive disk usage
- Config file path for systemd: `/etc/twingate/connector.conf`

## Related Docs
- [AWS ECS Logging](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/logs.html)
- [Azure ACI Logs](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-get-logs)