# DNS Failures - Twingate Troubleshooting

## Summary
Twingate intercepts DNS queries for protected Resources and forwards them to a Connector for internal resolution. DNS failures prevent clients from obtaining correct IP addresses for Resources. This guide covers diagnosing and resolving DNS issues at both the client and connector levels.

## Key Information
- Twingate reserves `100.96.0.0/12` (range: `100.96.0.0`–`100.127.255.255`) for internal virtual IPs
- Successful DNS interception returns a CGNAT IP in the `100.96.0.0/12` range
- "DNS lookup error" in Activity report = Connector-side failure (not client-side)
- If DNS resolves to a `100.x.x.x` address but connection still fails, the problem is with the Connector or network routing

## Common Symptoms
- Browser errors: `DNS_PROBE_FINISHED_NXDOMAIN` or "This site can't be reached"
- App errors: "host not found" / "cannot resolve hostname"
- Activity report shows "DNS lookup error" status for Resource

## Troubleshooting Steps

### 1. Test DNS on Client Device
```bash
nslookup <resource_fqdn>
# e.g., nslookup jira.mycompany.internal
```
- **Pass**: Returns IP in `100.96.0.0/12` range → client interception working
- **Fail** (timeout, public IP, or error): Client not intercepting; check Resource definition, Group membership, or Client health

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
- Run from the Connector's server/container host
- **Fix if failing**: Edit `/etc/resolv.conf`, check cloud VPC DNS settings, verify network path to internal DNS servers
- **Best practice**: Disable all but one Connector when troubleshooting to isolate the issue

### 4. Check Multiple Active Network Interfaces (Windows/Linux)
- Concurrent wired + wireless on same subnet causes unpredictable DNS/routing
- **Fix**: Update NIC drivers (especially Realtek chipsets); disable one interface as workaround

## Configuration Values
| Item | Value |
|------|-------|
| Twingate CGNAT range | `100.96.0.0/12` |
| Conflict check range | `100.96.0.0`–`100.127.255.255` |
| Google DNS fallback | `8.8.8.8`, `8.8.4.4` |
| Quad9 DNS fallback | `9.9.9.9` |

## Gotchas
- CGNAT range conflicts are frequently overlooked; ISPs or corporate networks sometimes use this range
- "DNS lookup error" in Activity report specifically indicates Connector-side failure—don't troubleshoot the client
- Multiple NICs on same subnet can cause intermittent, hard-to-reproduce failures
- Successful DNS (`100.x.x.x` returned) does not guarantee connectivity—Connector/routing issues can still block access

## Related Docs
- How DNS Works with Twingate
- Twingate Activity Report
- Connector deployment guides