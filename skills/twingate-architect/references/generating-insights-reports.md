## Insights Reports from Network Events

A Jupyter Notebook (Python) that generates multi-tab Excel reports from a Twingate Network Events Export. Admins use it to identify overly broad Resources, unused Resources, high-traffic connections, users with errors, and per-Connector activity trends. The notebook is hosted in the Twingate repository and can be customized.

**Key Information**
- Input: Network Events Export downloaded from Admin Console
- Output: multi-tab `.xlsx` report
- Requires: Python 3, Jupyter Notebook, enough RAM to load the full export
- Report tabs and their purpose:
  - **Full Resource List**: all addresses connected to; total connections, errors, failure rate, TX/RX, ports/protocols
  - **Resource Matching List**: maps Resource definitions (FQDN/IP) to actual connected IPs -- identifies overly broad access
  - **User Activity Details**: per-user connections, errors, bandwidth
  - **User IP Details**: all public IPs each user has connected from
  - **General Error Report**: Resources with any connection or DNS error
  - **Connection Errors**: addresses with connection errors and occurrence count
  - **DNS Errors**: addresses with DNS resolution failures
  - **Connector Activities**: per-Connector connections (total, successful, errored) and DNS errors
  - **Per-Connector tabs**: Connector activity broken down by day for trend analysis

**Prerequisites**
- Network Events Export from Twingate Admin Console
- Python 3 and Jupyter Notebook installed
- Familiarity with Python and dataframes for customization

**Step-by-Step**
1. Export Network Events from Admin Console and download locally
2. Install Python 3 and Jupyter Notebook
3. Pull the Jupyter Notebook from the Twingate repository
4. In the second code cell, set the path to the downloaded export and the output xlsx file path
5. Run all cells in sequence

**Gotchas**
- Requires sufficient RAM to load the full Network Events Export in memory -- large exports may need a machine with 8GB+ RAM
- The notebook can be customized; functions can be combined for additional insights not covered by default tabs

**Related Docs**
- /docs/network-events-ac-export
- /docs/exporting-network-traffic
- /docs/analytics
- /docs/audit-logs
