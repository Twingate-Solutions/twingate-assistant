---
source: https://help.twingate.com/articles/4995810632-connector-cannot-connect-to-the-twingate-relay
type: help
fetched: 2026-11-01
source_version: 56516f3ef77dbe1612d23838ae42af47f34b26cb6fc036910bc39bcfe0b2c752
trust: official
---

# Connector Cannot Connect to Twingate Relay

## Summary
When a Connector fails to reach the Twingate Relay, all Resource connections fail even if internet connectivity otherwise works. The root cause is typically the Connector VM lacking a public IPv4 address.

## Key Information
- Affects: Twingate Connector component
- Symptom: Client works, but no Resource connections succeed
- Admin console shows Connector unable to reach Resources
- Relay connectivity requires a public IPv4 address

## Symptoms
- Connector has outbound internet access and meets all Network Requirements
- Zero Resource connections succeed
- Admin console connection details confirm Connector-side failure

## Error Messages in Connector Logs
```
[Timestamp][Connector]: [ERROR] [libsdwan] listen::channel_event: Failed to preconnect a relay listener "ice://any": 110 (Connection timed out)
[Timestamp][Connector]: [ERROR] [libsdwan] listen::maintain_relay_connectivity: relay [IP address and port] is not available, disconnect
```
May also include: `resource temporarily unavailable`

## Root Cause
The Connector VM instance has **only a public IPv6 address** assigned — no public IPv4 address. The Twingate Relay requires IPv4 connectivity.

## Resolution
Assign a **public IPv4 address** to the Connector VM instance.

Steps vary by cloud provider but generally involve:
1. Allocate/associate a static public IPv4 address to the VM (e.g., Elastic IP in AWS, static external IP in GCP, public IP in Azure)
2. Verify the Connector instance reflects the new IPv4 assignment
3. Restart the Connector service and check logs to confirm relay connectivity is restored

## Gotchas
- IPv6-only VM configurations will silently fail relay connectivity — the Connector may appear online but all Resource connections fail
- Confirm against [Twingate Network Requirements](https://www.twingate.com/docs/connector-requirements) that all necessary ports/protocols are open for the IPv4 address

## Related Docs
- Twingate Network Requirements
- Connector deployment documentation