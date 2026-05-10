# Location Requirements (Geoblocking)

## Page Title
Location Requirements via Geoblocking

## Summary
Twingate Enterprise allows admins to control Resource access based on user geolocation using IP address-based country detection. Admins configure allowlists or denylists of countries within Resource Policies. Certain countries are permanently blocked regardless of configuration.

## Key Information
- **Tier**: Enterprise only
- Geoblocking is configured at the **Resource Policy** level
- Uses IP-based geolocation via MaxMind GeoLite2 data + Google Cloud load balancers
- Coordinates truncated to 2 decimal places, then mapped to country using Natural Earth boundary data
- Two restriction modes: **Allowlist** (permit listed countries) or **Denylist** (block listed countries)

## Prerequisites
- Enterprise tier subscription
- Existing Resource Policy to attach location requirements to

## Step-by-Step Configuration
1. Navigate to the Resource Policy to modify
2. Click **Enable** on location requirements
3. Choose restriction type: **Allowlist** or **Denylist**
4. Select target countries for the chosen restriction type

## Configuration Values
| Option | Description |
|--------|-------------|
| Allowlist | Only listed countries can access Resources using this policy |
| Denylist | Listed countries are blocked from Resources using this policy |

## Permanently Blocked Countries
Always blocked, non-configurable, cannot be overridden:
- Cuba
- Iran
- North Korea
- Syria

These countries do not appear in the country selection UI. Additional non-country regions are also permanently blocked.

## Gotchas
- **Accuracy limitations**: IP geolocation is inherently imprecise; VPNs, proxies, or mobile IPs can misrepresent location
- Permanently blocked countries cannot be added to allowlists — no override possible
- Blocked users see an error message on their device (no bypass from client side)
- Geoblocking applies per Resource Policy, not per individual Resource directly

## Common Use Cases
- Compliance-driven blocking of high-risk countries
- Restricting access to office-presence countries only
- Limiting contractor access to known geographic regions

## Related Docs
- Resource Policies documentation
- Twingate pricing page (Enterprise tier)