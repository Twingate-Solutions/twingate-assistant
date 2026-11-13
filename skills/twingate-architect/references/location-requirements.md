---
source: https://www.twingate.com/docs/location-requirements
type: docs
fetched: 2026-11-13
source_version: 5612b0771c6e2239ea3d684662b01553dbc1692b27da26993103ba0daf1ac839
trust: official
---

# Location Requirements

## Summary
Twingate Location Requirements let admins restrict access to Resources by country using allowlists or denylists configured on individual Resource Policies. Location is determined from the device's IP address. The feature (geoblocking) is Enterprise plan only.

## Key Information
- Applies per Resource Policy, so it controls every Resource assigned to that policy.
- Two restriction types:
  - **Allowlist**: only devices in the selected countries can access; all others are blocked.
  - **Denylist**: devices in the selected countries are blocked; all others are allowed.
- Common use cases: blocking high-risk countries for compliance, limiting access to countries with company offices, restricting contractors to known working locations.
- Location method: IP address is mapped to geographic coordinates, truncated to two decimal places, then mapped to a country using Natural Earth boundary data.
- Coordinate sources: MaxMind GeoLite2 data and Google Cloud load balancers.
- Blocked devices see an error message saying their location does not meet the policy requirements.

## Prerequisites
- Twingate Enterprise plan.
- Admin access to edit Resource Policies.

## Step-by-Step
1. Open the Resource Policy to configure.
2. Click **Enable** next to **Location Requirements**.
3. Choose **Allowlist** or **Denylist**.
4. Select the countries for that restriction type.
5. Save the policy.

## Configuration Values
No env vars, CLI flags, or API parameters are documented on this page. Configuration is done in the Admin Console UI:
- Location Requirements: Enable toggle
- Restriction type: Allowlist | Denylist
- Country selection list

## Gotchas
- IP-based geolocation accuracy varies and may be imprecise (e.g., VPNs, mobile carriers, shared egress IPs).
- Cuba, Iran, North Korea, and Syria are always blocked due to embargoes or legal restrictions. This cannot be overridden, and these countries don't appear in the selectable list.
- Certain non-country regions are also always blocked.
- With an allowlist, any country not selected is blocked, so check the list carefully to avoid locking out legitimate users.
- Settings are per policy. Resources under other policies are not affected.

## Related Docs
- Resource Policies
- Twingate pricing page (plan availability)
- Natural Earth (boundary data) and MaxMind GeoLite2 (geolocation data)