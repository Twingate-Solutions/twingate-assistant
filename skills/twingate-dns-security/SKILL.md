---
name: twingate-dns-security
description: |
  Twingate Internet Security — DNS filtering, exit networks, browser security,
  and DNS-over-HTTPS. Use this skill when the user mentions DNS filtering,
  content filtering, internet security, exit networks, egress routing, browser
  security, NextDNS, DoH, or DNS categories.
---

# Twingate DNS Security

## When to Use This Skill

Trigger this skill when the user:

- Asks about DNS filtering, content filtering, or category-based DNS blocking in Twingate
- Wants to block or allow specific categories of internet traffic (malware, phishing, social media, streaming, etc.)
- Asks about exit networks, fixed egress IPs, or egress routing through Twingate
- Needs a fixed public IP for SaaS allowlisting (e.g., Office 365, Salesforce, Okta IP restrictions)
- Mentions Internet Security, DNS Security Profiles, NextDNS, or DNS-over-HTTPS in a Twingate context
- Asks about browser security controls in Twingate
- Is configuring different filtering policies for different user groups or departments
- Asks how DNS filtering interacts with Twingate's split DNS model or private resource access
- Needs to route contractor or department traffic through a compliance egress point

## Quick Reference

| Concept | Attached to | Purpose |
|---|---|---|
| DNS Security Profile | Group | Block/allow DNS categories for group members |
| Exit Network | Group | Route internet traffic through a fixed egress point |
| NextDNS Integration | Tenant | Extended filtering via NextDNS category library |
| DNS-over-HTTPS (DoH) | Tenant | Encrypted DNS resolution for Twingate-mediated queries |
| Browser Security | Tenant / Group | Browser-level access controls |

**Profile priority:** Lower priority number wins. "Everyone" is the lowest-priority catch-all.
**Internet Security is a separate product area from Private Access.** Confirm the customer has an entitlement before designing around it.

## Evergreen Knowledge

### Internet Security vs. Private Access

Twingate has two distinct product areas:

- **Private Access** — the core ZTNA product. Secure, identity-aware access to private resources (internal apps, databases, cloud services). This is what Connectors, Remote Networks, and Resources are about.
- **Internet Security** — DNS filtering, exit networks, browser security, and DoH. This governs how users' general internet traffic is handled when Twingate is active.

A customer can have Private Access without Internet Security, and vice versa. Internet Security features require a separate license or plan tier in some configurations. Always confirm entitlement before designing a DNS filtering or exit network solution.

Both areas coexist on the same Client. When a user browses an internal app, Private Access handles it. When the same user visits a public website, Internet Security (if configured) governs filtering and egress.

### DNS Filtering

DNS filtering intercepts DNS resolution for internet-bound traffic and applies policy based on the category of the destination domain. Blocked domains return a block page or NXDOMAIN; allowed domains resolve normally.

**Categories**
Twingate organizes domains into categories including (but not limited to):
- Security: malware, phishing, cryptomining, ransomware
- Adult content
- Gambling
- Social media
- Streaming / video
- Gaming
- Piracy / torrenting
- Advertising and trackers
- Productivity risks (varies by configuration)

Category coverage is maintained by Twingate's classification engine. Domains can fall into multiple categories. Custom allow/block lists can supplement category-based policy for domains not classified as expected.

**DNS Security Profiles**
A DNS Security Profile is the configuration object that defines filtering policy. Each profile specifies:
- Which categories are blocked
- Which categories are explicitly allowed
- The fallback method: **AUTO** or **STRICT**
  - **AUTO**: if a domain doesn't match any category rule, it resolves normally (permissive default)
  - **STRICT**: if a domain isn't on the explicit allow list, it is blocked (deny-by-default)

STRICT mode is appropriate for high-security environments but requires maintaining an allow list of legitimate domains — it will break unfamiliar SaaS tools until they are added. AUTO is the practical default for most enterprise deployments.

**Profiles Are Assigned to Groups, Not Users**
DNS Security Profiles attach to Twingate Groups. Every member of the group inherits the profile. There is no per-user profile assignment — access control granularity is at the group level, consistent with the rest of Twingate's policy model.

Assign profiles to IdP-synced groups (via SCIM) for automatic membership management. Avoid manually-managed groups for filtering policy unless SCIM is not available.

**Priority and Conflict Resolution**
A user can belong to multiple groups, each with a different DNS Security Profile. Priority resolves conflicts:
- Priority is a numeric value on each group's profile assignment — lower number = higher priority (wins)
- The highest-priority profile that matches the user is applied; lower-priority profiles for the same user are not evaluated for that session
- The built-in "Everyone" group can have a profile assigned; it always acts as the lowest-priority catch-all
- If a user is in no group with an assigned profile, no DNS filtering is applied to their traffic

Design priority deliberately. If a permissive profile (e.g., "Engineering — relaxed") has a lower priority number than a restrictive profile (e.g., "Corporate — standard"), Engineering users in both groups will get the permissive profile. Test priority ordering before rolling out to production.

**Everyone Group as Baseline**
The "Everyone" system group contains all users in the tenant. Assigning a profile to "Everyone" creates an org-wide filtering baseline. Specific groups can then have higher-priority profiles that override the baseline for their members. This is the recommended pattern: configure "Everyone" with a sensible default (malware + phishing block at minimum), then layer department-specific profiles on top.

### Exit Networks

An exit network routes a user's general internet traffic (traffic that does not match a Twingate-managed private Resource) through a specific egress point, giving that traffic a fixed, predictable public IP address.

**Primary Use Cases**

1. **SaaS IP allowlisting** — Many SaaS platforms (Office 365, Salesforce, Okta, GitHub Enterprise, etc.) support restricting access to known IP ranges. Without an exit network, remote users access SaaS from their ISP's dynamic IP, which cannot be added to an allowlist. With an exit network, all traffic exits from a fixed IP that can be added once and never change.

2. **Regional compliance egress** — Regulations (GDPR, data sovereignty requirements) may require that certain users' internet traffic exit through a specific country or region. An exit network anchored in that region satisfies the requirement.

3. **Compliance egress logging** — Some compliance frameworks require that all internet traffic from employees flows through a logged egress point. An exit network provides the fixed egress; a firewall or proxy at that egress can provide logging.

**What Exit Networks Are NOT**
Exit networks do not restrict what users can access — they only control where traffic exits. An exit network does not block a website; DNS filtering does. Do not conflate the two. Specifically:
- If you want to prevent access to a SaaS app, use DNS filtering (block the domain) or a Twingate Resource policy, not an exit network
- If you want traffic to a SaaS app to come from a fixed IP, use an exit network

**Exit Network Types**
Twingate supports both cloud-hosted and customer-managed exit networks:
- **Cloud-hosted** — Twingate operates the egress infrastructure. Traffic exits through Twingate's PoP in the configured region.
- **Customer-managed** — The customer's own Connector (in a VPC or data center with a fixed public IP or NAT gateway) acts as the egress point. This requires configuring the Connector with exit network capability. Useful when the customer already owns static IPs or has specific egress infrastructure.

Multiple exit networks can be configured per tenant. Each exit network is assigned to one or more groups. Members of those groups have their internet traffic routed through the assigned exit network.

### NextDNS Integration

Twingate integrates with NextDNS to extend DNS filtering beyond Twingate's native category library. The integration works as follows:
- The customer creates a NextDNS profile in the NextDNS dashboard, configuring advanced category blocks, custom blocklists, allow lists, and analytics
- The NextDNS profile ID is linked to Twingate's Internet Security configuration at the tenant level
- Twingate forwards applicable DNS queries to the customer's NextDNS profile for resolution and filtering

NextDNS's category library is broader than Twingate's native categories and includes threat intelligence feeds, parental controls, and fine-grained productivity filtering. Use NextDNS when the native Twingate categories are insufficient or when the customer already has a NextDNS profile they want to reuse.

Note: NextDNS integration is configured at the tenant level, not per group. All users are subject to the NextDNS profile when it is enabled, in addition to any group-level Twingate DNS Security Profiles.

### DNS-over-HTTPS (DoH)

DNS-over-HTTPS encrypts DNS resolution to prevent ISPs, network operators, or passive observers from seeing which domains users are resolving. When DoH is enabled in Twingate:
- DNS queries that flow through Twingate's DNS interception (for private resources and Internet Security filtering) are sent over HTTPS rather than plain UDP/TCP port 53
- This protects the DNS resolution path from eavesdropping and tampering

**Important scope limitation:** DoH in Twingate only covers DNS queries that Twingate intercepts. It does not encrypt OS-level DNS queries for traffic outside Twingate's scope. If a user's device makes DNS queries that bypass the Twingate Client (e.g., before the Client connects, or for traffic not in Twingate's scope), those queries go through the system resolver unencrypted unless the customer separately configures DoH at the OS or network level.

DoH is configured at the tenant level in the Twingate admin console.

### Browser Security

Twingate's browser security feature provides additional controls for browser-based access patterns. This feature set evolves with the product — refer to current documentation for the specific controls available. Check `./references/` or fetch the canonical doc at `https://www.twingate.com/docs/browser-security` for current configuration steps.

## Current Documentation

Reference files in `./references/` are auto-generated by the update pipeline and contain summaries of current Twingate documentation. Read them for up-to-date configuration steps, category lists, and UI-specific instructions.

If a reference file is missing or appears outdated, fetch the canonical doc directly:

```
curl -s https://www.twingate.com/docs/dns-filtering
curl -s https://www.twingate.com/docs/exit-networks
curl -s https://www.twingate.com/docs/browser-security
curl -s https://www.twingate.com/docs/nextdns
curl -s https://www.twingate.com/docs/dns-over-https
curl -s https://www.twingate.com/docs/dns-security-profiles
```

Key doc slugs for this skill:
- `dns-filtering` — category overview and profile configuration
- `dns-security-profiles` — profile creation, fallback modes, and group assignment
- `exit-networks` — cloud-hosted and customer-managed egress configuration
- `nextdns` — NextDNS integration setup
- `dns-over-https` — DoH configuration and scope
- `browser-security` — browser security controls

## Common Patterns

**Org-wide malware and phishing block (recommended baseline)**
Assign a DNS Security Profile to the "Everyone" group that blocks malware and phishing categories with fallback mode AUTO. This is the minimum viable Internet Security configuration: protects all users from the most common threats without requiring any department-specific tuning. No other categories are blocked at the baseline — add department profiles on top.

**Department-specific layered filtering**
Create per-department groups (or use IdP-synced groups via SCIM). Assign stricter profiles to groups that require it:
- HR and Finance: block social media, streaming, and gambling in addition to security categories
- Engineering: baseline (malware + phishing) only — engineers need access to broad technical resources
- Contractors: strict profile (malware, phishing, social media, streaming, gaming, piracy blocked) + STRICT fallback

Use priority to ensure department profiles override the "Everyone" baseline for group members.

**SaaS IP allowlisting with exit network**
Configure an exit network for the egress region where the customer's SaaS allowlist expects traffic. Assign the exit network to a group (or "Everyone" for org-wide). Add the exit network's fixed IP to the SaaS platform's IP allowlist (e.g., Office 365 conditional access named locations, Salesforce trusted IP ranges). All users in the assigned group will access SaaS from the fixed IP, satisfying the allowlist requirement regardless of their physical location.

**Contractor compliance egress**
Create a "Contractors" group. Assign a strict DNS Security Profile (block social media, streaming, piracy, gambling) and a compliance exit network (customer-managed egress through a firewall with logging). This gives contractors internet access through a logged, filtered egress point while keeping their traffic separate from employees'.

**NextDNS for advanced filtering**
When Twingate's native categories are insufficient (e.g., customer needs fine-grained parental-style controls, custom domain blocklists, or DNS analytics), configure a NextDNS profile and link it to the tenant. The NextDNS profile supplements native Twingate profiles — both apply simultaneously.

## Anti-Patterns and Gotchas

**Using an exit network to block a website**
Exit networks route traffic to a fixed egress — they do not block destinations. If the goal is to prevent users from accessing a website, configure a DNS Security Profile to block the relevant category or add the domain to a custom block list. Exit networks and DNS filtering serve different purposes and are not substitutes.

**Profile priority misconfiguration**
If a permissive profile (Engineering) has a lower priority number than a restrictive profile (Corporate), users in both groups get the permissive profile — the lower number wins. Always map out which groups users belong to and what their effective priority ordering will be before assigning profiles. Test with a pilot user before org-wide rollout.

**Forgetting the "Everyone" baseline**
If profiles are assigned only to specific groups without configuring "Everyone", users not in those groups receive no DNS filtering at all. Always configure "Everyone" with at minimum a malware + phishing block. Users in specific groups with higher-priority profiles will still get those profiles; "Everyone" only applies where no higher-priority profile exists.

**Assuming DoH encrypts all device DNS**
DoH in Twingate only covers DNS queries that flow through the Twingate Client. OS-level DNS for non-Twingate traffic, DNS queries made before the Client starts, or queries from applications that bypass the system resolver are not encrypted by Twingate's DoH configuration. If full-device DoH is required, the customer must configure it at the OS or network level in addition to Twingate.

**Deploying Internet Security without confirming entitlement**
Internet Security is a separate product area and may require a separate license or higher plan tier. If the customer does not have Internet Security entitlement, DNS Security Profiles and exit network configuration options will not appear in the admin console. Confirm entitlement before building a design that depends on these features.

**Confusing DNS filtering with Private Access resource policy**
DNS filtering governs internet-bound traffic by category. It does not control access to Twingate-managed private Resources — that is handled by Group membership and Resource access policy. Do not attempt to use DNS filtering to restrict access to internal applications. Use Group-level Resource assignment for that.

**STRICT mode blocking legitimate tools**
STRICT fallback mode (deny-by-default) is powerful but will block any domain not on the explicit allow list, including legitimate SaaS tools the customer uses. Before enabling STRICT mode, audit the customer's tool inventory and pre-populate the allow list. Roll out STRICT mode to a pilot group first to catch unintended blocks before applying org-wide.

**DNS filtering interfering with private resource resolution**
Twingate's split DNS model means the Client only intercepts DNS for managed private Resources; all other DNS resolves normally. DNS filtering adds a policy layer on top of non-private-resource DNS resolution. If a private Resource's FQDN happens to fall under a blocked category or domain, investigate whether the domain is being incorrectly classified. Always test connectivity to private resources after enabling DNS filtering.

## Related Skills

- [twingate-architect](../twingate-architect/SKILL.md) — understand the split DNS model before configuring Internet Security DNS features; know which DNS queries Twingate intercepts vs. passes through
- [twingate-identity](../twingate-identity/SKILL.md) — groups are the control plane for profile and exit network assignment; understand group management, SCIM provisioning, and security policies before designing a filtering hierarchy
- [twingate-troubleshoot](../twingate-troubleshoot/SKILL.md) — DNS filtering can interfere with connectivity; troubleshoot DNS issues before assuming connectivity problems are infrastructure-related
