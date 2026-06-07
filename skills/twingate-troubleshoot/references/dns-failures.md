# DNS Failures - Twingate Troubleshooting

## Page Title
DNS Failures: How to Troubleshoot User DNS Issues

## Summary
Twingate intercepts DNS queries for protected Resources and forwards them to a Connector for internal resolution. DNS failures prevent clients from obtaining correct IP addresses, causing connection errors. Troubleshooting involves checking Client interception, CGNAT conflicts, Connector-side resolution, and network interface issues.

## Key Information
- Twingate reserves `100.96.0.0/12` (range: `100.96.0.0`–`100.127.255.255`) for internal virtual IPs
- Successful Client interception returns a CGNAT IP (`100.96.0.0/12`) from `nslookup`
- "DNS lookup error" in Activity report = Connector-side failure (not Client-side)
- Successful DNS to `100.x.x.x` but still failing = Connector/network routing issue

## Common Symptoms
- Browser errors: `DNS_PROBE_FINISHED_NXDOMAIN` or "This site can't be reached"
- App logs: "host not found" / "cannot resolve hostname"
- Admin Console Activity report shows "DNS lookup error" status

## Step-by-Step Troubleshooting

### 1. Test DNS on Client Device
```bash
nslookup <resource_fqdn>
# e.g., nslookup jira.mycompany.internal
```
- **Pass**: Returns IP in `100.96.0.0/12` range → Client intercepting correctly
- **Fail**: Timeout, public IP, or error → Client not intercepting (check Resource definition, Group membership, or Client health)

### 2. Check for CGNAT IP Conflicts
```bash
# Windows
ipconfig /all

# macOS
scutil --dns
```
- Look for assigned IPs or DNS server addresses falling in `100.96.0.0`–`100.127.255.255`
- **Fix**: Set device DNS to public resolver outside conflicting range:
  - Google DNS: `8.8.8.8`, `8.8.4.4`
  - Quad9: `9.9.9.9`

### 3. Test DNS on Connector Host
```bash
nslookup <resource_fqdn>
# or
dig <resource_fqdn>
```
- Run from the Connector server/container host
- Failure confirms local DNS misconfiguration on Connector host
- **Fix**: Edit `/etc/resolv.conf` (Linux), check cloud VPC DNS settings, verify network path to internal DNS servers
- **Best practice**: Disable all but one Connector to isolate the problem

### 4. Check Multiple Active Network Interfaces
- Windows/Linux with simultaneous Ethernet + Wi-Fi on same subnet causes routing/DNS conflicts
- **Fix**: Update NIC drivers (especially Realtek chipsets); disable one interface as workaround

## Configuration Values
| Item | Value |
|------|-------|
| Twingate CGNAT range | `100.96.0.0/12` (`100.96.0.0`–`100.127.255.255`) |
| Google DNS fallback | `8.8.8.8`, `8.8.4.4` |
| Quad9 DNS fallback | `9.9.9.9` |

## Gotchas
- CGNAT conflict is "often overlooked" — check DNS *server* addresses, not just device IPs
- "DNS lookup error" in Activity report specifically indicates Connector failure, not Client failure
- Successful CGNAT resolution with continued failure points to Connector/routing issues, not DNS

## Related Docs
- How DNS Works with Twingate
- Activity Report (Admin Console)
- Connector deployment guides