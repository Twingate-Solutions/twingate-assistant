# Network Overview

## Page Title
Network Overview (Twingate Admin Dashboard)

## Summary
The Network Overview tab provides a high-level dashboard snapshot of your Twingate network's current state, including device counts, resource status, user roles, and connection history. Admins use it as a starting point to assess network health and drill into specific activity details.

## Key Information

### Network Insights Metrics
- **Devices**: Active (status=Active), Online (client logged in), Trusted (meets Trusted Profile requirements)
- **Resources**: Total, Online (in Online Remote Networks), Disconnected (in Offline Remote Networks)
- **Remote Networks**: Total, Online (≥1 online Connector), Offline (no online Connectors)
- **Users by role**: Admin, DevOps, Support, Member counts displayed separately
- **Services**: Count of Service Accounts

### Connection History Graph
- Time ranges: 7, 30, and 90 days
- **7-day view**: Each bar = connections per hour
- **30/90-day view**: Each bar = connections per day
- Displays both successful and failed connections

### Recent Activity
- Shows network traffic across **all** Remote Networks
- Click individual events for details: Resource IP, protocol, connection type, duration

## Prerequisites
- Admin role required to access Network Overview tab
- Connectors must be online for Remote Networks to show as "Online"

## Configuration Values
None — this is a read-only dashboard view with no configurable parameters.

## Gotchas
- A Remote Network is "Offline" if **no** Connectors are online; a single online Connector marks it "Online"
- "Active Devices" (status=Active) differs from "Online Devices" (user logged into client) — these are distinct states
- Connection History only goes back 90 days maximum
- "Disconnected Resources" reflects the state of the Remote Network (offline), not the resource itself

## Related Docs
- Device status and Trusted Profiles
- Remote Networks and Connectors
- Service Accounts
- User roles (Admin, DevOps, Support, Member)
- Connection logs / activity details