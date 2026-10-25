---
source: https://www.twingate.com/docs/filtering-analytics
type: docs
fetched: 2026-10-25
source_version: 8c7cdf1d3bc646965f976268486346c812fcfec0ea528637352fa38e0c1f9f8c
trust: official
---

# Filtering Analytics

## Page Title
Filtering Analytics (Twingate DNS Activity Monitoring)

## Summary
Filtering Analytics displays DNS query activity resolved by Twingate across devices, accessible in the Admin Console under **Internet Security > Secure DNS**. It provides charts, ranked lists, and an event log for monitoring DNS filtering behavior. DNS filtering rules are configured separately via the DNS Filtering settings.

## Key Information

- **Location**: Admin Console → Internet Security → Secure DNS → Filtering Analytics tab
- **Time ranges**: 7, 30, or 90 days
- **Filter scope**: All controls apply globally to the selected DNS filtering profile and time range
- Data includes both allowed and blocked DNS events

## Components

| Component | Description |
|---|---|
| **Queries chart** | Total queries, blocked queries, block percentage, time-series plot |
| **Top Block Reasons** | Ranked list of block triggers (denylist entries, security/content categories, privacy rules) |
| **Top Domains** | Ranked by attempt count; toggle Resolved/Blocked; switch to Top Devices via dropdown |
| **Recent DNS Activity** | Event log; filterable by all/blocked; searchable by domain name |

## Event Detail Fields
When selecting a log event:
- Device hostname and IP address
- Filtering profile applied
- Block reason (if blocked)

## Signed-Out Device Behavior
Devices can log DNS activity even when users are signed out (requires "always-on DNS filtering" configuration). Identity shown in logs:
- **Never signed in**: device hostname
- **One prior user**: Twingate device name
- **Multiple prior users**: most recently signed-in Twingate device name

## Prerequisites
- DNS Filtering must be configured (see DNS Filtering docs)
- Devices must be configured for always-on DNS filtering to capture signed-out activity
- Admin Console access

## Gotchas
- Signed-out multi-user devices attribute logs to the **most recent** user's device name, not the current user — can cause attribution confusion on shared/recycled hardware
- Search in Recent DNS Activity applies **within** the currently selected filter (all vs. blocked only), not across both
- "Show More Results" required to see domains beyond the initial top list

## Related Docs
- DNS Filtering (configuration for what gets blocked)
- DNS Filtering profiles
- Always-on DNS filtering device configuration