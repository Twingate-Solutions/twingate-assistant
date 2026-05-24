# Insights Reports from Network Events

## Page Title
Generating Insights Reports from Network Events

## Summary
The Insights Report is a Jupyter Notebook-based tool that processes Twingate Network Events exports to provide admins with deep visibility into Resource activity, connection errors, user behavior, and Connector performance. It helps identify misconfigured Resources, unused access, and user experience issues to support Zero Trust optimization.

## Key Information
- Output is an `.xlsx` file with multiple tabs covering Resources, users, errors, and Connectors
- Notebook is customizable; functions can be combined for additional insights
- Source data comes from the Network Events Export (Admin Console)
- One tab is generated per Connector for time-based trend analysis

## Prerequisites
- System with sufficient RAM to process a Network Events Export
- Python 3 installed
- Jupyter Notebook installed
- Network Events Export downloaded from Admin Console
- Python/dataframes familiarity required only for customization

## Step-by-Step

1. Export Network Events from the Admin Console and download locally
2. Install [Python 3](https://www.python.org/) and [Jupyter Notebook](https://jupyter.org/)
3. Pull the Jupyter Notebook from the [Twingate repository](https://github.com/Twingate)
4. Edit the **second code cell** to set:
   - Full path to the downloaded Network Events Export
   - Output path for the `.xlsx` report
5. Run all cells in sequence

## Report Tabs Reference

| Tab | Key Use Case |
|-----|-------------|
| Full Resource List | Active resources, error rates, ports/protocols, traffic volume |
| Resource Matching List | Broad access detection, FQDN/IP mapping |
| User Activity Details | Per-user connections, bandwidth, error counts |
| User IP Details | User source IPs, network diversity |
| General Error Report | Resources with any connection or DNS error |
| Connection Errors | Addresses with recurring connection failures |
| DNS Errors | Resources failing DNS resolution at Connectors |
| Connector Activities | Per-Connector load, error trends over time |
| Connector Name (per Connector) | Daily activity breakdown, capacity planning |

## Configuration Values
- **Second code cell parameters:**
  - Input: full path to Network Events Export file
  - Output: full path for generated `.xlsx` report

## Gotchas
- Requires sufficient RAM — large Network Events exports can be memory-intensive; no specific minimum is documented
- Must run cells **in sequence** — out-of-order execution will cause failures
- Notebook pulled from repository may need updates if Network Events export schema changes

## Related Docs
- [Network Events Export](https://www.twingate.com/docs/network-events-export)
- Feedback: [Twingate Subreddit](https://www.reddit.com/r/Twingate)