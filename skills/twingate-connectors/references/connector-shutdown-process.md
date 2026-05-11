# Connector Shutdown Process

## Summary
When a Connector shuts down (intentionally or unintentionally), connected Clients automatically attempt failover to other Connectors and Relays. The process involves a ~20-second timeout before the Client tries the next available Connector-Relay pair.

## Key Information
- Each Connector maintains connections to **4 Relays** simultaneously
- Connectors report their connected Relays to the Controller via **regular heartbeat**
- On Client connection, Controller sends an **ordered list of Connector-Relay pairs** to try
- The ordered list is **randomly generated but seeded by unique device ID** — consistent per device, may differ between devices
- List iterates over all Connectors to minimize downtime (not all Relays on one Connector first)

## Failover Sequence (2-Connector Example)

1. Connector A goes down → active Client connections terminate
2. Client attempts reconnection to first Connector-Relay pair in its list
3. Relay waits ~**20 seconds** for Connector A to establish connection
4. Relay responds to Client: connection failed
5. Client tries **second Connector-Relay pair** (Connector B)
6. Client successfully connects via Connector B

## Configuration Values
- **Relay timeout**: ~20 seconds before declaring a Connector-Relay pair unreachable
- **Relays per Connector**: 4

## Gotchas
- **~20-second downtime** is expected per failed Connector-Relay pair attempt — plan accordingly
- Single-Connector setups have no failover path; deploy **2+ Connectors per Remote Network** for HA
- The ordered list is fixed per device — if a device's first pair is always Connector A, that device will always experience the 20-second delay when Connector A is down
- Unintentional shutdowns (crashes) follow the same process as intentional ones (upgrades)

## Prerequisites
- Multiple Connectors per Remote Network for automatic failover
- Clients must be online and connected to Twingate to receive the Connector-Relay pair list from the Controller

## Related Docs
- Connector deployment and management
- Remote Network configuration
- High availability planning for Connectors