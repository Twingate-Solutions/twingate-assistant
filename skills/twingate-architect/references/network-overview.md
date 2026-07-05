# Network Overview

## Page Title
Network Overview

## Summary
The Network Overview tab is an admin dashboard providing a high-level snapshot of network health, usage metrics, and recent activity. It consolidates device, resource, remote network, and user statistics in one view, with drill-down capability for detailed event inspection.

## Key Information

- **Network Insights** section displays real-time counts across devices, resources, remote networks, and users/services
- **Connection History** graph covers 7, 30, or 90-day windows; 7-day uses hourly bars, 30/90-day uses daily bars
- **Recent Activity** shows traffic across all Remote Networks with per-event details (Resource IP, protocol, connection type, duration)

## Metrics Reference

### Devices
- `Active Devices` — devices with Active status
- `Online Devices` — devices with a logged-in Twingate Client user
- `Trusted Devices` — devices meeting a Trusted Profile's requirements

### Resources
- `Resources` — total Resources added to Twingate
- `Online Resources` — Resources in Online Remote Networks
- `Disconnected Resources` — Resources in Offline Remote Networks

### Remote Networks
- `Remote Networks` — total created
- `Online Remote Networks` — at least one online Connector present
- `Offline Remote Networks` — no online Connectors

### Users & Services
| Role | Description |
|------|-------------|
| Admin | Admin Role assigned |
| DevOps | DevOps Role assigned |
| Support | Support Role assigned |
| Reviewer | Access Reviewer Role assigned |
| Billing | Billing Role assigned |
| Member | Member Role assigned |
| Services | Service Accounts created |

## Prerequisites
- Admin access to Twingate network console

## Step-by-Step
1. Navigate to the **Network** section in the Twingate Admin Console
2. Select the **Overview** tab
3. Review **Network Insights** for current counts
4. Select time range (7/30/90 days) in **Connection History** to analyze connection trends
5. Click individual events in **Recent Activity** to view Resource IP, protocol, connection type, and duration

## Configuration Values
None — this is a read-only dashboard tab with no configurable parameters.

## Gotchas
- A Remote Network is **Online** only if it has **at least one** online Connector; a single offline Connector does not mark it offline
- `Online Devices` ≠ `Active Devices` — Active status and having a logged-in user are tracked separately
- Connection History bars represent **different time granularities** depending on selected range (hourly for 7-day, daily for 30/90-day)
- `Disconnected Resources` reflects Remote Network state, not individual Resource health

## Related Docs
- Devices and Device Status
- Trusted Profiles
- Remote Networks and Connectors
- Service Accounts
- User Roles and Permissions
- Connection Logs / Activity