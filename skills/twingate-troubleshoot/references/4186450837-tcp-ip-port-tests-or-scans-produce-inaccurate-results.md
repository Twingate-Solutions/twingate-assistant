---
source: https://help.twingate.com/articles/4186450837-tcp-ip-port-tests-or-scans-produce-inaccurate-results
type: help
fetched: 2026-11-08
source_version: 77c17deaf86d10349794f6b190410ef3263f8d4c8ca6ed10c367c37344e7ef53
trust: official
---

# TCP/IP Port Tests or Scans Produce Inaccurate Results

## Summary
Port scanning tools (Nmap, telnet, netcat, curl) produce inaccurate results when used against Twingate Resources from a Twingate Client. Traffic is intercepted and proxied by the Client/Connector architecture, causing both false positives and false negatives depending on port restriction configuration.

## Key Information
- **Affected components:** Twingate Client, Twingate Connector
- **Affected tools:** Nmap, telnet, netcat, curl telnet mode, any raw TCP/IP port scanner
- Two distinct failure modes depending on whether Twingate port restrictions are applied to the Resource

## Behavior by Configuration

### Restricted Ports (port-specific Resource rules defined)
- Nmap/scanners report ports as **open when they are not**
- Client intercepts traffic, evaluates against policy, and silently drops non-matching flows (no forwarding occurs)
- Log entry confirms drop: `is_protocol_port_allowed: protocol TCP, port X is not allowed`

### Unrestricted Ports (no Twingate port restrictions on Resource)
- TCP connection reports **connected even if destination firewall blocks the port**
- Connection is established against the Connector, not the actual target — Connector handshake succeeds regardless of target availability
- False positive persists even if the target host is powered off
- Connection only fails if **all Connectors for the Resource are offline**

## Root Cause
Twingate Client intercepts matching traffic at the network layer. For restricted resources, it enforces policy locally without forwarding. For unrestricted resources, the TCP handshake completes against the Connector (proxy), masking the real target's port/firewall state.

## Recommended Testing Approach
Do **not** use port scanners or raw TCP tests to validate Twingate Resource connectivity. Instead:

| Use Case | Correct Test Method |
|----------|-------------------|
| SSH access | Interactive SSH client session |
| RDP access | Interactive RDP client connection |
| Web services | HTTPS request returning HTTP 200 |
| General app | Application-layer session establishment |

## Debugging Tips
- Enable **debug-level logs** on the Twingate Client to observe flow authorization decisions
- Look for log entries containing `authorize_hydra_viper_flow` and `is_protocol_port_allowed`
- Use packet captures to confirm whether traffic is actually forwarded

## Gotchas
- A `Connected to <host>` response from curl/telnet does **not** confirm the target port is open — it may only reflect Connector reachability
- Powering down the target resource does not break existing curl/telnet "connections" if the Connector remains up
- Port scan results showing open ports may be entirely an artifact of Client-side interception, not real open ports

## Related Docs
- Twingate Resource port restrictions configuration
- Twingate Client debug logging
- Twingate Connector deployment