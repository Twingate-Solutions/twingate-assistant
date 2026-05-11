# Network Overview

## Page Title
Twingate Network Overview

## Summary
The Network Overview tab provides admins a dashboard snapshot of network health, usage metrics, and recent activity. It aggregates device, resource, remote network, and user counts alongside connection history and traffic logs.

## Key Information

- **Network Insights** displays real-time counts across six categories: Devices, Resources, Remote Networks, and Users/Services
- **Connection History** graph covers 7, 30, or 90-day windows; 7-day uses hourly bars, 30/90-day use daily bars
- **Recent Activity** shows traffic across all Remote Networks with drilldown for IP, protocol, connection type, and duration

## Metrics Reference

### Devices
| Metric | Definition |
|--------|------------|
| Active Devices | Devices with status = Active |
| Online Devices | Devices with a logged-in Twingate Client user |
| Trusted Devices | Devices meeting a Trusted Profile's requirements |

### Resources
| Metric | Definition |
|--------|------------|
| Resources | Total Resources added to Twingate |
| Online Resources | Resources in Online Remote Networks |
| Disconnected Resources | Resources in Offline Remote Networks |

### Remote Networks
| Metric | Definition |
|--------|------------|
| Remote Networks | Total created |
| Online Remote Networks | At least one online Connector present |
| Offline Remote Networks | No online Connectors |

### Users & Services
| Metric | Definition |
|--------|------------|
| Admin/DevOps/Support/Member Users | Count per role |
| Services | Total Service Accounts created |

## Prerequisites
- Admin role required to access Network Overview tab
- Remote Networks and Connectors must be configured for meaningful resource/network metrics

## Step-by-Step: Investigating Connection Issues
1. Navigate to **Network Overview** tab in Admin console
2. Check **Offline Remote Networks** count — indicates Connectors are down
3. Review **Connection History** graph for spike in failed connections
4. Select time range (7/30/90 days) to scope investigation
5. Scroll to **Recent Activity**, click a failed event for details (IP, protocol, connection type, duration)

## Gotchas
- A Remote Network is **Online** only if *at least one* Connector is online — multiple Connectors required for true HA
- **Active Devices** ≠ **Online Devices**: Active is a status flag; Online requires an authenticated Client session
- Connection History bars represent different time resolutions depending on selected range (hourly vs. daily)
- Recent Activity reflects all Remote Networks aggregated — no per-network filtering shown on this page

## Related Docs
- Device Status and Trusted Profiles
- Remote Networks and Connectors
- Resources configuration
- Service Accounts
- User Roles (Admin, DevOps, Support, Member)