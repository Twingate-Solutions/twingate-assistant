# Split Tunnel Failures

## Summary
Twingate uses split tunneling by default, routing only explicitly defined Resource traffic through the tunnel. Two failure categories exist: local subnet collisions (Twingate captures traffic it shouldn't) and missing Resource definitions (Twingate doesn't capture traffic it should).

## Key Information
- Split tunnel only routes traffic matching defined Resource IPs/domains
- All other traffic uses the device's normal network path
- Exit Networks provide intentional full-tunnel mode (user-selectable)
- `.local` domains conflict with mDNS/Bonjour—requires special handling

## Local Subnet Collisions

### Symptoms
- Local printer/NAS unreachable when Twingate is active
- Other VPN clients fail when Twingate is running

### Diagnosis Steps
1. Get user's local IP/subnet: `ipconfig` (Windows) or `ifconfig`/`ip addr` (macOS/Linux)
2. Check Admin Console Resource definitions for overlapping CIDR ranges
3. If corporate Resource matches user's local subnet (e.g., `192.168.1.0/24`), that's the collision

### Fix
- Use specific IPs (`10.0.5.23`) instead of broad CIDRs (`10.0.0.0/16`)
- Use smaller CIDR blocks (`10.0.5.0/24`) when ranges are needed
- For intentional full-tunnel: deploy an **Exit Network** with Connectors as exit points

## Missing Resource Definitions

### Symptoms
- SaaS app partially loads; features broken
- HTTP 401/403 errors on gated applications
- App works on some pages but not others

### Diagnosis: Browser DevTools
1. Open app in Chrome/Edge/Firefox with Twingate active
2. Press `F12` → **Network** tab → reload page
3. Filter for 401, 403, blocked/cancelled requests
4. Note failing domains → add as `*.domain.com` wildcard Resources in Admin Console
5. Assign same Groups/Security Policies as primary Resource

### Diagnosis: Test Resources (when DevTools insufficient)
**⚠️ Remove test Resources immediately after testing**

1. Create two Resources on the same Remote Network:
   - DNS Resource: `*.*` (name: "Test DNS")
   - IP Resource: `0.0.0.0/0` (name: "Test IP")
   - No port/protocol restrictions; **no Groups assigned**
2. Create new Group (e.g., "Test Group"), add both Resources
3. Add affected user to Test Group; wait for Resources to appear in Client
4. User loads failing application workflow
5. Remove user from Test Group immediately after test
6. Review activity logs on user profile or Resource pages for uncovered domains/IPs
7. Add missing entries as permanent Resources with appropriate Groups
8. Delete/disable Test Group and test Resources

## Configuration Values
| Resource Type | Test Value | Purpose |
|--------------|------------|---------|
| DNS Resource | `*.*` | Capture all DNS traffic |
| IP Resource | `0.0.0.0/0` | Capture all IP traffic |
| Wildcard DNS | `*.domain.com` | Cover all subdomains |

## Gotchas
- Leaving test Resources (`*.*`, `0.0.0.0/0`) enabled causes unexpected behavior for users
- `.local` TLD conflicts with mDNS—see separate KB article
- Modern web apps use many subdomains; always prefer wildcard (`*.domain.com`) over individual subdomains
- Specific IP collisions also trigger local network issues, not just CIDR overlaps

## Related Docs
- Twingate Exit Networks documentation
- `.local` domain KB article (linked in source)
- Activity/logs page for troubleshooting network requests