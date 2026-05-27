# Configure Cloudflare DoH and DNS Filtering with Twingate

## Summary
Integrates Cloudflare Zero Trust DNS-over-HTTPS with Twingate, enabling DNS filtering and DoH protection. Requires retrieving a custom DoH URL from Cloudflare and adding it to the Twingate Admin Console as a custom DoH provider.

## Key Information
- Cloudflare Zero Trust trial account is sufficient (paid account not required)
- DNS filtering policies are optional — DoH protection can be used without them
- Integration is one-way: Cloudflare provides the DoH endpoint; Twingate consumes it

## Prerequisites
- Valid Cloudflare Zero Trust account (trial acceptable)
- Access to Twingate Admin Console
- Ability to configure custom DoH resolver in Twingate

## Step-by-Step

1. **Create a DNS Location in Cloudflare**
   - Navigate to Cloudflare Zero Trust dashboard → **Gateway** → **DNS Locations**
   - Add a new DNS location
   - Save and close

2. **Retrieve the Custom DoH URL**
   - Go to **Gateway** → **DNS Locations**
   - Click the newly created location
   - Copy the **DNS over HTTPS** URL

3. **Configure DNS Filtering Rules (Optional)**
   - Go to **Gateway** → **Policies**
   - Create desired filtering policies

4. **Add DoH URL to Twingate**
   - In Twingate Admin Console, add the copied Cloudflare DoH URL as a custom DoH provider
   - Follow Twingate's "Configure a Custom DoH resolver" documentation

## Configuration Values
| Parameter | Source | Notes |
|-----------|--------|-------|
| DoH URL | Cloudflare DNS Location detail page | Unique per location; format is a Cloudflare subdomain URL |

## Gotchas
- DNS filtering policies must be created in Cloudflare separately — they are not automatically applied just by enabling DoH
- The DoH URL is location-specific; ensure you copy from the correct location if managing multiple

## Related Docs
- [Configure a Custom DoH Resolver in Twingate](https://www.twingate.com/docs/custom-doh) *(referenced in source)*
- Cloudflare Zero Trust Gateway DNS Locations documentation