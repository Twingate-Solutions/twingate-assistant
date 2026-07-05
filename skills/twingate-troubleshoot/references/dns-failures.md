# DNS Failures - Twingate Troubleshooting

## Page Title
DNS Failures: How to Troubleshoot User DNS Issues

## Summary
Twingate intercepts DNS queries for protected Resources and forwards them to a Connector for internal resolution. Failures in this chain prevent clients from getting correct IP addresses. This page covers diagnosis and resolution for common DNS failure scenarios.

## Key Information
- Twingate reserves `100.96.0.0/12` (range: `100.96.0.0`–`100.127.255.255`) for internal virtual IPs
- Successful DNS interception by the Client returns a CGNAT IP in the `100.96.0.0/12` range
- "DNS lookup error" in Activity report = Connector-side failure (Client successfully forwarded the request)
- No CGNAT IP returned = Client-side failure (interception not occurring)

## Common Symptoms
- Browser errors: `DNS_PROBE_FINISHED_NXDOMAIN` or "This site can't be reached"
- App logs showing "host not found" or "cannot resolve hostname"
- Activity report showing "DNS lookup error" status

## Step-by-Step Troubleshooting

### 1. Test DNS on Client Device
```bash
nslookup <resource_fqdn>
# e.g., nslookup jira.mycompany.internal
```
- **Pass**: Returns IP in `100.96.0.0/12` → Client interception working
- **Fail** (timeout, public IP, or error) → Client not intercepting; check Resource definition, Group membership, or Client health

### 2. Check for CGNAT IP Conflicts
```bash
# Windows
ipconfig /all

# macOS
scutil --dns
```
- Look for assigned IPs or DNS server addresses falling in `100.96.0.0`–`100.127.255.255`
- **Fix**: Set DNS to public resolver outside conflict range:
  - Google DNS: `8.8.8.8`, `8.8.4.4`
  - Quad9: `9.9.9.9`

### 3. Test DNS on Connector Host
```bash
nslookup <resource_fqdn>
# or
dig <resource_fqdn>
```
- Run from the Connector's host machine
- **Fix if failing**: Edit `/etc/resolv.conf`, check cloud VPC DNS settings, or verify network path to internal DNS servers
- **Best practice**: Disable all but one Connector when troubleshooting to isolate the issue

### 4. Check Multiple Active Network Interfaces
- Applies mainly to Windows and Linux with simultaneous Ethernet + Wi-Fi on same subnet
- **Fix**: Update NIC drivers (especially Realtek chipsets); or disable one interface

## Configuration Values
| Item | Value |
|------|-------|
| Twingate CGNAT range | `100.96.0.0/12` (`100.96.0.0`–`100.127.255.255`) |
| Google DNS fallback | `8.8.8.8`, `8.8.4.4` |
| Quad9 DNS fallback | `9.9.9.9` |
| Connector DNS config (Linux) | `/etc/resolv.conf` |

## Gotchas
- CGNAT conflict is frequently overlooked—some ISPs and corporate networks use `100.x.x.x` ranges
- If `nslookup` returns a CGNAT IP but connection still fails, the problem is Connector-side or network routing, not DNS
- Multiple active NICs on Windows/Linux can cause unpredictable DNS routing

## Related Docs
- How DNS Works with Twingate
- Activity Report (Admin Console)
- Connector deployment and configuration