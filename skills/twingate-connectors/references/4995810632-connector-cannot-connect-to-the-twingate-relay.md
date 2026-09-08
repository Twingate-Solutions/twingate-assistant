---
source: https://help.twingate.com/articles/4995810632-connector-cannot-connect-to-the-twingate-relay
type: help
fetched: 2026-09-06
source_version: 3e8f2814858296e5bd5606096baa1e9ac4d431e8d3b710b10ca18332e8ae3fc2
---

# Connector Cannot Connect to Twingate Relay

## Summary
Connector fails to establish connections to Resources due to inability to connect to the Twingate Relay architecture. The root cause is the Connector VM having only a public IPv6 address assigned, as the Relay requires IPv4 connectivity.

## Key Information
- Affects: Twingate Connector component
- Clients may work normally while Resource connections fail completely
- Relay connectivity requires public IPv4 address on the Connector instance
- Error appears in Connector logs, not Client logs

## Symptoms
- Connector passes outbound internet traffic checks and meets all Network Requirements
- Zero connections to any Resources succeed
- Twingate Admin console shows Connector unable to connect to Resources

## Diagnostic Log Errors
Look for these specific errors in Connector logs:

```
[Timestamp][Connector]: [ERROR] [libsdwan] listen::channel_event: Failed to preconnect a relay listener "ice://any": 110 (Connection timed out)

[Timestamp][Connector]: [ERROR] [libsdwan] listen::maintain_relay_connectivity: relay [IP address and port] is not available, disconnect
```

Also may appear:
```
resource temporarily unavailable
```

## Root Cause
Connector VM instance is assigned **only a public IPv6 address** — no public IPv4 address. The Twingate Relay infrastructure requires IPv4.

## Resolution

**Assign a public IPv4 address to the Connector VM instance.**

Steps vary by cloud provider:
- **AWS**: Assign an Elastic IP or enable auto-assign public IPv4 on the subnet/instance
- **GCP**: Assign an external IPv4 address to the network interface
- **Azure**: Attach a public IP resource (IPv4) to the NIC

After assigning the IPv4 address, restart the Connector service to re-establish relay connectivity.

## Gotchas
- IPv6-only environments are **not supported** for Connector instances — even if general outbound internet works fine via IPv6
- Passing standard network connectivity checks does not rule out this issue if those checks use IPv6
- Admin console showing "Connector unable to connect to Resource" may appear identical to other failure modes — check logs for the specific relay errors above

## Related Docs
- [Twingate Network Requirements](https://help.twingate.com/articles/network-requirements)
- Twingate Connector deployment guides (per cloud provider)