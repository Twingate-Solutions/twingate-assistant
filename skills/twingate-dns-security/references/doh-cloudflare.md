# How to Configure Cloudflare DoH and DNS Filtering with Twingate

## Summary
Integrates Cloudflare Zero Trust DNS-over-HTTPS (DoH) and optional DNS filtering with Twingate. Involves creating a DNS location in Cloudflare, retrieving the custom DoH URL, and configuring it in the Twingate Admin Console.

## Key Information
- Enables Cloudflare DNS filtering policies on top of DoH encryption when used with Twingate
- Cloudflare acts as the custom DoH resolver provider
- DNS filtering rules in Cloudflare are optional but available if needed

## Prerequisites
- Valid Cloudflare Zero Trust account (trial account sufficient)
- Access to Twingate Admin Console with permissions to configure DoH settings

## Step-by-Step

1. **Add a DNS Location in Cloudflare**
   - Navigate to Cloudflare Zero Trust dashboard → **Gateway** → **DNS Locations**
   - Create a new DNS location
   - Save and close the location

2. **Retrieve the Custom DoH URL**
   - Return to **Gateway** → **DNS Locations**
   - Click on the newly created location
   - Copy the **DNS over HTTPS** URL

3. **Set Up DNS Filtering Rules (Optional)**
   - Navigate to **Policies** in Cloudflare Zero Trust
   - Create desired DNS filtering policies

4. **Configure Twingate with the Cloudflare DoH URL**
   - In the Twingate Admin Console, add the copied Cloudflare DoH URL as a custom DoH provider
   - Follow Twingate's "Configure a Custom DoH resolver" documentation

## Configuration Values
| Parameter | Source |
|-----------|--------|
| Custom DoH URL | Copied from Cloudflare Zero Trust → Gateway → DNS Locations → [location] → DNS over HTTPS field |

## Gotchas
- The DoH URL is location-specific — must be retrieved from the specific location you created, not a generic Cloudflare endpoint
- DNS filtering policies are managed entirely in Cloudflare; Twingate only consumes the DoH endpoint
- No mention of per-client or per-network scoping — applies broadly once configured in Twingate

## Related Docs
- [Configure a Custom DoH resolver in Twingate](https://www.twingate.com/docs/custom-doh) *(linked in source)*
- Cloudflare Zero Trust Gateway documentation (external)