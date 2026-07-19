# AWS ECS with Twingate (Headless & Userspace)

## Summary
Twingate supports secure private access for ECS workloads via service accounts, with two modes depending on launch type. ECS Fargate is limited to userspace (HTTP/HTTPS proxy) mode due to kernel capability restrictions. ECS on EC2 supports full headless TUN mode and is recommended for most deployments.

## Key Information
- **ECS Fargate**: Userspace proxy mode only (`--tun off`), no TUN device or `CAP_NET_ADMIN` available
- **ECS on EC2**: Full TUN/headless mode supported; recommended to run one client per EC2 host via systemd
- Twingate client expects service key at `/etc/twingate/service_key.json` (file, not env var)
- AWS Secrets Manager only injects secrets as env vars, requiring an init container workaround
- Avoid sidecar-per-task pattern at scale on EC2 (API throttling risk, overhead)

## Prerequisites
- Twingate service account with service key JSON
- AWS Secrets Manager secret storing service key JSON
- ECS task execution IAM role with Secrets Manager read permissions (`ecsTaskExecutionAndSecretsRead`)
- For EC2 mode: managed EC2 instances with systemd support

## Step-by-Step (Fargate)
1. Store service key JSON in AWS Secrets Manager
2. Create ECS task with three containers:
   - **init-write-key** (alpine): reads `SERVICE_KEY_JSON` env var, writes to `/etc/twingate/service_key.json` on shared volume
   - **tg-userspace-client**: depends on `init-write-key SUCCESS`, mounts same volume, runs `twingated --http-proxy 0.0.0.0:9999 --tun off`
   - **application container**: depends on `tg-userspace-client START`, routes traffic via `http://127.0.0.1:9999`
3. Share `/etc/twingate` between init and client containers via named volume `twingate-etc`

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Proxy listen address | `0.0.0.0:9999` |
| Proxy port (host/container) | `9999/tcp` |
| TUN flag (Fargate) | `--tun off` |
| Entrypoint | `twingated` |
| Service key path | `/etc/twingate/service_key.json` |
| Client image | `twingate/client:latest` |
| Network mode | `awsvpc` |
| Task CPU/Memory | `1024` / `2048` |
| Secret env var name | `SERVICE_KEY_JSON` |

## Gotchas
- Fargate blocks all kernel capabilities beyond `SYS_PTRACE` — TUN mode will not work
- Applications must **explicitly** configure the HTTP proxy; traffic is not transparently intercepted
- Raw TCP/UDP connections will fail in userspace mode — HTTP/HTTPS only
- Twingate client image has no writable entrypoint, requiring the init container pattern
- Running one sidecar client per ECS task at scale risks API throttling and high resource usage
- File permissions on service key: set to `0444`

## Deployment Model Comparison

| Environment | Mode | Recommendation |
|-------------|------|----------------|
| ECS Fargate | Userspace only | HTTP/HTTPS workloads |
| ECS on EC2 | Full headless | Default/recommended |
| ECS on EC2 | Userspace | HTTP-only or least-privilege |

## Related Docs
- [Userspace Networking](https://www.twingate.com/docs/userspace-networking)
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)