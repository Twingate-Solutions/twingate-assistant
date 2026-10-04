---
source: https://help.twingate.com/articles/3353935754-connectivity-timeout-issues-when-using-passive-pasv-ftp-mode
type: help
fetched: 2026-10-04
source_version: f1c662de65fb8f1a7151bccc87f85d30878b79984fafe67ebb82fd7e1cb32b85
trust: official
---

# Connectivity/Timeout Issues with Passive (PASV) FTP Mode

## Summary
PASV FTP fails through Twingate when only the FTP hostname is defined as a resource. In passive mode, the FTP server returns its real IP address for data connections, which Twingate doesn't intercept since it only proxies traffic to the defined hostname—not the raw IP.

## Key Information
- Affects FTP passive (PASV) mode only
- Initial authentication succeeds; file transfers/directory listings time out
- Root cause: PASV mode returns the server's actual IP (e.g., `1.2.3.4`), bypassing Twingate's CGNAT interception which only activates on the defined hostname/FQDN
- Twingate intercepts DNS lookups and returns a CGNAT IP, but PASV data channel connects directly to the real server IP

## Symptoms
- FTP resource defined by FQDN only (no IP)
- Auth completes successfully
- Transfers hang or timeout after `227 Entering Passive Mode (x,x,x,x,p,p)`
- Error messages:
  - `TLS/SSL connection refused, turning off session resuming and retrying.`
  - `425: Failed to establish connection.`

## Resolution (Two Options)

**Option 1 — Add the FTP server's IP as a Twingate resource (recommended)**
1. Identify the real IP address of the FTP server (e.g., `1.2.3.4`)
2. In the Twingate Admin Console, add a new Resource using that IP address
3. Assign it to the same Remote Network and the appropriate Group(s)
4. Twingate will now intercept PASV data channel connections to that IP

**Option 2 — Disable passive mode on the FTP client**
- Switch the FTP client to Active (PORT) mode
- Active mode does not involve the server advertising its own IP for the data channel

## Prerequisites
- Access to Twingate Admin Console
- Knowledge of the FTP server's real IP address (resolve via DNS externally before adding resource)

## Gotchas
- Defining the resource by FQDN alone is **insufficient** for PASV FTP—the IP must also be explicitly added
- If the FTP server's IP changes (dynamic DNS), the IP resource will need to be updated manually
- This is a PASV-specific issue; Active mode FTP is not affected
- The PASV response encodes IP as comma-separated octets: `(1,2,3,4,24,123)` = IP `1.2.3.4`, port `24*256+123`

## Related Docs
- Twingate Resource configuration (Admin Console)
- Twingate Component: Resource (connection via Client)