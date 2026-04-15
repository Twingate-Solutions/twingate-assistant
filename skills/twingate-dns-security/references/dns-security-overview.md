<!-- initial seed — to be refreshed by pipeline -->

## Page Title
Twingate DNS Security and DNS Filtering Overview

## Summary
Twingate DNS Security routes all internet-bound DNS queries and optionally all internet traffic through Twingate's infrastructure, enabling centralized filtering, threat blocking, and policy enforcement across managed devices. Unlike Resource access (which applies only to traffic destined for private Resources), DNS Security applies to general internet traffic and is configured through Security Policies in the admin console.

## Key Information
- **Scope distinction:** Resource access controls traffic to private Resources; DNS Security controls *all* internet traffic from managed devices — these are two separate, complementary planes
- **DNS-over-HTTPS (DoH) enforcement:** The Twingate Client intercepts and upgrades DNS queries to DoH, preventing DNS leakage over plaintext UDP/53 and blocking users from bypassing filters by switching DNS servers
- **Exit nodes:** A designated Connector acts as an egress point; internet-bound traffic from managed devices leaves through that Connector's public IP, enabling IP allowlisting at SaaS providers and consistent geo-egress
- **DNS filtering policies:** Admins define block/allow lists and subscribe to threat-intelligence categories (malware, phishing, command-and-control, adult content, etc.); matched queries are blocked before resolution
- **Device trust integration:** DNS Security policies can be scoped to device posture groups — e.g., enforce stricter filtering for BYOD devices or unmanaged endpoints, while allowing managed corporate devices broader access
- **Always-on enforcement:** When DNS Security is active, filtering applies regardless of whether the user is accessing a private Resource; there is no "split" that would let internet traffic bypass policy

## Prerequisites
- Twingate Business or Enterprise plan (DNS Security is not available on the Starter tier)
- At least one Connector deployed and online to serve as an exit node (if exit node egress is required)
- Twingate Client 4.x or later installed on managed devices
- Security Policies feature enabled in the tenant (Admin > Security > DNS Security)
- Device trust / MDM enrollment if policy scoping by device posture is needed

## Step-by-Step
1. Navigate to **Admin Console > Security > DNS Security** and enable the feature for your tenant.
2. Create or edit a **Security Policy** — assign it a name and choose the target group (all users, or a specific group).
3. Under **DNS Filtering**, enable threat categories to block (malware, phishing, botnet C2, etc.) and optionally add custom domain block/allow list entries.
4. Under **Exit Node**, select the Connector that internet-bound traffic should egress through; configure the Remote Network that Connector belongs to.
5. Enable **DoH enforcement** to prevent DNS bypass — the Client will reject non-DoH resolver configurations on the device.
6. If using device trust scoping, create separate Security Policies per device posture group and assign accordingly in **Access > Groups**.
7. Deploy/update the Twingate Client on target devices; verify DNS Security status appears as active in the Client UI tray icon.
8. Test by attempting to resolve a known-blocked domain (e.g., a test phishing domain from your threat intelligence vendor) — confirm the Client shows a block page or NXDOMAIN response.

## Configuration Values
- **Threat categories:** Malware, Phishing, Command & Control (C2), Cryptomining, Adult Content, Gambling — each toggled independently per policy
- **Custom block list:** Individual FQDNs or wildcard domains (e.g., `*.example-bad.com`)
- **Custom allow list:** Domains whitelisted from category blocks (useful for legitimate services miscategorized by threat feeds)
- **Exit node Connector:** One Connector per Security Policy designated as the egress point; multiple policies can reference different Connectors for geo-specific egress
- **DoH enforcement:** Boolean per policy — when enabled, the Client ignores OS DNS resolver settings and uses Twingate's DoH endpoint exclusively

## Gotchas
- **Exit node Connector carries all internet traffic** — size the host appropriately; a Connector handling exit node traffic for hundreds of users needs significantly more CPU/bandwidth than one serving only Resource access
- **DNS Security and Resource access use the same Client tunnel** — enabling DNS Security does not create a separate VPN-like tunnel; it extends the existing Twingate tunnel to cover internet traffic, so there is no double-tunneling overhead
- **DoH enforcement can break captive portals** — hotel/airport Wi-Fi captive portals rely on DNS hijacking; consider a policy exception or automatic captive portal detection (check Twingate Client release notes for the relevant version)
- **Policy evaluation order matters** — allow list entries take precedence over category blocks; if a malicious domain is on an allow list, it will not be blocked even if the malware category is enabled
- **Exit node is not the same as a Connector for Resource access** — the exit node Connector does not need to be co-located with your Resources; it can be a dedicated internet-egress Connector in a cloud region
- **Filtering applies to DNS queries, not TLS SNI or HTTP payloads** — DNS Security cannot inspect encrypted payloads; it blocks at the resolution layer only; HTTPS connections to IPs (bypassing DNS) are not filtered

## Related Docs
- `/docs/dns-security` — DNS Security feature overview
- `/docs/dns-security/exit-nodes` — Configuring Connectors as exit nodes
- `/docs/dns-security/filtering-policies` — Block/allow list and category configuration
- `/docs/dns-security/doh` — DNS-over-HTTPS enforcement details
- `/docs/security-policies` — Security Policies overview and group scoping
- `/docs/device-trust` — Device posture integration for policy scoping
