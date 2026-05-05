## Firewall Failures (Troubleshooting)

Diagnostic playbook for performance issues caused by firewalls / NAT misconfig forcing connections to the Twingate Relay instead of P2P.

### The Core Distinction

| Connection Type | Speed | When It Happens |
|---|---|---|
| **Peer-to-Peer (P2P)** | Direct, low-latency | When NAT traversal succeeds |
| **Relay** | Indirect, possibly higher latency | Fallback when P2P fails |

Diagnosing performance issues = diagnosing why P2P is failing.

### Common Symptoms

- Users report Twingate as "slow" or "laggy"
- Admin Console: most/all Connector connections show as "Relayed"
- Total connection failure to the Twingate network

### Required Outbound Rules

Both Clients and Connectors need outbound:

| Destination / Protocol | Purpose |
|---|---|
| `*.twingate.com` on TCP 443 | Controller + Relay control |
| TCP 30000-31000 | Relay fallback connections |
| **UDP to all destinations** | **Critical** -- NAT traversal / P2P |

**Blocked outbound UDP is the #1 cause of forced-Relay performance issues.**

### Troubleshoot NAT Traversal Failures

If connections are relayed, P2P failed. Check in this order:

#### 1. Blocked UDP/QUIC

Test from the Connector host using `nmap` against a public test port. Or visit `https://quic.nginx.org/` from the Connector host (works = QUIC OK).

#### 2. Incompatible NAT Type

NAT traversal requires **endpoint-independent NAT**. Most consumer routers do this; some enterprise firewalls / cloud NAT use **symmetric NAT** which breaks NAT traversal.

**Double NAT** (device behind two routers) also breaks P2P.

#### 3. AWS NAT Gateway Specifically

Standard AWS NAT Gateway is **incompatible with NAT traversal** in some scenarios.

**Workarounds:**
- Self-hosted NAT instance on EC2
- Third-party NAT product from AWS Marketplace (Cohesive Cloud NAT, fck-nat, alterNAT)

#### 4. Verify in Admin Console

Connector detail page -> **STUN Discovery: Available** is the prerequisite for P2P.

If unavailable -> outbound UDP blocked. Specifically check **UDP port 3478** (STUN protocol).

### Decision Notes

- For cloud Connector deployments: AWS NAT Gateway is the most common cause -- design around it from day one (use self-hosted NAT)
- For on-prem: check enterprise firewalls for "Persistent NAT" / "Consistent NAT" / "Endpoint-independent NAT" settings (varies by vendor)
- Forcing all-Relay isn't a security issue (still secure), just a performance issue -- but for global teams, the latency adds up

### Related Docs

- /docs/troubleshooting-p2p -- Deeper P2P diagnostic playbook
- /docs/how-nat-traversal-works -- NAT fundamentals
- /docs/peer-to-peer-communication-in-twingate -- P2P overview
- /docs/firewalls-and-twingate -- Firewall coexistence
- /docs/connector-failures -- Sibling: Connector itself failing
- /docs/split-tunnel-failures -- Next failure mode in the decision tree
