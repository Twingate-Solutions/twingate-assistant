# Connector Shutdown Process

## Summary
When a Connector shuts down (intentionally or unintentionally), connected Clients attempt to reconnect by iterating through an ordered list of Connector-Relay pairs provided by the Controller. The failover process takes approximately 20 seconds per failed Connector before moving to the next option.

## Key Information
- Each Connector maintains connections to **4 Relays** simultaneously
- Connectors report their connected Relays to the Controller via **regular heartbeat**
- Controller sends each Client an **ordered list of Connector-Relay pairs** at connection time
- The list is **randomly generated but seeded by unique device ID** — consistent per device, may differ between devices
- List ordering **iterates over Connectors** to minimize downtime (not Relays first)

## Failover Sequence (2-Connector Example)

1. Connector A goes down → Client connections to Connector A terminate
2. Client attempts to reconnect to first Connector-Relay pair in its list
3. Relay waits ~**20 seconds** for Connector A to respond
4. Relay notifies Client that Connector A is unreachable
5. Client moves to next pair in list (Connector B, different Connector)
6. Client successfully connects via Connector B

## Configuration Values
- **Relay timeout per failed Connector:** ~20 seconds
- **Relays per Connector:** 4

## Gotchas
- **20-second delay is per failed Connector** — with only 1 Connector deployed, clients will experience a ~20 second outage on shutdown with no fallback
- The ordered list is **sent at connection time** by the Controller; if the list isn't refreshed, stale ordering could affect failover behavior
- Failover is automatic but **not instantaneous** — plan for ~20s interruption per unavailable Connector in availability SLAs
- Device-specific list ordering means **different clients may fail over differently** under the same conditions

## Prerequisites
- Minimum 2 Connectors per Remote Network for automatic failover
- Connectors must be heartbeating to the Controller to keep Relay assignments current

## Related Docs
- Connector deployment and configuration
- Remote Network setup
- Relay architecture
- High availability planning