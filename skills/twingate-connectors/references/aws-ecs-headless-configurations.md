# AWS ECS with Twingate (Headless & Userspace)

## Page Title
AWS ECS with Twingate (Headless & Userspace Configurations)

## Summary
Twingate supports secure private access for ECS workloads via service accounts, with two networking modes depending on launch type. ECS Fargate is limited to userspace (HTTP/HTTPS proxy) mode due to kernel capability restrictions, while ECS on EC2 supports full headless TUN mode. The recommended deployment for EC2 is one Twingate client per host via systemd, not per-task sidecars.

## Key Information
- **Fargate**: Userspace proxy mode only (`--tun off`); no `/dev/net/tun` or `CAP_NET_ADMIN` available
- **ECS on EC2**: Full TUN mode supported; recommended as default
- **Service key path**: `/etc/twingate/service_key.json` (must be a file, not env var)
- **Init container pattern**: Required on Fargate to write AWS Secrets Manager env var to file before `twingated` starts
- **Sidecar per task is NOT recommended at scale** on EC2 — use one client per host instead
- Proxy listens on `0.0.0.0:9999`; apps use `http://127.0.0.1:9999`

## Prerequisites
- Twingate service account with service key stored in AWS Secrets Manager
- ECS task execution IAM role with Secrets Manager read permissions (`ecsTaskExecutionAndSecretsRead`)
- For EC2 mode: Linux host with kernel capabilities enabled

## Step-by-Step (Fargate Deployment)
1. Store service key JSON in AWS Secrets Manager
2. Create shared EFS/volume `twingate-etc`
3. Deploy **init container** (`alpine`) that writes `$SERVICE_KEY_JSON` env var → `/etc/twingate/service_key.json`
4. Deploy **Twingate client container** with `dependsOn: init-write-key (SUCCESS)`, entrypoint `twingated`, args `--http-proxy 0.0.0.0:9999 --tun off`
5. Configure application containers to use proxy `http://127.0.0.1:9999`, `dependsOn: tg-userspace-client (START)`

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Client image | `twingate/client:latest` |
| Entrypoint | `twingated` |
| TUN disabled flag | `--tun off` |
| Proxy binding | `--http-proxy 0.0.0.0:9999` |
| Service key path | `/etc/twingate/service_key.json` |
| Network mode | `awsvpc` |
| Task CPU/Memory | `1024` / `2048` |
| Secret env var name | `SERVICE_KEY_JSON` |
| Init file write command | `printf '%s' "$SERVICE_KEY_JSON" > /etc/twingate/service_key.json` |

## Gotchas
- Fargate blocks `CAP_NET_ADMIN` and `/dev/net/tun` — TUN mode **will not work**
- AWS Secrets Manager only injects secrets as env vars, not files — init container is mandatory
- Applications must **explicitly configure** the HTTP proxy; traffic is not intercepted automatically
- Running per-task sidecar clients at scale risks API throttling and high resource usage
- Raw TCP/UDP connections will fail in userspace mode — HTTP/HTTPS only

## Related Docs
- [Userspace Networking](https://www.twingate.com/docs/userspace-networking)
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- Twingate Troubleshooting Guide