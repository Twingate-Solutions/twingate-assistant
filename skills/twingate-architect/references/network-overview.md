# Network Overview

## Page Title
Network Overview (Twingate Admin Console)

## Summary
The Network Overview tab is an admin dashboard providing a high-level snapshot of network status, including device counts, resource availability, user roles, and connection history. It enables admins to monitor network health and drill into specific activity details.

## Key Information

**Network Insights Metrics:**
- **Devices:** Active (status=Active), Online (user logged in), Trusted (meets Trusted Profile requirements)
- **Resources:** Total, Online (in Online Remote Networks), Disconnected (in Offline Remote Networks)
- **Remote Networks:** Total, Online (≥1 online Connector), Offline (no online Connectors)
- **Users by role:** Admin, DevOps, Support, Member
- **Services:** Count of Service Accounts

**Connection History:**
- Time ranges: 7, 30, 90 days
- 7-day graph: each bar = connections per **hour**
- 30/90-day graphs: each bar = connections per **day**
- Tracks both successful and failed connections

**Recent Activity:**
- Displays network traffic across all Remote Networks
- Clicking an event reveals: Resource IP address, protocol, connection type, duration

## Prerequisites
- Admin role access to Twingate Admin Console
- Remote Networks and Connectors configured to see meaningful data

## Gotchas
- "Online Resources" and "Disconnected Resources" are determined by the Remote Network's Connector status, not the Resource itself
- A Remote Network is "Offline" if **no** Connectors are online — a single online Connector makes it "Online"
- Active Devices ≠ Online Devices: Active refers to device status flag; Online requires an active user session in the Client
- Connection history granularity changes between time ranges (hourly vs. daily) — be aware when interpreting spikes

## Configuration Values
None — this is a read-only dashboard view with no configurable parameters.

## Related Docs
- Devices and Trusted Profiles
- Remote Networks and Connectors
- Service Accounts
- User Roles (Admin, DevOps, Support, Member)
- Connection Logs / Activity