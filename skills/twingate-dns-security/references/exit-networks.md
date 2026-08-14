---
source: https://www.twingate.com/docs/exit-networks
type: docs
fetched: 2026-08-14
source_version: 9abe010090c1fe7ff03b58ce09cfb9bad85aa9c559c0550666db374981a89b2f
---

# Exit Networks

## Summary
Exit Networks route all user traffic through Twingate Connectors acting as exit nodes, replacing the default split-tunnel behavior. Traffic is fully encrypted end-to-end, including non-Resource traffic. Available on Home, Business, and Enterprise plans only.

## Key Information
- Routes **all** traffic through Twingate, not just Resource traffic (full tunnel vs. default split tunnel)
- Uses geographically closest Connector for routing, with automatic failover
- Sessions limited to **12 hours** maximum
- Cannot be enforced on users — must be manually toggled in the Client
- DNS filtering continues to work normally
- IPv6 not supported — AAAA queries are blocked

## Prerequisites
- Home, Business, or Enterprise plan
- Connectors deployed with peer-to-peer friendly NAT
- Admin Console access (Internet Security section)

## Step-by-Step Configuration

1. Navigate to **Admin Console → Internet Security → Exit Networks**
2. Create a new Exit Network with a descriptive name (e.g., region or function)
3. Deploy Connectors within the Exit Network (follow Deploying Connectors guide)
4. (Optional) Restrict access to specific Groups via **"Enabled for Everyone"** button
5. Users select **"Route All Traffic Through Twingate"** in the Client, then choose an Exit Network

## Configuration Values
- **Session limit**: 12 hours per session
- **Minimum Connectors**: 2 per Exit Network (recommended)
- **Group access**: All groups by default; configurable per Exit Network

## Gotchas
- **Security isolation required**: Deploy Exit Network Connectors outside existing infrastructure (separate VPC). If Connectors can reach your Resources, users bypass auth checks on those Resources.
- **No enforcement**: Users must opt-in manually; cannot be administratively forced.
- **IPv6 blocked**: Sites requiring IPv6 will be unreachable.
- **Egress costs**: AWS/GCP/Azure have high bandwidth costs — consider DigitalOcean, Vultr, Linode, or Hetzner (bundled bandwidth, P2P-friendly NAT).
- **Peer-to-peer matters**: Non-P2P connections consume more bandwidth and have higher latency; validate P2P compatibility per deployment.

## Tips
| Provider | Bundled Bandwidth |
|---|---|
| DigitalOcean | 0.5–11 TB |
| Vultr | 0.5–12 TB |
| Linode | 1–20 TB |
| Hetzner | 1–20 TB |

## Related Docs
- Deploying Connectors guide
- Peer-to-peer connections setup
- Troubleshooting peer-to-peer connections
- Connector selection for Resources
- Fair Use Policy (bandwidth)
- DNS filtering