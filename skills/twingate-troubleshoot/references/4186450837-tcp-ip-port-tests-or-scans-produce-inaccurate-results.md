---
source: https://help.twingate.com/articles/4186450837-tcp-ip-port-tests-or-scans-produce-inaccurate-results
type: help
fetched: 2026-09-06
source_version: 15b112953cf8a55cf774e7c7c868b6febfbb564df1269f192a4e773d77fe0150
---

# TCP/IP Port Tests or Scans Produce Inaccurate Results

## Summary
Port scanning tools (Nmap, telnet, netcat, curl) produce unreliable results when testing Twingate Resources from a Twingate Client. This occurs because the Client intercepts traffic and proxies connections through the Connector, causing false positives and false negatives regardless of actual port availability.

## Key Information

- **Affected components**: Twingate Client, Twingate Connector
- **Affected tools**: Nmap, telnet, netcat, curl, any TCP/IP port scanner
- **Two failure modes** depending on whether Resource ports are restricted in Twingate

### Restricted Ports (False Negatives / Unexpected Open Ports)
- Client intercepts all traffic matching the Resource
- Client evaluates traffic against defined port rules before forwarding
- Non-matching ports are **bypassed, not forwarded** — but the scan still reports them as open
- Log entry `does not match any policy, use bypass` confirms traffic is not sent
- Example: Resource restricted to TCP/UDP 8001 + ICMP; Nmap reports other ports open incorrectly

### Unrestricted Ports (False Positives)
- Client proxies all traffic through the Connector
- TCP handshake completes **against the Connector**, not the target Resource
- Result: `Connected` even if target firewall blocks the port
- Result: `Connected` even if the target host is powered off
- Connection only fails if the **Connector itself** is taken offline

## Gotchas

- Powering down the target Resource does **not** cause connection failure — only taking down the Connector will
- These behaviors apply when testing **from the Twingate Client**; scans from outside Twingate are unaffected
- Port restrictions in Twingate ≠ firewall rules on the Resource — both layers exist independently
- Debug logs on the Client can confirm whether traffic is actually being forwarded

## Recommended Testing Approach

Do **not** rely on TCP/IP port tests to validate Twingate Resource connectivity. Use application-layer tests instead:

| Protocol | Recommended Test |
|----------|-----------------|
| SSH | Interactive SSH client session |
| RDP | RDP client connection |
| HTTPS | Verify HTTP 200 response |
| Other | Application-specific session validation |

## Debugging

Enable Client debug logs to verify actual traffic handling:
```
# Look for in logs:
"does not match any policy, use bypass"
"is_protocol_port_allowed: protocol TCP, port X is not allowed"
```
Packet captures can further confirm whether traffic is forwarded.

## Related Docs
- Twingate Client debug logging
- Resource port restriction configuration
- Twingate Connector deployment