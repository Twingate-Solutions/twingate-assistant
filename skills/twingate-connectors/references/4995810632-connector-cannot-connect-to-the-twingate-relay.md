---
source: https://help.twingate.com/articles/4995810632-connector-cannot-connect-to-the-twingate-relay
type: help
fetched: 2026-08-06
source_version: 3644cbd41c69c737e92c2b19eda883b2c70a2258f5a434e04a045fd955ff298e
---

# Connector Cannot Connect to Twingate Relay

## Summary
Connector fails to establish connections to the Twingate Relay despite successful outbound internet traffic. Root cause is the Connector VM having only a public IPv6 address assigned. Fix requires assigning a public IPv4 address to the Connector instance.

## Key Information
- Affects: Twingate Connector component only
- Symptom: All Resource connections fail while Connector appears otherwise healthy
- Admin console shows Connector unable to connect to Resource
- Twingate Relay requires IPv4 connectivity

## Prerequisites
- Access to the Connector VM/instance networking configuration
- Ability to assign a public IPv4 address to the instance (cloud provider or network admin access)

## Symptoms Checklist
- [ ] Connector has successful outbound internet traffic
- [ ] All network requirements are otherwise met
- [ ] Zero Resource connections succeed
- [ ] Admin console connection details show Connector-to-Resource failures

## Diagnostic Log Errors
Look for these specific errors in Connector logs:
```
[ERROR] [libsdwan] listen::channel_event: Failed to preconnect a relay listener "ice://any": 110 (Connection timed out)
[ERROR] [libsdwan] listen::maintain_relay_connectivity: relay [IP address and port] is not available, disconnect
```
Also look for: `resource temporarily unavailable`

## Resolution
**Assign a public IPv4 address to the Connector instance.**

Steps vary by environment:
- **AWS**: Allocate and associate an Elastic IP (IPv4) to the EC2 instance
- **GCP**: Assign an external IPv4 address to the VM network interface
- **Azure**: Assign a public IPv4 address to the VM's NIC
- **On-prem/other**: Ensure the host has a routable public IPv4 address or NAT with IPv4 egress

## Gotchas
- IPv6-only instances will appear to have working internet connectivity, making this hard to diagnose without checking the address type specifically
- Connector logs may show generic timeout errors that don't immediately point to IPv6-only as the cause
- The `resource temporarily unavailable` message is a secondary indicator, not the primary error

## Related Docs
- [Twingate Network Requirements](https://help.twingate.com/articles/network-requirements) — verify all port/protocol requirements are met before investigating this issue
- Twingate Relay architecture documentation
- Connector deployment guides (AWS, GCP, Azure)