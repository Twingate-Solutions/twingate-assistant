## AWS ECS Headless Configurations

How to run the Twingate Client in AWS ECS to give containerized workloads (frontend apps, AI agents, batch jobs) private access to backend Resources via a Service Account.

**Mode Selection by Launch Type:**

| ECS Launch Type | Supported Mode | Reason |
|---|---|---|
| **Fargate** | Userspace (HTTP proxy) only | Fargate disallows `CAP_NET_ADMIN` and `/dev/net/tun`; full TUN mode not possible |
| **EC2 / Managed Instances** | Full headless (TUN) **or** userspace | Customer-managed hosts allow kernel capabilities |

**Recommendation:**
- **Fargate**: userspace HTTP/HTTPS proxy (only option; raw TCP/UDP not supported)
- **EC2 (recommended at scale)**: install the Client directly on each EC2 host as a `systemd` service (one Client per host) authenticated by a Service Account
- **EC2 (sidecar)**: possible but not recommended -- adds connection overhead, risks API throttling, increases resource usage

### Fargate Pattern (Userspace)

**Why an init container is required:**
- AWS Secrets Manager injects secrets only as **environment variables**, not as files
- The Twingate Client expects the service key at `/etc/twingate/service_key.json`
- The Client image has no writable entrypoint, so the file must exist before `twingated` starts

**Init container behavior:**
- Pull the service key from Secrets Manager (env var)
- Write it to `/etc/twingate/service_key.json` on a shared volume
- Set permissions `0444` (read-only)
- Twingate Client container `dependsOn: { condition: SUCCESS, containerName: init-write-key }`

**Twingate Client container (Fargate):**
- Image: `twingate/client:latest`
- `entryPoint`: `["twingated"]`
- `command`: `["--http-proxy", "0.0.0.0:9999", "--tun", "off"]`
- Mount shared volume at `/etc/twingate`
- Expose port 9999/TCP (HTTP proxy)

**Application containers** must explicitly use the proxy: `curl --proxy http://127.0.0.1:9999 http://my-private-backend`

### EC2 Pattern (Full Headless)

- Install the Twingate Client on the EC2 host (apt/yum/rpm package)
- Authenticate as a `systemd` service using a Service Account key
- One Client per host services all tasks on that host
- Full TCP/UDP/ICMP supported

**Gotchas:**
- Fargate userspace mode supports HTTP/HTTPS only -- no raw TCP/UDP
- Service key permissions: must be present at `/etc/twingate/service_key.json` before `twingated` starts (init container ordering matters)
- Verify Secrets Manager IAM permissions on the ECS task execution role
- Sidecar-per-task at scale increases connection count and risks API throttling -- prefer host-level Client on EC2

**Related Docs:**
- /docs/services-headless-clients -- Headless Client modes overview
- /docs/linux-userspace-networking -- Userspace proxy mechanics
- /docs/service-accounts-guide -- Service Account key management
- /docs/how-to-troubleshoot -- Diagnostic steps
