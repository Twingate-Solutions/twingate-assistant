---
source: https://help.twingate.com/articles/3353935754-connectivity-timeout-issues-when-using-passive-pasv-ftp-mode
type: help
fetched: 2026-11-01
source_version: 473823b256f5948e59295609d3491a3a484f3c5fd9723f73e60a88e315af1f60
trust: official
---

# Connectivity/Timeout Issues with PASSIVE (PASV) FTP Mode

## Summary
PASV FTP connections fail through Twingate when the resource is defined by hostname only. The FTP server returns its real IP in the PASV response, and Twingate does not intercept traffic to that IP — only to the resolved hostname — causing the data connection to fail.

## Key Information
- Affects PASV/passive FTP mode only; initial authentication (control channel) succeeds
- Twingate intercepts traffic by resolving the hostname to a CGNAT IP; it does not automatically cover the server's raw IP
- The FTP `227 Entering Passive Mode` response embeds the server's actual IP (e.g., `1,2,3,4,24,123`), which the FTP client then tries to reach directly, bypassing Twingate

## Symptoms
- FTP resource defined by FQDN only
- Authentication completes, but file transfers or directory listings time out
- Error messages:
  - `TLS/SSL connection refused, turning off session resuming and retrying.`
  - `425: Failed to establish connection.`

## Prerequisites
- FTP server already added as a Twingate Resource (by hostname)
- Access to Twingate Admin Console to add/modify Resources

## Resolution (Two Options)

**Option 1 — Add the FTP server's IP as a Twingate Resource (recommended)**
1. Identify the actual IP address of the FTP server (e.g., `1.2.3.4`)
2. In the Twingate Admin Console, add the IP address as an additional Resource on the same network/Connector
3. Ensure the Resource covers the IP and relevant port range used for PASV data connections
4. Test PASV FTP — Twingate will now intercept the data channel connection to the raw IP

**Option 2 — Disable passive mode on the FTP client**
- Switch the FTP client to active (PORT) mode, which does not redirect the client to a separate IP/port returned by the server

## Configuration Values
| Parameter | Value |
|---|---|
| Resource type to add | IP address of FTP server |
| Ports to cover | Control: `21`; PASV data ports (range defined by FTP server config, commonly `1024–65535` or a restricted range) |

## Gotchas
- Defining the FTP server by hostname alone is insufficient for PASV mode — the IP **must** be separately added
- If the FTP server's PASV port range is not included in the Resource definition, data connections may still fail
- Active (PORT) mode FTP has its own NAT/firewall considerations and may not work in all environments

## Related Docs
- Twingate Resource configuration (Admin Console)
- Twingate CGNAT IP behavior and DNS interception