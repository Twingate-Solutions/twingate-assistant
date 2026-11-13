---
source: https://www.twingate.com/docs/nextdns-configuration
type: docs
fetched: 2026-11-13
source_version: 77fbc4febc58deaeefad772fbe1d6c2e6770a71a80761369052a0b579c095730
trust: official
---

# NextDNS Integration Guide

## Summary
Twingate integrates with NextDNS, a DNS filtering service, so admins can use NextDNS as the DNS-over-HTTPS (DoH) resolver for Secure DNS. It is enabled from the Admin Console, and NextDNS profiles can be selected there. No extra app installation or network configuration is needed beyond enabling the integration.

## Key Information
- Secure DNS is available only on macOS, Windows, and Linux Clients. Mobile devices are not supported.
- NextDNS profiles (sets of DNS security settings) are pulled in automatically and can be selected in the Admin Console.
- Once connected, the Twingate Client routes all DNS traffic to the selected NextDNS profile.
- Device details are added to DNS requests so NextDNS admins can view traffic per device. By default Twingate sends the user's **first name** and the **device model**.
- Billing is separate from Twingate and is managed in the NextDNS account page.

## Prerequisites
- Twingate Admin Console access.
- A NextDNS account (one can be created during setup) and its API key, found on the NextDNS account page.
- Desktop Clients (macOS, Windows, Linux).

## Step-by-Step
1. In the Admin Console, go to **Internet Security > Secure DNS**.
2. Under **DNS Filtering Integrations**, select **Connect** next to NextDNS.
3. Enter the NextDNS API key (or create a NextDNS account if you don't have one).
4. Select the NextDNS profile to use as the DoH Resolver and confirm.

**Change profile:** select **Change** next to NextDNS in the DoH Resolver section.
**Disconnect:** in the DNS Filtering Integrations section, open the NextDNS options and select **Disconnect**.

## Configuration Values
- **NextDNS API key**: obtained from the NextDNS account page and entered in the Admin Console.
- **NextDNS profile**: chosen as the DoH Resolver.
- No environment variables, CLI flags, or API parameters are documented on this page.

## Gotchas
- Mobile clients do not get Secure DNS or NextDNS filtering.
- User first name and device model are shared with NextDNS by default. Consider privacy implications.
- NextDNS billing is not part of the Twingate subscription, so check NextDNS pricing separately.

## Related Docs
- Twingate DNS-over-HTTPS (DoH) / Secure DNS documentation
- NextDNS account page and pricing (NextDNS site)