# AWS ECS with Twingate (Headless & Userspace)

## Summary
Twingate supports secure private access for ECS workloads via service accounts. ECS Fargate is limited to userspace (HTTP/HTTPS proxy) mode due to kernel capability restrictions. ECS on EC2 supports full headless TUN mode and is the recommended path for production deployments.

## Key Information
- **Fargate**: Userspace proxy mode only (`--tun off`); AWS blocks `CAP_NET_ADMIN` and `/dev/net/tun`
- **ECS on EC2**: Supports full TUN mode; recommended to run one client per EC2 host as a systemd service
- Service key must exist as a file at `/etc/twingate/service_key.json` before `twingated` starts
- AWS Secrets Manager only injects secrets as environment variables, not files—requires init container workaround

## Prerequisites
- Twingate service account with generated service key JSON
- AWS Secrets Manager secret storing the service key JSON
- ECS task execution role (`executionRoleArn`) with Secrets Manager read permissions
- For EC2: Linux host with kernel capability support

## Step-by-Step (Fargate)
1. Store service key JSON in AWS Secrets Manager
2. Create init container (`alpine`) to write env var secret to `/etc/twingate/service_key.json` via shared volume
3. Configure Twingate container with `entryPoint: ["twingated"]` and `command: ["--http-proxy", "0.0.0.0:9999", "--tun", "off"]`
4. Set `dependsOn` condition `SUCCESS` from init container to Twingate container
5. Configure application containers to use proxy at `http://127.0.0.1:9999`
6. Mount shared volume `twingate-etc` to both init and Twingate containers at `/etc/twingate`

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Twingate image | `twingate/client:latest` |
| Entrypoint | `twingated` |
| TUN off flag | `--tun off` |
| Proxy flag | `--http-proxy 0.0.0.0:9999` |
| Proxy port | `9999` (TCP) |
| Service key path | `/etc/twingate/service_key.json` |
| Secret env var name | `SERVICE_KEY_JSON` |
| Task CPU/Memory | `1024` / `2048` |
| Network mode | `awsvpc` |

## Gotchas
- Fargate only permits `SYS_PTRACE` capability—TUN mode will fail silently or at startup
- Application containers must **explicitly** set proxy (`--proxy http://127.0.0.1:9999`); traffic is not transparently intercepted
- Raw TCP/UDP connections will not work in userspace mode—HTTP/HTTPS only
- Running one Twingate sidecar per ECS task at scale risks API throttling and increases resource overhead
- Init container must complete with `SUCCESS` before Twingate container starts

## Troubleshooting
- Verify `/etc/twingate/service_key.json` exists and has correct permissions (`0444`)
- Check ECS task logs for auth errors on startup
- Confirm execution role has Secrets Manager read permissions
- Review Resource Recent Activity in Twingate Admin Console
- Ensure no app attempts non-HTTP/HTTPS connections in Fargate deployments

## Related Docs
- [Userspace Networking](https://www.twingate.com/docs/userspace-networking)
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)