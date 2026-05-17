# Exit Networks

## Summary
Exit Networks route all user traffic through Twingate Connectors acting as exit nodes, replacing the default split-tunnel behavior. All non-Resource traffic is encrypted and routed through the selected Exit Network, while Resource traffic continues routing normally. Available on Home, Business, and Enterprise plans.

## Key Information
- Overrides default split-tunnel routing to send **all** traffic through Twingate
- Traffic routes through geographically closest Connector in the Exit Network
- Automatic failover to other Connectors if one goes down
- Sessions limited to **12 hours** maximum
- Cannot be enforced on users — must be manually toggled in client
- Group-based access control available (defaults to all users)
- IPv6 not supported — `AAAA` queries are blocked when active

## Prerequisites
- Home, Business, or Enterprise plan
- Admin Console access
- Connectors deployed (minimum 2 recommended per Exit Network)
- Connectors must be deployed **outside existing infrastructure** (separate VPC)

## Step-by-Step Configuration

1. Navigate to **Admin Console → Internet Security → Exit Networks**
2. Create new Exit Network with descriptive name (e.g., region or use case)
3. Deploy Connectors within the new Exit Network (follow Deploying Connectors guide)
4. *(Optional)* Restrict access by clicking **Enabled for Everyone** and selecting specific Groups
5. Users activate via client: hover over **"Route All Traffic Through Twingate"** → select Exit Network

## Configuration Values
| Setting | Notes |
|---------|-------|
| Exit Network name | Unique; suggest region or function |
| Group access | Default: all users; optionally restrict to specific Groups |
| Minimum Connectors | 2 per Exit Network |
| Session limit | 12 hours |

## Gotchas
- **Security isolation required**: Connectors in Exit Networks must not have access to your protected Resources — deploy in a separate VPC/environment. Users routing all traffic could access Resources without auth checks otherwise.
- **IPv6 broken**: AAAA queries blocked; sites requiring IPv6 will be unreachable.
- **Peer-to-peer required**: Without P2P-compatible NAT, performance degrades and bandwidth costs increase (Fair Use Policy risk).
- **No enforcement**: Cannot force users to enable Exit Networks — client toggle only.
- **Egress costs**: Avoid AWS/GCP/Azure for Connector hosting; prefer DigitalOcean, Vultr, Linode, or Hetzner for bundled bandwidth.

## Related Docs
- [Deploying Connectors](https://www.twingate.com/docs/connectors)
- [Peer-to-peer connections setup](https://www.twingate.com/docs/peer-to-peer)
- [Troubleshooting peer-to-peer](https://www.twingate.com/docs/troubleshooting-peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
- [Connector selection / split tunnel routing](https://www.twingate.com/docs/split-tunnel)