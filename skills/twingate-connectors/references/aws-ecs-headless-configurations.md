# AWS ECS with Twingate (Headless & Userspace)

## Summary
Twingate provides secure private access for ECS workloads using service accounts. ECS Fargate supports only userspace (HTTP/HTTPS proxy) mode due to kernel capability restrictions, while ECS on EC2 supports full TUN-mode headless clients. Deployment model depends on launch type and traffic requirements.

## Key Information
- **Fargate**: Userspace proxy mode only (`--tun off`); AWS blocks `CAP_NET_ADMIN` and `/dev/net/tun` access
- **ECS on EC2**: Full TUN headless mode supported; recommended to run one client per EC2 host as a systemd service
- Service key must exist as a file at `/etc/twingate/service_key.json` before `twingated` starts
- Init container pattern required on Fargate because AWS Secrets Manager injects secrets as env vars, not files

## Prerequisites
- Twingate service account with a generated service key
- AWS Secrets Manager secret containing the service key JSON
- ECS task execution IAM role with `secretsmanager:GetSecretValue` permission (`ecsTaskExecutionAndSecretsRead`)
- Twingate resources configured and accessible via the service account

## Step-by-Step (Fargate)
1. Store service key JSON in AWS Secrets Manager
2. Define a shared volume (`twingate-etc`) in the task definition
3. Add init container (`alpine`) that reads `SERVICE_KEY_JSON` env var and writes to `/etc/twingate/service_key.json`
4. Add Twingate client container with `dependsOn: init-write-key (SUCCESS)`, entrypoint `twingated`, args `--http-proxy 0.0.0.0:9999 --tun off`
5. Mount shared volume to `/etc/twingate` in both init and client containers
6. Configure application containers to use proxy `http://127.0.0.1:9999`, with `dependsOn: tg-userspace-client (START)`

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Client image | `twingate/client:latest` |
| Entrypoint | `twingated` |
| TUN disabled flag | `--tun off` |
| Proxy bind address | `--http-proxy 0.0.0.0:9999` |
| Service key path | `/etc/twingate/service_key.json` |
| Proxy URL (app containers) | `http://127.0.0.1:9999` |
| Network mode | `awsvpc` |
| Task CPU/Memory | `1024` / `2048` (minimum example) |

## Gotchas
- **Fargate only allows `SYS_PTRACE`** — cannot add `CAP_NET_ADMIN`; full TUN mode will fail silently or error
- **Raw TCP/UDP won't work on Fargate** — userspace proxy is HTTP/HTTPS only; applications must explicitly route through proxy
- **Init container is mandatory** — the client image has no writable entrypoint to handle secret injection directly
- **Sidecar-per-task is discouraged at scale on EC2** — risks API throttling and adds resource overhead; use one client per host instead
- **File permissions**: service key should be `chmod 0444`
- Secret ARN format: `arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-name>`

## Troubleshooting
- Verify `/etc/twingate/service_key.json` exists and is readable
- Check ECS task logs for auth/startup errors
- Confirm execution role has Secrets Manager read permissions
- Review Resource activity in Twingate Admin Console
- For Fargate: ensure no app attempts raw TCP/UDP connections

## Related Docs
- [Userspace Networking](https://www.twingate.com/docs/userspace-networking)
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- Twingate Troubleshooting Guide