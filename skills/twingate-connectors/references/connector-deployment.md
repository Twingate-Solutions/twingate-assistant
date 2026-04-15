<!-- initial seed — to be refreshed by pipeline -->

## Page Title
Deploying Twingate Connectors

## Summary
A Twingate Connector is a lightweight proxy process deployed inside a private network that brokers encrypted connections between Twingate Clients and private Resources. Connectors require only outbound connectivity and are stateless, enabling high-availability deployments with no single point of failure.

## Key Information
- **Role:** Connectors sit in the data plane; they relay traffic from authenticated Clients to Resources without ever exposing those Resources to the internet
- **Deployment targets:** Linux (systemd service via apt or rpm), Docker (official image `twingate/connector`), Kubernetes (sidecar container or DaemonSet), and cloud marketplace AMIs/images
- **Network requirement:** Outbound-only — TCP 443 (HTTPS/QUIC relay fallback) and UDP 443 (QUIC preferred); no inbound firewall ports required
- **Connector token:** Each Connector is associated with a Remote Network in the admin console; a unique token is generated per Connector and passed as the `TWINGATE_ACCESS_TOKEN` environment variable at startup
- **High availability:** Deploy two or more Connectors per Remote Network; Clients automatically load-balance and failover between them with no additional configuration
- **Metrics endpoint:** Exposes Prometheus-compatible metrics at `http://localhost:9340/metrics` — includes active sessions, bytes transferred, relay vs. direct connection ratio, and DNS query counts

## Prerequisites
- A Twingate account with at least one Remote Network configured in the admin console
- A Connector token generated from the admin console (Admin > Remote Networks > [network] > Add Connector)
- Outbound internet access on TCP 443 and UDP 443 from the host or container
- Linux kernel 4.15+ for the systemd package; Docker 20.10+ for the container image

## Step-by-Step

### Linux (apt — Debian/Ubuntu)
1. Add the Twingate apt repository: `curl -s https://binaries.twingate.com/connector/setup.sh | sudo bash`
2. Set the access token: `sudo twingate-connector setup --access-token=<TOKEN>`
3. Start and enable the service: `sudo systemctl enable --now twingate-connector`
4. Verify status: `sudo systemctl status twingate-connector`

### Linux (rpm — RHEL/CentOS/Amazon Linux)
1. Add the Twingate rpm repository and install: `curl -s https://binaries.twingate.com/connector/setup.sh | sudo bash`
2. Configure and start identically to the apt path above.

### Docker
1. Pull the image: `docker pull twingate/connector:latest`
2. Run with the access token as an environment variable:
   ```
   docker run -d --restart=unless-stopped \
     -e TWINGATE_ACCESS_TOKEN=<TOKEN> \
     twingate/connector:latest
   ```
3. Confirm connectivity in the admin console — the Connector status should turn green within ~30 seconds.

### Kubernetes (sidecar pattern)
1. Store the token as a Kubernetes Secret: `kubectl create secret generic twingate-connector --from-literal=access-token=<TOKEN>`
2. Add the `twingate/connector` container to the relevant Deployment or DaemonSet spec, referencing the secret as `TWINGATE_ACCESS_TOKEN`.
3. Ensure the pod has egress to TCP/UDP 443; no host networking or privileged mode required.

### Upgrading
- **apt/rpm:** `sudo apt-get update && sudo apt-get install twingate-connector` (systemd service restarts automatically)
- **Docker:** `docker pull twingate/connector:latest` and recreate the container
- **Kubernetes:** Update the image tag in the manifest and apply; rolling update proceeds normally

## Configuration Values
- `TWINGATE_ACCESS_TOKEN` — required; the per-Connector token from the admin console
- `TWINGATE_LOG_LEVEL` — optional; valid values: `error`, `warning`, `info` (default), `debug`
- `TWINGATE_LOG_ANALYTICS` — optional; set to `v2` to enable enhanced analytics reporting
- `TWINGATE_LABEL_<KEY>` — optional; arbitrary key/value labels surfaced in the admin console (e.g., `TWINGATE_LABEL_ENV=production`)
- Metrics port: `9340` (not configurable via env var; bind to localhost only by default)

## Gotchas
- **Tokens are single-use identifiers, not secrets that rotate automatically** — if a token is compromised, revoke it in the admin console and generate a new one; the Connector will go offline immediately on revocation
- **UDP 443 blocked outbound?** The Connector falls back to TCP 443 automatically, but direct peer-to-peer (P2P) connections between Client and Connector require UDP; without it all traffic routes through the Twingate relay, adding latency
- **Two Connectors minimum for HA** — a single Connector is a hard SPOF; the second Connector in the same Remote Network enables automatic Client failover
- **Connector does not terminate TLS for Resources** — it forwards raw TCP/UDP; the Resource itself handles its own TLS; do not expect the Connector to provide certificate inspection
- **Systemd service name changed** in versions prior to 1.x — if upgrading from very old packages, verify the unit name with `systemctl list-units | grep twingate`
- **Docker on macOS/Windows (desktop)** is not recommended for production; use Linux hosts or Kubernetes

## Related Docs
- `/docs/connector` — Connector overview and architecture diagram
- `/docs/connector/deployment` — Full platform-specific deployment guides
- `/docs/connector/ha` — High-availability connector design
- `/docs/connector/metrics` — Prometheus metrics reference
- `/docs/connector/upgrade` — Connector upgrade procedures
- `/docs/remote-networks` — Managing Remote Networks in the admin console
