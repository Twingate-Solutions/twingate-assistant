# Split Tunnel Failures

## Summary
Twingate uses split tunneling by default, routing only explicitly defined Resource traffic through the tunnel. Two failure categories exist: local subnet collisions (Twingate captures traffic it shouldn't) and missing Resource definitions (Twingate doesn't capture traffic it should).

## Key Information
- Split tunnel = only defined Resources are routed through Twingate
- Local network traffic bypasses Twingate unless a Resource definition overlaps with it
- Missing domain definitions cause partial app failures for web/SaaS gating use cases
- Exit Networks = intentional full-tunnel mode (not default); user-selectable

## Local Subnet Collision

### Symptoms
- Local printer/NAS unreachable when Twingate is active
- Other VPN clients fail when Twingate is running

### Diagnosis Steps
1. Get user's local IP/subnet (`ipconfig` / `ifconfig` / `ip addr`)
2. Check Admin Console Resource definitions for overlapping CIDRs or IPs
3. If overlap found, that Resource is intercepting local traffic

### Fix
- Use specific IPs (`10.0.5.23`) or small CIDRs (`10.0.5.0/24`) instead of broad ranges (`10.0.0.0/16`)
- `.local` domains conflict with mDNS/Bonjour — see dedicated KB article

## Missing Resource Definitions

### Symptoms
- App partially loads; features broken
- HTTP 401/403 errors on gated web apps
- Styles/scripts fail to load; intermittent failures

### Fix: Browser DevTools
1. Open app in browser with Twingate active → F12 → Network tab
2. Reload page; filter for 401/403/blocked requests
3. Note failing domains → add as wildcard DNS Resources (e.g., `*.partnersite.com`)
4. Assign same Groups/Security Policies as primary Resource

### Fix: Test Resources (when DevTools insufficient)
1. Create two temporary Resources on same Remote Network:
   - DNS Resource: `*.*` (name: "Test DNS")
   - IP Resource: `0.0.0.0/0` (name: "Test IP")
2. Assign **no Groups** initially
3. Create "Test Group" → add both test Resources
4. Add affected user to Test Group; wait for Resources to appear in Client
5. User reproduces failing workflow (should now work)
6. **Remove user from Test Group immediately after test**
7. Review activity logs on user profile or test Resource pages → identify uncovered domains/IPs
8. Add missing entries as permanent Resources with proper Groups/Policies
9. **Delete or disable test Group and test Resources**

## Configuration Values
| Resource Type | Test Value | Purpose |
|---|---|---|
| DNS Resource | `*.*` | Catch all DNS traffic |
| IP Resource | `0.0.0.0/0` | Catch all IP traffic |
| Wildcard DNS | `*.example.com` | Cover all subdomains |

## Gotchas
- Test Resources (`0.0.0.0/0`, `*.*`) must be removed after diagnosis — leaving them active causes unexpected behavior
- `.local` TLD conflicts with mDNS — requires special handling
- Modern web apps use many domains; always prefer wildcard (`*.domain.com`) over individual subdomains
- Broad CIDR Resources are the primary cause of local network collisions

## Related Docs
- Twingate Exit Networks documentation
- `.local` domain KB article (linked in page)
- Activity/logging documentation for diagnosing test Resource traffic