---
source: https://github.com/Twingate-Solutions/network-utilities
type: github
fetched: 2026-08-06
source_version: 2981e82635f81fe203c764f961b7c9031bd846fc
---

<!-- triage: unassigned -->

# Twingate-Solutions/network-utilities

## Summary
A collection of shell and Python scripts for network troubleshooting in Twingate environments. Scripts assist with diagnosing connectivity issues, DNS resolution, and network path analysis. Intended for use by Twingate administrators and support engineers.

## Key Information
- Repository contains multiple standalone utility scripts
- Scripts cover DNS lookups, connectivity checks, traceroute-style analysis, and Twingate-specific diagnostics
- Mix of shell (bash) and Python scripts
- No single unified CLI; each script is run independently
- Primarily diagnostic/read-only tooling; does not modify network configuration

## Prerequisites
- Linux or macOS (most scripts)
- `bash` 4.x+ or `python3`
- Standard network tools: `curl`, `dig`, `ping`, `traceroute`, `nslookup`
- Python dependencies vary per script (check individual script headers)
- Twingate Client must be installed and authenticated where Twingate-specific checks are performed
- Appropriate network access to the targets being tested

## Usage / Step-by-Step

1. **Clone the repository**
   ```bash
   git clone https://github.com/Twingate-Solutions/network-utilities.git
   cd network-utilities
   ```

2. **Make scripts executable**
   ```bash
   chmod +x <script-name>.sh
   ```

3. **Run a script directly**
   ```bash
   ./<script-name>.sh [options]
   # or
   python3 <script-name>.py [options]
   ```

4. **Review output** — scripts print results to stdout; redirect to a file for sharing with support:
   ```bash
   ./<script-name>.sh > results.txt 2>&1
   ```

## Configuration Values

| Parameter / Variable | Description |
|---|---|
| Target hostname/IP | Passed as a positional argument to most scripts |
| Port | Specified inline or as an argument where TCP checks are performed |
| Twingate network name | Required by Twingate-specific scripts (e.g., `<account>.twingate.com`) |
| DNS server | Some scripts accept an explicit resolver address |

*(No persistent config file; values are passed at runtime.)*

## Gotchas
- Scripts assume standard system tools are in `$PATH`; missing tools will cause silent failures or misleading errors
- Some checks require `sudo` (raw socket operations, certain `traceroute` modes)
- DNS results may differ depending on whether the Twingate Client is active — run both with and without the client to compare
- Python scripts may require specific versions of libraries not installed by default; no `requirements.txt` is provided in all cases
- Output is not structured (JSON/CSV); parsing programmatically requires manual effort
- Scripts are diagnostic only — they do not log results centrally or integrate with monitoring systems

## Related Docs
- [Twingate Documentation](https://www.twingate.com/docs/)
- [Twingate Client Troubleshooting](https://www.twingate.com/docs/troubleshooting)
- [Twingate Support](https://support.twingate.com/)