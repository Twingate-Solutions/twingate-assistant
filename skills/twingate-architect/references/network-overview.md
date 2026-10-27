---
source: https://www.twingate.com/docs/network-overview
type: docs
fetched: 2026-10-25
source_version: 5f456799f34d1124d2ace4615d458b65040a993ddf3e53ad3b908f4c66099fbe
trust: official
---

# Network Overview

## Page Title
Network Overview (Twingate Admin Console)

## Summary
The Network Overview tab is an admin dashboard providing a high-level snapshot of network health, usage, and activity. It aggregates key metrics across devices, resources, remote networks, users, and connection history in one view.

## Key Information

### Network Insights Metrics
- **Active Devices**: Devices with `Active` status
- **Online Devices**: Devices with a user logged into the Twingate Client
- **Trusted Devices**: Devices meeting a Trusted Profile's requirements
- **Resources**: Total Resources added to Twingate
- **Online Resources**: Resources in Online Remote Networks
- **Disconnected Resources**: Resources in Offline Remote Networks
- **Remote Networks**: Total Remote Networks created
- **Online Remote Networks**: Remote Networks with ≥1 online Connector
- **Offline Remote Networks**: Remote Networks with no online Connectors
- **Users**: Count per role (Admin, Viewer, DevOps, etc.) plus non-admin Members
- **Services**: Total Service Accounts created

### Connection History Graph
- Time ranges: **7 days**, **30 days**, **90 days**
- 7-day view: each bar = connections per **hour**
- 30/90-day view: each bar = connections per **day**
- Tracks both **successful** and **failed** connections

### Recent Activity
- Displays network traffic across all Remote Networks
- Clicking an event reveals: Resource IP address, protocol, connection type, duration

## Prerequisites
- Admin access to the Twingate admin console
- Remote Networks and Connectors configured to see meaningful data

## Gotchas
- A Remote Network is "Offline" if it has **zero** online Connectors — even one online Connector makes it "Online"
- Disconnected Resources reflect Remote Network status, not individual Resource health
- Connection History granularity changes based on selected time range (hourly vs. daily bars)

## Related Docs
- Device status and Trusted Profiles
- Remote Networks and Connectors setup
- User roles and Service Accounts
- Resource configuration