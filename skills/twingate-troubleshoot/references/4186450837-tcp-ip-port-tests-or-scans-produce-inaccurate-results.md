---
source: https://help.twingate.com/articles/4186450837-tcp-ip-port-tests-or-scans-produce-inaccurate-results
type: help
fetched: 2026-08-06
source_version: 5222a052e72edf770df60fc585996b38fd0f103fdcbe435ef7aa387a405e76a9
---

# TCP/IP Port Tests or Scans Produce Inaccurate Results

## Summary
Port scanning tools (Nmap, telnet, netcat, curl) produce unreliable results when run from a Twingate Client against Twingate Resources. This occurs because the Client intercepts traffic before it reaches the destination, causing false positives and false negatives regardless of actual port availability.

## Key Information
- Affects both restricted and unrestricted Twingate Resources
- Two distinct failure modes depending on port restriction configuration
- Issue is architectural — not a bug or misconfiguration

### Restricted Ports (False Negatives → False Positives)
- Twingate Client intercepts traffic matching defined Resources
- Traffic not matching allowed ports is **not forwarded** but scan still reports ports as open
- Log entry shows: `is_protocol_port_allowed: protocol TCP, port X is not allowed`
- Nmap returns ports as open even when blocked by Twingate policy

### Unrestricted Ports (False Positives)
- Client proxies connection through the Connector
- TCP handshake completes **against the Connector**, not the actual Resource
- Result: `Connected to <resource>` even when:
  - Target host firewall blocks the port
  - Target host is powered off
- Connection only fails if the Connector itself is powered down

## Prerequisites
- Debug logging enabled on Twingate Client (for log verification)
- Understanding that Twingate operates as a traffic interceptor/proxy

## Configuration Values
- Twingate Resource port restriction example: `stor:TCP[[8001]]:UDP[[8001]]:ICMP`
- Debug log identifier: `[SDWAN]` prefix in Client logs
- Log indicator for blocked traffic: `match: no matching rule` / `does not match any policy, use bypass`

## Gotchas
- **Do not use TCP/IP port scans to validate Twingate Resource connectivity** — results are always misleading
- Powering off the target Resource does NOT cause curl/telnet to fail if the Connector is still running
- A single Connector deployment will show failure only when the Connector itself goes down — multi-Connector deployments will remain misleadingly "connected" longer
- `curl -v telnet://` returns false positives for unrestricted resources regardless of actual port state

## Recommended Testing Methods
- **SSH**: Establish an interactive SSH session
- **RDP**: Confirm full RDP client connection
- **HTTPS**: Verify a `200` response is returned
- Use application-layer connectivity tests, not transport-layer port probes

## Related Docs
- Twingate Client debug logging configuration
- Resource port restriction configuration
- Connector deployment documentation