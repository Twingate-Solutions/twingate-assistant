---
source: https://www.twingate.com/docs/ai-services
type: docs
fetched: 2026-09-20
source_version: dcb175d3f213bf53cf20109647dae4be0822100120f8b46b1c4791e7226b680d
---

# AI Usage Overview

## Page Title
AI Usage Overview (Twingate Internet Security / Secure DNS)

## Summary
Tracks AI service usage across devices using DNS query data already collected by DNS filtering. Provides visibility into which AI tools employees use, usage trends, and device spread. Accessible in Admin Console under **Internet Security > Secure DNS**.

## Key Information
- Data source: DNS queries resolved by Twingate (blocked queries are **not** counted)
- Tracks general-purpose AI assistants (ChatGPT, Claude) and AI-native tools (Granola, Cursor)
- Does **not** track AI features added to existing products (e.g., Copilot in Office 365)
- Device counting uses Twingate device ID; Machine Key devices disambiguated by hostname
- AI service taxonomy is a maintained list—recently launched services may be missing

## Prerequisites
- DNS filtering must be configured and active
- Clients should be configured to always run Internet Security (recommended: deploy Machine Key for coverage when users are signed out)
- See: *Internet Security Client Configuration*

## Controls
| Control | Options |
|---|---|
| Time range | 7, 30, or 90 days |
| Metric toggle | Queries (total DNS queries) or Devices (unique devices) |
| Profile scope | Filter by specific DNS filtering profile |

## UI Components
- **AI Usage by Date**: Daily chart of AI activity
- **AI Exposure**: Half-donut showing AI DNS activity as % of all DNS activity
- **Top AI Services**: Ranked list; hover for category, days active, % of AI traffic; expand for matched domains

## AI Usage Summary Report
Generated via **Generate Report** button. One row per device+service combination.

| Column | Description |
|---|---|
| `device_id` | Twingate device ID or hostname (Machine Key) |
| `device_name` | Human-readable name |
| `ai_service` | Canonical name (e.g., "OpenAI ChatGPT") |
| `category` | Service category |
| `total_requests` | DNS request count in window |
| `days_active` | Distinct days with ≥1 request |
| `first_seen` / `last_seen` | Timestamps of first/last request |
| `top_10_domains` | Up to 10 most-requested domains |

## Gotchas
- **Blocked queries excluded**: DNS requests blocked by filtering rules don't appear in counts
- **Device ≠ User**: Device counts are not precise user counts; Machine Key devices may share IDs
- **High query count ≠ heavy usage**: Background app DNS requests count equally with deliberate use
- **Coverage gaps**: Only traffic Twingate resolved is visible; users not running the Client are invisible
- **Domain changes**: If an AI service migrates domains, undercounting occurs until taxonomy is updated
- **AI features in existing products** (e.g., GitHub Copilot within GitHub): not tracked

## Common Uses
- Audit/compliance reporting on AI tool usage
- Identify consolidation candidates (multiple services in same category)
- Cross-reference with procurement/license records
- Verify DNS filtering rules cover expected domains
- Identify specific devices for follow-up via Summary Report

## Related Docs
- Internet Security Client Configuration
- Full tracked AI services list (available in-console via "View the full list with usage definitions")