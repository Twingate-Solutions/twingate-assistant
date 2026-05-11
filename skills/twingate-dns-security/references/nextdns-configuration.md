# NextDNS Integration with Twingate

## Summary
Twingate integrates with NextDNS to provide DNS filtering via DNS-over-HTTPS (DoH). Admins enable the integration from the Admin Console, automatically routing all DNS traffic through a selected NextDNS profile. No additional app installation or network reconfiguration is required.

## Key Information
- Integration provides DNS filtering/security via NextDNS profiles
- Uses DNS-over-HTTPS (DoH) as the transport mechanism
- Automatically pulls configured NextDNS profiles into Twingate Admin Console
- Sends device details to NextDNS per request: **user first name** and **device model**
- Billing for NextDNS is **separate** from Twingate and managed in NextDNS directly

## Prerequisites
- Twingate Admin Console access
- NextDNS account with API key (create at NextDNS account page if needed)
- At least one NextDNS profile configured
- **Platform restriction**: Only available on **macOS, Windows, and Linux** — not mobile

## Step-by-Step Setup
1. Go to **Settings → Secure DNS** in Twingate Admin Console
2. Under **DNS Filtering Integrations**, click **Connect** next to NextDNS
3. Enter the NextDNS API key (from NextDNS account page)
4. Select the desired NextDNS profile as the DoH Resolver
5. Confirm settings — clients will automatically route DNS traffic to selected profile

## Management Operations
| Action | Location |
|--------|----------|
| Change profile | DoH Resolver section → **Change** next to NextDNS |
| Disconnect | DNS Filtering Integrations → NextDNS options → **Disconnect** |

## Configuration Values
- **API Key**: Retrieved from NextDNS account page
- **DoH Resolver**: Set to NextDNS (selectable from Admin Console)
- **Profile**: Selected from auto-pulled list of configured NextDNS profiles

## Gotchas
- Mobile (iOS/Android) is **not supported** — desktop only
- NextDNS billing is independent; Twingate does not manage or consolidate it
- Device metadata (user first name, device model) is sent to NextDNS automatically with no opt-out mentioned
- DNS traffic for **all** users on desktop platforms is routed through the selected profile — no per-user profile assignment documented

## Related Docs
- DNS-over-HTTPS (DoH) — Twingate DoH feature overview
- NextDNS pricing — `nextdns.io/pricing`
- NextDNS account page — API key retrieval