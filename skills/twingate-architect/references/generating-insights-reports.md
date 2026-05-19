# Insights Reports from Network Events

## Page Title
Generating Insights Reports from Network Events

## Summary
The Insights Report is a Jupyter Notebook-based tool that processes Twingate Network Events exports to provide admins with detailed visibility into Resource activity, user behavior, connectivity errors, and Connector performance. It helps identify misconfigurations, unused Resources, and optimization opportunities toward Zero Trust posture.

## Key Information
- Output format: Excel (`.xlsx`) with multiple tabs
- Notebook is customizable; functions can be combined for additional analysis
- Hosted in [Twingate's GitHub repository](https://github.com/Twingate)
- Report tabs: Full Resource List, Resource Matching List, User Activity Details, User IP Details, General Error Report, Connection Errors, DNS Errors, Connector Activities, per-Connector tabs

## Prerequisites
- Sufficient RAM to process a Network Events Export file
- Python 3 installed
- Jupyter Notebook installed
- Network Events Export downloaded from Admin Console
- Python/dataframe familiarity required only for customization

## Step-by-Step

1. Export Network Events from Twingate Admin Console → download locally
2. Install [Python 3](https://www.python.org/) and [Jupyter Notebook](https://jupyter.org/)
3. Clone/pull the Jupyter Notebook from the Twingate repository
4. Edit the **second code cell**: set full path to the downloaded Network Events export and the desired output `.xlsx` path
5. Run all cells sequentially

## Configuration Values
| Parameter | Location | Description |
|---|---|---|
| Input file path | Second code cell | Full path to Network Events export file |
| Output file path | Second code cell | Full path for generated `.xlsx` report |

## Report Tab Reference
| Tab | Primary Use Case |
|---|---|
| Full Resource List | Active resources, errors, ports/protocols, traffic |
| Resource Matching List | Overly broad resource definitions, IP mapping |
| User Activity Details | Per-user connections, bandwidth, errors |
| User IP Details | User source IPs, network diversity |
| General Error Report | Resources with any connection/DNS errors |
| Connection Errors | Per-address connection failure counts |
| DNS Errors | DNS resolution failures per address |
| Connector Activities | Per-Connector load, errors, DNS errors |
| Per-Connector tabs | Daily trend analysis per Connector |

## Gotchas
- RAM is a constraint — large Network Events exports may require significant memory; plan accordingly
- Cells must be run **in sequence**; out-of-order execution will fail
- No built-in scheduling — this is a manual, on-demand process
- Customization requires Python/pandas dataframe knowledge

## Related Docs
- [Network Events Export](https://www.twingate.com/docs/network-events-export)
- Twingate Subreddit (for feedback on missing insights)