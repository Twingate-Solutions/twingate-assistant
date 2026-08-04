# Network Overview

## Page Title
Network Overview (Twingate Admin Console)

## Summary
The Network Overview tab provides a dashboard snapshot of network health, usage metrics, and activity for admins. It aggregates device status, resource availability, user role counts, and connection history in one view.

## Key Information

- **Access**: Available via the Network Overview tab in the Twingate admin console
- **Purpose**: High-level monitoring and quick drill-down into network activity
- **Data refresh**: Real-time status indicators for devices, resources, and remote networks

## Network Insights Metrics

**Devices**
- `Active Devices` — devices with Active status
- `Online Devices` — devices with a logged-in Twingate Client user
- `Trusted Devices` — devices meeting a Trusted Profile's requirements

**Resources**
- `Resources` — total Resources in Twingate
- `Online Resources` — Resources in Online Remote Networks
- `Disconnected Resources` — Resources in Offline Remote Networks

**Remote Networks**
- `Remote Networks` — total count
- `Online Remote Networks` — networks with ≥1 online Connector
- `Offline Remote Networks` — networks with no online Connectors

**Users and Services**
- Separate counts per role: Admin, DevOps, Support, Reviewer, Billing, Member
- `Services` — total Service Accounts created

## Connection History

- Time ranges: **7 days**, **30 days**, **90 days**
- 7-day graph: each bar = connections per **hour**
- 30/90-day graphs: each bar = connections per **day**
- Tracks both **successful** and **failed** connections

## Recent Activity

- Shows network traffic across **all** Remote Networks
- Click individual events to view:
  - Resource IP address
  - Protocol
  - Connection type
  - Duration

## Gotchas

- A Remote Network is **Offline** if it has **zero** online Connectors — even one online Connector makes it Online
- `Active Devices` ≠ `Online Devices` — Active is a device status flag; Online requires an authenticated Client session
- `Disconnected Resources` reflects Remote Network status, not individual Resource configuration issues
- Connection History granularity changes by time range (hourly vs. daily bars)

## Prerequisites

- Admin role required to access Network Overview tab
- Connectors must be deployed and online for Remote Networks to appear active
- Twingate Client must be installed and users logged in for Online Device counts

## Related Docs

- Device Status / Trusted Profiles
- Remote Networks and Connectors
- Resources configuration
- Service Accounts
- User Roles (Admin, DevOps, Support, Reviewer, Billing, Member)