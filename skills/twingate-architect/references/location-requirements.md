# Location Requirements

## Page Title
Location Requirements (Geoblocking)

## Summary
Twingate allows admins to restrict Resource access by country-level geolocation using allowlists or denylists on Resource Policies. Location is determined via IP address geolocation using MaxMind GeoLite2 data and Google Cloud load balancers. This feature is **Enterprise plan only**.

## Key Information
- Configured per **Resource Policy** (not per Resource directly)
- Two modes: **Allowlist** (whitelist specific countries) or **Denylist** (block specific countries)
- IP geolocation accuracy is variable — coordinates truncated to 2 decimal places, then mapped to country
- Country boundary data sourced from [Natural Earth](https://www.naturalearthdata.com/)
- Geolocation data from MaxMind GeoLite2 + Google Cloud load balancers

## Prerequisites
- **Enterprise plan** required
- Must have an existing Resource Policy to configure
- Admin access to Twingate console

## Step-by-Step

1. Navigate to the **Resource Policy** you want to configure
2. Click **Enable** next to **Location Requirements**
3. Choose restriction type:
   - **Allowlist** — only listed countries can access; all others blocked
   - **Denylist** — listed countries are blocked; all others allowed
4. Select target countries from the available list
5. Save the policy

## Configuration Values

| Setting | Options |
|---|---|
| Restriction Type | `Allowlist` or `Denylist` |
| Country Selection | Per-country checkboxes (restricted countries excluded) |

## Gotchas

- **Permanently blocked countries** (cannot be added to allowlists): Cuba, Iran, North Korea, Syria — these do not appear in the selection UI
- Certain non-country regions are also always blocked (unspecified)
- IP geolocation is inherently imprecise — VPNs, proxies, or GeoIP database inaccuracies can affect results
- Location requirements are scoped to the **Resource Policy**, so all Resources under that policy share the same geoblocking rules
- Blocked users see an error message stating their location doesn't meet policy requirements (no bypass option shown)

## Related Docs
- [Resource Policies](https://www.twingate.com/docs/resource-policies)
- [Twingate Pricing](https://www.twingate.com/pricing)