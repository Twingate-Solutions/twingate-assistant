---
source: https://www.twingate.com/docs/internet-security
type: docs
fetched: 2026-11-13
source_version: 9ac576f0a57081246d506d881f22fd5bab5100071c23a4dea242bdc97c56aeed
trust: official
---

# Internet Security Overview

**Source:** https://www.twingate.com/docs/internet-security

## Summary
Twingate Internet Security protects public internet traffic on desktop devices through three features: DNS filtering, automatic DNS-over-HTTPS (DoH) encryption, and Exit Networks. Because Twingate operates at the network level on the device, these protections apply system-wide without per-application configuration.

## Key Information
- **Platform scope:** Internet Security features apply only to users running the Twingate Client on macOS, Windows, or Linux.
- **Headless Clients excluded:** Headless Clients running as Service Accounts never use Internet Security features, regardless of platform.
- **DNS filtering:**
  - Blocks domains hosting security threats.
  - Can restrict access to content categories and specific domains.
  - Available as an add-on for the Business and Enterprise plans.
- **DNS-over-HTTPS (DoH):**
  - Encrypts all DNS traffic regardless of the originating application.
  - No configuration changes needed beyond running the Twingate Client.
- **Exit Networks:**
  - Route all of a user's traffic, not only Resource traffic, through Connectors acting as exit nodes.
- Twingate's DNS handling is designed to be configuration-less for end users.

## Prerequisites
- Twingate Client installed on a macOS, Windows, or Linux device.
- Business or Enterprise plan with the DNS filtering add-on (for DNS filtering only).
- Connectors deployed (implied for Exit Networks, since traffic exits through Connectors).

## Step-by-Step
Not applicable. This is an overview page. Detailed setup lives in the subpages (see Related Docs).

## Configuration Values
None specified on this page.

## Gotchas
- Do not plan Internet Security for Service Accounts or Headless Clients; they are never covered.
- Mobile platforms are not listed as supported; the page only names macOS, Windows, and Linux.
- DNS filtering requires a paid add-on and is limited to Business and Enterprise plans.
- Exit Networks affect all user traffic, not just Twingate Resource traffic, so consider the bandwidth and capacity of the Connectors used as exit nodes.

## Related Docs
- DNS Filtering Overview
- DNS-over-HTTPS (DoH)
- Exit Networks
- DNS and Twingate (how Twingate works with DNS)
- Clients and Headless Clients / Service Accounts documentation