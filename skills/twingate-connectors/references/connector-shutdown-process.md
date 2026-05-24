# Connector Shutdown Process

## Summary
When a Connector shuts down, connected Clients attempt to reconnect by iterating through an ordered list of Connector-Relay pairs provided by the Controller. The failover process takes approximately 20 seconds per failed pair before moving to the next option.

## Key Information
- Each Connector maintains connections to **4 Relays** simultaneously
- Connectors report their connected Relays to the Controller via **regular heartbeat**
- Controller provides each Client an **ordered list of Connector-Relay pairs** at connect time
- The list is **randomly generated but seeded by unique device ID** — consistent per device, may differ between devices
- List iterates over all Connectors to minimize downtime (e.g., alternates A→B→A→B across pairs)

## Failover Sequence (2-Connector Example)

1. Connector A goes down → active Client connections terminate
2. Client attempts reconnection to first Connector-Relay pair in its list
3. Relay waits ~**20 seconds** for Connector A to establish connection
4. Relay notifies Client that connection to first pair failed
5. Client moves to **second pair** in list (Connector B)
6. Client successfully connects through Connector B

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Relay wait timeout per pair | ~20 seconds |
| Relays per Connector | 4 |

## Gotchas
- **~20 second failover delay per failed pair** — with only 1 Connector, downtime equals the full relay timeout before failure is confirmed
- Clients receive the pair list **at connection time** — if the list becomes stale, behavior may not reflect current Connector state until reconnect
- Shutdown can be **intentional** (upgrade) or **unintentional** (crash) — both follow the same failover path with no differentiation in client behavior

## Availability Planning Implications
- **Minimum 2 Connectors per Remote Network** recommended to reduce failover time impact
- Single-Connector setups will experience the full ~20s timeout before a definitive failure response
- Device-specific ordering means different Clients may fail over to different Connectors, distributing load

## Related Docs
- Connector deployment and configuration
- Remote Network setup
- Relay architecture
- High availability planning