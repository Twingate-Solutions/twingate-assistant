## How to Troubleshoot Twingate Issues

Top-level **methodology + decision tree** for diagnosing user-reported Twingate issues. The framework: trace the connection chain, isolate the broken link.

### Twingate Architecture (Recap)

| Component | Role |
|---|---|
| **Client** | Runs on user device; intercepts traffic, authenticates, establishes connections |
| **Connector** | Lightweight software in your private networks; outbound-only to Twingate; forwards traffic to Resources |
| **Relay** | Twingate-hosted; facilitates NAT traversal for P2P; backup channel when P2P fails |
| **Controller** | Twingate cloud control plane; decides IF a user is allowed |

**Key concept: control plane vs. data plane** -- access failure could be policy (Controller) or network (Client/Connector/Relay). Identify which BEFORE chasing logs.

### Logical Connection Chain

A successful Twingate connection unfolds in 5 stages. Find the broken link:

1. **Identity & Authentication** -- IdP authenticates user
2. **Device & Client** -- Client receives signed ACL from Controller
3. **DNS Resolution** -- Client intercepts FQDN -> CGNAT IP
4. **Routing & Connection** -- Client establishes encrypted tunnel to Connector (P2P or Relay)
5. **Connector to Resource** -- Connector forwards decrypted traffic to Resource

At each stage, Security Policies are evaluated. A connection can fail for non-technical reasons (untrusted device, blocked geography, etc.).

### Repeatable Troubleshooting Methodology

#### Step 1: Define the Scope

| Question | What It Tells You |
|---|---|
| **One user vs. all users?** | Per-user = identity/device/local network. All = systemic (Connector, global service) |
| **One Resource vs. all Resources?** | Per-Resource = Resource def or specific Connector. All = Client/network/identity |
| **One location vs. all locations?** | Location-specific = network/firewall there |
| **When did it start?** | Correlate with recent changes |

#### Step 2: Check Known States and Recent Changes

- **Twingate Status Page** -- ongoing incidents?
- Recent admin changes -- review Audit Logs

#### Step 3: Verify Identity and Device Posture

- User in correct Group(s) with Resource access? (cross-reference with IdP for sync)
- Resource policy requires Trusted Device? Check device status

#### Step 4: Trace the Connection Attempt

**Most valuable tool**: Resource **Activity** report (Admin Console -> Network -> Resources -> select Resource -> Activity).

| What You See | What It Means |
|---|---|
| **No events** | Traffic never reached Connector. Client / network / DNS issue (user-side) |
| **DNS lookup error** | Connector can't resolve the FQDN. Connector-host DNS issue |
| **Unable to connect** | Connector reached but couldn't route to Resource. Network/firewall/security group |
| **Successful events but user reports failure** | Twingate path OK; issue with destination app (perms, etc.) |
| **Successful events but SaaS partially loads** | Missing Resource definitions for CDN/auth subdomains. Use DevTools to find missing |

### Diagnostic Quick Reference Table

| Symptom | Failure Point | Tool | First Question | Doc |
|---|---|---|---|---|
| Can't log in to Twingate | Auth & Identity | IdP Console | User active + assigned to Twingate app in IdP? | /docs/identity-providers |
| App won't connect / service not running | Device or Client | Client logs / `services.msc` / `launchctl` | Twingate service running? | /docs/device-failures |
| Connected but can't reach internal-app | DNS Resolution | `nslookup` + Activity report | Returns CGNAT IP? Connector DNS error? | /docs/dns-failures |
| All users blocked from Resources today | Connector | Admin Console (status) | Connectors online + clock in sync? | /docs/connector-failures |
| Everything is slow on Twingate | Firewall/NAT/Routing | Admin Console (Connector details) | P2P or Relayed? UDP outbound blocked? | /docs/firewall-failures |
| Can't print to home printer when on | Split tunnel + IP conflict | `ipconfig` / Resource defs | Resource CIDR overlaps user's local subnet? | /docs/split-tunnel-failures |
| SaaS app partially loads | Missing Resources | Browser DevTools (Network) | Are all dependent domains defined? | /docs/split-tunnel-failures |

### Essential Tools

**Twingate-specific:**
- Admin Console: **Resource Activity Events**, **Connector Details** (status + clock + P2P/Relay), **Audit Logs**
- Twingate Client logs (More -> Troubleshoot -> View Logs)
- Connector logs (`journalctl -u twingate-connector` or `docker logs <container>`)

**General:**
- `ping`, `traceroute`, `nslookup`/`dig`, `ipconfig`/`ifconfig`, `nmap`, `curl`, browser DevTools, Wireshark

### Escalation

Customers on Teams/Business/Enterprise plans can submit support tickets via Help -> Support in the Admin Console. Gather:
- Issue scope
- Affected users/Resources
- Complete log bundles (Client + Connector)

### Decision Notes

- **Always start with scope** -- "all users" vs. "one user" determines 80% of the diagnostic path
- **Resource Activity report is the single most valuable diagnostic** -- check it second only to scope
- **Most "weird" issues** trace to either DNS conflicts (CGNAT range) or missing Resource definitions for SaaS apps -- check these patterns first

### Related Docs

- /docs/troubleshooting -- KB / community resources
- /docs/dns-failures, /docs/connector-failures, /docs/firewall-failures, /docs/split-tunnel-failures, /docs/device-failures -- Per-failure-mode playbooks
- /docs/troubleshooting-p2p -- P2P-specific playbook
- /docs/network-overview -- Activity report reference
