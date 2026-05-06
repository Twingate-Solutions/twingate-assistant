# Location Requirements (Geoblocking)

## Page Title
Location Requirements via Geoblocking

## Summary
Twingate Enterprise allows admins to control Resource access based on user geolocation using IP address-based country detection. Admins configure allowlists or denylists of countries at the Resource Policy level. Certain countries are always blocked regardless of configuration due to legal restrictions.

## Key Information
- **Tier**: Enterprise only
- Geoblocking is configured per **Resource Policy**, not per individual Resource
- Two restriction modes: **allowlist** (permit listed countries) or **denylist** (block listed countries)
- Location determined via IP address geolocation using MaxMind GeoLite2 data + Google Cloud load balancers
- Coordinates truncated to two decimal places, then mapped to country via Natural Earth boundary data
- Geolocation accuracy is not guaranteed in all cases

## Prerequisites
- Enterprise tier subscription
- Existing Resource Policy to attach location requirements to

## Step-by-Step Configuration
1. Navigate to the target **Resource Policy**
2. Click **Enable** on location requirements
3. Choose restriction type: **Allowlist** or **Denylist**
4. Select countries to allow or deny access

## Permanently Restricted Countries
Always blocked; not configurable or overridable:
- Cuba
- Iran
- North Korea
- Syria

> These countries plus certain non-country regions do not appear in the country selection UI.

## Gotchas
- IP geolocation is inherently imprecise — VPNs, proxies, or ISP routing can cause misattribution
- Restricted countries are silently excluded from the UI selection list — no error shown to admins
- Blocked users see an error message on their device; no fallback access
- Geoblocking applies at the Resource Policy level — all Resources using that policy inherit the restriction
- Non-country regions (e.g., territories) are also always blocked but not documented explicitly

## Common Use Cases
- Compliance-driven blocking of high-risk countries
- Limiting access to office-presence countries only
- Restricting contractor access to known locations

## Related Docs
- Resource Policies
- [Pricing page](https://www.twingate.com/pricing) (Enterprise tier details)