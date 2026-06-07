# Exit Networks

## Summary
Exit Networks route all user traffic through Twingate Connectors acting as exit nodes, providing full traffic encryption beyond just protected Resources. This is an opt-in feature (not default split-tunnel behavior) available on Home, Business, and Enterprise plans. Users manually enable it from the Twingate Client.

## Key Information
- Routes **all** traffic through Twingate, not just Resource traffic (full tunnel vs. default split tunnel)
- Traffic goes through geographically closest Connector in the Exit Network
- Automatic failover between Connectors if one goes down
- Sessions limited to **12 hours** maximum
- Cannot be enforced on users — must be manually toggled in Client
- IPv6 not supported (AAAA queries blocked)
- DNS filtering continues to work normally

## Prerequisites
- Home, Business, or Enterprise plan
- Twingate Admin Console access
- Connectors deployed in Exit Network (minimum 2 recommended)
- Connectors must be peer-to-peer friendly

## Step-by-Step Configuration

1. Navigate to **Admin Console → Internet Security → Exit Networks**
2. Create new Exit Network with a descriptive name (e.g., "United States" or "Coffee Shop Mode")
3. Deploy Connectors within the new Exit Network (follow Deploying Connectors guide)
4. (Optional) Restrict access by Group: click **Enabled for Everyone** → select specific Groups
5. Users enable via Client: hover over **"Route All Traffic Through Twingate"** → select Exit Network

## Configuration Values
- No CLI flags or environment variables — configured via Admin Console UI
- Group-level access control available (default: all users)

## Gotchas
- **Security isolation required**: Connectors in Exit Networks must be deployed **outside existing infrastructure** (separate VPC). If they can reach internal Resources, users bypass Resource authentication checks.
- **Egress costs**: AWS/GCP/Azure have high egress bandwidth costs. Consider DigitalOcean, Vultr, Linode, or Hetzner for bundled bandwidth.
- **Peer-to-peer**: Connectors must be P2P-friendly for acceptable performance and to stay within Fair Use Policy bandwidth limits.
- Exit Network use **cannot be enforced** — users must opt in manually.
- Deploy at least **2 Connectors** per Exit Network for redundancy.

## Recommended Providers (Low Egress Cost)
| Provider | Bundled Bandwidth |
|---|---|
| DigitalOcean | 0.5–11 TB/instance |
| Vultr | 0.5–12 TB/instance |
| Linode | 1–20 TB/instance |
| Hetzner | 1–20 TB/region |

## Related Docs
- Deploying Connectors guide
- Split tunnel routing
- Peer-to-peer connections setup
- Troubleshooting peer-to-peer connections
- Fair Use Policy