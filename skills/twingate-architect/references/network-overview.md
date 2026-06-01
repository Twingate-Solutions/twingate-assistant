# Network Overview

## Page Title
Network Overview (Twingate Admin Console)

## Summary
The Network Overview tab provides a high-level dashboard for admins to monitor network health, user activity, and connection history. It aggregates device, resource, remote network, and user statistics in one view with drill-down capability.

## Key Information

### Network Insights Metrics
- **Devices**: Active (status=Active), Online (client logged in), Trusted (meets Trusted Profile requirements)
- **Resources**: Total, Online (in online Remote Networks), Disconnected (in offline Remote Networks)
- **Remote Networks**: Total, Online (≥1 online Connector), Offline (no online Connectors)
- **Users by Role**: Admin, DevOps, Support, Member counts displayed separately
- **Services**: Count of Service Accounts

### Connection History
- Time ranges: 7, 30, 90 days
- **7-day graph**: Each bar = connections per **hour**
- **30/90-day graphs**: Each bar = connections per **day**
- Tracks both successful and failed connections

### Recent Activity
- Shows traffic across all Remote Networks
- Click individual events for details: Resource IP, protocol, connection type, duration

## Prerequisites
- Admin role required to access Network Overview tab
- Twingate admin console access

## Step-by-Step
N/A — Read-only dashboard, no configuration required.

## Configuration Values
None — display-only interface.

## Gotchas
- **Online vs. Active devices differ**: "Active" = device status flag; "Online" = user currently logged into client. These are not the same count.
- **Disconnected Resources** are determined by Remote Network Connector status, not the Resource itself — a Resource appears disconnected if its Remote Network has no online Connectors.
- **7-day granularity is hourly**, not daily — bars represent hours, not days (unlike 30/90-day views).
- A Remote Network is "Online" if it has *at least one* online Connector; partial Connector failures may still show network as Online.

## Related Docs
- Device Status / Trusted Profiles documentation
- Remote Networks & Connectors documentation
- Service Accounts documentation
- Role-based access (Admin, DevOps, Support, Member roles)
- Connection logs / activity details