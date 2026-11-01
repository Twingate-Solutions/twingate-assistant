---
source: https://help.twingate.com/articles/4186450837-tcp-ip-port-tests-or-scans-produce-inaccurate-results
type: help
fetched: 2026-11-01
source_version: cf158e66e721271b2f3583f8bddbe5d20182cce6525b20ec9f19d0e400e47ff0
trust: official
---

# TCP/IP Port Tests or Scans Produce Inaccurate Results

## Summary
Port scanning tools (Nmap, telnet, netcat, curl) produce inaccurate results when run from a Twingate Client against Twingate Resources. Traffic interception by the Client and proxying via the Connector cause both false positives and false negatives depending on port restriction configuration.

## Key Information
- **Affected components:** Twingate Client, Twingate Connector
- **Affected tools:** Nmap, telnet, netcat, curl telnet mode, any TCP/IP port scanner
- Two distinct failure modes depending on whether port restrictions are configured on the Resource

## Two Failure Modes

### Restricted Ports (False Negatives → Unexpectedly Open Ports)
- Client intercepts all traffic matching the Resource
- Client applies the port ruleset locally and drops disallowed traffic **without forwarding it**
- Nmap reports ports as open even though they are blocked
- Log entry confirms: `protocol TCP, port 7 is not allowed` + `use bypass`

### Unrestricted Ports (False Positives → Connected to Offline Host)
- Client proxies connection through the Connector
- Initial TCP handshake completes **against the Connector**, not the target host
- Result: `Connected to 10.168.0.6` even when:
  - Target host has a local firewall blocking the port
  - Target host is powered off
- Connection only fails if the **Connector itself** is powered down

## Root Cause
Twingate intercepts and proxies traffic at the Client level. Port test tools measure TCP handshake success, which reflects the Client/Connector layer — not the actual target service availability.

## Recommended Testing Approach
Do **not** rely on TCP/IP port scans to validate Resource connectivity. Use application-level session tests instead:

| Protocol | Recommended Test |
|----------|-----------------|
| SSH | Interactive SSH client connection |
| RDP | Full RDP client session establishment |
| HTTPS | Verify HTTP 200 response |
| Other | Application-native connectivity check |

## Debugging Tips
- Enable debug-level logging on the Twingate Client to observe traffic authorization decisions
- Log lines containing `is_protocol_port_allowed` confirm whether traffic is forwarded or dropped
- Packet capture can further confirm whether traffic leaves the Client

## Gotchas
- Shutting down only the target Resource host still returns "Connected" for unrestricted ports — misleading
- Port scans from **outside** Twingate (e.g., from the Connector's network directly) will return accurate results
- This behavior is by design, not a bug — it is a consequence of how Twingate intercepts and routes traffic

## Related Docs
- Twingate Resource port restriction configuration
- Twingate Client debug logging
- Twingate Connector deployment