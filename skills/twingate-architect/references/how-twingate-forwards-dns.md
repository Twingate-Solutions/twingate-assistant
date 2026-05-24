# How Twingate Forwards DNS

## Summary
Twingate Client resolves DNS `A` records locally using CGNAT IP addresses (`100.64.0.0/10`) and routes traffic through the local Twingate interface. Non-`A` record types (e.g., `TXT`, `MX`) are forwarded to the Remote Network via the Connector using the private DNS server. DNS forwarding can be blocked by Resource port restrictions.

## Key Information
- `A` record requests → resolved locally to CGNAT IPs (`100.64.0.0/10`); traffic routed via `100.96.0.0/12` through Twingate interface
- Non-`A` record requests → forwarded to Remote Network, resolved by Connector using private DNS
- DNS uses port `53/UDP`; Twingate treats DNS traffic as regular UDP traffic to the Connector
- If port `53/UDP` is blocked on a Resource, non-`A` queries return empty responses (status: `NOERROR`, 0 answers)

## Prerequisites
To use explicit DNS forwarding, minimum versions required:
| Platform | Min Version |
|----------|-------------|
| Connector | 1.46.0 |
| macOS Client | 1.0.26 |
| Linux Client | 1.0.74 |
| iOS Client | 1.0.26 |
| Android Client | 1.0.23 |
| Windows Client | Not yet released |

## Explicit DNS Forwarding

**Use case:** Bypass CGNAT address assignment or query non-`A` records when port restrictions exist.

**Method:** Target a private Resource that is also a DNS server using `@<dns-server>` syntax.

```bash
dig @10.0.0.2 TXT nas.home.int       # Returns TXT record via private DNS server
dig @dns-server A nas.home.int        # Returns real IP, not CGNAT address
```

**Requirement:** The DNS server Resource must have port `53/UDP` open in its Twingate Resource configuration.

## Gotchas
- **Port 53/UDP blocked on Resource** → non-`A` queries return empty response with `NOERROR` status (misleading, not an error code)
- Port restriction applies to the **queried Resource**, not the DNS server Resource — use explicit `@dns-server` to route through a Resource with port `53/UDP` open
- Explicit DNS forwarding returns the **real** IP for `A` records, not the CGNAT address the Client would normally assign
- Windows explicit DNS forwarding is not yet supported
- Twingate intentionally avoids special-casing DNS traffic; DNS is treated as plain UDP

## Configuration Values
- CGNAT range for local resolution: `100.64.0.0/10`
- Routing range via Twingate interface: `100.96.0.0/12`
- DNS port: `53/UDP`

## Related Docs
- [How DNS works with Twingate](https://www.twingate.com/docs/dns)
- [Port restrictions](https://www.twingate.com/docs/port-restrictions)