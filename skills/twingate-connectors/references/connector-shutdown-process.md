---
source: https://www.twingate.com/docs/connector-shutdown-process
type: docs
fetched: 2026-08-14
source_version: 265ab863d94211551ab149cb56fceab0c5eb150e110db762d92fe28fc51bdc94
---

# Connector Shutdown Process

## Summary
When a Connector shuts down (planned or unplanned), connected Clients automatically attempt failover through an ordered list of Connector-Relay pairs. The process involves a ~20-second timeout per failed pair before moving to the next option.

## Key Information
- Each Connector maintains connections to **4 Relays** simultaneously
- Connectors report their connected Relays to the Controller via **regular heartbeat**
- Controller provides each Client an **ordered list of Connector-Relay pairs** at connection time
- List is **randomly generated but seeded by unique device ID** — consistent per device, may differ between devices
- List iterates over all Connectors to minimize downtime

## Failover Process (Step-by-Step)

Assuming 2 Connectors (A and B) in a Remote Network, when Connector A goes down:

1. Connections between Connector A and all connected Clients are terminated
2. Client attempts to reconnect to first Connector-Relay pair in its list
3. Relay waits for Connector A to establish connection (~**20 seconds**)
4. Relay notifies Client that connection to first pair failed
5. Client moves to second Connector-Relay pair (Connector B, per list ordering)
6. Client successfully connects to Connector B

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Relay wait timeout | ~20 seconds |
| Relays per Connector | 4 |

## Gotchas
- **~20-second gap** per failed Connector-Relay pair — factor this into availability SLAs
- With only 1 Connector, there is no failover; deploy minimum 2 Connectors per Remote Network for HA
- The ordered list is **fixed at connection time** from the Controller — clients don't dynamically reorder mid-session
- List order differs per device, so failover behavior may not be uniform across all clients simultaneously

## Prerequisites
- Multiple Connectors per Remote Network (minimum 2 recommended for high availability)
- Connectors must be actively heartbeating to the Controller to appear in Client lists

## Related Docs
- Connector deployment and configuration
- Remote Networks setup
- High availability planning for Connectors