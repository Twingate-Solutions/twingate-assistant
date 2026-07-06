# Exit Networks

## Summary
Exit Networks route all non-Resource traffic through Twingate Connectors acting as exit nodes, providing full traffic encryption (not just split-tunnel). Available on Home, Business, and Enterprise plans. Sessions are limited to 12 hours.

## Key Information
- Routes all traffic through Twingate (vs. default split-tunnel which only routes Resource traffic)
- Traffic goes to geographically closest Connector in the Exit Network
- Automatic failover if a Connector goes down
- IPv6 not supported — AAAA queries are blocked
- DNS filtering continues to work normally
- Exit Network use **cannot be enforced** — users must manually toggle in Client
- Session limit: **12 hours**

## Prerequisites
- Home, Business, or Enterprise plan
- At least one Exit Network created in Admin Console
- Connectors deployed within the Exit Network
- Connectors must be deployed **outside existing infrastructure** (separate VPC)

## Step-by-Step

1. Navigate to **Admin Console → Internet Security → Exit Networks**
2. Create new Exit Network with descriptive name (e.g., region or function)
3. Deploy Connectors inside the Exit Network (minimum 2 recommended)
4. (Optional) Restrict access by Group via **Enabled for Everyone** button
5. Users select **Route All Traffic Through Twingate** in Client and choose Exit Network

## Configuration Values
- No env vars or CLI flags documented
- Group access: per-Exit-Network group selection in Admin Console

## Gotchas
- **Security isolation required**: Connectors in Exit Networks must not have access to your protected Resources — any user routing through Twingate could access Resources without auth checks if Connectors are on the same network
- **IPv6 broken**: AAAA queries blocked; sites requiring IPv6 will fail
- **Egress costs**: AWS/GCP/Azure charge high bandwidth fees — consider DigitalOcean, Vultr, Linode, or Hetzner (bundled bandwidth, peer-to-peer friendly NAT)
- **Peer-to-peer required for performance**: Connectors not configured for P2P will result in higher latency and higher relay bandwidth consumption (Fair Use Policy implications)
- Cannot enforce Exit Network usage on users

## Tips
- Deploy ≥2 Connectors per Exit Network for redundancy
- Validate P2P compatibility for your specific cloud deployment
- Peer-to-peer setup guide: see Twingate P2P troubleshooting docs

## Related Docs
- Deploying Connectors guide
- Peer-to-peer connections setup
- Troubleshooting peer-to-peer connections
- Fair Use Policy
- DNS filtering documentation