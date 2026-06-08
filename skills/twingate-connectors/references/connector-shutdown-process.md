# Connector Shutdown Process

## Summary
When a Connector shuts down, connected Clients automatically attempt failover by cycling through an ordered list of Connector-Relay pairs. The process involves a ~20-second timeout per failed pair before moving to the next option. Understanding this process is essential for availability planning.

## Key Information
- Each Connector maintains connections to **4 Relays simultaneously**
- Connectors report their connected Relays to the Controller via **regular heartbeat**
- Upon Client connection, the Controller sends an **ordered list of Connector-Relay pairs** to try
- The ordered list is **randomly generated but seeded by a unique device ID** — consistent per device, may differ between devices
- The list **iterates over Connectors** (not Relays first), minimizing downtime during failover

## Failover Sequence (2 Connectors: A and B)

1. Connector A goes down → active Client connections to A are terminated
2. Client attempts to reconnect to the **first Connector-Relay pair** in its list
3. Relay waits for Connector A to establish a connection (~**20-second timeout**)
4. Relay notifies Client that Connector A is unavailable
5. Client moves to the **second Connector-Relay pair** (Connector B)
6. Client successfully connects via Connector B

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Relay wait timeout | ~20 seconds per failed pair |
| Relays per Connector | 4 |

## Gotchas
- **~20-second delay per failed Connector-Relay pair** — with only one Connector deployed, clients will experience this full timeout before failing over to a Relay-only path
- The failover list **iterates over Connectors first**, so deploying 2+ Connectors per Remote Network ensures faster recovery
- Shutdown can be **intentional** (upgrades) or **unintentional** (crash) — both trigger the same Client failover behavior
- Per-device seeding means **different clients may hit different Connectors first**, distributing load but making behavior harder to predict uniformly

## Prerequisites
- Minimum 2 Connectors per Remote Network recommended for high availability
- Clients must be online and able to reach the Controller to receive the Connector-Relay pair list

## Related Docs
- Connector deployment and configuration
- Relay architecture
- High availability / redundancy planning
- Connector heartbeat and health monitoring