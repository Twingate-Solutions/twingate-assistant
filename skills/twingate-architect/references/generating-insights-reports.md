---
source: https://www.twingate.com/docs/generating-insights-reports
type: docs
fetched: 2026-08-14
source_version: 6fbb9b71cb740649215aafc4c7fca1224745647df1bb226cae889a9eecf9abe1
---

# Insights Reports from Network Events

## Page Title
Generating Insights Reports from Network Events

## Summary
The Insights Report is a Jupyter Notebook-based tool that processes Twingate Network Events exports to provide admins with detailed analysis of Resource activity, connection errors, user behavior, and Connector performance. It helps identify misconfigured Resources, unused access, and connectivity issues to support Zero Trust optimization and troubleshooting.

## Key Information
- Output is an `.xlsx` file with multiple tabs covering Resources, users, errors, and Connectors
- Notebook is customizable; functions can be combined for additional insights
- One Connector-specific tab is generated per existing Connector
- Report helps identify overly broad Resource definitions, unused Resources, and over/under-provisioned Remote Networks

## Prerequisites
- Twingate Admin Console access to export Network Events
- System with sufficient RAM to process the Network Events Export file
- Python 3 installed
- Jupyter Notebook installed
- Python/dataframe familiarity required only for customization

## Step-by-Step

1. Export Network Events from Admin Console and download locally
2. Install [Python 3](https://python.org) and [Jupyter Notebook](https://jupyter.org)
3. Pull the Jupyter Notebook from [Twingate's repository](https://github.com/Twingate)
4. Edit the second code cell to set:
   - Full path to the downloaded Network Events export
   - Full path/name for the output `.xlsx` report
5. Run all cells in sequence

## Report Tabs & Content

| Tab | Key Insights |
|-----|-------------|
| Full Resource List | Active resources, error rates, TX/RX, ports/protocols, duplicate address detection |
| Resource Matching List | Broad access patterns, FQDN/IP-to-address mapping |
| User Activity Details | High-bandwidth users, users with most errors |
| User IP Details | User connection origins, network diversity |
| General Error Report | Resources with any connection or DNS errors |
| Connection Errors | Intermittently unreachable Resources |
| DNS Errors | DNS resolution failures per address |
| Connector Activities | Per-Connector load, error trends over time |
| Per-Connector Tabs | Daily activity trends, capacity planning |

## Configuration Values
- **Cell 2 parameters**: Input file path (Network Events export), output file path (`.xlsx`)

## Gotchas
- RAM requirements are not specified — large exports may require significant memory; size accordingly
- Must run cells **in sequence** — skipping cells will cause failures
- No built-in scheduling; must be re-run manually after each export
- Customization requires Python/pandas dataframe knowledge

## Related Docs
- [Network Events Export](https://www.twingate.com/docs/network-events-export)
- Twingate subreddit (feedback channel)