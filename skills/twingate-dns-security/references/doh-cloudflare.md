# How to Configure Cloudflare DoH and DNS Filtering with Twingate

## Summary
Integrates Cloudflare Zero Trust DNS-over-HTTPS (DoH) and DNS filtering with Twingate by configuring a Cloudflare DNS location and adding its DoH URL as a custom resolver in Twingate's Admin Console.

## Key Information
- Requires a Cloudflare Zero Trust account (trial account sufficient)
- Cloudflare handles DNS filtering via Gateway Policies; Twingate consumes the DoH endpoint
- DNS filtering rules in Cloudflare are optional — DoH protection works without them

## Prerequisites
- Active Cloudflare Zero Trust account (trial acceptable)
- Access to Twingate Admin Console
- Familiarity with Twingate custom DoH resolver configuration

## Step-by-Step

1. **Create a DNS Location in Cloudflare**
   - Navigate to Cloudflare Zero Trust dashboard → **Gateway** → **DNS Locations**
   - Add a new DNS location and save

2. **Retrieve the Custom DoH URL**
   - Return to **Gateway** → **DNS Locations**
   - Click the newly created location
   - Copy the **DNS over HTTPS** URL

3. **Configure DNS Filtering Rules (Optional)**
   - Navigate to **Policies** in Cloudflare Zero Trust dashboard
   - Create desired filtering policies

4. **Add DoH URL to Twingate**
   - In Twingate Admin Console, add the Cloudflare DoH URL as a custom DoH provider
   - Follow Twingate's "Configure a Custom DoH resolver" documentation

## Configuration Values
| Parameter | Source | Notes |
|-----------|--------|-------|
| DoH URL | Cloudflare DNS Location detail page | Unique per location; format: `https://<id>.cloudflare-gateway.com/dns-query` |

## Gotchas
- The DoH URL is location-specific — must copy from the correct location after creation, not during
- DNS filtering policies are Cloudflare-side configuration; Twingate only uses the DoH endpoint
- Cloudflare Zero Trust trial accounts are sufficient but may have policy or query limits

## Related Docs
- [Configure a Custom DoH Resolver in Twingate](https://www.twingate.com/docs/custom-doh) — required next step
- Cloudflare Zero Trust Gateway DNS Locations documentation