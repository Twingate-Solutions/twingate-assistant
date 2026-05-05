## Connector Shutdown Process

How Twingate handles Connector downtime and how Clients fail over to available Connectors and Relays. Critical for HA planning.

**Key Facts:**
- Each Connector maintains connections to 4 Relays simultaneously
- Each Connector reports its Relay connections to the Controller via regular heartbeats
- When a Client connects, the Controller sends an ordered list of Connector-Relay pairs to try
- The ordered list is seeded by a unique device ID and iterates over all Connectors — consistent per device but different across devices

**Failover Flow (2-Connector setup, Connector A goes down):**
1. Connections between Connector A and its Clients are terminated
2. Client tries to reconnect to its first Connector-Relay pair (still Connector A)
3. Relay waits ~20 seconds for Connector A to establish a connection
4. Relay notifies Client that Connector A is unreachable
5. Client moves to the next pair in its list (Connector B)
6. Client successfully connects through Connector B

**Gotchas:**
- ~20-second failover delay per failed Connector-Relay pair attempt; deploy 2 Connectors per Remote Network to limit exposure
- The ordered list from the Controller iterates over Connectors, so the second attempt in the list will be a different Connector (not a different Relay for the same Connector)

**Related Docs:**
- /docs/connector-placement-best-practices -- HA deployment patterns
- /docs/understanding-connectors -- Connector fundamentals
- /docs/understanding-relays -- Relay role
