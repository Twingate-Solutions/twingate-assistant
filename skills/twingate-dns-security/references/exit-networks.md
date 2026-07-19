# Exit Networks

## Summary
Exit Networks route all user traffic through Twingate Connectors acting as exit nodes, providing full traffic encryption beyond just protected Resources. Unlike Twingate's default split tunnel mode, Exit Networks capture all outgoing traffic. Available on Home, Business, and Enterprise plans only.

## Key Information
- Routes **all** traffic through Twingate, not just Resource traffic (full tunnel vs. split tunnel)
- Traffic routes through geographically closest Connector in the Exit Network
- Automatic failover to another Connector if one goes down
- Sessions limited to **12 hours** maximum
- Group-level access control supported (restrict which groups can use Exit Networks)
- Exit Network use **cannot be enforced** — users must manually enable it in the Client
- IPv6 is not supported — AAAA queries are blocked when routing through Exit Networks

## Prerequisites
- Home, Business, or Enterprise plan
- Admin Console access
- Connectors deployed (minimum 2 recommended per Exit Network)

## Step-by-Step Configuration

1. Navigate to **Admin Console → Internet Security → Exit Networks**
2. Create a new Exit Network with a descriptive name (e.g., region or function)
3. Deploy Connectors within the new Exit Network (follow [Deploying Connectors guide](https://www.twingate.com/docs/connectors))
4. (Optional) Restrict access by clicking **Enabled for Everyone** and selecting specific Groups
5. Users enable via Twingate Client → hover **"Route All Traffic Through Twingate"** → select Exit Network

## Configuration Values
- No specific env vars or API params documented; managed via Admin Console UI

## Gotchas

- **Security isolation required**: Deploy Exit Network Connectors **outside** existing infrastructure (separate VPC). If Exit Network Connectors can reach your Resources, users routing all traffic through Twingate bypass Resource authentication checks.
- **Egress costs**: AWS/GCP/Azure have high egress fees. Consider DigitalOcean, Vultr, Linode, or Hetzner (bundled bandwidth, lower overages).
- **Peer-to-peer compatibility**: Verify NAT is P2P-friendly to stay within Fair Use Policy and reduce latency. Test even with recommended providers.
- **IPv6 broken**: Sites requiring IPv6 will be unreachable when Exit Network is active.
- **12-hour session cap**: Users must re-enable after session expires.
- DNS filtering continues to function normally with Exit Networks active.

## Tips
- Deploy **at least 2 Connectors** per Exit Network for redundancy and load balancing
- Ensure Connectors are peer-to-peer friendly (check [P2P troubleshooting guide](https://www.twingate.com/docs/troubleshoot-peer-to-peer))
- Use providers with bundled bandwidth (DigitalOcean, Vultr, Linode, Hetzner) to minimize egress costs

## Related Docs
- [Deploying Connectors](https://www.twingate.com/docs/connectors)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Troubleshoot P2P Connections](https://www.twingate.com/docs/troubleshoot-peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
- [Split Tunnel Routing](https://www.twingate.com/docs/split-tunnel)