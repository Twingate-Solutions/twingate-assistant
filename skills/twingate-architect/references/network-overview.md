# Network Overview

## Page Title
Network Overview

## Summary
The Network Overview tab is an admin dashboard providing a snapshot of network health, usage metrics, and activity. It consolidates device status, resource availability, user roles, and connection history into a single view with drill-down capability.

## Key Information

### Network Insights Metrics
- **Active Devices**: Devices with `Active` status
- **Online Devices**: Devices with a user logged into Twingate Client
- **Trusted Devices**: Devices meeting Trusted Profile requirements
- **Resources**: Total Resources added to Twingate
- **Online Resources**: Resources in Online Remote Networks
- **Disconnected Resources**: Resources in Offline Remote Networks
- **Remote Networks**: Total Remote Networks created
- **Online Remote Networks**: Networks with ≥1 online Connector
- **Offline Remote Networks**: Networks with no online Connectors

### User Role Counts
Tracks counts for: Admin, DevOps, Support, Reviewer (Access Reviewer), Billing, Member roles, and Service Accounts

### Connection History
- Time ranges: 7, 30, and 90 days
- **7-day graph**: Each bar = connections per **hour**
- **30/90-day graphs**: Each bar = connections per **day**
- Distinguishes successful vs. failed connections

### Recent Activity
- Shows network traffic across all Remote Networks
- Clicking an event reveals: Resource IP address, protocol, connection type, duration

## Prerequisites
- Admin role required to access Network Overview tab

## Gotchas
- **Online vs. Active Devices**: "Active" and "Online" are distinct statuses — a device can be Active without a user logged in
- **Disconnected Resources** ≠ deleted; they exist in Offline Remote Networks (no Connectors online)
- A Remote Network is only "Online" if at least one Connector is online — a single offline Connector does not make the network offline
- Connection History granularity changes by time range (hourly vs. daily bars)

## Configuration Values
None — this is a read-only dashboard view with no configurable parameters.

## Related Docs
- Devices and Device Status
- Trusted Profiles
- Remote Networks and Connectors
- Resources
- User Roles
- Service Accounts
- Access Logs / Connection History