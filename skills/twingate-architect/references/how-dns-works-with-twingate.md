## Page Title
How DNS Works with Twingate

## Summary
Twingate uses a transparent proxy model where the Client intercepts DNS queries and assigns CGNAT-range IPs to private resources — the private network's DNS resolver is never exposed to the end user's device. The Connector resolves DNS inside the private network and proxies traffic back, keeping the resource's real IP hidden. This allows users to access internal FQDNs from anywhere without joining the private network.

## Key Information
- **DNS interception**: Twingate Client adds itself as the primary DNS resolver (`100.95.0.251–254`) on the device
- **CGNAT IP assignment**: Resources resolve to IPs in the `100.64.0.0/10` (CGNAT) range on the client — e.g. `nas.home.int` → `100.108.194.142` — not the actual private IP
- **Routing table modification**: Client routes all `100.96/12` traffic through its virtual network interface (`utun7` on macOS)
- **Connector does the real DNS lookup**: the Connector queries the private DNS server and proxies the connection — the client never learns the private IP
- **Works for public DNS resources too**: even resources with public DNS entries route through the Connector, overriding the public DNS path
- **Resource list is local**: Client holds a local copy of all FQDNs/IPs it has access to; only those are intercepted

## Prerequisites
- Twingate Client installed on end-user device
- Connector deployed with access to the private DNS resolver
- Resources defined as FQDNs in Twingate (most common case)

## Step-by-Step
Not a how-to page — see Quick Start for deployment steps. The DNS flow is automatic once Client + Connector are running.

## Configuration Values
- CGNAT DNS resolver IPs assigned by Client: `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254`
- CGNAT range used for resource IP assignment: `100.64.0.0/10` (specifically `100.96/12` for routing)

## Gotchas
- If a resource FQDN is not in the user's access list, the Client ignores the DNS query — it won't resolve via Twingate even if the Connector can reach it
- The resolved CGNAT IP changes between Client restarts; do not hardcode it
- Running `dig` with Twingate ON will show a CGNAT IP, not the real private IP — this is expected and correct
- Connector must be able to reach the private DNS server; if the DNS server is itself a Twingate Resource, resolution will fail

## Related Docs
- `/docs/architecture` — component overview
- `/docs/resources` — FQDN vs IP vs CIDR resource types
- `/docs/nat-traversal` — relay fallback
