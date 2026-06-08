# AWS ECS with Twingate (Headless & Userspace)

## Summary
Twingate provides secure private access for ECS workloads using service accounts. ECS Fargate supports only userspace (HTTP/HTTPS proxy) mode due to kernel capability restrictions, while ECS on EC2 supports full headless TUN mode. Deployment model depends on launch type and traffic requirements.

## Key Information
- **Fargate**: Userspace only (`--tun off`) — AWS blocks `/dev/net/tun` and `CAP_NET_ADMIN`
- **ECS on EC2**: Full TUN mode supported; one client per EC2 host (systemd service) recommended at scale
- Service key must exist as file at `/etc/twingate/service_key.json` before `twingated` starts
- Init container pattern required on Fargate to bridge Secrets Manager env vars → file

## Prerequisites
- Twingate service account with generated service key stored in AWS Secrets Manager
- ECS task execution role with Secrets Manager read permissions (`ecsTaskExecutionAndSecretsRead`)
- For EC2 mode: customer-managed Linux hosts with kernel capabilities available

## Step-by-Step (Fargate)
1. Store service key JSON in Secrets Manager at `arn:aws:secretsmanager:<region>:<account-id>:secret:twingate/service-key`
2. Create init container (`alpine`) that writes `$SERVICE_KEY_JSON` env var to `/etc/twingate/service_key.json`
3. Mount shared volume `twingate-etc` to both init container and Twingate client container
4. Start Twingate client with `dependsOn: init-write-key (SUCCESS)`
5. Configure application containers to proxy through `http://127.0.0.1:9999`

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Client entrypoint | `twingated` |
| TUN disabled flag | `--tun off` |
| HTTP proxy flag | `--http-proxy 0.0.0.0:9999` |
| Proxy address (app containers) | `http://127.0.0.1:9999` |
| Service key path | `/etc/twingate/service_key.json` |
| Shared volume name | `twingate-etc` |
| Network mode | `awsvpc` |
| Task CPU/memory | `1024` / `2048` |

## Gotchas
- Fargate only allows `SYS_PTRACE` capability — no TUN device possible
- Applications must **explicitly** set proxy; traffic is not transparently intercepted in userspace mode
- Raw TCP/UDP connections will fail on Fargate — HTTP/HTTPS only
- Running sidecar clients per-task on EC2 at scale risks API throttling and increases overhead
- Secret is injected as env var by Secrets Manager, not as a file — init container is mandatory workaround
- `chmod 0444` on service key file is set in init container command

## Deployment Model Decision Table

| Environment | Mode | Recommendation |
|-------------|------|----------------|
| ECS Fargate | Userspace only | HTTP/HTTPS workloads |
| ECS on EC2 | Full headless (TUN) | Default/recommended |
| ECS on EC2 | Userspace | HTTP-only or least-privilege |

## Related Docs
- [Userspace Networking](https://www.twingate.com/docs/userspace-networking)
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)