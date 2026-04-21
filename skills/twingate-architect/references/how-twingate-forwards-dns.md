## Page Title
How Twingate Forwards DNS

## Summary
Documents exactly which DNS query types the Twingate Client handles locally versus forwards to the Connector, and how to work around cases where non-A record queries are blocked. The Client resolves A records to CGNAT addresses locally; all other record types (TXT, MX, CNAME, etc.) are forwarded through the Connector to the private DNS server.

## Key Information
- **A records**: resolved locally by Client to CGNAT range (`100.64.0.0/10`); traffic routed through Twingate interface
- **Non-A records** (TXT, MX, CNAME, PTR, etc.): forwarded to Connector, resolved against private network DNS server
- **Port 53/UDP blocking**: if a Resource has port 53/UDP blocked, non-A DNS queries for that resource return empty responses (not an error, just no answer)
- **Explicit DNS forwarding workaround**: if private DNS server (`10.0.0.2`) is itself a Twingate Resource with port 53/UDP open, use `dig @10.0.0.2 <name>` to bypass the port restriction and get real IPs or non-A records
- `dig @<private-dns-server> A nas.home.int` returns the real private IP, not the CGNAT address

## Prerequisites
- Connector version >= 1.46.0
- Client minimum versions for explicit DNS forwarding:
  - macOS: 1.0.26+
  - Linux: 1.0.74+
  - iOS: 1.0.26+
  - Android: 1.0.23+
  - Windows: future release (not yet supported at time of writing)

## Step-by-Step
Not applicable — reference page with diagnostic examples.

## Configuration Values
- DNS forwarding uses port `53/UDP` — must be allowed in Resource port restrictions for the DNS server Resource

## Gotchas
- Non-A queries for a Resource with port 53/UDP blocked silently return empty responses — this can break applications that rely on TXT (SPF, DKIM) or SRV records
- `dig @<dns-server>` bypasses CGNAT assignment and returns the real private IP — useful for diagnostics but may break applications that expect the CGNAT address
- Windows Client does not yet support explicit DNS forwarding (feature pending)

## Related Docs
- `/docs/how-dns-works-with-twingate` — full DNS interception flow
- `/docs/introduction-to-dns` — DNS primer
- `/docs/private-dns-best-practices` — private DNS configuration
- `/docs/supporting-unqualified-domain-names` — search domain handling
