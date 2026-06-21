# Connector Shutdown Process

## Summary
When a Connector shuts down (planned or unplanned), connected Clients automatically attempt failover through an ordered list of Connector-Relay pairs. The process involves a ~20-second relay timeout before the Client moves to the next available Connector.

## Key Information
- Each Connector maintains connections to **4 Relays** simultaneously
- Connectors report their connected Relays to the Controller via **regular heartbeat**
- On Client connect, the Controller sends an **ordered list of Connector-Relay pairs** to try
- The ordered list is **randomly generated but seeded by unique device ID** — consistent per device, may differ between devices
- List iterates over all Connectors to minimize downtime

## Failover Process (Step-by-Step)

Assumes 2 Connectors (A and B) in a Remote Network:

1. Connector A goes down
2. Active connections between Connector A and Clients are terminated
3. Client attempts to reconnect to the **first** Connector-Relay pair in its Controller-provided list
4. Relay waits for Connector A to connect — times out after **~20 seconds**
5. Relay notifies Client that the first pair failed
6. Client moves to the **second** Connector-Relay pair (Connector B, due to list ordering)
7. Client successfully connects via Connector B

## Configuration Values
- No configurable parameters for this process — behavior is automatic
- Timeout before failover: **~20 seconds** (fixed, not user-configurable)

## Gotchas
- **~20-second downtime** is expected per failed Connector-Relay pair during failover — plan accordingly
- Failover only works if additional Connectors exist in the Remote Network; single-Connector setups have no fallback
- Device-specific list ordering means failover behavior may differ between Clients — not all Clients fail over to the same Connector simultaneously
- Unintentional shutdowns (crashes) follow the same process as intentional ones (upgrades)

## Prerequisites
- Minimum 2 Connectors per Remote Network for high availability
- Connectors must be connected to Relays (verified via heartbeat to Controller)

## Related Docs
- Connector deployment and configuration
- High availability / redundancy planning
- Relay architecture