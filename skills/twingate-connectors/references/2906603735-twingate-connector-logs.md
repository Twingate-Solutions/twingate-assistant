---
source: https://help.twingate.com/articles/2906603735-twingate-connector-logs
type: help
fetched: 2026-10-04
source_version: 59dc8ff055a812a9e615a6c4baf10e8f22bd2fd3fa230b44c0164aed341be56f
trust: official
---

# Twingate Connector Logs

## Summary
Covers enabling debug-level logging, exporting logs, and restoring default error-level logging for Twingate Connectors. Applies to Linux (systemd), Docker, and other container deployments (ECS, ACI, Kubernetes). Debug logging is off by default due to high verbosity.

## Key Information
- Default log level: **error**
- Debug log level value: `7`
- Environment variable: `TWINGATE_LOG_LEVEL`
- Config file (systemd): `/etc/twingate/connector.conf`
- Disable debug logging when not actively troubleshooting to avoid excessive disk usage

## Configuration Values
| Parameter | Value | Description |
|---|---|---|
| `TWINGATE_LOG_LEVEL` | `7` | Enable debug logging |
| `TWINGATE_LOG_LEVEL` | *(unset/absent)* | Default error-level logging |

---

## Step-by-Step by Deployment Method

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

**Enable debug logging** — script sourced from Twingate's official binary host:
```bash
curl -s https://binaries.twingate.com/connector/docker-change-log-level.sh | sudo bash -s 7
```

**Export logs** (replace `<container>` with container ID or name):
```bash
cont=<container> && ts=$(date -d "today" +"%Y%m%d%H%M") && sudo docker logs -t $cont 2>&1 | sudo tee $cont_$ts.log && sudo gzip $cont_$ts.log
```
> `2>&1` is required to capture full output (both stdout and stderr).

**Disable debug logging:**
```bash
curl -s https://binaries.twingate.com/connector/docker-change-log-level.sh | sudo bash
```

---

### Other Containers (ECS, ACI, Kubernetes)

**Enable:** Add `TWINGATE_LOG_LEVEL=7` to the connector deployment YAML, then redeploy.

**Disable:** Remove `TWINGATE_LOG_LEVEL=7` from the YAML and redeploy.

**Export logs — platform references:**
- **ECS:** [AWS ECS Logging Docs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/logs.html)
- **ACI:** `az container logs --resource-group <rg> --name <name>` — [ACI Docs](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-get-logs)
- **Kubernetes:** `kubectl logs` — [kubectl Docs](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs)

> Ensure logs include both stderr/stdout and timestamps before compressing.

## Gotchas
- Leaving `TWINGATE_LOG_LEVEL=7` set long-term causes unnecessary disk consumption
- Docker export command requires `2>&1` to capture stderr (most connector output)
- For non-Docker containers, YAML must be redeployed for env var changes to take effect

## Related Docs
- [AWS ECS Logging](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/logs.html)
- [Azure Container Instance Logs](https://docs.microsoft.