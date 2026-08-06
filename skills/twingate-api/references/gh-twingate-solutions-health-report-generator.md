---
source: https://github.com/Twingate-Solutions/health-report-generator
type: github
fetched: 2026-08-06
source_version: 8fa4ae54c8b5f4639bf2c615a950b9427b01bab1
---

<!-- triage: unassigned -->

# Twingate Health Report Generator

## Summary
A Python notebook that generates insights and health reports from Twingate Network Events exports. It analyzes resource usage, user activity, connector health, and network topology to surface operational questions about a Twingate deployment.

## Key Information
- Language: Python (Jupyter Notebook)
- Input: Twingate Network Events export data
- Output: Insights reports covering resources, users, connectors, and remote networks
- Repo: `Twingate-Solutions/health-report-generator`

## Prerequisites
- Python environment with Jupyter Notebook support
- Twingate Network Events export file (CSV or equivalent)
- Standard Python data analysis libraries (likely pandas, matplotlib — check `requirements.txt` or notebook imports)

## Usage / Step-by-Step
1. Export Network Events from the Twingate Admin Console
2. Clone the repository:
   ```bash
   git clone https://github.com/Twingate-Solutions/health-report-generator
   ```
3. Install dependencies (check notebook or repo for `requirements.txt`)
4. Open the Jupyter notebook
5. Point the notebook at your Network Events export file
6. Run all cells to generate the report

## Configuration Values
- **Input file path**: Set within the notebook to reference the Network Events export
- No documented environment variables or CLI flags in the README; check notebook cells for configurable parameters

## Report Coverage Areas
| Category | Examples |
|---|---|
| Resources | Most active, most errors, unused, highest traffic, ambiguous definitions |
| Services | Ports, protocols, addresses served by multiple resources/networks |
| Users | Busiest by connections/bandwidth, most errors, source networks |
| Connectors | Redundancy gaps, load imbalance, error correlation, seasonality |
| Remote Networks | Missing redundancy, candidates for additional connectors |

## Gotchas
- Report quality depends entirely on the completeness and time range of the exported Network Events data; sparse exports will produce limited insights
- Network Events exports may have retention or volume limits in Twingate — ensure the export covers a meaningful time window
- No live API integration mentioned; this is a static export analysis tool, not real-time
- Notebook-based tooling means output is not automatically scheduled or alerting — manual re-run required for fresh reports

## Related Docs
- [Twingate Network Events documentation](https://www.twingate.com/docs/network-events)
- [Twingate Admin Console](https://www.twingate.com/docs/administration)
- Twingate-Solutions GitHub org for other operational utilities