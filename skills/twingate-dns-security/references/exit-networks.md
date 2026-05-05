## Exit Networks (Full-Tunnel Routing)

**Exit Networks** route ALL user traffic (not just Resource traffic) through Twingate Connectors -- effectively giving Twingate full-tunnel VPN-like behavior on demand.

**Plan Requirement:**
- **Home, Business, Enterprise** plans only

### Default vs. Exit Networks

| Mode | Behavior |
|---|---|
| **Default (split tunnel)** | Only Resource traffic routes through Twingate; public traffic goes direct via the user's local network |
| **Exit Network (full tunnel)** | All non-Resource traffic ALSO routes through Twingate via a chosen Exit Network's Connectors |

Split tunnel is the default and is the right choice for most use cases (best performance / latency).

### Use Cases for Exit Networks

- **Untrusted networks**: coffee shop / hotel / airport Wi-Fi -- encrypt all egress
- **Geo-localization testing**: confirm content renders correctly when traffic exits from a specific region
- **Personal "back home" access**: users traveling who want to appear from their home country

### How It Works

- An Exit Network is a Remote Network that **also** acts as an exit node
- All non-Resource traffic on the user's device routes to the Exit Network's nearest Connector
- Resource traffic continues to its specific Connector as usual
- Failover: if the chosen Exit Network Connector is unreachable, traffic routes through other Connectors in that Exit Network
- Geographic Connector selection (closest first), like Resource routing

### Setup

**Step 1**: Admin Console -> **Internet Security -> Exit Networks** -> create new
**Step 2**: Deploy 2+ Connectors inside the Exit Network -- treat them like points of presence:
- **Important: deploy in a SEPARATE VPC from your Resources** (otherwise Exit Network Connectors can reach Resources without auth checks)
- Make Connectors P2P-friendly (per /docs/troubleshooting-p2p)
- 2+ Connectors for HA / load balancing

**Step 3**: Optionally restrict access to specific Groups via "Enabled for X Groups" (default: Everyone)

### User Experience

- Twingate Client -> hover **Route All Traffic Through Twingate** -> select an Exit Network
- Toggleable per-session
- **Maximum session length: 12 hours** -- after that, must re-toggle
- Cannot be **enforced** by admins -- always opt-in by the user

### Tips for Connector Placement

**Cost matters**: AWS / GCP / Azure egress is expensive. Lower-cost cloud providers with bundled bandwidth:
- DigitalOcean: 0.5-11 TB/month bundled per Droplet
- Vultr: 0.5-12 TB/month
- Linode: 1-20 TB/month
- Hetzner: 1 or 20 TB/month per region

These providers also typically have P2P-friendly NAT (verify per deployment).

### FAQ

- **DNS Filtering still works** with Exit Networks -- DNS is resolved by the Client regardless of full/split tunnel
- **IPv6**: NOT supported. AAAA queries are blocked when full-tunnel is on; IPv6-only sites won't load
- **Specific site unreachable**: contact support; Exit Networks are still relatively new

### Decision Notes

- **Always deploy Exit Network Connectors OUTSIDE existing Resource VPCs** -- mixing them creates a security loophole (any user with Exit Network access can reach Resources without auth)
- For globally distributed teams: create per-region Exit Networks (e.g., "US-West", "EU", "APAC") so users get low-latency egress
- Use cheaper cloud providers for Exit Network Connectors -- this is heavy bandwidth territory

### Gotchas

- Cannot be enforced -- if compliance requires full-tunnel always, this isn't the right tool
- 12-hour session cap -- users on long sessions see prompts
- Mixing Exit Network Connectors with Resource Connectors in the same VPC = severe security risk

### Related Docs

- /docs/internet-security -- IS overview
- /docs/troubleshooting-p2p -- P2P-friendly Connector setup
- /docs/connector-best-practices -- Connector deployment
- /docs/dns-filtering -- Continues to work with Exit Networks
- /docs/peer-to-peer-communication-in-twingate -- P2P fundamentals
