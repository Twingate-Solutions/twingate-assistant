---
name: twingate-dns-security
description: >
  Twingate Internet Security — DNS filtering, exit networks, browser security,
  and DNS-over-HTTPS. Load when the user mentions DNS filtering, content filtering,
  internet security, exit networks, egress routing, browser security, NextDNS,
  DoH, DNS categories, or profile priority. Also trigger on 'Internet Security',
  'DNS Security Profile', 'fixed egress IP', or 'SaaS allowlisting' in a Twingate
  context.
---

## Role

This skill owns Twingate's Internet Security product area: DNS filtering, exit networks, DNS-over-HTTPS, and browser security. It covers DNS Security Profile design, priority ordering, group-based policy assignment, exit network egress patterns, and the licensing boundary between Internet Security and Private Access. It is the authority on when to use DNS filtering versus exit networks versus resource-level access policy.

## Decisions & Guidelines

- **Confirm Internet Security entitlement before designing any solution around DNS filtering or exit networks.** Internet Security is a separate product area and may require a different license tier. If the customer doesn't have entitlement, DNS Security Profiles and exit network configuration won't appear in the admin console.
- **Exit networks route traffic to a fixed egress point — they do not block destinations.** If the goal is to prevent access to a website, use DNS filtering. If the goal is to ensure traffic exits from a fixed IP, use an exit network. These are not substitutes.
- **Priority is numeric, and lower number = higher priority.** This is the most commonly confused aspect of DNS Security Profile assignment. A permissive Engineering profile at priority 1 beats a restrictive Corporate profile at priority 2, even when the user is in both groups.
- **Always configure the "Everyone" group as a baseline with at minimum malware and phishing categories blocked.** Users not in any group with a profile receive no filtering at all. "Everyone" is the safety net.
- **Enable STRICT fallback mode only after pre-populating the allow list with the customer's known-good domains.** STRICT mode (deny-by-default) will block legitimate SaaS tools until they are explicitly allowed. Always roll out STRICT to a pilot group first.
- **DNS-over-HTTPS in Twingate covers only DNS queries that flow through the Twingate Client.** It does not encrypt OS-level DNS for non-Twingate traffic or queries made before the Client starts. If full-device DoH is required, configure it at the OS or network level in addition to Twingate.

## Routing

- **→ twingate-identity**: DNS Security Profiles attach to Groups; for group management, SCIM provisioning, or understanding how group membership determines which profile applies
- **→ twingate-architect**: for split DNS model questions — understanding which DNS queries Twingate intercepts before configuring Internet Security
- **→ twingate-troubleshoot**: when DNS filtering appears to be interfering with private resource access or general connectivity

## References

See [`references/`](./references/) for auto-generated doc summaries.

Key references:
- [`dns-security-overview.md`](./references/dns-security-overview.md) — DNS Security feature overview, exit node configuration, filtering policy setup, DoH enforcement
