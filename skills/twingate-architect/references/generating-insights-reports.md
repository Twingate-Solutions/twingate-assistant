# Insights Reports from Network Events

## Page Title
Generating Insights Reports from Network Events

## Summary
The Insights Report is a Jupyter Notebook-based tool that processes Twingate Network Events exports to provide admins with detailed visibility into Resource activity, user connections, and network errors. It helps identify misconfigurations, unused Resources, high-traffic patterns, and connectivity issues to support Zero Trust permission modeling and environment optimization.

## Key Information
- Output is an `.xlsx` file with multiple tabs covering Resources, users, errors, and Connector activity
- Notebook is customizable; functions can be combined for additional insights
- Report is generated locally — requires sufficient RAM to process large Network Events exports
- Community feedback accepted via Twingate subreddit

## Prerequisites
- Downloaded **Network Events Export** from Twingate Admin Console
- **Python 3** installed
- **Jupyter Notebook** installed
- System RAM sufficient to process the export file
- Python/dataframe familiarity required only for customization

## Step-by-Step

1. Export Network Events from Admin Console and download locally
2. Install Python 3 and Jupyter Notebook
3. Pull the Jupyter Notebook from [Twingate's repository](https://www.twingate.com/docs/generating-insights-reports)
4. Configure the **second code cell** with:
   - Full path to the downloaded Network Events export
   - Full path for the output `.xlsx` report
5. Run all cells in sequence

## Configuration Values
| Parameter | Location | Description |
|-----------|----------|-------------|
| Input file path | Second code cell | Full path to Network Events export |
| Output file path | Second code cell | Full path for generated `.xlsx` report |

## Report Tabs Reference
| Tab | Key Use Case |
|-----|-------------|
| Full Resource List | Active resources, error rates, ports/protocols, traffic |
| Resource Matching List | Broad access detection, IP-to-resource mapping |
| User Activity Details | Per-user connections, bandwidth, errors |
| User IP Details | User source IPs, network diversity |
| General Error Report | Resources with any connection/DNS errors |
| Connection Errors | Per-address connection failure counts |
| DNS Errors | DNS resolution failures per address |
| Connector Activities | Per-Connector load, errors, DNS errors over time |
| Connector Name (per connector) | Daily activity trends, capacity planning |

## Gotchas
- The **second code cell** must be configured before running — paths are not auto-detected
- RAM requirements scale with export size; large exports may fail on low-memory systems
- One tab is generated **per Connector** — large deployments produce many tabs
- Notebook must be run **in sequence** (cells are order-dependent)

## Related Docs
- [Network Events Export](https://www.twingate.com/docs/network-events-export)
- Twingate GitHub repository (notebook source)
- Twingate subreddit (feedback)