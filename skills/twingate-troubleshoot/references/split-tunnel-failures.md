# Split Tunnel Failures

## Summary
Twingate uses split tunneling by default, only routing traffic for explicitly defined Resources. Two failure categories exist: local subnet collisions (Twingate captures traffic it shouldn't) and missing Resource definitions (Twingate misses traffic it should capture).

## Key Information
- Split tunnel = only defined Resources route through Twingate; all other traffic uses normal path
- Full-tunnel mode requires explicitly configuring an **Exit Network** (user-selectable)
- `.local` domains conflict with mDNS/Bonjour; requires special handling

## Local Subnet Collisions

### Symptoms
- Local printer/NAS/file server unreachable when Twingate active
- Other VPN clients fail when Twingate is running

### Diagnosis Steps
1. Get user's local subnet: `ipconfig` (Windows) or `ifconfig`/`ip addr` (macOS/Linux)
2. Compare against Resource definitions in Admin Console
3. Overlap = collision (e.g., corporate Resource `192.168.1.0/24` vs user's home network `192.168.1.0/24`)

### Fix
- Use specific IPs (`10.0.5.23`) or narrow CIDRs (`10.0.5.0/24`) instead of broad ranges (`10.0.0.0/16`)
- For full-tunnel requirements, deploy an Exit Network with Connectors

## Missing Resource Definitions

### Symptoms
- App partially loads; features broken or unresponsive
- HTTP 401/403 errors on gated web applications
- App works on some pages but not others

### Fix: Browser DevTools Method
1. Open app in browser with Twingate active → F12 → Network tab → reload
2. Filter by error status codes (401, 403, blocked/cancelled)
3. Note failing domains → add as wildcard DNS Resources (e.g., `*.partnersite.com`)
4. Assign same Groups/Security Policies as primary Resource

### Fix: Test Resources Method (when DevTools insufficient)
**⚠️ Temporary diagnostic only — remove after testing**

1. Create two Resources on same Remote Network:
   - DNS Resource: `*.*` (name: "Test DNS")
   - IP Resource: `0.0.0.0/0` (name: "Test IP")
   - No port/protocol restrictions; **assign to no Groups initially**
2. Create new Group (e.g., "Test Group") → add both test Resources
3. Add affected user to Test Group; wait for Resources to appear in Client
4. User reproduces failing workflow (should now work)
5. **Immediately remove user from Test Group**
6. Review activity logs on user profile or Resource activity page
7. Identify domains/IPs captured by test Resources not in existing definitions
8. Add missing entries as permanent Resources with proper Groups/Policies
9. **Delete or disable Test Group and test Resources**

## Configuration Values

| Resource Type | Wildcard Pattern | Use Case |
|---|---|---|
| DNS | `*.partnersite.com` | All subdomains of a domain |
| DNS | `*.*` | Test only — all DNS |
| IP | `0.0.0.0/0` | Test only — all IP traffic |

## Gotchas
- Broad CIDR Resources (e.g., `10.0.0.0/8`) likely to collide with RFC1918 home networks
- Modern web apps use many domains; single-domain Resources are rarely sufficient
- `.local` domain Resources conflict with mDNS device discovery
- Test Resources (`*.*`, `0.0.0.0/0`) route **all** user traffic — never leave assigned permanently
- New Resources require time to propagate to user's Client before testing

## Related Docs
- Twingate knowledge base article on `.local` domain conflicts
- Exit Networks documentation
- Activity logs / user profile page in Admin Console