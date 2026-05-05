## Internet Security Overview

Twingate's Internet Security feature set focuses on **DNS encryption (DoH)** and **DNS filtering** at the network level on user devices. Available on **macOS, Windows, Linux** desktop Clients only.

### Two Core Capabilities

| Capability | What It Does | Plan |
|---|---|---|
| **DoH (DNS-over-HTTPS)** | Encrypts all device DNS traffic via the Twingate Client | All plans |
| **DNS Filtering** | Blocks malicious / unwanted domains at the DNS layer | Business / Enterprise (add-on) |

### Mobile / Headless Limitations

- Mobile Clients (iOS, Android, ChromeOS) **do NOT** currently support DoH or DNS Filtering
- **Headless Clients** (running with Service Account) never use DoH -- by design, since service workloads typically need direct DNS

### How It Works

The Twingate Client operates at the **network level** on the device, intercepting DNS traffic regardless of application. Unlike browser-based DNS encryption (which only protects browser traffic), Twingate DoH protects:
- Browser DNS lookups
- App DNS lookups (Slack, Zoom, etc.)
- CLI DNS lookups (`curl`, `dig` -- when targeting public DNS)
- OS-level lookups

No per-application configuration required -- run the Client and it works.

### Setup

Both capabilities are configured in **Admin Console -> Internet Security**:

- **DoH**: see /docs/dns-security for resolver options + fallback behavior
- **DNS Filtering**: see /docs/dns-filtering for blocklist/allowlist + threat categories
- **Always-on Internet Security**: see /docs/internet-security-client-configuration for keeping protection enabled when users are signed out

### Related Docs

- /docs/dns-security -- DoH configuration
- /docs/dns-filtering -- DNS filtering rules + threat categories
- /docs/internet-security-client-configuration -- Machine Keys for always-on
- /docs/nextdns-configuration, /docs/doh-cloudflare -- Third-party DoH/filter integrations
- /docs/browser-security -- Browser-layer security (companion)
