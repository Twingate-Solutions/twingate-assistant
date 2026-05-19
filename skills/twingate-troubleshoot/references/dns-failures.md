# DNS Failures - Twingate Troubleshooting

## Page Title
DNS Failures: How to Troubleshoot User DNS Issues

## Summary
Twingate intercepts DNS queries for protected Resources and forwards them to a Connector for resolution via internal DNS servers. Failures result in users being unable to reach Resources despite being connected. This page covers diagnosis and resolution of common DNS failure scenarios.

## Key Information
- Twingate reserves CGNAT range **100.96.0.0/12** (100.96.0.0–100.127.255.255) for internal virtual IPs
- Successful Client DNS interception returns an IP in the CGNAT range
- "DNS lookup error" in Activity report = Connector-side failure (Client successfully forwarded the request)
- No CGNAT IP returned = Client-side failure (misconfiguration, permissions, or Client issue)

## Common Symptoms
- Browser errors: `DNS_PROBE_FINISHED_NXDOMAIN` or "This site can't be reached"
- App logs: "host not found" / "cannot resolve hostname"
- Activity report shows "DNS lookup error" status

## Step-by-Step Diagnosis

### 1. Test DNS on Client Device
```bash
nslookup <resource_fqdn>
# e.g., nslookup jira.mycompany.internal
```
- **Expected**: Returns IP in `100.96.0.0/12` range → Client intercepting correctly
- **Bad**: Timeout, public IP, or error → Client not intercepting

**Client-side failure causes:**
- Resource not defined correctly in Admin Console
- User's Group lacks access to the Resource
- Client application issue

### 2. Check for CGNAT IP Conflicts
```bash
# Windows
ipconfig /all

# macOS
scutil --dns
```
- Look for assigned IPs or DNS server addresses in range `100.96.0.0–100.127.255.255`
- **Fix**: Set device DNS to public resolver outside conflicting range

### 3. Test DNS on Connector Host
```bash
nslookup <resource_fqdn>
# or
dig <resource_fqdn>
```
- Run from the Connector's host machine
- Failure here confirms Connector cannot reach internal DNS

**Fix options:**
- Edit `/etc/resolv.conf` (Linux)
- Check VPC DNS settings in cloud provider
- Ensure network path to internal DNS servers exists

### 4. Check Multiple Active Network Interfaces (Windows/Linux)
- Dual active NICs (Ethernet + Wi-Fi) on same subnet causes routing/DNS conflicts
- Update NIC drivers (especially Realtek chipsets)
- **Workaround**: Disable one interface

## Configuration Values
| Item | Value |
|------|-------|
| Twingate CGNAT range | `100.96.0.0/12` |
| Conflict check range | `100.96.0.0–100.127.255.255` |
| Google DNS fallback | `8.8.8.8`, `8.8.4.4` |
| Quad9 DNS fallback | `9.9.9.9` |

## Gotchas
- CGNAT conflict is frequently overlooked—some ISPs and corporate networks use this range
- If DNS resolves to a `100.x.x.x` address but connection still fails, the problem is Connector or routing, not DNS
- Isolate to one Connector when troubleshooting to pinpoint the failing host
- "DNS lookup error" in Activity logs specifically means Connector-side failure, not Client-side

## Related Docs
- How DNS Works with Twingate
- Activity Report documentation
- Connector deployment guides