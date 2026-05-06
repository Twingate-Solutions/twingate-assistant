# Insights Reports from Network Events

## Page Title
Generating Insights Reports from Network Events

## Summary
The Insights Report is a Jupyter Notebook-based tool that processes Twingate Network Events exports to provide admins with detailed analytics on Resource usage, user activity, errors, and Connector performance. It helps identify misconfigured resources, unused access, connectivity issues, and optimization opportunities. The notebook is customizable for additional insights.

## Key Information
- Output is an `.xlsx` file with multiple tabs covering resources, users, errors, and connectors
- One tab generated per Connector showing time-based activity trends
- Source notebook available in [Twingate's GitHub repository](https://github.com/Twingate)
- Community feedback accepted via subreddit

## Prerequisites
- Network Events Export downloaded from Twingate Admin Console
- Python 3 installed
- Jupyter Notebook installed
- Sufficient RAM to process the Network Events Export file
- Python/dataframe familiarity required only for customization

## Step-by-Step

1. Export Network Events from Admin Console and download locally
2. Install Python 3 and Jupyter Notebook
3. Pull the Jupyter Notebook from Twingate's repository
4. Edit the **second code cell** — set:
   - Full path to the downloaded Network Events report
   - Full path/name for the output `.xlsx` report
5. Run all cells in sequence

## Configuration Values
| Parameter | Location | Description |
|---|---|---|
| Input file path | Second code cell | Full path to downloaded Network Events export |
| Output file path | Second code cell | Full path for generated `.xlsx` report |

## Report Tabs Reference

| Tab | Key Use Case |
|---|---|
| Full Resource List | Active resources, error rates, ports/protocols, TX/RX traffic |
| Resource Matching List | Broad resource definitions, IP-to-resource mapping |
| User Activity Details | Busiest users, bandwidth, error-prone users |
| User IP Details | User connection origins, network diversity |
| General Error Report | Resources with any connection or DNS errors |
| Connection Errors | Intermittent availability issues |
| DNS Errors | Connector DNS resolution failures |
| Connector Activities | Per-connector load, error trends over time |
| Per-Connector Tabs | Daily activity trends, capacity planning |

## Gotchas
- Must configure the **second code cell** specifically — not first or other cells
- RAM requirements scale with export size; large environments may need significant memory
- Cells must be run **in sequence** — out-of-order execution will fail
- Customization requires Python/pandas dataframe knowledge

## Related Docs
- [Network Events Export](https://www.twingate.com/docs/network-events-export)
- Twingate GitHub Repository (notebook source)
- Twingate Subreddit (feedback)