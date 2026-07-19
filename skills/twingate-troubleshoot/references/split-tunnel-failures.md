# Split Tunnel Failures

## Summary
Twingate uses split tunneling by default, routing only explicitly defined Resource traffic through the tunnel. Two failure categories exist: local subnet collisions (Twingate captures traffic it shouldn't) and missing Resource definitions (Twingate doesn't capture traffic it should).

## Key Information
- Split tunnel = only defined Resources are tunneled; all other traffic follows normal network path
- Two failure modes: **local subnet collisions** and **missing Resource definitions**
- Exit Networks enable full-tunnel mode (intentional, user-selectable)
- `.local` domains conflict with mDNS/Bonjour — requires special handling

## Local Subnet Collision Troubleshooting

**Symptoms:** Can't reach home printer, local NAS, or another VPN client while Twingate is active

**Steps:**
1. Get user's local IP/subnet via `ipconfig` (Windows) or `ifconfig`/`ip addr` (macOS/Linux)
2. Compare against Resource definitions in Admin Console for overlapping CIDR ranges
3. Refine Resource definitions to be more specific (e.g., `10.0.5.23` instead of `10.0.0.0/16`)

**Best Practice:** Use specific IPs or small CIDR blocks rather than broad ranges

## Missing Resource Definitions (Web App Gating)

**Symptoms:** App partially loads, broken features, HTTP 401/403 errors, intermittent failures

### Method 1: Browser Developer Tools
1. Open app in browser with Twingate active
2. Press `F12` → Network tab → reload page
3. Filter for failed requests (401, 403, blocked/cancelled)
4. Note domains of failed requests
5. Add wildcard DNS Resources (e.g., `*.partnersite.com`) in Admin Console
6. Assign same Groups/Security Policies as primary Resource
7. Wait for Client sync, reload, repeat

**Best Practice:** Use `*.domain.com` wildcards to cover all current and future subdomains

### Method 2: Test Resources (Temporary Full-Tunnel Diagnostic)
1. Create two Resources on same Remote Network as problem app:
   - DNS Resource: `*.*` (name: "Test DNS")
   - IP Resource: `0.0.0.0/0` (name: "Test IP")
   - No port/protocol restrictions; **assign to no Groups initially**
2. Create new Group (e.g., "Test Group"), add both test Resources
3. Add affected user to Test Group; wait for Resources to appear in Client
4. User loads app — should work fully with all traffic tunneled
5. **Remove user from Test Group immediately after test**
6. Review activity logs on user profile or Resource activity page for uncovered domains/IPs
7. Add missing entries as permanent Resources with proper Groups/Policies
8. Retest without test Resources
9. Delete/disable Test Group and test Resources

## Configuration Values
| Resource Type | Test Value | Purpose |
|---|---|---|
| DNS Resource | `*.*` | Capture all DNS traffic |
| IP Resource | `0.0.0.0/0` | Capture all IP traffic |
| Wildcard DNS | `*.domain.com` | Cover all subdomains |

## Gotchas
- **Test Resources must be removed after testing** — leaving them active causes unexpected behavior
- `.local` domains conflict with mDNS; see separate KB article
- Full-tunnel mode requires Exit Networks, not broad Resource definitions
- Web apps commonly depend on CDN, auth, and third-party domains not obvious from the main URL
- Subnet collision applies to both CIDR ranges AND specific IPs within a range

## Related Docs
- Exit Networks documentation
- `.local` domain KB article
- Activity/log review (user profile page or Resource activity page)
- Twingate log collection for unresolved issues