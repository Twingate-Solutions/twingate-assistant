---
source: https://www.twingate.com/docs/doh-cloudflare
type: docs
fetched: 2026-08-14
source_version: 8e9905aa2b95a1662f0f3c46c72ec75d385bf6a78e814e15766854e983a1dd20
---

# How to Configure Cloudflare DoH and DNS Filtering with Twingate

## Summary
Configures Twingate to use Cloudflare Zero Trust's DNS-over-HTTPS (DoH) for encrypted DNS resolution and optional DNS filtering. Requires a Cloudflare Zero Trust account and uses Twingate's custom DoH provider feature.

## Key Information
- Enables Cloudflare Gateway DNS filtering alongside DoH protection in Twingate
- DNS filtering policies are optional — DoH alone can be configured without them
- The custom DoH URL from Cloudflare is added to Twingate Admin Console as a custom DoH provider

## Prerequisites
- Valid Cloudflare Zero Trust account (free trial sufficient)
- Access to Twingate Admin Console
- Ability to configure custom DoH resolver in Twingate

## Step-by-Step

1. **Add DNS Location in Cloudflare**
   - Navigate to Cloudflare Zero Trust dashboard → **Gateway** → **DNS Locations**
   - Create a new DNS location
   - Save and close the location

2. **Retrieve Custom DoH URL**
   - Return to **Gateway** → **DNS Locations**
   - Click on the newly created location
   - Copy the **DNS over HTTPS** URL

3. **Configure DNS Filtering Policies (Optional)**
   - Navigate to **Policies** in Cloudflare Zero Trust dashboard
   - Create desired filtering policies

4. **Add DoH URL to Twingate**
   - Go to Twingate Admin Console
   - Add the Cloudflare DoH URL as a custom DoH provider
   - Follow Twingate's "Configure a Custom DoH resolver" documentation

## Configuration Values
| Parameter | Source | Notes |
|-----------|--------|-------|
| DoH URL | Cloudflare Gateway → DNS Locations → location detail | Per-location unique URL |

## Gotchas
- DNS filtering policies must be created in Cloudflare separately — adding the DoH URL alone does not enable filtering
- The DoH URL is location-specific; ensure you copy from the correct location if managing multiple

## Related Docs
- [Configure a Custom DoH Resolver in Twingate](https://www.twingate.com/docs/custom-doh) *(referenced in page)*
- Cloudflare Zero Trust Gateway DNS Locations documentation