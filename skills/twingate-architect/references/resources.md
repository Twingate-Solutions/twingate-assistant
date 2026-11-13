---
source: https://www.twingate.com/docs/resources
type: docs
fetched: 2026-11-13
source_version: 761e52563047158f72139d5eeca218606ce411be0c8e1541a5126b84a30b77ad
trust: official
---

# Page Title
Twingate Resources

## Summary
A Resource is any network address (FQDN, wildcard, IP, or CIDR) that users reach through Twingate. Addresses are resolved from the Connector(s) in the Resource's Remote Network, so private DNS and private IPs work without DNS changes. Access is denied by default and granted through groups.

## Key Information
- **Common scenarios:** private DNS (`host.autoco.internal`, `*.autoco.internal`), private IP or CIDR, and IP allowlisting of public SaaS destinations (traffic exits via the Connector).
- **Resource fields:** label, address, alias, port restrictions, Remote Network, tags (optional), client visibility, and group access.
- **Address types:** FQDN, wildcard FQDN, IP, CIDR. Unqualified names (e.g. `host`) need extra Connector configuration and the latest Client.
- **Wildcards:** `*` matches 0 or more characters, `?` matches exactly 1. `*.autoco.internal` matches subdomains at any depth but not `autoco.internal` itself.
- **Aliases:** an extra address for the Resource. No DNS entry is needed, and the alias need not be resolvable from the Connector.
- **Default traffic:** all TCP and UDP ports plus ICMP ping.
- **Resolution:** done at the Connector, so local IPs and private DNS names work for remote users.
- **Overlap precedence:** the most specific match wins. Single IP beats a smaller CIDR, which beats a larger CIDR. An exact domain beats a wildcard, and a wildcard with more literal characters beats a broader one. Truly ambiguous matches are picked arbitrarily.
- **Visibility options:** Standard Address (listed in the Client), Browser Address (listed with an "Open in Browser" shortcut), Background Address (only under "Hidden Resources"). These do not affect Admin Console visibility.

## Prerequisites
- A Remote Network with at least one Connector that can resolve and route to the Resource address.
- For port restrictions: all Connectors on the Remote Network must be v1.20.0 or higher.
- Groups to grant access (no access is given by default).

## Step-by-Step (conceptual)
1. Choose the Remote Network.
2. Define the label and address (FQDN, wildcard, IP, or CIDR).
3. Optionally add an alias, port restrictions, tags, and visibility.
4. Assign groups for access, and review via the Access Graph on the Resource detail page.

## Configuration Values
- Port restrictions: TCP and UDP set separately (e.g. TCP 22,443 and UDP 53). ICMP can be enabled or blocked.
- To give different users different ports on one host, create separate Resources (e.g. `host.autoco.internal:22` and `host.autoco.internal:443`) and assign each to different groups.
- Reserved Client subnet: `100.96.0.0/12`.

## Gotchas
- Invalid CIDRs such as `10.1.0.1/16` return the error `Invalid IP or FQDN`. Use the network address (e.g. `10.1.0.0/16`).
- Client blocks access to IPs in `100.96.0.0/12` (reserved CGNAT range).
- With DNS rebinding protection, a public DNS name that resolves to a private IP should be defined as a DNS Resource. Preferred order: private DNS resolution, FQDN Resource, private IP Resource, then CIDR Resource (least granular).
- Port restriction options don't appear if any Connector is older than v1.20.0.
- Avoid overlapping addresses where possible. See the IP overlap guide.

## Related Docs
- How DNS Works with Twingate
- Whitelisting Traffic to Public Resources
- Resource aliases
- Port restrictions
- Hiding resources in the Client
- Upgrading Connectors
- IP overlap guide
- Tags