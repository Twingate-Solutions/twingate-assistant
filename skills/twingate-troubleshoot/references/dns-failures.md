---
source: https://www.twingate.com/docs/dns-failures
type: docs
fetched: 2026-08-14
source_version: c19209f19807c7ff3f143153917f350ac98d335005cd8e23380977b90a25af1e
---

# DNS Failures - Twingate Troubleshooting

## Page Title
DNS Failures: How to Troubleshoot User DNS Issues

## Summary
Twingate intercepts DNS queries for protected Resources and forwards them to a Connector for internal resolution. DNS failures prevent users from obtaining correct IP addresses for Resources. This guide covers diagnosing and resolving DNS issues at the Client, network, and Connector levels.

## Key Information
- Twingate reserves `100.96.0.0/12` (range: `100.96.0.0`–`100.127.255.255`) for internal virtual IPs
- Successful Client DNS interception returns a CGNAT IP in the `100.96.0.0/12` range
- "DNS lookup error" in Activity report = Connector-side failure (not Client)
- Multiple active NICs on same subnet can cause unpredictable DNS/routing behavior

## Common Symptoms
- Browser errors: `DNS_PROBE_FINISHED_NXDOMAIN` or "This site can't be reached"
- App logs: "host not found" or "cannot resolve hostname"
- Activity report shows "DNS lookup error" status for Resource

## Step-by-Step Troubleshooting

### 1. Test DNS on Client Device
```bash
nslookup <resource_fqdn>
# e.g., nslookup jira.mycompany.internal
```
- **Pass**: Returns IP in `100.96.0.0/12` → Client intercepting correctly
- **Fail**: Timeout, public IP, or error → Resource misconfigured, user not in authorized Group, or Client issue

### 2. Check for CGNAT IP Conflicts
```bash
# Windows
ipconfig /all

# macOS
scutil --dns
```
- Check assigned IPs and DNS server addresses
- If any fall in `100.96.0.0–100.127.255.255` (excluding Twingate adapter) → conflict exists
- **Fix**: Set DNS to public resolver: Google (`8.8.8.8`, `8.8.4.4`) or Quad9 (`9.9.9.9`)

### 3. Test DNS on Connector Host
```bash
nslookup <resource_fqdn>
# or
dig <resource_fqdn>
```
- Run from Connector host when Activity report shows "DNS lookup error"
- **Fix if fails**: Edit `/etc/resolv.conf`, check cloud VPC DNS settings, verify network path to internal DNS servers
- **Best practice**: Disable all but one Connector when troubleshooting to isolate to single host

### 4. Check Multiple Active Network Interfaces
- Applies to Windows and Linux with both Ethernet and Wi-Fi active on same subnet
- **Fix**: Update NIC drivers (especially Realtek chipsets); disconnect one interface

## Configuration Values
| Item | Value |
|------|-------|
| Twingate CGNAT range | `100.96.0.0/12` |
| Conflict range | `100.96.0.0`–`100.127.255.255` |
| Google DNS fallback | `8.8.8.8`, `8.8.4.4` |
| Quad9 DNS fallback | `9.9.9.9` |

## Gotchas
- CGNAT conflicts are commonly overlooked; ISPs sometimes use this range
- If DNS resolves to `100.x.x.x` but connection still fails → problem is at Connector or network routing layer, not DNS
- "DNS lookup error" in Activity report specifically indicates Connector-side failure, not Client-side

## Related Docs
- How DNS Works with Twingate
- Connector deployment and configuration
- Activity report / Admin Console monitoring