---
source: https://www.twingate.com/docs/filtering-analytics
type: docs
fetched: 2026-09-20
source_version: 770d4a4b128849a2142a2149bd42f4caed361619d570967296114c043a0d7948
---

<!-- triage: unassigned -->

# Filtering Analytics

## Summary
Filtering Analytics displays DNS activity resolved by Twingate for devices, accessible under **Internet Security > Secure DNS** in the Admin Console. It provides query statistics, block reasons, top domains/devices, and a searchable event log. Configuration of what gets blocked is handled separately in DNS Filtering settings.

## Key Information
- Time range options: 7, 30, or 90 days
- Filter data by DNS filtering profile
- Four main components: Queries chart, Top Block Reasons, Top Domains/Devices, Recent DNS Activity
- Block reasons map to specific rules: security categories (e.g., Google Safe Browsing, Typosquatting), content categories, privacy protection rules
- Top Domains toggles between **Resolved** and **Blocked** views
- Top Devices view available via dropdown on the Top Domains component
- Recent DNS Activity log filters: all activity (allowed + blocked) or blocked only; search by domain name

## Prerequisites
- DNS Filtering must be configured to generate data
- Devices must have Twingate Client installed
- For persistent DNS filtering when signed out: device must be [configured to run DNS filtering all of the time](https://www.twingate.com/docs/dns-filtering)

## Configuration Values
None (analytics is read-only; no env vars or API params)

## Signed-Out Device Behavior
| Scenario | Display Name |
|----------|-------------|
| Never signed into Twingate | Device hostname |
| Single user ever on device | Twingate device name |
| Multiple users on device | Most recently signed-in Twingate device name |

## Gotchas
- **Older Client versions** (macOS before `2024.311`, Windows before `2024.351`) show generic info for signed-out devices — may display `"No hostname"` or `"No device"` instead of hostname
- Search in Recent DNS Activity applies **within** the selected filter (all vs. blocked), not across both simultaneously
- Analytics only reflects DNS queries Twingate resolves; queries handled by other resolvers won't appear
- "Top Block Reasons" shows individual denylist entries or rule names, not aggregate categories

## Step-by-Step: Finding Blocked Domain Details
1. Navigate to **Internet Security > Secure DNS > Filtering Analytics**
2. Select DNS filtering profile and time range
3. In **Recent DNS Activity**, set filter to **Blocked**
4. Search for domain name in search box
5. Select an event to view: device hostname, IP address, filtering profile used, block reason

## Related Docs
- [DNS Filtering](https://www.twingate.com/docs/dns-filtering) — configure block rules
- [Security Categories](https://www.twingate.com/docs/dns-filtering) — Google Safe Browsing, Typosquatting, etc.
- Configuring DNS filtering for always-on (signed-out devices)