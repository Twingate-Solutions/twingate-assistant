# Configure Cloudflare DoH and DNS Filtering with Twingate

## Summary
Integrates Cloudflare Zero Trust DNS-over-HTTPS (DoH) and optional DNS filtering with Twingate. Requires retrieving a custom DoH URL from Cloudflare and adding it as a custom DoH provider in the Twingate Admin Console.

## Key Information
- Cloudflare Zero Trust trial account is sufficient (no paid tier required)
- DNS filtering policies are optional; DoH protection works independently
- Twingate consumes the Cloudflare DoH URL via its custom DoH provider configuration

## Prerequisites
- Active Cloudflare Zero Trust account (trial acceptable)
- Access to Twingate Admin Console with permission to configure DNS settings

## Step-by-Step

1. **Add a DNS Location in Cloudflare**
   - Navigate to Cloudflare Zero Trust dashboard → **Gateway** → **DNS Locations**
   - Create a new DNS location and save it

2. **Retrieve the Custom DoH URL**
   - Go to **Gateway** → **DNS Locations**
   - Click the newly created location
   - Copy the **DNS over HTTPS** URL

3. **Configure DNS Filtering (Optional)**
   - Navigate to **Policies** in Cloudflare Zero Trust
   - Create desired filtering policies to apply to DNS queries

4. **Add DoH URL to Twingate**
   - In Twingate Admin Console, add the copied Cloudflare DoH URL as a custom DoH provider
   - Follow Twingate's "Configure a Custom DoH resolver" documentation for exact steps

## Configuration Values
| Field | Value |
|-------|-------|
| DoH URL source | Cloudflare Zero Trust → Gateway → DNS Locations → [location] → DNS over HTTPS field |

## Gotchas
- DNS filtering policies (step 3) are independent of DoH setup — DoH can be configured without any filtering policies
- The Cloudflare DoH URL is location-specific; ensure you copy from the correct location if managing multiple

## Related Docs
- [Configure a Custom DoH Resolver in Twingate](https://www.twingate.com/docs/custom-doh) (referenced but not linked inline)
- Twingate Admin Console DNS settings