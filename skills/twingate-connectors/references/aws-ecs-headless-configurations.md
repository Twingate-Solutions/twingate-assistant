# AWS ECS with Twingate (Headless & Userspace)

## Summary
Twingate provides secure private access for ECS workloads using service accounts. ECS Fargate supports only userspace (HTTP/HTTPS proxy) mode due to kernel capability restrictions; ECS on EC2 supports full TUN-based headless mode. Choose deployment model based on launch type and traffic requirements.

## Key Information
- **Fargate**: Userspace proxy mode only (`--tun off`), HTTP/HTTPS traffic exclusively
- **ECS on EC2**: Full headless TUN mode supported; recommended to run one client per EC2 host as a systemd service, not per task
- Fargate requires an init container to write the service key file before `twingated` starts
- Service key must exist at `/etc/twingate/service_key.json` before client starts
- Running sidecar clients per-task at scale risks API throttling and increased resource overhead

## Prerequisites
- AWS Secrets Manager secret containing service key JSON
- IAM execution role with Secrets Manager read permissions (`ecsTaskExecutionAndSecretsRead`)
- Twingate service account configured
- For EC2 full headless: Linux EC2 instances with kernel capability support

## Mode Selection

| Environment | Supported Mode | Recommendation |
|---|---|---|
| ECS Fargate | Userspace only | HTTP/HTTPS workloads |
| ECS on EC2 | Full headless | Default/recommended |
| ECS on EC2 | Userspace | HTTP-only or least-privilege |

## Step-by-Step: Fargate Userspace Deployment

1. Store service key JSON in AWS Secrets Manager
2. Create ECS task with three containers (init, twingate client, app)
3. Init container reads `SERVICE_KEY_JSON` env var, writes to `/etc/twingate/service_key.json` on shared volume
4. Twingate client container starts after init succeeds (`dependsOn: SUCCESS`)
5. App container starts after client starts (`dependsOn: START`), sends traffic via `http://127.0.0.1:9999`

## Configuration Values

| Parameter | Value |
|---|---|
| Client entrypoint | `twingated` |
| TUN disable flag | `--tun off` |
| HTTP proxy bind | `--http-proxy 0.0.0.0:9999` |
| Service key path | `/etc/twingate/service_key.json` |
| Shared volume name | `twingate-etc` (example) |
| Init container image | `alpine:latest` |
| Client image | `twingate/client:latest` |
| Proxy address (app) | `http://127.0.0.1:9999` |
| Network mode | `awsvpc` |
| Secret env var | `SERVICE_KEY_JSON` |

## Gotchas
- Fargate blocks `CAP_NET_ADMIN` and `/dev/net/tun` access — TUN mode will fail silently or error
- Secrets Manager injects secrets as env vars, not files — init container pattern is mandatory
- Applications **must** explicitly configure the HTTP proxy; traffic is not intercepted automatically in userspace mode
- Raw TCP/UDP connections will fail in Fargate userspace mode
- Sidecar-per-task pattern at scale causes API throttling on EC2
- Init container must complete with `SUCCESS` before client starts; ensure write permissions on volume

## Troubleshooting
- Verify `/etc/twingate/service_key.json` exists and is readable
- Check ECS task logs for auth errors at startup
- Confirm app uses `--proxy http://127.0.0.1:9999` explicitly
- Review Secrets Manager IAM permissions on execution role
- Check Recent Activity for the Resource in Twingate Admin Console

## Related Docs
- [Userspace Networking](https://www.twingate.com/docs/userspace-networking)
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- Twingate Troubleshooting Guide