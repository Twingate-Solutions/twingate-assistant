---
source: https://help.twingate.com/articles/4186450837-tcp-ip-port-tests-or-scans-produce-inaccurate-results
type: help
fetched: 2026-10-04
source_version: d25bf16bb1404130a978c4bed0ac133dd55d1ea6f3f9414779c059e4c4ab99d0
trust: official
---

# TCP/IP Port Tests or Scans Produce Inaccurate Results

## Summary
Port scanning or connectivity testing tools (Nmap, telnet, netcat, curl) produce unreliable results when run against Twingate Resources from a Twingate Client. This occurs because Twingate intercepts traffic at the network level, causing false positives regardless of whether port restrictions are configured on the Resource.

## Key Information

- **Affected components:** Twingate Client, Twingate Connector
- **Affected tools:** Nmap, telnet, netcat, curl telnet mode, any TCP/IP port scanner
- **Two distinct failure modes exist** depending on whether the Resource has port restrictions configured

### Restricted Port Resources (False Negatives / Unexpected Open Ports)
- Twingate Client intercepts traffic destined for the Resource
- Traffic not matching the allowed ruleset is **not forwarded** but the scan may still report ports as open
- Logs will show `is_protocol_port_allowed: protocol TCP, port X is not allowed` and `use bypass`
- Ports appear open in scan results even though traffic is blocked

### Unrestricted Port Resources (False Positives)
- Twingate Client proxies the connection through the Connector
- Initial TCP handshake completes **against the Connector**, not the actual target
- Result: `Connected to <resource>` even if the target has a firewall blocking that port
- Resource being powered off still returns "Connected"
- Only powering down the **Connector itself** will cause the connection to fail

## Gotchas

- A successful `curl -v telnet://` or telnet connection does **not** confirm the target port is open on the actual Resource
- Nmap results from inside the Twingate Client are not representative of actual Resource port state
- Port restrictions enforced by Twingate are **not** visible to scanning tools — the scan bypasses or misreports them
- Do not use scan results to validate Twingate policy enforcement

## Recommended Testing Approach

Use **application-layer tests** instead of TCP/IP port tests:

| Protocol | Valid Test |
|----------|-----------|
| SSH | Establish an interactive SSH session |
| RDP | Connect via RDP client |
| HTTPS | Confirm a 200 HTTP response is returned |
| Other | Test at the application protocol level, not raw TCP |

## Related Docs
- Twingate Resource configuration (port restrictions)
- Twingate Client debug logging
- Twingate Connector deployment