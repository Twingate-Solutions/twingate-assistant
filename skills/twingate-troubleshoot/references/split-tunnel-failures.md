## Split Tunnel Failures (Troubleshooting)

Diagnostic playbook for two split-tunnel issues: **traffic captured when it shouldn't be** (local subnet collisions) and **traffic NOT captured when it should be** (missing Resource definitions).

### Background

Twingate is **split-tunnel by default** -- only Resource-destined traffic is intercepted. Two failure modes:

1. **Subnet overlap**: a Resource definition includes IPs that match the user's local network -> Twingate captures local printer/NAS traffic
2. **Missing definitions**: app traffic goes to undefined domains -> bypasses Twingate entirely, fails IP allowlist checks

### Failure Mode 1: Local Subnet Collisions

**Symptoms:**
- "I can't print to my home printer (`192.168.1.50`) when Twingate is on"
- Can't access local NAS / file server / IoT device when connected
- Other (non-Twingate) VPN client breaks when Twingate is active

**Diagnose:**

1. Get the user's local subnet (`ipconfig` on Windows, `ifconfig`/`ip addr` on macOS/Linux)
2. Compare to Twingate Resource definitions in Admin Console
3. Look for overlap: e.g., `192.168.1.0/24` Resource conflicting with the user's home network

**Fix:**

- **Be specific in Resource definitions** -- avoid broad CIDRs like `10.0.0.0/16`
- Prefer specific IPs (`10.0.5.23`) or smaller CIDRs (`10.0.5.0/24`)
- For full-tunnel use cases (untrusted Wi-Fi): use **Exit Networks** (per /docs/exit-networks) -- the proper full-tunnel feature

**`.local` domain caveat:** Don't define `.local` Resources lightly -- conflicts with mDNS/Bonjour for local device discovery. See Twingate's specific KB article for the right pattern.

### Failure Mode 2: Missing Resource Definitions (App Gating)

**Symptoms:**
- SaaS app partially loads; key features broken
- HTTP 401/403 errors on a web app that works without Twingate
- Page loads but styles/scripts/embedded content fail
- App "works sometimes" / "works on some pages but not others"

**Cause:** Twingate only tunnels traffic for **defined Resources**. Modern web apps load resources from many domains (CDN, auth, API subdomains, third-party). Undefined domains bypass the tunnel and fail IP-allowlist checks at the destination.

#### Diagnose with Browser Developer Tools

1. Open the app while signed in to Twingate
2. Browser DevTools -> **Network** tab -> reload page
3. Filter for failed requests (HTTP 401/403, blocked, cancelled)
4. Note the domains in failed requests
5. For each domain, add a **wildcard DNS Resource** (`*.partnersite.com`)
6. Assign same Groups + Security Policies as the primary app Resource
7. Wait for Resources to appear in the Client; reload and retest

**Use wildcard Resources** (`*.partnersite.com`) over individual subdomains -- web apps add subdomains over time.

#### Diagnose with Test Resources (Last Resort)

For tricky apps where DevTools doesn't surface all traffic:

**Setup (Admin Console):**

1. Create two Resources on the affected Remote Network (do NOT assign Groups initially):
   - DNS Resource: `*.*` (name: "Test DNS")
   - IP Resource: `0.0.0.0/0` (name: "Test IP")
2. Create a "Test Group", assign both test Resources to it
3. Add the affected user to the Test Group temporarily

**Test:**

4. User loads the app and completes the broken workflow
5. With test Resources active, all traffic flows through Twingate -- app should work
6. **Immediately remove the user from the Test Group**
7. Review **Network Activity** logs for the test session (User profile or Resource activity page)
8. Find domains/IPs captured by test Resources but NOT covered by existing definitions
9. Add those as permanent Resources (right Groups + Policies)
10. Retest without test Resources
11. **Delete or disable the test Group + test Resources**

**Critical: never leave test Resources enabled for users -- routes ALL traffic through Twingate, breaks normal operation.**

### Decision Notes

- **Most production "broken SaaS" issues** trace to missing Resource definitions for CDN / auth / third-party domains
- Always be specific with Resource CIDRs -- broad ranges = collision risk
- For real full-tunnel: Exit Networks; never use a `0.0.0.0/0` Resource permanently

### Related Docs

- /docs/exit-networks -- Proper full-tunnel feature
- /docs/resources -- Resource definition best practices
- /docs/saas-app-gating-best-practices -- App gating overview
- /docs/dns-failures, /docs/connector-failures, /docs/firewall-failures -- Other failure classes
- /docs/how-to-troubleshoot -- Decision tree
