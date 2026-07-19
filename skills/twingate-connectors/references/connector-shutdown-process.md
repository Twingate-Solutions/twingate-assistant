# Connector Shutdown Process

## Summary
When a Connector shuts down (intentionally or unintentionally), connected Clients automatically attempt to reconnect using an ordered list of Connector-Relay pairs. The failover process involves a ~20-second relay timeout before the Client moves to the next available Connector.

## Key Information
- Each Connector maintains connections to **4 Relays** simultaneously
- Connectors report their connected Relays to the Controller via **regular heartbeats**
- Controller provides each Client an **ordered list of Connector-Relay pairs** at connection time
- The ordered list is **randomly generated but seeded by unique device ID** — consistent per device, may differ between devices
- List iterates over all Connectors to minimize downtime exposure

## Failover Sequence (2-Connector Example)

1. Connector A goes down → active Client connections terminate
2. Client attempts reconnection to first Connector-Relay pair in its list
3. Relay waits ~**20 seconds** for Connector A to establish connection
4. Relay notifies Client that connection to first pair failed
5. Client moves to second pair in list (Connector B, per iteration order)
6. Client successfully connects via Connector B

## Configuration Values
- **Relay wait timeout**: ~20 seconds (fixed, not configurable)
- **Relays per Connector**: 4 (fixed)

## Gotchas
- **20-second timeout is unavoidable** per failed Connector-Relay pair — plan availability SLAs accordingly
- With only 1 Connector in a Remote Network, there is no failover target; downtime persists until Connector recovers
- Device-specific list ordering means different clients may experience different failover behavior
- Unintentional shutdowns (crashes) follow the same process as intentional ones — no fast-path failure detection

## Prerequisites
- Minimum 2 Connectors per Remote Network for high availability
- Clients must be authenticated and have received the Connector-Relay list from the Controller

## Related Docs
- Connector deployment and configuration
- Remote Network setup
- High availability planning for Connectors
- Relay architecture