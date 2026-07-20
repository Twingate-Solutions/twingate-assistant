# DNS Failures - Twingate Troubleshooting

## Page Title
DNS Failures: How to Troubleshoot User DNS Issues

## Summary
Twingate intercepts DNS queries for protected Resources and forwards them to a Connector for internal resolution. DNS failures prevent users from obtaining correct IP addresses to reach Resources. This guide covers diagnosing and resolving DNS issues at the Client, network, and Connector levels.

## Key Information
- Twingate reserves `100.96.0.0/12` (range: `100.96.0.0`–`100.127.255.255`) for internal virtual IPs
- Successful Client DNS interception returns a CGNAT IP in the `100.96.0.0/12` range
- "DNS lookup error" in Activity report = Connector-side failure (Client reached Connector successfully)
- No CGNAT IP returned = Client-side failure (interception not working)

## Common Symptoms
- Browser errors: `DNS_PROBE_FINISHED_NXDOMAIN` or "This site can't be reached"
- App logs: "host not found" or "cannot resolve hostname"
- Activity report shows "DNS lookup error" status for the Resource

## Step-by-Step Troubleshooting

### 1. Test DNS on Client Device
```bash
nslookup <resource_fqdn>
# e.g., nslookup jira.mycompany.internal
```
- **Pass**: Returns IP in `100.96.0.0/12` → Client interception working
- **Fail** (timeout, public IP, or error): Client not intercepting → check Resource definition, Group membership, or Client health

### 2. Check for CGNAT IP Conflicts
```bash
# Windows
ipconfig /all

# macOS
scutil --dns
```
- Look for any assigned IPs or DNS server addresses in `100.96.0.0`–`100.127.255.255` (excluding Twingate adapter)
- **Fix**: Set DNS manually to public resolver outside conflicting range

### 3. Check DNS on Connector Host
```bash
nslookup <resource_fqdn>
# or
dig <resource_fqdn>
```
- Run on the Connector's host machine
- Failure here confirms local DNS misconfiguration on Connector host
- **Fix**: Edit `/etc/resolv.conf`, check cloud VPC DNS settings, or ensure network path to internal DNS servers exists

### 4. Check Multiple Active Network Interfaces
- Concurrent Ethernet + Wi-Fi on same subnet causes routing/DNS conflicts
- **Fix**: Update NIC drivers (especially Realtek); workaround is to disable one interface

## Configuration Values
| Item | Value |
|------|-------|
| Twingate CGNAT range | `100.96.0.0/12` |
| Google DNS (fallback) | `8.8.8.8`, `8.8.4.4` |
| Quad9 DNS (fallback) | `9.9.9.9` |

## Gotchas
- CGNAT conflict is frequently overlooked—some ISPs and corporate networks use `100.96.0.0/12`
- "DNS lookup error" in Activity report specifically means the Connector failed to resolve, not the Client
- Disable all but one Connector when troubleshooting to isolate the problem host
- If DNS resolves to `100.x.x.x` but connection still fails, the issue is Connector/routing, not DNS

## Prerequisites
- Access to user's device CLI
- SSH/terminal access to Connector host
- Admin Console access to view Activity reports

## Related Docs
- How DNS Works with Twingate
- Connector deployment and configuration
- Activity report / monitoring