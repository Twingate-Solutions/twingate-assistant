---
source: https://www.twingate.com/docs/network-overview
type: docs
fetched: 2026-08-14
source_version: 895668983e8236b627510419cfee2a99d3d8a7f7225f6d34d81e82a4f037aa2b
---

# Network Overview

## Page Title
Network Overview

## Summary
The Network Overview tab is an admin dashboard providing a high-level snapshot of Twingate network health, including device status, resource availability, user role distribution, and connection history. It enables admins to monitor usage and drill into specific events for detailed traffic analysis.

## Key Information

### Network Insights Metrics
- **Active Devices**: Devices with `Active` status
- **Online Devices**: Devices with a user logged into the Twingate Client
- **Trusted Devices**: Devices meeting Trusted Profile requirements
- **Resources**: Total Resources added to Twingate
- **Online/Disconnected Resources**: Based on Remote Network connector status
- **Online Remote Networks**: Has ≥1 online Connector
- **Offline Remote Networks**: Has 0 online Connectors

### Users and Services Metrics
Counts users by role: Admin, DevOps, Helpdesk, Support, Reviewer (Access Reviewer), Billing, Member
- **Services**: Total Service Accounts created

### Connection History
- Time ranges: 7, 30, or 90 days
- **7-day graph**: Each bar = connections per **hour**
- **30/90-day graphs**: Each bar = connections per **day**
- Displays successful vs. failed connections

### Recent Activity
- Shows network traffic across all Remote Networks
- Clicking an event reveals: Resource IP address, protocol, connection type, duration

## Prerequisites
- Admin role required to access Network Overview tab

## Gotchas
- A Remote Network is **Online** only if it has **at least one** online Connector — a single offline Connector does not make the network offline if others are online
- Resource online/offline status is derived from its Remote Network's Connector status, not the Resource itself
- The 7-day graph granularity is hourly (not daily), which differs from the 30/90-day views — important when interpreting spike patterns

## Configuration Values
None — this is a read-only dashboard with no configurable parameters or API fields documented on this page.

## Related Docs
- Trusted Profiles (for Trusted Devices criteria)
- Remote Networks & Connectors (for online/offline status behavior)
- Service Accounts (for Services count)
- User Roles (Admin, DevOps, Helpdesk, Support, Reviewer, Billing, Member)
- Connection Logs / Activity reporting