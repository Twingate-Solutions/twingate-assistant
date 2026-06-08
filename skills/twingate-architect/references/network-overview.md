# Network Overview

## Page Title
Network Overview (Twingate Admin Console)

## Summary
The Network Overview tab is an admin dashboard providing a high-level snapshot of network health, usage metrics, and recent activity. It aggregates device, resource, remote network, and user statistics in one view, with drill-down capability for individual events.

## Key Information

**Network Insights Metrics:**
- **Devices:** Active (status=Active), Online (user logged in), Trusted (meets Trusted Profile requirements)
- **Resources:** Total, Online (in Online Remote Networks), Disconnected (in Offline Remote Networks)
- **Remote Networks:** Total, Online (≥1 Connector online), Offline (no Connectors online)
- **Users by Role:** Admin, DevOps, Support, Member counts displayed separately
- **Services:** Count of Service Accounts

**Connection History Graph:**
- Time ranges: 7, 30, 90 days
- 7-day view: each bar = 1 hour of connections
- 30/90-day view: each bar = 1 day of connections
- Displays successful vs. failed connections distinctly

**Recent Activity:**
- Shows network traffic across all Remote Networks
- Clicking an event reveals: Resource IP address, protocol, connection type, duration

## Prerequisites
- Admin role required to access the Network Overview tab

## Step-by-Step
1. Log into the Twingate Admin Console
2. Navigate to the **Network Overview** tab
3. Review Network Insights tiles for current counts
4. Select Connection History time range (7/30/90 days) to view trends
5. Scroll to Recent Activity; click individual events for connection details

## Configuration Values
None — this is a read-only dashboard; no configurable parameters.

## Gotchas
- **Online vs. Active Devices:** "Online" requires a logged-in user; "Active" is a device status — these are distinct counts
- **Resource status is derived from Remote Network status:** A Resource is "Disconnected" if its Remote Network has no online Connectors, not based on the Resource itself
- **Remote Network online threshold:** Only one Connector needs to be online for a Remote Network to count as "Online"
- **7-day graph granularity is hourly** — do not compare bar heights directly between 7-day and 30/90-day views

## Related Docs
- Devices and Device Status
- Trusted Profiles
- Remote Networks and Connectors
- Service Accounts
- User Roles (Admin, DevOps, Support, Member)
- Connection Logs / Activity