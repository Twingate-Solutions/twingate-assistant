# How Twingate Forwards DNS

## Summary
Twingate Client resolves DNS `A` records locally using CGNAT IPs (`100.64.0.0/10`) and routes traffic through the local Twingate interface to the Connector. Non-`A` record types are forwarded to the Remote Network's private DNS server via the Connector. DNS forwarding is subject to Resource port restrictions.

## Key Information
- Client resolves `A` records locally → assigns CGNAT IP → routes via Twingate interface → proxied to Connector
- Routing range modified in local table: `100.96/12`
- Non-`A` record queries (TXT, MX, etc.) forwarded to Remote Network, resolved by Connector using private DNS
- DNS uses port `53/UDP`; Twingate treats DNS traffic as standard UDP traffic (no special-casing)
- DNS server used when forwarding: shown as `100.95.0.251` (CGNAT range) in responses

## When DNS Forwarding Fails
- If Resource has **port 53/UDP blocked**, non-`A` queries return **empty responses** (ANSWER: 0)
- This is expected behavior due to port restriction enforcement, not a bug
- Most applications function normally when non-`A` DNS requests are blocked

## Explicit DNS Forwarding (Workaround)

### Prerequisites / Version Requirements
| Platform | Minimum Version |
|----------|----------------|
| Connector | 1.46.0+ |
| macOS Client | 1.0.26+ |
| Linux Client | 1.0.74+ |
| iOS | 1.0.26+ |
| Android | 1.0.23+ |
| Windows | Not yet released |

### How It Works
- Add your DNS server (e.g., `10.0.0.2`) as a **private Resource** in Twingate
- Ensure **port 53/UDP is open** on the DNS server Resource
- Query using `@<dns-server-ip>` syntax — Client will not intercept this traffic

### Example Commands
```bash
# Returns real IP (not CGNAT) for resource
dig @10.0.0.2 A nas.home.int

# Returns TXT record even if nas.home.int has port 53/UDP blocked
dig @10.0.0.2 TXT nas.home.int
```

## Gotchas
- Explicit forwarding only works if port 53/UDP is **open on the DNS server Resource**, not on the queried resource
- `A` record queries via explicit DNS server return the **real IP**, not the Twingate CGNAT address
- Windows explicit forwarding support not yet available
- Blocking port 53/UDP on a Resource blocks all DNS forwarding for that Resource's hostname, regardless of record type

## Related Docs
- [How DNS works with Twingate](https://www.twingate.com/docs/) (prerequisite reading)
- Port restrictions documentation