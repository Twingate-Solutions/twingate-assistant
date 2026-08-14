---
source: https://www.twingate.com/docs/split-tunnel-failures
type: docs
fetched: 2026-08-14
source_version: 53eced3f1241374884f2dfeaa67f948545130d5fe9cdecd3f536e82b264e23f0
---

# Split Tunnel Failures

## Summary
Twingate uses split tunneling by default, routing only explicitly defined Resource traffic through the tunnel. Two failure categories exist: local subnet collisions (Twingate captures traffic it shouldn't) and missing Resource definitions (Twingate misses traffic it should capture).

## Key Information
- Split tunnel = only defined Resources are routed through Twingate
- Local traffic and public internet traffic bypass Twingate by default
- Exit Networks provide full-tunnel mode (user-selectable, not default)
- `.local` domains conflict with mDNS/Bonjour protocol

## Local Subnet Collision Troubleshooting

### Symptoms
- Local printer/NAS inaccessible when Twingate active
- Other VPN clients fail when Twingate is running

### Diagnosis Steps
1. User runs `ipconfig` (Windows) or `ifconfig`/`ip addr` (macOS/Linux) to find local subnet
2. Check Admin Console Resource definitions for overlapping CIDR ranges
3. If corporate Resource matches user's local subnet (e.g., both `192.168.1.0/24`), collision confirmed

### Fix
- Use specific IPs (`10.0.5.23`) instead of broad CIDR blocks (`10.0.0.0/16`)
- Use smallest precise CIDR blocks possible

## Missing Resource Definitions Troubleshooting

### Symptoms
- SaaS app partially loads, broken features
- HTTP 401/403 errors on gated applications
- Missing styles, scripts, or embedded content
- Intermittent failures across pages

### Method 1: Browser DevTools
1. Open app in browser with Twingate active → F12 → Network tab
2. Reload page, filter by error status codes (401, 403, blocked/cancelled)
3. Identify failing domains
4. Add `*.parentdomain.com` wildcard DNS Resource in Admin Console
5. Assign same Groups/Security Policies as primary Resource
6. Retest after Client updates

### Method 2: Test Resources (temporary diagnostic)
1. Create two Resources on same Remote Network:
   - DNS Resource: `*.*` (name: "Test DNS")
   - IP Resource: `0.0.0.0/0` (name: "Test IP")
2. Assign **no Groups** initially
3. Create new Group (e.g., "Test Group"), add both Resources
4. Add affected user to Test Group → wait for Resources to appear in Client
5. User completes failing workflow (should work now)
6. **Immediately remove user from Test Group**
7. Review activity logs on user profile or Resource pages for uncovered domains/IPs
8. Add missing entries as permanent Resources with proper Groups/Policies
9. **Delete/disable Test Group and test Resources**

## Configuration Values
| Resource Type | Test Value | Purpose |
|---|---|---|
| DNS Resource | `*.*` | Capture all DNS traffic |
| IP Resource | `0.0.0.0/0` | Capture all IP traffic |
| Wildcard DNS | `*.domain.com` | Cover all subdomains |

## Gotchas
- **Test Resources must be removed after use** — leaving them active causes unexpected behavior
- `.local` TLD conflicts with mDNS (Bonjour); requires special handling per KB article
- Modern web apps use many domains (CDN, auth, assets) — all must be defined as Resources
- Specific IP collision possible even without full subnet overlap if individual IPs match

## Related Docs
- Exit Networks (full-tunnel mode)
- `.local` domain KB article
- Activity/logging documentation