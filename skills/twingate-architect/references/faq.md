## FAQ

Frequently Asked Questions covering Twingate fundamentals: deployment, architecture, performance, end-user experience, and billing. Includes a glossary of core terms.

**Glossary:**
- **Resource** -- any TCP/UDP destination (host, server, application); defined by address, not protocol
- **Connector** -- software component on the private network that proxies Resource traffic; all traffic appears to originate from the Connector host; delivered as a Docker container (no special host privileges required)
- **Security Policy** -- defines authentication controls required to access a Resource (e.g., MFA for SSH access)
- **Group** -- logical grouping of Users with access to a set of Resources; associated with a single Security Policy

**Key Facts:**
- Split tunnel by default -- only Resource traffic goes through Twingate; public internet traffic is unaffected
- No inbound firewall rules required -- Connectors make outbound connections only; no public-facing gateways
- Twingate URL (subdomain) cannot be changed after network creation
- Clients available for macOS, Windows, Linux, ChromeOS, Android, iOS/iPadOS
- Compatible with existing VPN infrastructure -- no rip-and-replace required
- Supports any TCP/UDP application; no app, device, or server reconfiguration needed
- Transport: TLS v1.2 with standard ciphers
- IdP integration supported (Okta, Entra ID, Google Workspace, OneLogin, others) -- Twingate does not store passwords
- Two Connectors per Remote Network recommended for HA failover

**Related Docs:**
- /docs/how-twingate-works -- Architecture deep dive
- /docs/twingate-vs-vpn -- VPN comparison
- /docs/connector-placement-best-practices -- Connector deployment recommendations
