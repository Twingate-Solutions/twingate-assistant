---
source: https://www.twingate.com/docs/location-requirements
type: docs
fetched: 2026-08-05
source_version: 26e02da492797bf4d13b26053ab7927a959cf7512e2d3da36b479e7a2ae72658
---

# Location Requirements

## Page Title
Location Requirements (Geoblocking)

## Summary
Twingate allows admins to restrict Resource access by country-level geolocation using allowlists or denylists on Resource Policies. Location is determined via IP address geolocation using MaxMind GeoLite2 data and Google Cloud load balancers. This feature is Enterprise plan only.

## Key Information
- Configured per **Resource Policy** (not per Resource directly)
- Two modes: **Allowlist** (whitelist specific countries) or **Denylist** (block specific countries)
- Location determined by IP → geo-coordinates (truncated to 2 decimal places) → country mapping
- Uses MaxMind GeoLite2 + Google Cloud load balancer data
- Country boundary data from Natural Earth
- Blocked users see an explicit error message about location policy

## Prerequisites
- **Enterprise plan** required
- Admin access to configure Resource Policies
- Resource Policy must exist before enabling location requirements

## Step-by-Step

1. Open the target **Resource Policy**
2. Click **Enable** next to **Location Requirements**
3. Choose restriction type:
   - **Allowlist**: only listed countries allowed; all others blocked
   - **Denylist**: listed countries blocked; all others allowed
4. Select countries for the chosen restriction type
5. Save the policy

## Configuration Values

| Setting | Options |
|---|---|
| Restriction Type | `Allowlist` \| `Denylist` |
| Country Selection | Any country except permanently blocked ones |

## Permanently Blocked Countries (cannot be overridden)
- Cuba
- Iran
- North Korea
- Syria
- Certain non-country regions (unspecified)

These countries do not appear in the selection UI at all.

## Gotchas
- **IP geolocation is not precise** — accuracy varies; VPNs, proxies, or unusual routing can cause misidentification
- Geoblocking applies at the **Resource Policy level**, so multiple Resources sharing a policy are all affected
- Permanently restricted countries are silently excluded from the country picker — no override possible
- Coordinates are truncated to 2 decimal places before country mapping, which can cause edge-case misclassification near borders

## Related Docs
- [Resource Policies](https://www.twingate.com/docs/resource-policies)
- [Pricing Page](https://www.twingate.com/pricing)