# Insights Reports from Network Events

## Page Title
Generating Insights Reports from Network Events

## Summary
Twingate's Insights Report is a Jupyter Notebook-based tool that processes Network Events Export data to provide admins with detailed analysis of Resource activity, user connections, and network errors. It helps identify misconfigured Resources, high-traffic patterns, unused Resources, and connectivity issues to support Zero Trust optimization.

## Key Information
- Output format: Excel (`.xlsx`) with multiple tabs
- Processing tool: Python/Jupyter Notebook
- Input: Network Events Export from Admin Console
- Notebook is customizable; functions can be combined for additional insights
- One tab generated per Connector showing time-based activity trends

## Prerequisites
- Sufficient RAM to process Network Events Export file
- Python 3 installed
- Jupyter Notebook installed
- Network Events Export downloaded from Admin Console
- Python/dataframe familiarity required only for customization

## Step-by-Step

1. Export Network Events from Admin Console → download locally ([Network Events Export](https://www.twingate.com/docs/network-events-export))
2. Install [Python 3](https://python.org) and [Jupyter Notebook](https://jupyter.org)
3. Clone/pull the Jupyter Notebook from [Twingate's repository](https://github.com/Twingate)
4. Edit the **second code cell** to set:
   - Full path to the downloaded Network Events Export file
   - Full path/name for the output `.xlsx` report
5. Run all cells in sequence

## Configuration Values
| Parameter | Location | Description |
|-----------|----------|-------------|
| Input file path | Second code cell | Full path to Network Events Export |
| Output file path | Second code cell | Full path for generated `.xlsx` report |

## Report Tabs Reference
| Tab | Key Use Case |
|-----|-------------|
| Full Resource List | Active resources, errors, ports/protocols, traffic |
| Resource Matching List | Broad access detection, IP-to-resource mapping |
| User Activity Details | Busy users, high-bandwidth users, error-prone users |
| User IP Details | User connection origins, network diversity |
| General Error Report | Resources with any connection or DNS error |
| Connection Errors | Intermittent unavailability, failure points |
| DNS Errors | DNS resolution failures per resource |
| Connector Activities | Per-connector load, error rates, trends |
| Connector `<Name>` | Per-connector daily activity trends (one tab each) |

## Gotchas
- RAM requirements scale with the size of the Network Events Export — large environments may require significant memory
- The second code cell must be configured **before** running; missing this step will cause path errors
- One tab is created per Connector — large deployments produce many tabs
- Notebook must be run **in sequence** (cell order matters)

## Related Docs
- [Network Events Export](https://www.twingate.com/docs/network-events-export)
- Twingate Subreddit (feedback channel)
- Twingate GitHub Repository (notebook source)