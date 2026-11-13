---
source: https://www.twingate.com/docs/dns-security
type: docs
fetched: 2026-11-13
source_version: 03a81ab830890a098d8f67363815e208e8ed4ee8ee99a41a84aa6604af58432f
trust: official
---

# DNS-over-HTTPS (DoH)

## Summary
Twingate provides native DoH on the macOS, Windows, and Linux Clients. It encrypts all DNS traffic from every application on the device, with no configuration beyond running the Client. DoH is configured account-wide in the Admin Console under **Internet Security > Secure DNS**.

## Key Information
- **Not available on mobile devices.** Only macOS, Windows, and Linux Clients are supported.
- DoH is **disabled by default**.
- Admin options:
  - Enable or disable DoH for the whole account.
  - Choose the resolver: a pre-configured public resolver or a custom one.
  - Set the fallback behavior.
  - Define Exception Groups.
- **Client behavior:**
  - When a user signs in, the Client fetches the DoH configuration from the server.
  - DoH is enabled unless the user is in an Exception Group.
  - DNS **A queries** not destined for a Twingate Resource are wrapped in DoH requests and sent to the resolver.
  - **AAAA (IPv6) queries are not supported.** Resolution falls back to IPv4 before DoH encapsulation.
  - If the Client starts at login, DoH is active as soon as the Client launches after boot.
- **Exception Groups:** members receive no DoH configuration, and their Client uses the DNS servers configured on the device. Any number of groups can be chosen.

## Prerequisites
- Twingate Client on macOS, Windows, or Linux.
- Admin Console access.
- For a custom resolver: an HTTPS DoH endpoint.

## Setup (Admin Console)
1. Go to **Internet Security > Secure DNS**.
2. Enable DoH for the account.
3. Select a public resolver or enter a custom resolver URL.
4. Choose the fallback method (Strict or Automatic).
5. Optionally add Exception Groups.

## Configuration Values
- **Fallback method:**
  - *Automatic* (default): falls back to regular DNS if the DoH resolver is unavailable or the lookup fails.
  - *Strict*: never falls back. If the resolver is unavailable, all DNS fails, including private DNS the resolver can't resolve.
- **Custom resolver URL template fields:**
  - `${deviceName}`
  - `${deviceId}`
  - `${deviceModel}`
  - `${deviceHostname}`
  - `${userEmail}`
  - Example: `https://doh.example/query?deviceHostname=${deviceHostname}` becomes `https://doh.example/query?deviceHostname=alexs-macbook-pro.local`.

## DoH as a Resource
- If the DoH resolver's domain matches a Twingate Resource, DoH traffic is routed through that Resource. Example: resolver `https://doh.autoco.internal/dns-query` with Resource `doh.autoco.internal`.
- Wildcard Resources such as `*.autoco.internal` are supported.
- The Resource **must have a Device-only Resource Policy**. Otherwise users cannot authenticate and will have no working DNS.

## Gotchas
- Twingate only checks that a custom resolver is an HTTPS endpoint, not that it is a valid DoH resolver. A misconfigured URL combined with **Strict** mode can break DNS for all users.
- Strict mode can break private DNS resolution, because public resolvers can't resolve private names.
- Custom resolvers are most common with DNS filtering services.

## Related Docs
- Twingate Clients (macOS, Windows, Linux)
- Resources and Resource Policies (device-only policies)
- Groups (for Exception Groups)

Source: https://www.twingate.com/docs/dns-security