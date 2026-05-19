# Network Overview

## Page Title
Network Overview (Twingate Admin Console)

## Summary
The Network Overview tab provides a dashboard snapshot of your Twingate network's current state, including device counts, resource status, user roles, and connection history. It serves as an entry point for admins to monitor usage and drill down into specific activity details.

## Key Information

**Network Insights Metrics:**
- **Devices:** Active (status=Active), Online (client logged in), Trusted (meet Trusted Profile requirements)
- **Resources:** Total, Online (in Online Remote Networks), Disconnected (in Offline Remote Networks)
- **Remote Networks:** Total, Online (≥1 online Connector), Offline (no online Connectors)
- **Users by Role:** Admin, DevOps, Support, Member counts displayed separately
- **Services:** Total Service Account count

**Connection History Graph:**
- Time ranges: 7, 30, 90 days
- 7-day view: bars = per-hour connection counts
- 30/90-day views: bars = per-day connection counts
- Tracks successful vs. failed connections separately

**Recent Activity:**
- Shows network traffic across all Remote Networks
- Click individual events for details: Resource IP, protocol, connection type, duration

## Prerequisites
- Admin role access to Twingate Admin Console
- Existing network configuration (Remote Networks, Connectors, Resources) to populate metrics

## Step-by-Step
1. Navigate to the **Network Overview** tab in the Twingate Admin Console
2. Review **Network Insights** cards for high-level counts
3. Select connection history timeframe (7/30/90 days) to view trend data
4. Click individual entries in **Recent Activity** to inspect connection details

## Configuration Values
None — this is a read-only dashboard tab with no configurable parameters.

## Gotchas
- A Remote Network is **Online** only if it has **at least one** online Connector; any Remote Network with zero online Connectors shows as Offline
- Resources inherit online/offline status from their parent Remote Network, not from individual health checks
- Connection history granularity differs by timeframe (hourly vs. daily) — don't conflate bar heights across views
- "Active Devices" and "Online Devices" are distinct: Active refers to device status flag; Online requires an active user session in the client

## Related Docs
- Devices and Device Status
- Trusted Profiles
- Remote Networks and Connectors
- Service Accounts
- Connection Logs / Activity Logs