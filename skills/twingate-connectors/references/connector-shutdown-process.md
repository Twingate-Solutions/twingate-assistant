# Connector Shutdown Process

## Summary
When a Connector shuts down (intentionally or unexpectedly), connected Clients automatically attempt failover through an ordered list of Connector-Relay pairs. The process involves a ~20-second relay timeout before the Client moves to the next available Connector.

## Key Information
- Each Connector maintains connections to **4 Relays** simultaneously
- Connectors report connected Relays to the Controller via **regular heartbeat**
- Controller sends each Client an **ordered list of Connector-Relay pairs** at connection time
- The ordered list is **randomly generated but seeded by unique device ID** — consistent per device, may differ between devices
- List iterates over all Connectors to minimize downtime

## Failover Process (Step-by-Step)

Assuming 2 Connectors (A and B) in a Remote Network, when Connector A goes down:

1. Connections between Connector A and all connected Clients are terminated
2. Client attempts to reconnect to the first Connector-Relay pair from its Controller-provided list
3. Relay waits for Connector A to connect (~**20-second timeout**)
4. Relay notifies Client that connection to first pair failed
5. Client moves to second Connector-Relay pair (Connector B, due to list ordering)
6. Client successfully connects to Connector B

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Relay wait timeout | ~20 seconds |
| Relays per Connector | 4 |

## Gotchas
- **~20-second downtime** per failed Connector-Relay pair before failover proceeds — plan availability requirements accordingly
- With only 1 Connector in a Remote Network, there is no failover target; Resources will be unavailable until the Connector recovers
- The failover list is determined at **Client connection time** by the Controller — clients don't dynamically reorder during a session
- Device-specific list ordering means different clients may have different failover sequences

## Prerequisites
- Minimum 2 Connectors per Remote Network for failover capability
- Connectors must be actively heartbeating to ensure Controller has current Relay mapping

## Related Docs
- Connector deployment and high availability
- Remote Network configuration
- Relay architecture