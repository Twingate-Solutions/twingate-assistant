# Location Requirements (Twingate Geoblocking)

## Summary
Twingate restricts Resource access by country-level geolocation via allowlists or denylists configured on Resource Policies. IP-based geolocation determines device location using MaxMind GeoLite2 and Google Cloud load balancer data. This feature is exclusive to the Enterprise plan.

## Key Information
- Operates at **country level** only (not city/region)
- Configured per **Resource Policy** (affects all Resources assigned to that policy)
- Two modes: **allowlist** (whitelist countries) or **denylist** (blocklist countries)
- Location determined via IP → coordinates (truncated to 2 decimal places) → country mapping
- Country boundary data from [Natural Earth](https://www.naturalearthdata.com/)
- Geolocation accuracy is not guaranteed in all cases

## Prerequisites
- **Enterprise plan** required
- Admin access to Twingate console
- Resource Policy must exist before enabling location requirements

## Step-by-Step Configuration
1. Navigate to the target **Resource Policy**
2. Click **Enable** next to **Location Requirements**
3. Choose restriction type:
   - **Allowlist** – only listed countries can access; all others blocked
   - **Denylist** – listed countries are blocked; all others allowed
4. Select countries from the provided list
5. Save the policy

## Configuration Values
| Setting | Options |
|---|---|
| Restriction Type | `Allowlist` / `Denylist` |
| Country Selection | UI-based multi-select (per policy) |

## Permanently Blocked Countries (Cannot Override)
These countries are always blocked regardless of policy configuration and **do not appear** in the country selection list:
- Cuba
- Iran
- North Korea
- Syria
- Certain non-country regions (unspecified)

## Gotchas
- **VPNs/proxies** can defeat IP-based geolocation — not a substitute for strong auth controls
- Blocked users see an error message stating their location doesn't meet policy requirements (no workaround from user side)
- Location requirements are scoped to the **policy**, not individual Resources — changing a policy affects all Resources under it
- Geolocation accuracy varies; edge cases (border regions, satellite IPs, mobile carriers) may be misclassified

## Common Use Cases
- Compliance blocking of high-risk countries
- Restricting access to office-present countries only
- Limiting contractor access to known geographic locations

## Related Docs
- [Resource Policies](https://www.twingate.com/docs/resource-policies)
- [Pricing Page](https://www.twingate.com/pricing) (Enterprise plan)