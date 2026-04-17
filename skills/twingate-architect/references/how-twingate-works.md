## How Twingate Works

**Page Title:** How Twingate Works

**Summary:** Twingate's architecture uses four components — Controller, Client, Connector, and Relay — where no single component can independently authorize traffic flow. Authorization always requires confirmation across multiple components, with user authentication delegated to a third-party IdP. The result is that authenticated users access private Resources using their native FQDNs/IPs without knowledge of underlying network topology.

---

**Key Information:**

- **Controller** (Twingate-hosted, multi-tenant): stores config, delegates auth to IdP, generates signed ACLs for both Clients and Connectors, registers/authenticates Connectors
- **Client** (installed on user device): handles auth redirect, holds signed user ACL, intercepts DNS/TCP/UDP for protected Resources, establishes certificate-pinned TLS tunnel to Connector
- **Connector** (deployed inside private network): maintains outbound connection to Relay, verifies Client TLS integrity + ACL signature on every inbound connection, performs local DNS resolution for FQDN Resources
- **Relay** (Twingate-hosted): acts as TURN server equivalent — stores only an anonymous hash-based Connector ID, never terminates data connections, brokers Client↔Connector tunnel establishment
- ACL intersection model: traffic only flows if the Resource appears in *both* the Client ACL and the Connector ACL — dual check prevents single-component compromise
- P2P is always attempted first; Relay is fallback only
- DNS for protected Resources resolves locally on the Remote network (via Connector), not on the client network
- Connector ID shared with Clients is an anonymized hash — no network-identifying information exposed

---

**Prerequisites:** N/A (architectural overview, no setup steps)

**Step-by-Step:** N/A (conceptual doc)

**Configuration Values:** None specified in this doc

---

**Gotchas:**

- The Controller never touches data flow — it only handles coordination/authorization
- Connectors make *outbound* connections to Relays, so no inbound firewall rules are needed on the Remote network
- Client ACL is signed by Controller; Connector verifies the signature on every connection — tampering is detectable
- Connector ID is the only information Clients ever receive about a Connector — no IP, hostname, or network details are exposed to Clients

---

**Related Docs:**
- Connector deployment guide
- Client installation
- Identity Provider configuration
- Relay architecture
- Connection flow / registration flow (referenced as "next article in this guide")