# DNS Failures - Twingate Troubleshooting

## Summary
Twingate intercepts DNS queries for protected Resources and forwards them to a Connector for internal resolution. DNS failures prevent users from reaching Resources even when connected. This guide covers diagnosis and resolution of common DNS failure scenarios.

## Key Information
- Twingate reserves CGNAT range **`100.96.0.0/12`** (`100.96.0.0`–`100.127.255.255`) for internal virtual IPs
- Successful Client DNS interception returns an IP in the `100.96.0.0/12` range
- "DNS lookup error" in Activity report = Connector-side failure (not Client-side)
- If DNS resolves to `100.x.x.x` but connection still fails → problem is with Connector or network routing

## Common Symptoms
- Browser errors: `DNS_PROBE_FINISHED_NXDOMAIN` or "This site can't be reached"
- App logs: "host not found" or "cannot resolve hostname"
- Admin Console Activity report shows "DNS lookup error" status

## Diagnostic Steps

### 1. Test DNS on Client Device
```bash
nslookup <resource_fqdn>
```
- **Pass**: Returns IP in `100.96.0.0/12` → Client intercepting correctly
- **Fail**: Timeout, public IP, or error → Client not intercepting

Possible causes for failure:
- Resource not defined correctly in Admin Console
- User not in a Group with access to Resource
- Client issue

### 2. Check for CGNAT IP Conflicts
```bash
# Windows
ipconfig /all

# macOS
scutil --dns
```
Check assigned IPs and DNS server addresses. If any fall in `100.96.0.0`–`100.127.255.255` (excluding Twingate adapter), there is a conflict.

**Fix**: Manually configure DNS to public resolver outside conflicting range:
- Google DNS: `8.8.8.8`, `8.8.4.4`
- Quad9: `9.9.9.9`

### 3. Test DNS on Connector Host
Only needed when Activity report shows "DNS lookup error":
```bash
nslookup <resource_fqdn>
# or
dig <resource_fqdn>
```
**Fix if failing**: Resolve DNS config on Connector host:
- Edit `/etc/resolv.conf` (Linux)
- Check VPC DNS settings (cloud provider)
- Verify network path to internal DNS servers

> **Best practice**: Disable all but one Connector when troubleshooting to isolate to a single host.

### 4. Check Multiple Active Network Interfaces
Applies to Windows/Linux with simultaneous Ethernet + Wi-Fi on same subnet.

**Fix**:
- Update NIC drivers (especially Realtek chipsets)
- Disable one interface (unplug Ethernet or turn off Wi-Fi)

## Configuration Values
| Item | Value |
|------|-------|
| Twingate CGNAT range | `100.96.0.0/12` |
| Conflict check range | `100.96.0.0`–`100.127.255.255` |
| Google DNS fallback | `8.8.8.8`, `8.8.4.4` |
| Quad9 DNS fallback | `9.9.9.9` |

## Gotchas
- CGNAT conflicts are common and frequently overlooked—always check DNS server addresses, not just device IPs
- "DNS lookup error" in Activity log specifically means Connector failed to resolve, not Client
- Multiple active NICs cause unpredictable routing even when DNS appears correct

## Related Docs
- How DNS Works with Twingate
- Connector deployment guides
- Activity report documentation