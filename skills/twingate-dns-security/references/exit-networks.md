# Exit Networks

## Summary
Exit Networks route all user traffic through Twingate Connectors acting as exit nodes, providing full traffic encryption beyond just protected Resources. This overrides Twingate's default split-tunnel behavior. Available on Home, Business, and Enterprise plans only.

## Key Information
- Routes **all** traffic through Twingate, not just Resource traffic (full tunnel vs. split tunnel)
- Traffic routed through geographically closest Connector in the Exit Network
- Automatic failover to another Connector if one goes down
- Sessions limited to **12 hours** maximum
- Exit Network use **cannot be enforced** — users must manually toggle in the Client
- IPv6 is not supported — `AAAA` queries are blocked when routing through Exit Networks
- DNS filtering continues to function normally

## Prerequisites
- Home, Business, or Enterprise plan
- Connectors deployed within the Exit Network
- Recommend minimum **2 Connectors** per Exit Network

## Step-by-Step Configuration

1. Navigate to **Admin Console → Internet Security → Exit Networks**
2. Create new Exit Network with a descriptive name (e.g., region or use case)
3. Deploy Connectors inside the new Exit Network (follow [Deploying Connectors guide](https://www.twingate.com/docs/connectors))
4. (Optional) Restrict access by Group: click **Enabled for Everyone** → select specific Groups
5. Users select **Route All Traffic Through Twingate** in the Client and choose an Exit Network

## Configuration Values
- No specific env vars or API params documented
- Group-level access control available (all Groups enabled by default)

## Gotchas
- **Security risk**: If Exit Network Connectors can reach internal Resources, users routing all traffic through Twingate bypass normal authentication checks — deploy Exit Network Connectors in **isolated infrastructure** (separate VPC or standalone)
- Peer-to-peer connectivity required for acceptable performance; validate NAT compatibility before production deployment
- Major cloud providers (AWS, GCP, Azure) have high egress costs — consider DigitalOcean, Vultr, Linode, or Hetzner for bundled bandwidth
- Cannot force users to enable Exit Networks — opt-in only at the user level
- IPv6 breakage: sites requiring IPv6 will be unreachable

## Recommended Deployment
- Deploy at least 2 Connectors per Exit Network for redundancy
- Ensure Connectors are peer-to-peer friendly (check NAT configuration)
- Isolate Exit Network Connectors from internal infrastructure entirely

## Related Docs
- [Deploying Connectors](https://www.twingate.com/docs/connectors)
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Troubleshooting peer-to-peer connections](https://www.twingate.com/docs/troubleshooting-p2p)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
- [Split tunnel routing](https://www.twingate.com/docs/split-tunnel)