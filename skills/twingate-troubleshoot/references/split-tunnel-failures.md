# Split Tunnel Failures

## Summary
Twingate uses split tunneling by default, routing only explicitly defined Resource traffic through the tunnel. Two failure categories exist: local subnet collisions (Twingate captures traffic it shouldn't) and missing Resource definitions (Twingate doesn't capture traffic it should).

## Key Information
- Split tunnel = only defined Resources are routed through Twingate
- All other traffic follows normal network path
- Full-tunnel mode requires configuring an **Exit Network** (not default)
- `.local` domains conflict with mDNS/Bonjour — requires special handling

## Local Subnet Collision Troubleshooting

**Symptoms:** Can't reach home printer/NAS/local devices; other VPN clients break when Twingate is active

**Steps:**
1. Get user's local IP/subnet: `ipconfig` (Windows) or `ifconfig`/`ip addr` (macOS/Linux)
2. Check Admin Console Resources for overlapping CIDR ranges or specific IPs
3. Refine Resource definitions to smallest precise scope

**Best Practice:** Use specific IPs (`10.0.5.23`) or small CIDRs (`10.0.5.0/24`) instead of broad ranges (`10.0.0.0/16`)

## Missing Resource Definitions

**Symptoms:** App partially loads; HTTP 401/403 errors; broken styles/scripts; intermittent failures

### Fix with Browser DevTools
1. Open app in browser with Twingate active → F12 → Network tab
2. Reload page; filter for 401/403/blocked requests
3. Note failing domains → add as wildcard DNS Resources (e.g., `*.partnersite.com`)
4. Assign same Groups/Security Policies as primary Resource

### Fix with Test Resources (when DevTools insufficient)
1. Create two temporary Resources on same Remote Network:
   - DNS Resource: `*.*` (name: "Test DNS")
   - IP Resource: `0.0.0.0/0` (name: "Test IP")
2. Assign **no Groups** initially
3. Create "Test Group" → add both test Resources
4. Add affected user to Test Group → wait for Resources to appear in Client
5. User reproduces failing workflow (should now work)
6. **Remove user from Test Group immediately after**
7. Review activity logs on test Resources for uncovered domains/IPs
8. Add missing entries as permanent Resources with proper Groups/Security Policies
9. **Delete or disable Test Group and test Resources**

## Configuration Values
| Resource Type | Wildcard Syntax | Use Case |
|---|---|---|
| DNS Resource | `*.*` | Catch-all test |
| DNS Resource | `*.partnersite.com` | Cover all subdomains |
| IP Resource | `0.0.0.0/0` | Catch-all IP test |

## Gotchas
- Test Resources (`*.*` and `0.0.0.0/0`) route ALL user traffic — diagnostic use only, remove after testing
- `.local` domain Resources conflict with mDNS device discovery
- Modern web apps use multiple domains; missing any one breaks functionality
- IP collision can be a specific address overlap, not just subnet-level

## Prerequisites
- Access to Twingate Admin Console
- Ability to review Resource definitions and activity logs
- Browser DevTools familiarity for domain identification

## Related Docs
- Exit Networks (full-tunnel mode)
- `.local` domain knowledge base article
- Activity/network logs (user profile page or Resource activity page)