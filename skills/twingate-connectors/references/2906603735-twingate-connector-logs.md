---
source: https://help.twingate.com/articles/2906603735-twingate-connector-logs
type: help
fetched: 2026-11-01
source_version: d104b402dfff74d82924b42c5332373a91f8fd05b8889d250068a7e1988aa2f5
trust: official
---

# Twingate Connector Logs

## Summary
Covers how to enable debug-level logging on Twingate Connectors, collect logs for support, and restore default error-level logging. Applies to Linux (systemd), Docker, and other container deployments (ECS, ACI, Kubernetes).

## Key Information
- Default log level is **error**; debug logging must be explicitly enabled
- Debug logging is verbose — disable it after troubleshooting to avoid excess disk usage
- Log level is controlled via the `TWINGATE_LOG_LEVEL` environment variable
- Value `7` = debug; removing the variable restores error-level logging

## Configuration Values
| Variable | Value | Effect |
|---|---|---|
| `TWINGATE_LOG_LEVEL` | `7` | Enable debug logging |
| `TWINGATE_LOG_LEVEL` | *(unset)* | Default error logging |

---

## Step-by-Step by Deployment Type

### Systemd (Linux / AWS AMI)
**Enable debug:**
```bash
echo "TWINGATE_LOG_LEVEL=7" | sudo tee -a /etc/twingate/connector.conf
sudo systemctl restart twingate-connector
```
**Export logs:**
```bash
ts=$(date -d "today" +"%Y%m%d%H%M") && sudo journalctl --utc -u twingate-connector | tee /tmp/$(hostname -s)_$ts.log && sudo gzip /tmp/$(hostname -s)_$ts.log
```
**Disable debug:**
```bash
sudo sed -i '/TWINGATE_LOG_LEVEL=7/d' /etc/twingate/connector.conf && sudo systemctl restart twingate-connector
```

### Docker (Linux / macOS)
**Enable debug:** Download and run the log-level script from `binaries.twingate.com` — see [the official page](https://help.twingate.com/articles/2906603735-twingate-connector-logs). The script re-creates the container with `TWINGATE_LOG_LEVEL=7` preserving existing config.

**Export logs** (replace `<container>` with ID or name):
```bash
cont=<container> && ts=$(date -d "today" +"%Y%m%d%H%M") && sudo docker logs -t $cont 2>&1 | sudo tee ${cont}_$ts.log && sudo gzip ${cont}_$ts.log
```
> `2>&1` is required to capture full output (stderr + stdout).

**Disable debug:** Run the same script from `binaries.twingate.com` without arguments.

### Other Containers (ECS, ACI, Kubernetes)
**Enable debug:** Add `TWINGATE_LOG_LEVEL=7` to the connector deployment YAML, then redeploy.

**Export logs:** Platform-specific:
- **ECS:** [AWS ECS Logs docs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/logs.html)
- **ACI:** `az container logs --resource-group <rg> --name <name>` — [Azure docs](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-get-logs)
- **Kubernetes:** `kubectl logs` — [Kubernetes docs](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs)

**Disable debug:** Remove `TWINGATE_LOG_LEVEL=7` from the deployment YAML and redeploy.

---

## Gotchas
- Export both `stdout` and `stderr` with timestamps for all platforms
- Long-running debug logging causes unnecessary disk usage
- Config file path for systemd: `/etc/twingate/connector.conf`

## Related Docs
- [AWS ECS Logging](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/logs.html)
- [Azure ACI Logs](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-get-logs)
- [Kubernetes kubectl logs](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs)