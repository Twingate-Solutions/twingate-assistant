# How Twingate Forwards DNS

## Summary
Twingate Client locally resolves DNS `A` records to CGNAT IPs (`100.64.0.0/10`) and routes traffic through its local network interface. Non-`A` record types (e.g., `TXT`, `MX`) are forwarded to the Remote Network's Connector for resolution via the private DNS server. DNS forwarding is blocked when port 53/UDP is restricted on the Resource.

## Key Information
- Client resolves `A` records locally using CGNAT range `100.64.0.0/10`
- Traffic routing uses subnet `100.96/12` via the Twingate network interface
- Non-`A` DNS queries are proxied to the Connector using the remote network's private DNS server
- DNS traffic is treated as regular UDP traffic on port 53/UDP — no special-casing
- Non-`A` queries return **empty responses** (not errors) when port 53/UDP is blocked on a Resource

## Prerequisites
For explicit DNS forwarding support:
| Platform | Minimum Version |
|----------|----------------|
| Connector | 1.46.0+ |
| macOS Client | 1.0.26+ |
| Linux Client | 1.0.74+ |
| iOS Client | 1.0.26+ |
| Android Client | 1.0.23+ |
| Windows Client | Not yet released |

## When DNS Forwarding Fails
- Resource has port **53/UDP blocked** in its Twingate port restriction configuration
- Result: non-`A` queries return `ANSWER: 0` (empty response, `status: NOERROR`)

## Explicit DNS Forwarding (Workaround)

**Method:** Target a private Resource that is a DNS server directly using `@<dns-server>` syntax.

```bash
dig @10.0.0.2 TXT nas.home.int
```

**Requirements:**
- The DNS server IP (e.g., `10.0.0.2`) must be configured as a Twingate private Resource
- Port 53/UDP must be **allowed** on the DNS server Resource (not necessarily on the queried hostname's Resource)

**Use cases:**
- `dig @dns-server A nas.home.int` — returns real IP, not the CGNAT address
- `dig @dns-server TXT nas.home.int` — returns TXT records even if the target Resource blocks port 53/UDP

## Gotchas
- Port 53/UDP restriction on a Resource blocks ALL DNS queries (including non-`A`) for that Resource, not just direct connections
- Empty response (`ANSWER: 0`) with `NOERROR` status is the symptom of blocked DNS — easily misdiagnosed
- `dig @private-dns-ip` bypasses the CGNAT `A` record resolution — returns actual private IP, not Twingate-assigned CGNAT IP
- Windows explicit DNS forwarding not yet available

## Configuration Values
- CGNAT range: `100.64.0.0/10`
- Routing subnet: `100.96/12`
- DNS port: `53/UDP`

## Related Docs
- [How DNS works with Twingate](https://www.twingate.com/docs/dns)
- [Port restrictions](https://www.twingate.com/docs/port-restrictions)