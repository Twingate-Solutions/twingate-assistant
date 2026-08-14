---
source: https://www.twingate.com/docs/aws-ecs-headless-configurations
type: docs
fetched: 2026-08-14
source_version: d0b7590dd1e7dc0d01dee37599e8f2db6850b6148ea325e9e37de1831524591f
---

# AWS ECS with Twingate (Headless & Userspace)

## Summary
Twingate provides secure private access for ECS workloads using service accounts. ECS Fargate supports only userspace (HTTP/HTTPS proxy) mode due to kernel capability restrictions, while ECS on EC2 supports full headless TUN mode. Deployment model choice depends on launch type and traffic requirements.

## Key Information
- **Fargate**: Userspace proxy mode only (`--tun off`); AWS blocks `CAP_NET_ADMIN` and `/dev/net/tun`
- **ECS on EC2**: Full TUN mode supported; recommended to run one client per EC2 host via systemd, not per-task sidecar
- Service key must exist as file at `/etc/twingate/service_key.json` before `twingated` starts
- Init container pattern required on Fargate to write secret from env var to file

## Prerequisites
- AWS Secrets Manager secret containing service key JSON at a known ARN
- IAM execution role with `secretsmanager:GetSecretValue` permission (`ecsTaskExecutionAndSecretsRead`)
- Twingate service account configured in Admin Console
- ECS task network mode: `awsvpc`

## Step-by-Step (Fargate)
1. Store service account key in AWS Secrets Manager
2. Create init container (`alpine`) that writes `$SERVICE_KEY_JSON` env var to `/etc/twingate/service_key.json` via shared volume
3. Start Twingate client container with `dependsOn: init-write-key (SUCCESS)`
4. Application containers use `dependsOn: tg-userspace-client (START)` and route traffic through `http://127.0.0.1:9999`

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Client entrypoint | `twingated` |
| TUN disable flag | `--tun off` |
| Proxy flag | `--http-proxy 0.0.0.0:9999` |
| Proxy address (app containers) | `http://127.0.0.1:9999` |
| Service key path | `/etc/twingate/service_key.json` |
| Client image | `twingate/client:latest` |
| Fargate requires | `FARGATE` compatibility, `awsvpc` network mode |
| Task CPU/memory | `1024` / `2048` (minimum viable) |
| Client port mapping | `9999:9999/tcp` |
| Shared volume name | `twingate-etc` (mounted at `/etc/twingate`) |

## Gotchas
- **Fargate only allows `SYS_PTRACE`** — no `CAP_NET_ADMIN`, so TUN mode is permanently unsupported
- Applications must **explicitly configure** the HTTP proxy; traffic is not intercepted automatically
- Fargate supports HTTP/HTTPS only — no raw TCP/UDP through Twingate
- Running per-task sidecar clients at scale on EC2 risks **API throttling** and increases overhead; use per-host model instead
- AWS Secrets Manager injects secrets as env vars, not files — init container is mandatory to convert to file

## Troubleshooting
- Verify `/etc/twingate/service_key.json` exists and client authenticated before app container starts
- Check ECS task logs for startup/auth errors
- Review Recent Activity in Twingate Admin Console for the Resource
- Confirm execution role has Secrets Manager read permissions

## Related Docs
- [Userspace Networking](https://www.twingate.com/docs/userspace-networking)
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- Twingate Troubleshooting Guide