---
source: https://help.twingate.com/articles/3353935754-connectivity-timeout-issues-when-using-passive-pasv-ftp-mode
type: help
fetched: 2026-08-06
source_version: 198a3144c8a0727afbcc22e78e98bde7ea36a7602644171b85bd39b4434c476a
---

# Connectivity/Timeout Issues with PASSIVE (PASV) FTP Mode

## Page Title
Connectivity/Timeout Issues when using PASSIVE/PASV FTP Mode

## Summary
PASV FTP mode fails through Twingate when only the FTP hostname (FQDN) is defined as a resource. During passive mode negotiation, the FTP server returns its real IP address, which Twingate doesn't intercept since it only monitors the hostname—causing the data connection to bypass Twingate entirely.

## Key Information
- Twingate intercepts traffic by resolving hostnames to internal CGNAT IPs; it does **not** intercept by raw IP unless that IP is explicitly added as a resource
- PASV mode causes the FTP server to return its actual IP (e.g., `1,2,3,4,24,123` → `1.2.3.4`) in the `227` response
- The FTP client then connects directly to that IP, bypassing Twingate's interception
- This results in timeout or connection refusal since the raw IP is unreachable from the client without Twingate routing

## Symptoms
- FTP resource defined by FQDN only
- Initial authentication succeeds; file transfers or directory listings time out
- Error messages:
  - `TLS/SSL connection refused, turning off session resuming and retrying`
  - `425: Failed to establish connection`

## Prerequisites
- Twingate Client installed and connected
- FTP server accessible via a Twingate Connector

## Resolution Options

### Option 1: Add the FTP Server's IP as a Twingate Resource (Recommended)
1. Identify the real IP address of the FTP server (e.g., `1.2.3.4`)
2. In the Twingate Admin Console, add that IP address as an additional resource (or add it to the existing resource definition)
3. Ensure the resource is assigned to the same Remote Network and accessible via the same Connector
4. Test PASV FTP — Twingate will now intercept the data connection IP

### Option 2: Disable Passive Mode on FTP Client
- Switch FTP client to **Active (PORT) mode** instead of PASV
- Active mode does not involve the server returning an IP for the client to connect to, avoiding the bypass issue

## Configuration Values
| Item | Value |
|------|-------|
| Twingate Component | Resource (connection via Client) |
| Platform | Any |
| Protocol | FTP (PASV mode) |
| PASV response format | `227: Entering Passive Mode (o1,o2,o3,o4,p1,p2)` |

## Gotchas
- Defining only the FQDN is **insufficient** for PASV FTP — the IP must also be a resource
- If the FTP server has multiple IPs or uses dynamic IPs, all relevant IPs must be covered as Twingate resources
- This is a fundamental behavior of PASV FTP, not a Twingate bug

## Related Docs
- Twingate Resource configuration (adding IP-based resources)
- Remote Networks and Connector setup