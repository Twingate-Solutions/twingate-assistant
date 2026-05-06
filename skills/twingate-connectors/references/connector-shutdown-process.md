# Connector Shutdown Process

## Summary
When a Connector shuts down (planned or unplanned), connected Clients attempt to maintain connectivity by iterating through an ordered list of Connector-Relay pairs. The failover process takes approximately 20 seconds per failed pair before moving to the next option.

## Key Information
- Each Connector maintains connections to **4 Relays simultaneously**
- Connectors report their connected Relays to the Controller via **regular heartbeat**
- On Client connection, the Controller sends an **ordered list of Connector-Relay pairs** to try
- The ordered list is **randomly generated but seeded by a unique device ID** — consistent per device, but differs between devices
- The list **iterates over all Connectors** to minimize downtime (e.g., pairs alternate between Connector A and Connector B)

## Failover Flow (2 Connectors: A and B)

1. Connector A goes down → existing Client connections to Connector A terminate
2. Client attempts to reconnect to first Connector-Relay pair in its list (Connector A + Relay)
3. Relay waits ~**20 seconds** for Connector A to connect
4. Relay reports failure back to Client
5. Client moves to next pair in list (Connector B + Relay)
6. Client successfully connects via Connector B

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Relay wait timeout | ~20 seconds per failed pair |
| Relays per Connector | 4 |

## Gotchas
- **~20 second delay per failed Connector-Relay pair** — with only 1 Connector, clients experience ~20s of downtime before exhausting options
- Failover order is **device-specific** — don't assume all clients fail over in the same sequence
- Unintentional shutdowns (crashes) go through the same process as intentional ones (upgrades)
- For high availability, deploy **at least 2 Connectors** per Remote Network to ensure the second pair in the list points to a healthy Connector

## Prerequisites
- Multiple Connectors per Remote Network recommended for HA
- Clients must be online and connected to receive the Connector-Relay pair list from the Controller

## Related Docs
- Connector deployment and configuration
- High availability / redundancy planning
- Relay infrastructure