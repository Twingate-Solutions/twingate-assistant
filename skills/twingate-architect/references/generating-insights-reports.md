# Insights Reports from Network Events

## Page Title
Generating Insights Reports from Network Events

## Summary
The Insights Report is a Jupyter Notebook-based tool that processes Twingate Network Events exports to provide admins with detailed analysis of Resource activity, connection errors, user behavior, and Connector performance. It helps identify misconfigured Resources, unused access, and connectivity issues to support Zero Trust optimization.

## Key Information
- Output format: Excel workbook (`.xlsx`) with multiple named tabs
- Notebook is customizable; functions can be combined for additional insights
- Available via [Twingate GitHub repository](https://github.com/Twingate)
- Report tabs: Full Resource List, Resource Matching List, User Activity Details, User IP Details, General Error Report, Connection Errors, DNS Errors, Connector Activities, per-Connector tabs

## Prerequisites
- Sufficient RAM to process a Network Events Export file
- Python 3 installed
- Jupyter Notebook installed
- Network Events Export downloaded from Admin Console
- Python/dataframe familiarity required only for customization

## Step-by-Step

1. Export Network Events from Twingate Admin Console → download locally
2. Install Python 3 and Jupyter Notebook
3. Pull the Jupyter Notebook from the Twingate repository
4. **Configure second code cell** with:
   - Full path to the downloaded Network Events export
   - Full path/name for the output `.xlsx` report
5. Run all cells in sequence

## Configuration Values
| Parameter | Location | Description |
|-----------|----------|-------------|
| Input file path | Code cell 2 | Full path to Network Events export |
| Output file path | Code cell 2 | Full path for generated `.xlsx` report |

## Report Tab Reference
| Tab | Primary Use Case |
|-----|-----------------|
| Full Resource List | High-traffic resources, error rates, ports/protocols |
| Resource Matching List | Overly broad Resource definitions |
| User Activity Details | Busy users, high-error users |
| User IP Details | User connection origin diversity |
| General Error Report | Resources with any connection/DNS errors |
| Connection Errors | Intermittently unavailable Resources |
| DNS Errors | Connector DNS resolution failures |
| Connector Activities | Per-Connector load and error trends |
| Per-Connector tabs | Time-based activity trends per Connector |

## Gotchas
- RAM requirements scale with export size — large environments may need significant memory
- Must configure the input/output paths in **cell 2 specifically** before running
- Cells must be run **in sequence** — running out of order will cause failures
- The notebook pulls from a live repo; verify compatibility if notebook or dependencies update

## Related Docs
- [Network Events Export](https://www.twingate.com/docs/network-events-export)
- Twingate GitHub repository (notebook source)
- Twingate subreddit (feedback channel)