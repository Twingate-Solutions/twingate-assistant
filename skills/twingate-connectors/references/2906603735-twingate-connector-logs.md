---
source: https://help.twingate.com/articles/2906603735-twingate-connector-logs
type: help
fetched: 2026-09-06
source_version: dcba1da59ff33cf0267218f4a1d79c8994768e4218bd60cfe7083ade480d1bf6
---

# Twingate Connector Logs

## Summary
Covers enabling debug-level logging on Twingate Connectors across deployment types (systemd, Docker, and other container platforms). Default logging is error-level; debug level must be explicitly enabled for troubleshooting and disabled afterward to avoid excess disk usage.

## Key Information
- Default log level: error
- Debug log level value: `7`
- Environment variable: `TWINGATE_LOG_LEVEL=7`
- Debug logs are verbose — disable when not actively troubleshooting

## Configuration Values
| Variable | Value | Purpose |
|---|---|---|
| `TWINGATE_LOG_LEVEL` | `7` | Enable debug logging |
| *(unset/removed)* | — | Restores error-level logging |

---

## Step-by-Step by Deployment Type

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
**Enable:** Add `TWINGATE_LOG_LEVEL=7` to deployment YAML and redeploy.  
**Disable:** Remove `TWINGATE_LOG_LEVEL=7` from YAML and redeploy.  
**Export logs:** Platform-specific:
- ECS: [AWS docs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/logs.html)
- ACI: `az container logs --resource-group <rg> --name <name>`
- Kubernetes: `kubectl logs` ([docs](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs))

---

## Gotchas
- `2>&1` is required in Docker log export to capture full output (both stdout and stderr)
- Debug logging left enabled long-term causes unnecessary disk utilization
- For non-Docker containers, ensure exports include both `stderr`/`stdout` and timestamps before sending to support

## Related Docs
- [AWS ECS Logging](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/logs.html)
- [Azure Container Instance Logs](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-get-logs)
- [Kubernetes kubectl logs](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs)