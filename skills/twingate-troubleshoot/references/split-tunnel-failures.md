# Split Tunnel Failures

## Summary
Twingate uses split tunneling by default, routing only explicitly defined Resource traffic through the tunnel. Two failure categories exist: local subnet collisions (Twingate captures traffic it shouldn't) and missing Resource definitions (Twingate misses traffic it should capture).

## Key Information
- Split tunnel = only defined Resources are tunneled; all other traffic uses normal network path
- Two failure types: **local subnet collisions** and **missing Resource definitions**
- Exit Networks enable intentional full-tunnel mode (not default)
- `.local` domains conflict with mDNS/Bonjour protocol

## Local Subnet Collisions

### Symptoms
- Local printer/NAS inaccessible when Twingate is active
- Another VPN client stops working alongside Twingate

### Diagnosis Steps
1. Get user's local IP/subnet: `ipconfig` (Windows) or `ifconfig`/`ip addr` (macOS/Linux)
2. Check Admin Console Resource definitions for overlapping CIDR ranges or specific IPs
3. Overlap = Twingate routes local traffic to corporate Connector → fails

### Fix
- Use specific IPs (`10.0.5.23`) or narrow CIDRs (`10.0.5.0/24`) instead of broad ranges (`10.0.0.0/16`)
- For full-tunnel requirement: use **Exit Networks** (intentional, user-selectable)

## Missing Resource Definitions

### Symptoms
- SaaS app partially loads; features broken
- HTTP 401/403 errors on gated applications
- App "works sometimes" or "works on some pages"

### Diagnosis: Browser Dev Tools
1. Open app in browser with Twingate active → F12 → Network tab → reload
2. Filter by failed status codes (401, 403, blocked/cancelled)
3. Note failed request domains → add as wildcard DNS Resources (e.g., `*.partnersite.com`)
4. Assign same Groups/Security Policies as primary Resource → retest

### Diagnosis: Test Resources (Temporary Full-Tunnel)
1. Create two Resources on same Remote Network:
   - DNS Resource: address `*.*` (name: "Test DNS")
   - IP Resource: address `0.0.0.0/0` (name: "Test IP")
2. Assign **no Groups** initially
3. Create new Group (e.g., "Test Group") → add both Resources
4. Add affected user to Test Group → wait for Resources to appear in Client
5. User reproduces failing workflow (should now work)
6. **Immediately remove user from Test Group**
7. Review activity logs on user profile or test Resource pages for unmatched domains/IPs
8. Add missing entries as permanent Resources with proper Groups/Policies
9. **Delete or disable test Group and Resources**

## Configuration Values
| Resource Type | Address | Use Case |
|--------------|---------|----------|
| Wildcard DNS | `*.example.com` | Cover all subdomains |
| Catch-all DNS | `*.*` | Diagnostic only |
| Catch-all IP | `0.0.0.0/0` | Diagnostic only |

## Gotchas
- Test Resources (`*.*` and `0.0.0.0/0`) **must be deleted after testing** — leaving enabled causes unexpected behavior
- `.local` domains conflict with mDNS; requires special handling (see separate KB article)
- Wildcard Resources preferred over individual subdomains (covers future subdomains automatically)
- Exit Networks are not the default; users must explicitly select them

## Related Docs
- Twingate Exit Networks documentation
- `.local` domain KB article (linked in source)
- Activity/logging documentation for network traffic review