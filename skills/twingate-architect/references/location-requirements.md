# Location Requirements

## Page Title
Location Requirements (Geoblocking)

## Summary
Twingate allows admins to restrict Resource access based on country-level geolocation using allowlists or denylists configured on Resource Policies. Location is determined via IP address geolocation using MaxMind GeoLite2 data and Google Cloud load balancers. This feature is Enterprise-only.

## Key Information
- Configured per **Resource Policy** (not per individual Resource)
- Two modes: **Allowlist** (whitelist specific countries) or **Denylist** (blacklist specific countries)
- IP-to-country resolution uses MaxMind GeoLite2 + Google Cloud load balancers → coordinates truncated to 2 decimal places → mapped to country via Natural Earth boundary data
- Blocked users see an error message indicating location doesn't meet policy requirements

## Prerequisites
- **Enterprise plan** required
- Must have an existing Resource Policy to configure
- Admin access to Twingate console

## Step-by-Step Configuration
1. Open the target **Resource Policy**
2. Click **Enable** next to **Location Requirements**
3. Choose restriction type:
   - **Allowlist** – only listed countries can access Resources
   - **Denylist** – listed countries are blocked; all others allowed
4. Select target countries from the list

## Configuration Values
| Setting | Options |
|---|---|
| Restriction Type | `Allowlist` or `Denylist` |
| Country Selection | Any country except permanently blocked ones |

## Permanently Blocked Countries (non-overridable)
These never appear in the selection list:
- Cuba
- Iran
- North Korea
- Syria
- Certain non-country regions (unspecified)

## Gotchas
- **Geolocation accuracy varies** — IP-based location is not always precise; VPNs, proxies, or unusual ISP routing can cause misclassification
- Permanently restricted countries **cannot be added to an allowlist** — they are always blocked regardless of policy
- Location requirements are policy-scoped — if a Resource isn't assigned to a configured policy, geoblocking won't apply
- Feature is **Enterprise-only** — not available on lower-tier plans

## Related Docs
- [Resource Policies](https://www.twingate.com/docs/resource-policies)
- [Pricing Page](https://www.twingate.com/pricing)
- MaxMind GeoLite2 (external)
- Natural Earth boundary data (external)