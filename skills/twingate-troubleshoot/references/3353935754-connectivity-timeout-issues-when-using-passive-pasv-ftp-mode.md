---
source: https://help.twingate.com/articles/3353935754-connectivity-timeout-issues-when-using-passive-pasv-ftp-mode
type: help
fetched: 2026-09-06
source_version: 0003a0df52b1d9ad70f11a028b11b1e678753e3419f7a7fb8a61e88c3da89c89
---

# Connectivity/Timeout Issues with PASSIVE (PASV) FTP Mode

## Summary
PASV FTP mode fails through Twingate when only the FTP hostname is defined as a resource. The FTP server returns its actual IP in the PASV response, and Twingate doesn't intercept traffic to that raw IP, causing the data connection to fail.

## Key Information
- Affects PASV/passive mode FTP only; initial authentication succeeds but transfers fail
- Root cause: Twingate intercepts by hostname/DNS, but PASV mode bypasses DNS by returning a raw IP in the `227` response
- The FTP client then connects directly to that IP, which Twingate ignores, resulting in an unreachable host
- Twingate replaces DNS responses with CGNAT IPs to proxy traffic — this mechanism doesn't apply to IPs embedded in FTP protocol responses

## Symptoms
- FTP resource defined by FQDN only
- Authentication completes successfully
- Data transfers time out
- Error messages:
  - `TLS/SSL connection refused, turning off session resuming and retrying`
  - `425: Failed to establish connection`

## Resolution (Two Options)

### Option 1: Add the FTP Server's IP as a Twingate Resource (Recommended)
1. Identify the actual IP of the FTP server (e.g., `1.2.3.4` from the `227` PASV response)
2. Add that IP address as a separate Twingate resource in your network
3. Twingate will then intercept the PASV data connection to that IP via the Connector

### Option 2: Disable Passive Mode
- Configure the FTP client to use **active mode** instead of passive mode
- Not always feasible depending on firewall/NAT constraints on the client side

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Resource type to add | IP address of FTP server |
| Protocol | FTP (port 21 + data ports as needed) |

## Gotchas
- Adding only the FQDN is insufficient — **both** the hostname and the IP must be Twingate resources if using PASV mode
- The `227` PASV response encodes the IP as comma-separated octets: `(1,2,3,4,24,123)` = IP `1.2.3.4`, ports derived from last two numbers
- Active mode may be blocked by firewalls/NAT on the client side, making IP resource addition the more practical fix
- This issue applies regardless of platform (Windows, macOS, Linux, etc.)

## Related Docs
- Twingate Resource configuration
- Twingate Connector setup
- DNS interception behavior (CGNAT routing)