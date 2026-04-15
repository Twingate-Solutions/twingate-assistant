<!-- initial seed — to be refreshed by pipeline -->

## Page Title
Twingate Troubleshooting Decision Tree

## Summary
Twingate connectivity failures fall into four ordered layers — Client, DNS, Connector, and Network/Firewall — and should be diagnosed in that sequence to avoid chasing symptoms at the wrong layer. Resolving the issue at the earliest layer eliminates the need to investigate deeper ones.

## Key Information
- **Four failure layers (check in order):** 1. Client, 2. DNS, 3. Connector, 4. Network/Firewall — most issues are resolved at layer 1 or 2
- **Twingate DNS resolver address:** `100.95.0.1` (CGNAT range); this is the address Twingate installs as a split-DNS resolver on the client device
- **Connector outbound requirements:** TCP 443 and UDP 443 to `*.twingate.com`; both protocols must be permitted — Twingate uses QUIC (UDP 443) for performance and falls back to TCP 443
- **Log locations:** Linux systemd connector: `journalctl -u twingate-connector -f`; Docker connector: `docker logs <container_name> -f`; macOS client: Console app, filter by `Twingate`; Windows client: Event Viewer → Application logs
- **Admin Console visibility:** The Connectors page shows each connector's last-seen timestamp and online/offline status — check this before touching the connector host to confirm whether the issue is client-side or connector-side
- **Twingate CLI diagnostic command:** `twingate status` (or `twingatectl status` on some platforms) prints authentication state, active resources, and DNS resolver status in one call

## Prerequisites
- Admin or Owner access to the Twingate Admin Console (for verifying resource/group assignments and connector status)
- SSH or console access to the connector host (for connector-layer and network-layer checks)
- `nslookup` or `dig` installed on the client device for DNS-layer checks
- Knowledge of whether the connector is deployed as systemd, Docker, or Kubernetes (affects log and restart commands)

## Step-by-Step

### Layer 1 — Client Checks
1. Run `twingate status` on the affected client; confirm output shows `Authenticated: yes` and the target resource appears in the active resource list.
2. Open the Twingate Admin Console → Resources, locate the resource, and confirm the affected user's group is listed under Access — a missing group assignment is the single most common cause of "resource unreachable."
3. Check the client's split-tunnel configuration: if the resource CIDR or hostname is excluded from the Twingate tunnel (e.g., via an MDM-pushed exclusion), traffic bypasses Twingate entirely.
4. Confirm no VPN or other DNS-override tool is active on the device that could intercept Twingate's resolver traffic before it reaches `100.95.0.1`.
5. On macOS/Windows, check that the Twingate client service is running and not in a degraded state; restart the client app if the status command is unresponsive.

### Layer 2 — DNS Checks
1. Query the Twingate resolver directly: `nslookup <resource-hostname> 100.95.0.1` (or `dig @100.95.0.1 <resource-hostname>`). A successful response confirms Twingate DNS is active and the resource is resolvable.
2. If `nslookup` times out against `100.95.0.1`, the Twingate DNS resolver is not active on the device — restart the Twingate client or check system DNS settings.
3. If the resource uses a custom DNS suffix (e.g., `api.internal`), confirm the suffix is listed in the resource's DNS settings in the Admin Console and matches exactly (case-insensitive but no trailing dot differences).
4. Check for DNS caching: flush the OS DNS cache (`ipconfig /flushdns` on Windows, `sudo dscacheutil -flushcache` on macOS) if a recently added resource is not resolving.

### Layer 3 — Connector Checks
1. Verify the connector shows "Online" in the Admin Console → Connectors page. An "Offline" status means the connector cannot reach Twingate's control plane.
2. On the connector host, check service status:
   - Systemd: `systemctl status twingate-connector`
   - Docker: `docker ps` (confirm container is running); `docker logs <container> --tail 50`
3. Inspect logs for authentication errors — a common cause is an expired or revoked connector token. Regenerate tokens in the Admin Console if needed and restart the connector with the new values.
4. Confirm `TWINGATE_NETWORK` is set to the correct tenant subdomain (e.g., `acme`, not `acme.twingate.com`) and `TWINGATE_ACCESS_TOKEN` / `TWINGATE_REFRESH_TOKEN` are both present and non-empty.
5. Confirm the connector can resolve `<tenant>.twingate.com` from the connector host: `nslookup acme.twingate.com`. DNS failure on the connector host will prevent it from ever reaching the control plane.
6. Restart the connector service after any token or environment variable change:
   - Systemd: `sudo systemctl restart twingate-connector`
   - Docker: `docker restart <container>`

### Layer 4 — Network/Firewall Checks
1. Confirm outbound TCP 443 to `*.twingate.com` is permitted from the connector host — this is required for control-plane communication and the HTTPS relay fallback.
2. Confirm outbound UDP 443 to `relay.twingate.com` is permitted — Twingate prefers QUIC for data-plane relaying; blocking UDP 443 forces fallback to TCP relay and degrades performance but does not break connectivity if TCP is open.
3. Check whether a deep packet inspection (DPI) or TLS-intercepting firewall is present on the connector's egress path. DPI that terminates and re-signs TLS will break Twingate's certificate pinning and must be bypassed for `*.twingate.com`.
4. For peer-to-peer (direct) connections between client and connector, UDP traffic on ephemeral ports must be permitted between the two endpoints — if P2P fails, Twingate falls back to the relay automatically, but P2P failure will show up as higher latency rather than complete unavailability.
5. Review cloud security group / network ACL rules if the connector is hosted in AWS, Azure, or GCP — ensure the instance's egress rules are not more restrictive than the host OS firewall.

## Configuration Values
- Twingate DNS resolver IP: `100.95.0.1`
- Required outbound ports from connector: TCP 443, UDP 443
- Connector environment variables: `TWINGATE_NETWORK` (tenant subdomain), `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`
- Systemd service name: `twingate-connector`
- Docker image: `twingate/connector:latest` (or pinned version tag)
- Relay hostname: `relay.twingate.com`
- Control plane hostname: `<tenant>.twingate.com`

## Gotchas
- **Group assignment is the most commonly missed step:** A resource can be online and reachable but the user simply isn't in any group that has access — the client error "resource unreachable" is identical whether the issue is network or access policy
- **UDP 443 is frequently blocked by default firewall rules:** Many corporate firewalls only permit TCP 443 outbound; Twingate will still work via TCP relay, but if you see slow connections and expect P2P, UDP being blocked is the likely cause
- **TLS inspection breaks connector connectivity:** Any middlebox that performs TLS inspection must have a bypass rule for `*.twingate.com`; without it, the connector will fail to authenticate against the control plane with a certificate error
- **Connector tokens are single-use per connector instance:** Tokens cannot be shared across multiple connector containers/hosts — each connector registration generates its own unique token pair
- **`TWINGATE_NETWORK` must be the subdomain only:** Setting it to `https://acme.twingate.com` instead of `acme` is a common misconfiguration that produces a confusing authentication-failed error
- **Client DNS resolver address may differ on managed devices:** Some MDM profiles or VPN clients override the system DNS before Twingate can insert `100.95.0.1`; always verify with `nslookup` rather than assuming the resolver is active
- **Connector offline but resource still resolves:** DNS is cached on the client; even after a connector goes offline, the hostname may still resolve for several minutes — test actual connectivity (e.g., `curl` or `telnet` to the resource port) to confirm the issue is not stale DNS

## Related Docs
- `/docs/troubleshooting/connectivity` — Twingate connectivity troubleshooting guide
- `/docs/connectors/connector-deployment` — Connector deployment and token management
- `/docs/connectors/connector-logs` — Connector log format and log level configuration
- `/docs/client/twingate-client` — Client installation and status commands
- `/docs/access-control/resource-access` — Resource access policies and group assignments
- `/docs/network/dns` — Twingate DNS resolver behavior and split-DNS configuration
