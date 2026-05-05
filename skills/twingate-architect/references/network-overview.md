# Network Overview

## Page Title
Network Overview (Twingate Admin Console)

## Summary
The Network Overview tab provides a dashboard snapshot of network health, usage metrics, and recent activity. Admins can monitor device status, resource availability, user roles, and connection history in one place.

## Key Information

- **Location:** Network Overview tab in Twingate Admin Console
- Displays real-time counts for devices, resources, remote networks, users, and service accounts
- Connection history available for 7, 30, and 90 day windows
- Recent Activity shows traffic across all Remote Networks with drill-down capability

## Network Insights Metrics

**Devices:**
- `Active Devices` — devices with Active status
- `Online Devices` — devices with a logged-in Twingate Client user
- `Trusted Devices` — devices meeting a Trusted Profile's requirements

**Resources:**
- `Resources` — total resources added
- `Online Resources` — resources in Online Remote Networks
- `Disconnected Resources` — resources in Offline Remote Networks

**Remote Networks:**
- `Remote Networks` — total count
- `Online Remote Networks` — networks with ≥1 online Connector
- `Offline Remote Networks` — networks with no online Connectors

**Users & Services:**
- Counts broken out by role: Admin, DevOps, Support, Member
- `Services` — number of Service Accounts created

## Connection History

| Time Range | Bar Resolution |
|---|---|
| 7 days | Per hour |
| 30 days | Per day |
| 90 days | Per day |

- Bars show successful vs. failed connections
- Toggle between 7/30/90 day views

## Recent Activity

- Displays network traffic across **all** Remote Networks
- Click individual events to view:
  - Resource IP address
  - Protocol
  - Connection type
  - Duration

## Gotchas

- A Remote Network is "Online" only if it has **at least one** online Connector — partial Connector failures may still show as Online
- `Disconnected Resources` reflects Remote Network offline status, not individual Resource health
- 7-day graph uses hourly granularity; longer ranges aggregate to daily — spikes may appear smaller in 30/90 day views

## Prerequisites

- Admin role required to access Network Overview tab
- Connectors must be deployed and online for Remote Networks to appear active

## Related Docs

- Device Status / Trusted Profiles
- Remote Networks & Connectors
- Service Accounts
- User Roles (Admin, DevOps, Support, Member)
- Connection Logs / Activity Reports