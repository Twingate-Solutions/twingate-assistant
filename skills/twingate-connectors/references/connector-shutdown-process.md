# Connector Shutdown Process

## Summary
When a Connector shuts down (intentionally or unintentionally), connected Clients automatically failover to other available Connectors. The process involves Relay timeout detection (~20 seconds) before the Client moves to the next Connector-Relay pair in its ordered list.

## Key Information
- Each Connector maintains connections to **4 Relays**
- Connectors report connected Relays to the Controller via **regular heartbeat**
- Controller sends each Client an **ordered list of Connector-Relay pairs** on connection
- The list is **randomly generated but seeded by unique device ID** — consistent per device, may differ between devices
- List iterates over all Connectors to ensure failover coverage

## Failover Process (Step-by-Step)

Assumes 2 Connectors (A and B) in a Remote Network:

1. Connector A goes down → connections to all Clients terminate
2. Client attempts to reconnect to first Connector-Relay pair in its list
3. Relay waits for Connector A to connect — **~20 second timeout**
4. Relay notifies Client that connection to first pair failed
5. Client moves to second Connector-Relay pair (Connector B)
6. Client successfully connects through Connector B

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Relay timeout waiting for downed Connector | ~20 seconds |
| Relays per Connector | 4 |

## Gotchas
- **~20 second downtime window** is expected during failover — plan accordingly
- Failover only works if **multiple Connectors** exist in the Remote Network; single-Connector setups have no fallback
- The ordered list is **device-specific** — different clients may fail over in different sequences
- Unintentional shutdowns (crashes) follow the same process as intentional ones (upgrades)

## Availability Planning Recommendations
- Deploy **minimum 2 Connectors** per Remote Network to enable automatic failover
- Expect up to ~20 seconds of connectivity interruption per failover event
- Active sessions will drop and must reconnect — applications may need to handle reconnection

## Related Docs
- Connector deployment/configuration
- Remote Networks setup
- Relay architecture
- High availability planning