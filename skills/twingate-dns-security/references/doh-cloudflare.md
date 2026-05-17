# Configure Cloudflare DoH and DNS Filtering with Twingate

## Summary
Integrates Cloudflare Zero Trust DNS-over-HTTPS (DoH) with Twingate, enabling DNS filtering alongside DoH protection. Requires retrieving a custom DoH URL from Cloudflare and registering it in the Twingate Admin Console.

## Key Information
- Cloudflare Zero Trust provides both DoH encryption and optional DNS filtering policies
- Twingate accepts Cloudflare's custom DoH endpoint as a custom DoH provider
- DNS filtering policies in Cloudflare are optional but available if needed

## Prerequisites
- Valid Cloudflare Zero Trust account (trial account sufficient)
- Access to Twingate Admin Console with permissions to configure DoH settings

## Step-by-Step

1. **Add a DNS Location in Cloudflare**
   - Navigate to Cloudflare Zero Trust dashboard → **Gateway** → **DNS Locations**
   - Create a new DNS location
   - Save and close

2. **Retrieve the Custom DoH URL**
   - Go to **Gateway** → **DNS Locations**
   - Click your newly created location
   - Copy the **DNS over HTTPS** URL

3. **Configure DNS Filtering Rules (Optional)**
   - Navigate to **Policies** in the Cloudflare Zero Trust dashboard
   - Create desired filtering policies

4. **Register DoH URL in Twingate**
   - Add the copied Cloudflare DoH URL as a custom DoH provider in the Twingate Admin Console
   - Follow Twingate's "Configure a Custom DoH resolver" documentation

## Configuration Values
| Parameter | Value |
|-----------|-------|
| DoH URL source | Cloudflare Zero Trust → Gateway → DNS Locations → [location] → DNS over HTTPS field |

## Gotchas
- The custom DoH URL is location-specific — must be copied from the specific DNS Location you created, not a generic Cloudflare endpoint
- DNS filtering policies only apply if configured in Cloudflare; no filtering occurs by default

## Related Docs
- [Configure a Custom DoH Resolver in Twingate](https://www.twingate.com/docs/custom-doh) — required next step after retrieving the Cloudflare URL
- Twingate DoH documentation (general custom DoH provider setup)