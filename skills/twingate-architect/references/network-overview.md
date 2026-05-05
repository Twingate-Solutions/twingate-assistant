## Network Overview

The Network Overview tab in the Admin Console provides a real-time dashboard of key metrics across devices, resources, remote networks, users, and connection history.

**Key Information:**
- Found under the Network tab in the Admin Console
- Connection History: 7, 30, or 90-day views; 7-day uses hourly bars, 30/90-day uses daily bars
- Recent Activity shows all traffic across all Remote Networks with per-event details (Resource IP, protocol, connection type, duration)
- "Online Remote Networks" = at least one Connector online; "Offline" = no active Connectors

**Metrics Available:**
- Devices: Active, Online, Trusted
- Resources: total, Online (Connector up), Disconnected (Connector down)
- Remote Networks: total, Online, Offline
- Users by role: Admin, DevOps, Support, Member
- Services: total Service Accounts

**Gotchas:**
- "Active Devices" and "Online Devices" are distinct: Active = device status is Active; Online = user currently logged into the Client
- Disconnected Resources indicate a Remote Network with no running Connectors, not a problem with the Resource itself

**Related Docs:**
- /docs/audit-logs -- Full audit log access
- /docs/admin-console-export -- Exporting audit log reports
- /docs/connector -- Connector status affects Online/Offline Resource counts
