# Exit Networks

## Summary
Exit Networks route all user traffic through Twingate Connectors acting as exit nodes, providing full traffic encryption beyond just Resource traffic. This is an opt-in feature available on Home, Business, and Enterprise plans that overrides Twingate's default split-tunnel routing behavior.

## Key Information
- Routes **all** non-Resource traffic through selected Connectors (full tunnel vs. default split tunnel)
- Traffic routes through geographically closest Connector in the Exit Network
- Automatic failover if a Connector goes down
- Sessions limited to **12 hours** maximum
- Group-based access control available (optional)
- Exit Network use **cannot be enforced** — users must manually enable it in the Client
- IPv6 not supported (AAAA queries blocked when active)
- DNS filtering continues to work normally

## Prerequisites
- Home, Business, or Enterprise plan
- Twingate Admin Console access
- Connectors deployed (minimum 2 recommended per Exit Network)
- Peer-to-peer compatible network environment for Connectors

## Step-by-Step Configuration

1. Navigate to **Admin Console → Internet Security → Exit Networks**
2. Create a new Exit Network with a descriptive name (e.g., region or use case)
3. Deploy Connectors within the Exit Network (follow Deploying Connectors guide)
4. (Optional) Restrict access by clicking **Enabled for Everyone** and selecting specific Groups
5. Users activate via Client: hover over **"Route All Traffic Through Twingate"** → select Exit Network

## Configuration Values
- No specific env vars or CLI flags — managed entirely through Admin Console UI
- Group access: configurable per Exit Network (default: all users)

## Gotchas

- **Security isolation critical**: Connectors in Exit Networks must be deployed **outside existing infrastructure** (separate VPC). If Exit Network Connectors can reach internal Resources, users bypass authentication checks entirely.
- **Peer-to-peer required for performance**: Non-P2P connections increase latency and consume relay bandwidth (Fair Use Policy applies).
- **Egress costs**: Avoid AWS/GCP/Azure for Connector hosting due to high bandwidth costs. Prefer DigitalOcean, Vultr, Linode, or Hetzner (bundled bandwidth included).
- **IPv6 broken**: Sites requiring IPv6-only connectivity will be unreachable.
- **No enforcement**: Admins cannot force Exit Network usage — purely user-controlled.
- **12-hour session cap** requires users to re-enable after expiration.

## Tips
- Deploy **at least 2 Connectors** per Exit Network for redundancy/load balancing
- Validate Connectors are peer-to-peer friendly before production use
- Use cost-effective providers: DigitalOcean (0.5–11TB), Vultr (0.5–12TB), Linode (1–20TB), Hetzner (1–20TB) bundled bandwidth

## Related Docs
- Deploying Connectors guide
- Peer-to-peer connections setup
- Troubleshooting peer-to-peer connections
- Connector selection / split tunnel routing
- Fair Use Policy